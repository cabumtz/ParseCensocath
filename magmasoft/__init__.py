import os
import logging.config

LOGCONFIG_FILE = "conf/logging.conf"


print "--------------------------------------"
print "configurando logging"
print "cwd: %s" % os.getcwd()
print "logconfig_file: %s" % LOGCONFIG_FILE 

logging.config.fileConfig(LOGCONFIG_FILE)

print "logging configurado"

print "--------------------------------------"