

'''
Created on 01/10/2012

@author: carlos
'''
import logging

class ColoniaDAO(object):
    '''
    classdocs
    '''


    def __init__(self, conn):
        '''
        Constructor
        '''
        self.db = conn
        self.logger = logging.getLogger("daos")
        pass


    def obtenerColoniaId(self, nombreColonia):
        '''
        
        '''
        sqlParameters = ( nombreColonia, )
        
        try:
            cursor = self.db.cursor()
            colonia_id = 0
            
            # primer buscar en base de datos
            sql = """SELECT Id, Nombre FROM Colonia WHERE Nombre = %s"""
            result = None
            cursor.execute(sql, nombreColonia )
            result = cursor.fetchone()
            
            if (result != None) :
                # existe colonia
                colonia_id = result[0]
                
                self.db.commit()
                
                self.logger.debug("colonia existe. colonia_id: %s" % colonia_id)
                 
                return colonia_id
            
            else :
                
                self.logger.debug("result = None. colonia no existe")
                # no existe la colonia
                sql = """INSERT INTO Colonia(Nombre) VALUES ( %s )"""
                
                result = cursor.execute(sql, nombreColonia )
                
                self.logger.debug("execute result: %s" % result)
            
                colonia_id = self.db.insert_id()
            
                self.db.commit()
                
                self.logger.debug("colonia insertada. colonia_id: %s" % colonia_id)
                
                return colonia_id

            
        except Exception, e:
            self.logger.error("Exception: %s" % (e))
            self.db.rollback()
            raise e
            
        finally:
            if(cursor != None):
                cursor.close()
        
        pass
    
    
    