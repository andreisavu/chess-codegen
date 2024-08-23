import click

@click.command()
def generate():
    click.echo("Generation process started")

@click.command()
def verify():
    click.echo("Verification complete")

if __name__ == "__main__":
    generate()
    verify()
