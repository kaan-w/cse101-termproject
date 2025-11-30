from rich.layout import Layout

from dataclasses import dataclass

from components import Header
from models import Screen


@dataclass
class Dashboard(Screen):
  name: str = "Dashboard"

  def __rich__(self) -> Layout:
    self._layout.split_column(
      Layout(Header(screen_name=self.name), name="header"), Layout(name="main")
    )
    self._layout["header"].size = 3
    return self._layout

  def update(self) -> None:
    self._layout["header"].update(Header(screen_name=self.name))
