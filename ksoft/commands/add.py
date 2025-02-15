import click
import os
from rich.console import Console
from rich.prompt import Prompt

console = Console()

@click.command()
@click.argument("module_name", required=False)
def add(module_name):
    """[cyan]Dynamically add a module.[/cyan]"""
    if not module_name:
        module_name = Prompt.ask("[bold magenta]Enter module name[/bold magenta]")

    module_path = f"ksoft/modules/{module_name}.py"
    
    try:
        if not os.path.exists("ksoft/modules"):
            os.makedirs("ksoft/modules")
    except OSError as e:
        console.print(f"[bold red]❌ Error creating directory: {e}[/bold red]")
        return
        try:
            with open(module_path, "w") as f:
                f.write(f"# {module_name} module\n\ndef run():\n    print('Running {module_name}')\n")
            console.print(f"[bold green]✅ Module '{module_name}' created successfully![/bold green]")
        except OSError as e:
            console.print(f"[bold red]❌ Error creating module file: {e}[/bold red]")
    else:
        with open(module_path, "w") as f:
            f.write(f"# {module_name} module\n\ndef run():\n    print('Running {module_name}')\n")
        console.print(f"[bold green]✅ Module '{module_name}' created successfully![/bold green]")
