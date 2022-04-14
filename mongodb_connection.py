# libs
from pymongo import MongoClient
from pandas import DataFrame


class Connection_mongodb:
    """
    Mongodb database access module.
    """

    def __init__(self, client, data_base, collection, dict_filter={}):
        self.client = MongoClient(client)
        self.data_base = data_base
        self.collection = collection
        self.filter = dict_filter


    def all_data(self):
        """
        Access to all data in the collection of interest.
        """
        
        selected_data = self.client[self.data_base][self.collection].find()
        
        return selected_data


    def filtered_data(self):
        """
        Filtered access to data. The filter occurs through a dictionary of 
        fields and values.
        """
        
        selected_data = self.client[self.data_base][self.collection]
        selected_data = selected_data.find(filter=self.filter)
        
        return selected_data


    def data_cleansing(self):
        """
        *****
        """
        
        # del Nan
        raw = self.client[self.data_base][self.collection]
        
        teste = DataFrame(raw.find())

        teste = teste[teste['person_emp_length'].isnull()]
        
        
        print(teste['person_emp_length'])
        #for col in raw.find(filt):
        #    print(col)
