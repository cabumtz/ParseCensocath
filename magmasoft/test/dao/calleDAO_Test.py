'''
Created on 25/10/2012

@author: carlos
'''
import unittest
from magmasoft.config import Config
from magmasoft.factory.servicefactory import ServiceFactory

class CalleDAO_Test(unittest.TestCase):
    serviceFactory = None
    calleDAO = None

    def setUp(self):
        '''
        '''
        config = Config()
        self.serviceFactory = ServiceFactory(config)
        self.calleDAO = self.serviceFactory.daos["calleDAO"]
        pass


    def tearDown(self):
        self.serviceFactory.closeConnection()
        pass


    def test_obtenerCalleId(self):
        calle_id = self.calleDAO.obtenerCalleId(u"Perepepengue", 10, 11)
        print calle_id
        
        calle_id = self.calleDAO.obtenerCalleId(u"Sulum", 10, 11)
        print calle_id
        
        calle_id = self.calleDAO.obtenerCalleId(u"Terettt", 10, 11)
        print calle_id
    
        calle_id = self.calleDAO.obtenerCalleId(u"Perepepengue", 10, 11)
        print calle_id
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()