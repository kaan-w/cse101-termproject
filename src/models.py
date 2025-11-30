from rich.layout import Layout
from rich.panel import Panel

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pydantic import BaseModel


@dataclass
class Component(ABC):
  @abstractmethod
  def __rich__(self) -> Panel:
    pass


@dataclass
class Screen(ABC):
  name: str
  _layout: Layout = field(default_factory=Layout)

  @abstractmethod
  def __rich__(self) -> Layout:
    pass

  @abstractmethod
  def update(self) -> None:
    pass


class User(BaseModel):
  name: str
  password: str


@dataclass
class AppState:
  user: User
  screen: Screen
