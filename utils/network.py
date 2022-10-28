#https://excuser.herokuapp.com/

import requests
from datetime import datetime
# import datetime
import random

class Network:
    # pass
    def __init__(self):
        #These are list of topics on which we can get message.
        self.Topics = ['family','office', 'children', 'college', 'party', 'funny', 'unbelievable',
                      'developers','gaming']
        self.url = "https://excuser.herokuapp.com/v1/excuse/"
    
    # We have made this function protected to avoid accessing it from outside in suggesation.
    def _MakeRequest(self, Topic ='family'):
        """

        Parameters
        ----------
        Topic : TYPE, optional
            DESCRIPTION. The default is 'family'.

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
        
        # Adding Value between -100, 100 and current date time as per the requirement.
        self.Response[0]['value']= random.randint(-100,100)
        self.Response[0]['timestamp']= str(datetime.today().isoformat())
        
        
        return self.Headers, self.Response[0]