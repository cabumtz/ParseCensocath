'''
Created on 30/09/2012

@author: carlos
'''

class Config(object):
    '''
    classdocs
    '''
    db = None

    def __init__(self):
        '''
        Constructor
        '''
        self.db = {}
        self.db["host"] = "localhost"
        self.db["user"] = "root"
        self.db["password"] = "cuchara1"
        self.db["database"] = "censocath"
        