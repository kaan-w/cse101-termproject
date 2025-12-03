from rich.panel import Panel
from rich.table import Table

from dataclasses import dataclass
from datetime import datetime

from ._base import Component


@dataclass
class Header(Component):
  screen_name: str

  def __rich__(self) -> Panel:
    grid = Table.grid(expand=True)

    grid.add_column(justify="left")
    grid.add_column(justify="center", ratio=1)
    grid.add_column(justify="right")

    grid.add_row(
      "Fitness App", self.screen_name, datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    )

    return Panel(grid, style="bold")
