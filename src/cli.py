import uuid

import click

from app.auth import create_api_token


@click.group()
def cli():
    ...


@cli.command('issue-token')
def issue_api_token():
    """Create a new api token."""
    jti = str(uuid.uuid4())
    token = create_api_token(jti)
    click.echo(token)


if __name__ == '__main__':
    cli()
