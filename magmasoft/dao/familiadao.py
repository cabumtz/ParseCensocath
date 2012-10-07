'''
Created on 01/10/2012

@author: carlos
'''
import logging
from magmasoft.dao.abstractdao import AbstractDAO

class FamiliaDAO(AbstractDAO):
    '''
    classdocs
    '''
    db = None

    def __init__(self, conn):
        '''
        Constructor
        '''
        self.db = conn
        self.logger = logging.getLogger("familiaDAO")
        pass
    
    
    def insertar(self, idCalle, idManzana, idEncuesta, NoExt, NoInt, Lote):
        '''
        insert method
        '''
        cursor = None
        newId = None
        
        try:
            cursor = self.db.cursor()
            sql = """INSERT INTO Familia(IdCalle, IdManzana, IdEncuesta, NoExt, NoInt, Lote) VALUES (%s, %s, %s, %s, %s, %s )"""

            result = None
            try :
                result = cursor.execute(sql, (idCalle, idManzana, idEncuesta, NoExt, NoInt, Lote))
            except Exception, e1:
                self.logger.error("The error was here: %s" % e1)
                raise e1
                
                
            self.logger.debug("execute result: %s" % result)
            
            newId = self.db.insert_id()
            
            self.db.commit()
                        
            self.logger.debug("newId: %s" % newId)
            
            return newId
        except Exception, e:
            self.logger.error("Exception: %s" % (e))
            self.db.rollback()
            raise e
        finally:
            if(cursor != None):
                cursor.close()
        
        pass