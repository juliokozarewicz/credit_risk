# data base
from pymongo import MongoClient

# local
from config import client, data_base, collection


class Connection_mongodb:
    """
    Mongodb database access module.
    """

    def __init__(self):
        self.client = MongoClient(client)


    def all_data(self):
        """
        Access to all data in the collection of interest.
        """
        
        selected_data = self.client[data_base][collection].find()
        
        return selected_data


    def filtered_data(self, dict_filter):
        """
        Filtered access to data. The filter occurs through a dictionary of 
        fields and values.
        """
        
        selected_data = self.client[data_base][collection].find(filter=dict_filter)
        
        return selected_data


# data base connection
# ----------------------------------------------------------------------------
con = Connection_mongodb()
data_frame = con.all_data()
# ----------------------------------------------------------------------------
