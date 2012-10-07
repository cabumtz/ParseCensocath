'''
Created on 03/10/2012

@author: carlos
'''
import MySQLdb
import string

class DaoUtil(object):
    '''
    classdocs
    '''
    config = None


    def __init__(self, config):
        '''
        Constructor
        '''
        self.config = config
        pass
    
    
    def getConnection(self):
        '''
        '''
        my_conv = MySQLdb.converters.conversions.copy()
        
        dbConn = MySQLdb.connect(conv=my_conv,
                             host=self.config.db["host"],
                             user=self.config.db["user"],
                             passwd=self.config.db["password"],
                             db=self.config.db["database"])
        
        return dbConn
               
    def getSQLDateFromString(self, stringDate):
        '''
        '''
        if (stringDate != None) :
            dateElements = string.split(stringDate, "/")
            return "%04d/%02d/%02d" % ( int(dateElements[2]), int(dateElements[1]), int(dateElements[0]) )
        else :
            return None
        
        pass    

    
    