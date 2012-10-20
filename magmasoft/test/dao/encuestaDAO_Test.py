'''
Created on 30/09/2012

@author: carlos
'''
import unittest
import MySQLdb


from magmasoft.dao.encuestadao import EncuestaDAO
from magmasoft.dao.daoutil import DaoUtil

class EncuestaDAO_Test(unittest.TestCase):
    db = None
    encuestaDAO = None

    def setUp(self):
        self.db = MySQLdb.connect(host='localhost', user='root', passwd='cuchara1', db='censocath')
        self.encuestaDAO = EncuestaDAO(self.db)
        pass


    def tearDown(self):
        self.db.close()
        pass


    def test_insertar(self):
        newId = self.encuestaDAO.insertar( DaoUtil.getSQLDateFromString("30/09/2012")  , 1, "Esta es una prueba 5")
        print "newId: ", newId
        self.assertNotEqual(newId, None, "newId is NULL")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()