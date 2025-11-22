import json
from pathlib import Path

from models import User

DATA_DIR = Path.cwd() / "data"

def load_users() -> list[User]:
  with open(DATA_DIR / "users.json", "r") as file:
    raw = json.load(file)

  return [User.model_validate(u) for u in raw]
