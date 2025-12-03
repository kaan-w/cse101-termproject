from dataclasses import dataclass
from pydantic import BaseModel

from screens._base import Screen


class User(BaseModel):
  name: str
  password: str


@dataclass
class AppState:
  user: User
  screen: Screen
