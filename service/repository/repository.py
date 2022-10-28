from service.model.message import Message
import pandas as pd

class Repository:
    def __init__(self):
        # pass
        self.NetworkInfo = {}
        self.ResponseInfo = {}

    # def save(self, message: Message):
    #     pass

    def save(self, ResponseHeader, Response):
        # pass            
        
        for val in ResponseHeader:
            for key in val.keys():
                if key not in self.NetworkInfo:
                    self.NetworkInfo[key] = [val[key]]
                else:
                    self.NetworkInfo[key].append(val[key])
                                
        
        
        for val in Response:
            for key in val.keys():
                if key not in self.ResponseInfo:
                    self.ResponseInfo[key] = [val[key]]
                else:
                    self.ResponseInfo[key].append(val[key])

        # print(self.NetworkInfo)
        # print(self.ResponseInfo)
        
        try:
            pd.DataFrame(self.NetworkInfo).to_csv("NetworkInfo.csv", index=False)    
            pd.DataFrame(self.ResponseInfo).to_csv("ResponseInfo.csv", index=False)
        except:
            print("File is opened so can't write in the file, Please close the file.")
        