#!/usr/bin/env python
# -*- coding: utf-8 -*-

# s.w. Markierung

from __future__ import unicode_literals
from argparse import ArgumentParser

from .core import Core
# s.w. 
import logging.config
import logging
import sys
import os.path
import json
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
    path = os.path.realpath(os.path.abspath(__file__))
    dirname = os.path.dirname(path)
    logging_json = os.path.join(dirname, 'logging.json')
    try:
        print("load logging config from")
        print(logging_json)
        with open(logging_json) as f:
            logging_conf = json.load(f)
    except:
        print("warning: no logging_conf loaded")
    
    logging.config.dictConfig(logging_conf)
    print("logging config loaded")

    logger = logging.getLogger('ydl_webui')
#    logger.setLevel(logging.DEBUG)

#    fh = logging.FileHandler('/var/log/youtube-dl-webui/my.log')
#    fh.setLevel(logging.DEBUG)

#    logger.addHandler(fh)

    logger.debug('start ydl_webui')
    logger.debug(dirname)
#    logging.basicConfig(filename='/var/log/youtube-dl-webui/example.log',level=logging.DEBUG)
    logging.debug('Debug-Nachricht')
    logging.info('Info-Nachricht')
    logging.warning('Warnhinweis')
    logging.error('Fehlermeldung')
# s.w. end
    cmd_args = getopt(argv)
    core = Core(cmd_args=cmd_args)
    core.start()
