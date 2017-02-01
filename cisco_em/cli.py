# -*- coding: utf-8 -*-

import click

from .cisco_em import CiscoEM

CONTEXT_SETTINGS = dict(
    help_option_names=['-h'],
    obj=CiscoEM()
)

commands = click.Group('cisco_em', context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@commands.command()
@click.pass_context
def devices(ctx):
    for node in ctx.obj.inventory.devices:
        click.echo(node)


@commands.command()
@click.pass_context
def credentials(ctx):
    for credential in ctx.obj.credentials.list():
        click.echo(credential)
