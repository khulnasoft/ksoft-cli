import click
from rich.console import Console
from rich.panel import Panel
from ksoft.commands import init, add, list_modules, start_api

console = Console()

@click.group()
def cli():
    """[bold blue]🚀 KSoft[/bold blue] - A Developer Environment Tool"""
    console.print(Panel.fit("[cyan]Welcome to KSoft - Your Dev Environment Manager![/cyan]", title="🔥 KSoft", style="bold magenta"))

cli.add_command(init)
cli.add_command(add)
cli.add_command(list_modules)
cli.add_command(start_api)

if __name__ == "__main__":
    cli()
