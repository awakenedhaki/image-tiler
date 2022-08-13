import click
from commands import singular, batch

@click.group()
def cli():
    pass

cli.add_command(singular)
cli.add_command(batch)

if __name__ == '__main__':
    cli()