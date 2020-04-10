#!/usr/bin/env python
# -*- coding: utf-8 -*-

# s.w. Markierung

from __future__ import unicode_literals
from argparse import ArgumentParser

from .core import Core
# s.w. 
import logging
import sys
import os.path
# s.w. end

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
# s.w. begin
    print("++++++++++++++++++++++ init.main")
    path = os.path.realpath(os.path.abspath(__file__))
    dirname = os.path.dirname(path)
    print(dirname)
    logger = logging.getLogger('myLogger')
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler('/var/log/youtube-dl-webui/my.log')
    fh.setLevel(logging.DEBUG)

    logger.addHandler(fh)

    logger.debug('meine debug Ausgabe')
    logger.debug(dirname)
#    logging.basicConfig(filename='/var/log/youtube-dl-webui/example.log',level=logging.DEBUG)
#    logging.debug('Debug-Nachricht')
#    logging.info('Info-Nachricht')
#    logging.warning('Warnhinweis')
#    logging.error('Fehlermeldung')
# s.w. end
    cmd_args = getopt(argv)
    core = Core(cmd_args=cmd_args)
    core.start()
