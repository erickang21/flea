import click
import subprocess

SUCCESS = click.style("SUCCESS!", fg="green")

@click.command()
def flea():
    click.echo("lol this is flea")