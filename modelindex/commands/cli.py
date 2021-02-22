import os
import click

from modelindex.load_model_index import load


@click.group()
def cli():
    """model-index command line client."""
    pass


@cli.command()
@click.argument("filepath", default="")
def check(filepath):
    """Check if the file syntax is valid"""
    if filepath == "":
        filepath = "model-index.yml"
        if not os.path.isfile(filepath):
            click.echo("ERROR: model-index.yml not found in current directory.")
            return

    click.echo(f'Checking {filepath}')
    mi = load(filepath)
    mi.check()




