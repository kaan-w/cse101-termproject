# Fitness Tracking Application - CSE 101 Term Project
## Running
Choose one of the following methods to run the application:

1. With a virtual environment (recommended)
```bash
# create a virtual environment
python3 -m venv .venv

# activate the virtual environment
source .venv/bin/activate

# build & install the application
pip install .

# run the application 
fitness-app
```

2. With nix
```bash
# build & run the application (no local clone required)
nix run github:kaan-w/cse101-termproject
```

3. Direct execution
```bash
# install dependencies
pip install -r requirements.txt

# run the applicaiton 
python3 src/main.py
```
