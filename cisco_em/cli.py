# -*- coding: utf-8 -*-

import click

from .apic_em import ApicEM

CONTEXT_SETTINGS = dict(
    help_option_names=['-h'],
    obj=ApicEM()
)

commands = click.Group('apic_em', context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@commands.command()
@click.pass_context
def devices(ctx):
    for node in ctx.obj.devices.list():
        click.echo(node)


@commands.command()
@click.pass_context
def credentials(ctx):
    for credential in ctx.obj.credentials.list():
        click.echo(credential)
