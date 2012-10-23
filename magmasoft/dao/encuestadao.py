'''
Created on 30/09/2012

@author: carlos
'''


from magmasoft.dao.abstractdao import AbstractDAO
import logging

class EncuestaDAO(AbstractDAO):
    '''
    classdocs
    '''

    def __init__(self, conn):
        '''
        Constructor
        '''
        self.db = conn
        self.logger = logging.getLogger("encuestaDAO")

        pass

    def insertar(self, fecha, idEncuestador, Observacion):
        '''
        insertar function
        '''
        cursor = None
        newId = None

        try:

            #STR_TO_DATE(%s, %s)
            cursor = self.db.cursor()
            sql = """INSERT INTO Encuesta(Fecha, IdEncuestador, Observacion) VALUES (%s, %s, %s)"""

            result = None
            try :
                result = cursor.execute(sql, ( fecha, int(idEncuestador), Observacion))
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
