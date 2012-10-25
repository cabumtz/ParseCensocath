

'''
Created on 01/10/2012

@author: carlos
'''
import logging

class CalleDAO(object):
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


    def obtenerCalleId(self, nombreCalle, colonia_id, sector_id):
        '''

        '''
        sqlParameters = ( nombreCalle, colonia_id, sector_id )
        
        try:
            cursor = self.db.cursor()
            calle_id = 0
    
            # primer buscar en base de datos
            sql = """SELECT Id, Nombre FROM Calle WHERE Nombre = %s AND IdColonia = %s AND IdSector = %s"""

            result = None
            cursor.execute(sql, sqlParameters )
                        
            result = cursor.fetchone()
                              
            if (result != None) :
                # existe calle
                calle_id = result[0]

                self.db.commit()

                self.logger.debug("calle existe. calle_id: %s" % calle_id)

                return calle_id

            else :

                self.logger.debug("result = None. calle no existe")

                # no existe la calle

                sql = """INSERT INTO Calle(Nombre, IdColonia, IdSector) VALUES ( %s, %s, %s )"""

                result = cursor.execute(sql, sqlParameters )

                self.logger.debug("execute result: %s" % result)

                calle_id = self.db.insert_id()

                self.db.commit()

                self.logger.debug("calle insertada. calle_id: %s" % calle_id)

                return calle_id

        except Exception, e:
            self.logger.error("Exception: %s" % (e))
            self.db.rollback()
            raise e

        finally:
            if(cursor != None):
                cursor.close()

        pass
