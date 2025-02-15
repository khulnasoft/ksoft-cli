import click
import os
from rich.console import Console
from rich.table import Table

console = Console()

@click.command(name="list")
def list_modules():
    """[cyan]List available modules.[/cyan]"""
    module_dir = "ksoft/modules"
    if not os.path.exists(module_dir):
        console.print("[bold red]No modules found.[/bold red]")
        return

    modules = [f.replace(".py", "") for f in os.listdir(module_dir) if f.endswith(".py")]
    if modules:
        table = Table(title="📦 Available Modules", show_header=True, header_style="bold magenta")
        table.add_column("Module Name", style="cyan")

        for module in modules:
            table.add_row(module)
        
        console.print(table)
    else:
        console.print("[bold red]No modules found.[/bold red]")
