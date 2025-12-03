from rich.layout import Layout

from abc import ABC, abstractmethod

from components import Header


class Screen(ABC):
  @property
  def name(self) -> str:
    return self.__class__.__name__.upper()

  def get_default_layout(self) -> Layout:
    layout = Layout()
    layout.split_column(
      Layout(Header(screen_name=self.name), name="header"), Layout(name="main")
    )
    layout["header"].size = 3
    return layout

  @abstractmethod
  def __rich__(self) -> Layout:
    pass
