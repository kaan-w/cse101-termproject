from rich.console import Console
from rich.live import Live
from rich.padding import Padding
from rich.text import Text

import pyfiglet
import time

from models import AppState, User
from screens import Dashboard
import storage


def main():
  console = Console(highlight=False)
  console.clear()

  title_figlet = pyfiglet.figlet_format("Fitness-App", font="slant")
  console.print(title_figlet, end="", style="bold")

  subtitle = "-- CSE 101 Term Project --"
  left_pad = (title_figlet.find("\n") - len(subtitle)) // 2
  console.print(Padding(f"{subtitle}\n", (0, 0, 0, left_pad)), style="italic")

  name = console.input(Text("Username: ", style="bold blue"))
  password = console.input(Text("Password: ", style="bold blue"), password=True)

  users = storage.load_users()
  for user in users:
    if user.name == name and user.password == password:
      user = User(name=name, password=password)
      state = AppState(user=user, screen=Dashboard())

      with Live(state.screen, screen=True) as live:
        while True:
          live.update(state.screen)
          time.sleep(0.25)

      break
  else:
    console.print("Invalid username or password.", style="bold red")


if __name__ == "__main__":
  main()
