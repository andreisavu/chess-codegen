import click

@click.command()
def generate():
    click.echo("Starting the generation process...")

if __name__ == "__main__":
    generate()
