import click
from emtechstack.commands import (
    init_profile,
    start_infra as start_infra_function,
    stop_infra as stop_infra_function,
    start_api as start_api_function,
    stop_api as stop_api_function,
    build_env,
    clean_code,
    find_and_kill_processes,
    update_emtechstack,
    update_requirements as update_requirements_function,
    show_version,
)


@click.group()
def cli():
    """Emtechstack CLI Tool"""
    pass


@cli.command()
@click.option("--profile", required=True, help="Profile path to initialize")
@click.option("--name", help="Custom directory name for the cloned profile")
def init(profile, name):
    """Initialize the profile by cloning the repo"""
    init_profile(profile, name)


@cli.command()
def start_infra():
    """Start the infrastructure using docker-compose"""
    start_infra_function()


@cli.command()
def stop_infra():
    """Stop the infrastructure using docker-compose"""
    stop_infra_function()


@cli.command()
@click.option("--port", default="8000", help="Port to run the API on")
def start_api(port):
    """Start the FastAPI application"""
    start_api_function(port)


@cli.command()
def stop_api():
    """Stop the FastAPI application"""
    stop_api_function()


@cli.command()
@click.option("--name", help="Name of the Conda environment to create and activate")
def build(name):
    """Build and activate the Conda environment, and install dependencies from requirements.txt"""
    build_env(name)


@cli.command()
def clean():
    """Clean the code using black"""
    clean_code()


@cli.command()
@click.option("--port", required=True, help="Port to clean")
def clean_port(port):
    """Clean the port"""
    find_and_kill_processes(port)


@cli.command()
def update():
    """Update the emtechstack package"""
    update_emtechstack()


@cli.command()
def upgrade():
    """Update the emtechstack package"""
    update_emtechstack()

@cli.command()
def update_requirements():
    """Update the requirements.txt file with installed package versions"""
    update_requirements_function()
    

@cli.command()
def version():
    """Show the current version of EmTechStack"""
    show_version()
    
if __name__ == "__main__":
    cli()
