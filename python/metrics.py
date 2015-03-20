
import logging
import sys,os
from dblayer import *
from datetime import datetime
from sdds_constants import *

class metrics:
	''' This class contains functionalities to calculate important metrics in order to analyse the overall efficiency of the system.'''
	def __init__(self):
		try:
			self.db = dblayer()
		except Exception, e:
			logging.error("metrics:___init__: failed with error %s", e)
			return None

     	def get_saved_space(self):
		''' gets saved space '''
                try:
                        db_chunks_count = self.db.get_chunks_count()
                        files_saved_size = db_chunks_count * CHUNK_SIZE
                        total_input_size = self.db.get_total_input_size()
                        saved_space = total_input_size - files_saved_size
                        print "Total input size : %s Bytes" % total_input_size
                        logging.debug("Chunk saved space in the DB : %s Bytes", files_saved_size)
                        print "Chunk space in the DB : %s Bytes" % files_saved_size
                        logging.debug("Space removed by de-duplication : %s Bytes" % saved_space)
                        print "Space removed by de-duplication : %s Bytes" % saved_space
                except Exception, e:
                        logging.error('metrics:get_saved_space: error %s ', e)
                        return None

	
