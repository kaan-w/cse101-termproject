from rich.panel import Panel

from abc import ABC, abstractmethod


class Component(ABC):
  @abstractmethod
  def __rich__(self) -> Panel:
    pass
