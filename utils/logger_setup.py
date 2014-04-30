# -*- coding: utf-8 -*-

""" Handles log setup. """

import logging, os, pprint
import logging.handlers
from clusters_api.config import settings


def setup_logger():
    """ Returns a logger to write to a file. """
    filename = u'%s/clusters_api.log' % settings.LOG_DIR
    formatter = logging.Formatter( u'[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s' )
    logger = logging.getLogger( u'clusters_api' )
    level_dict = { u'debug': logging.DEBUG, u'info':logging.INFO }
    logger.setLevel( level_dict[settings.LOG_LEVEL] )
    file_handler = logging.handlers.RotatingFileHandler( filename, maxBytes=(5*1024*1024), backupCount=1 )
    file_handler.setFormatter( formatter )
    logger.addHandler( file_handler )
    return logger