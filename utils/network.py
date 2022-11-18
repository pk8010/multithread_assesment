#https://excuser.herokuapp.com/

# Need to check if this can work(In case excuser does not work)
# https://www.boredapi.com/api/activity
# https://www.boredapi.com/ # with different type given
# https://www.boredapi.com/documentation#endpoints-key


import requests
from datetime import datetime
# import datetime
import random

class Network:
    # pass
    def __init__(self):
        #These are list of topics on which we can get message.
        
        # This API stopped working after some time as checked take similar API to perform the operations.
        # self.Topics = ['family','office', 'children', 'college', 'party', 'funny', 'unbelievable',
        #               'developers','gaming']
        # self.url = "https://excuser.herokuapp.com/v1/excuse/"
        
        
        
        # We can switch to any API and the rest of the code will be same as it is.
        self.Topics = ["education", "recreational", "social", "diy", "charity", "cooking", 
                       "relaxation", "music", "busywork"]        
        self.url = "https://www.boredapi.com/api/activity?type="

    
    # We have made this function protected to avoid accessing it from outside in suggesation.
    
    # def _MakeRequest(self, Topic ='family'):
    def MakeRequest(self, Topic ='education'):
        """

        Parameters
        ----------
        Topic : TYPE, optional
            DESCRIPTION. The default is 'education'.

        Returns
        -------
        Response Header
            Response Header Contains all the information of API being called.
        Response 
            The Actual Response from the API call.

        """
        #This is calling the API with given topic by appending at last and giving different response based on that.
        response = requests.request("GET", self.url+Topic)
        
        
        self.Headers = response.headers
        self.Response = response.json()
        
        # print(self.Headers)
        
        # # Adding Value between -100, 100 and current date time as per the requirement.
        self.Response['value']= random.randint(-100,100)
        self.Response['timestamp']= str(datetime.today().isoformat())
        # print(self.Response)
        
        return self.Headers, self.Response
    
# n = Network()
# n._MakeRequest()
    

