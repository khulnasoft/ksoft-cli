import click
import os
import subprocess
from rich.console import Console
from rich.progress import Progress

console = Console()

@click.command()
def init():
    """[green]Initialize the development environment.[/green]"""
    console.print("[bold yellow]Setting up the development environment...[/bold yellow]")

    with Progress() as progress:
        task = progress.add_task("[cyan]Creating virtual environment...[/cyan]", total=1)
        if not os.path.exists(".venv"):
            result = subprocess.run(["python", "-m", "venv", ".venv"], check=True)
            if result.returncode != 0:
                console.print("[bold red]❌ Failed to create virtual environment.[/bold red]")
                return
        progress.update(task, advance=1)
        result = subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        if result.returncode != 0:
            console.print("[bold red]❌ Failed to install dependencies.[/bold red]")
            return

        task = progress.add_task("[cyan]Installing dependencies...[/cyan]", total=1)
        subprocess.run(["pip", "install", "-r", "requirements.txt"])
        progress.update(task, advance=1)
        console.print("[bold green]✅ Dependencies installed.[/bold green]")

    console.print("[bold blue]🎉 Development environment setup complete![/bold blue]")
