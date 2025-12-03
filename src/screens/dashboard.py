from rich.layout import Layout

from ._base import Screen


class Dashboard(Screen):
  def __rich__(self) -> Layout:
    self.layout = self.get_default_layout()
    return self.layout
