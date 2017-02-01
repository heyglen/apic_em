# -*- coding: utf-8 -*-

import click

from .cisco_em import CiscoEM

CONTEXT_SETTINGS = dict(
    help_option_names=['-h'],
)

commands = click.Group('cisco_em', context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@commands.command()
def main(args=None):
    """Console script for cisco_em"""
    cisco_em = CiscoEM()


if __name__ == "__main__":
    main()
