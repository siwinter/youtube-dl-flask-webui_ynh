#!/usr/bin/env python
# -*- coding: utf-8 -*-

# s.w. Markierung

from __future__ import unicode_literals
from argparse import ArgumentParser

from .core import Core

import logging

def getopt(argv):
    parser = ArgumentParser(description='Another webui for youtube-dl')

    parser.add_argument('-c', '--config', metavar="CONFIG_FILE", help="config file")
    parser.add_argument('--host', metavar="ADDR", help="the address server listens on")
    parser.add_argument('--port', metavar="PORT", help="the port server listens on")

    return vars(parser.parse_args())


def main(argv=None):
    from os import getpid

    print("pid is {}".format(getpid()))
    print("-----------------------------------")

    logging.basicConfig(filename='/var/log/example.log',level=logging.DEBUG)
    logger.debug('Debug-Nachricht')
    logger.info('Info-Nachricht')
    logger.warning('Warnhinweis')
    logger.error('Fehlermeldung')
    
    cmd_args = getopt(argv)
    core = Core(cmd_args=cmd_args)
    core.start()
