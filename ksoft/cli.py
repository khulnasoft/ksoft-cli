import click
from ksoft.core.bootstrap import init_db
from ksoft.core.database import get_db
from ksoft.core.module_manager import add_module, list_modules

@click.group()
def cli():
    """KSoft - A Development Environment Manager"""
    pass

@cli.command()
def init():
    """Initialize the development environment"""
    init_db()
    click.echo("✅ Environment initialized successfully!")

@cli.command()
@click.argument("name")
@click.option("--description", default="", help="Description of the module")
def add(name, description):
    """Add a new module"""
    db = next(get_db())
    module = add_module(db, name, description)
    click.echo(f"✅ Module '{module.name}' added successfully!")
    db.close()

@cli.command()
def list():
    """List all available modules"""
    db = next(get_db())
    modules = list_modules(db)
    if modules:
        for module in modules:
            click.echo(f"📦 {module.name} - {module.description}")
    else:
        click.echo("⚠️ No modules found.")
    db.close()

if __name__ == "__main__":
    cli()
