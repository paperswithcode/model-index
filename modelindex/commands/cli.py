import os

import click

from modelindex.load_model_index import load


@click.group()
def cli():
    """model-index command line client."""
    pass


@cli.command()
@click.argument("filepath", default="model-index.yml")
def check(filepath):
    """Check if the file syntax is valid"""
    click.echo(f'Checking {filepath}')
    mi = load(filepath)
    mi.check()




