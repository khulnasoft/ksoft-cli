import click
from fastapi import Depends
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
def add(name, description, db: Session = Depends(get_db)):
    """Add a new module"""
    module = add_module(db, name, description)
    click.echo(f"✅ Module '{module.name}' added successfully!")

@cli.command()
def list(db: Session = Depends(get_db)):
    """List all available modules"""
    modules = list_modules(db)
    if modules:
        for module in modules:
            click.echo(f"📦 {module.name} - {module.description}")
    else:
        click.echo("⚠️ No modules found.")

if __name__ == "__main__":
    cli()
