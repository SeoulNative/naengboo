import click
import os

@click.group()
def cli():
    pass

@cli.command()
@click.option(
    '--mode',
    type=str, 
    default="dev", 
    show_default='dev', 
    help="choose server mode"
)
def run(mode):
    '''
    run flask app for development server
    '''
    os.environ["FLASK_CONFIG"] = mode
    os.system("flask run")

@cli.command()
def test():
    '''
    run pytest
    '''
    os.system("pytest")

if __name__ == '__main__':
    cli()