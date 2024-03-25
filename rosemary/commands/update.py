# rosemary/commands/update.py

import click
import subprocess
import os


@click.command()
def update():
    """This command updates pip, all packages, and updates requirements.txt."""
    try:
        # Update pip
        subprocess.check_call(['pip', 'install', '--upgrade', 'pip'])

        # Get the list of installed packages and update them
        packages = subprocess.check_output(['pip', 'freeze']).decode('utf-8').split('\n')
        for package in packages:
            package_name = package.split('==')[0]
            if package_name:  # Check if the package name is not empty
                subprocess.check_call(['pip', 'install', '--upgrade', package_name])

        # Update requirements.txt
        requirements_path = os.path.join(os.getcwd(), 'requirements.txt')
        with open(requirements_path, 'w') as f:
            subprocess.check_call(['pip', 'freeze'], stdout=f)

        click.echo('Update completed!')
    except subprocess.CalledProcessError as e:
        click.echo(f'Error during the update: {e}')