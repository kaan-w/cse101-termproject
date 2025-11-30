{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    git-hooks = {
      url = "github:cachix/git-hooks.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { flake-parts, ... }@inputs:
    flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [
        inputs.git-hooks.flakeModule
      ];
      systems = [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" "x86_64-darwin" ];

      perSystem = { config, pkgs, ... }: let
        inherit (pkgs.lib) lists splitString;
        dependencies = builtins.map
          (p: pkgs.python313Packages.${p} ) 
          (lists.remove "" (splitString "\n" (builtins.readFile ./requirements.txt)));
      in {
        packages.default = pkgs.python313Packages.buildPythonApplication {
          pname = "fitness-app";
          version = "0.1.0";
          src = ./.;

          pyproject = true;
          build-system = with pkgs.python313Packages; [ setuptools ];
          inherit dependencies;
        };

        pre-commit.settings.hooks = {
          ruff.enable = true;
          ruff-format.enable = true;
        };

        devShells.default = pkgs.mkShellNoCC {
          buildInputs = with pkgs; [
            python3
            (pkgs.python3.withPackages (pp: with pp; [
              pytest
            ] ++ dependencies))
          ] ++ config.pre-commit.settings.enabledPackages;

          env = {
            PYTHONDONTWRITEBYTECODE = "1";
          };
        };
      };
    };
}