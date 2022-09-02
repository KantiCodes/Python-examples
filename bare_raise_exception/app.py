import click

def execute(divider):
    click.echo(f"result: {1 / divider}")

@click.command()
@click.argument('divider', type=int)
@click.option("-v", "--verbose", is_flag=True)
def cli(divider, verbose):
    if not verbose:
        click.echo("Running in silent mode, exceptions will not be shown")
    click.echo(f"divider: {divider}")
    try:
        execute(divider=divider)
    except Exception as e:

        # Propagate exception if verbose
        if verbose:
            raise


if __name__ == "__main__":
    cli()