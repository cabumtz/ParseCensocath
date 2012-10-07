'''
Created on 30/09/2012

@author: carlos
'''

class AbstractDAO(object):
    '''
    classdocs
    '''
    LOG_FILENAME = "dao.log.txt"
    db = None
    logger = None

    def __init__(self):
        '''
        Constructor
        '''
        