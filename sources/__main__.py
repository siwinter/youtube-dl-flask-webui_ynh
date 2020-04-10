#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
import os.path
import json
import logging
import logging.config

if __package__ is None and not hasattr(sys, 'frozen'):
    print("++++++++++++++++++++++ main. 1")
    path = os.path.realpath(os.path.abspath(__file__))
    dirname = os.path.dirname(path)
    print(dirname)
    print(__name__)
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))
else:
    path = os.path.realpath(os.path.abspath(__file__))
    dirname = os.path.dirname(path)
    print("++++++++++++++++++++++ main. 2")
    print(dirname)
    print(__name__)


import youtube_dl_webui
print("++++++++++++++++++++++ main. 3")
print(__name__)

if __name__ == '__main__':
    # Setup logger
    # s.w. begin 
    logger = logging.getLogger('myLogger')
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler('/var/log/youtube-dl-webui/my.log')
    fh.setLevel(logging.DEBUG)

    logger.addHandler(fh)

    logger.debug('meine debug Ausgabe')
#    logging.basicConfig(filename='/var/log/youtube-dl-webui/example.log',level=logging.DEBUG)
    logging.debug('Debug-Nachricht')
    logging.info('Info-Nachricht')
    logging.warning('Warnhinweis')
    logging.error('Fehlermeldung')
# s.w. end
    
    logging_json = os.path.join(dirname, 'logging.json')
#    logging.debug(dirname)
    logging.debug(logging_json)
#    with open(logging_json) as f:
#        logging_conf = json.load(f)
#    logging.config.dictConfig(logging_conf)

#    youtube_dl_webui.main()

