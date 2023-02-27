from rich.progress import Progress
import time
from time import sleep

from rich.console import Console
from rich.progress import Progress
from rich.traceback import install

import ai

install()

console = Console(record=True)

def loadscr():
    with Progress() as progress:

        task1 = progress.add_task("[red]Initializing...", total=100)
        task2 = progress.add_task("[green]Processing...", total=100)
        task3 = progress.add_task("[cyan]Building_Env...", total=100)

        while not progress.finished:
            progress.update(task1, advance=0.9)
            progress.update(task2, advance=0.6)
            progress.update(task3, advance=0.3)
            time.sleep(0.02)
    print("")
    console = Console()

    tasks = [f"Task {n}" for n in range(1, 6)]

    with console.status("[bold green]Generating Env..") as status:
        while tasks:
            task = tasks.pop(0)
            sleep(1)
            console.log(f"{task} success!")
    ai.assistant()

# console.save_html("log\\log_loadingscr.html")