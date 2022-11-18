import threading

from service.repository.repository import Repository
from utils.network import Network
from sensors.base_sensor import BaseSensor
import time

import logging


class Logging(threading.Thread):
    def __init__(self, repository: Repository, network: Network, sensor: BaseSensor):
        self.repository: Repository = repository
        self.network: Network = network            
        self.sensor: BaseSensor = sensor        
        logging.basicConfig(filename=r"loggings\loggingfile.log", level=logging.DEBUG)

    def run(self) -> None:
        NumberOfRecordsProcessed = 1
        while True:
            #You most save data present on network here, keep on mind that network could have at maximum 5 messages
            #at the time.            
            response = self.sensor.GetSensorMessageRandomly()
            print("\nResponse Header ====================================>")
            print (response[0])
            print("\nResponse ===========================================>")
            print (response[1])
            print("\nTimeTaken ==========================================>")
            print (response[2])
                    
            print("Number of Records Processed: ", NumberOfRecordsProcessed*response[3])
            NumberOfRecordsProcessed += 1
            
            print("\nWating for 5 seconds for next call.")            
            time.sleep(5)
            
            #This package is to store the logging information in the logging direcotry                                                             
            logging.info(response)
            
            print("File Saving in Progress.........")
            self.repository.save(response[0], response[1])
            
        
            
            
            
            
       
            
            


