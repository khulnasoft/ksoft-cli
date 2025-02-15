import click
import subprocess
from rich.console import Console

console = Console()

@click.command()
def start_api():
    """[cyan]Start the FastAPI server.[/cyan]"""
    console.print("[bold yellow]🚀 Starting API server on [blue]http://127.0.0.1:8000[/blue]...[/bold yellow]")
    subprocess.run(["uvicorn", "ksoft.api.main:app", "--reload"])
