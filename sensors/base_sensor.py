from utils.network import Network

import time
import random
from concurrent.futures import ThreadPoolExecutor

class BaseSensor(Exception):
    def __init__(self, network: Network, NumofSensors = 5):
        # pass
        # self.Network()
        self.network = network        

                
        if NumofSensors <= 9:            
            self.NumofSensors = NumofSensors
        else:
            raise BaseSensor("Please enter number of sensor less than or equal to", 9)
        
        
        
    def GetNetworkResponse(self):
        # pass
        ResponseHeader, Response = self.network.MakeRequest()
        print("Response Header----------->",ResponseHeader)
        print()
        print("Response ----------->",Response)
        # self.NetworkObject()
        
    def GetAvailableTopics(self):
        """
        Returns the topics available in the Network Class which is being called

        """
        return self.network.Topics

    def GetSensorMessageRandomly(self):
        self.HeaderResponse = []
        self.Response = []        
        ThreadResult = []
        elapsed_time = time.time()        
        
        #This line of code will select number of topics dynamically from available list.
        self.Topics = random.choices(self.GetAvailableTopics(), k = self.NumofSensors)

        ## Sequential Execution
        # for topic in self.Topics:
        #     HeaderResponseTemp, ResponseTemp = self.network._MakeRequest(topic)
        #     self.HeaderResponse.append(HeaderResponseTemp)
        #     self.Response.append(ResponseTemp)
        
        #Threading Execution, We have modified number of worker dynamically as per num of sensor                        
        with ThreadPoolExecutor(max_workers=(self.NumofSensors)) as executor:
            for topic in self.Topics:
                result = executor.submit(self.network._MakeRequest, topic)
                ThreadResult.append(result)
                
        for thread in ThreadResult:
            self.HeaderResponse.append(thread.result()[0]) 
            self.Response.append(thread.result()[1])            
        
        TimeTaken = "{:.6f}s".format(time.time() - elapsed_time)
        # print("Elapsed time: {:.6f}s".format(time.time() - elapsed_time))
        return (self.HeaderResponse), (self.Response), TimeTaken, self.NumofSensors
        
        

# n = Network()    
# b = BaseSensor(n)
# print(b.GetSensorMessageRandomly())