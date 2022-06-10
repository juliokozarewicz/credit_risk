from pymongo import MongoClient
from pandas import DataFrame, get_dummies, concat
from sklearn.preprocessing import StandardScaler, MinMaxScaler


class Pre_processing:
    """
    This class is responsible for pre-processing the data, regarding 
    normalization, standardization and treatment of categorical attributes.
    
    syntax: Connection_mongodb(client = Database address,
                               data_base = Database name,
                               collection = Collection name)
    """

    def __init__(self, data_frame, client, data_base, collection):
        self.data_frame = data_frame
        self.client = MongoClient(client)
        self.data_base = data_base
        self.collection = collection
        self.check_occurrence = self.client[self.data_base]['cleansing_status']


    def data_scaling(self):
        """
        Data standardization.
        """
        
        try:
            bkp_check = self.check_occurrence.find()
            
            if DataFrame(bkp_check)['pre_process'].iloc[-1] == 1:
                return
        
        except:
            self.check_occurrence.update_many({},
                                              {'$set': 
                                              {'pre_process': 0}}, 
                                              upsert=True, 
                                              array_filters=None)
        
        try:
            # standardzation
            data_frame_raw = DataFrame(self.data_frame).drop(['loan_status',
                                                              '_id'], axis=1)
            
            stand_data = data_frame_raw.select_dtypes(include=['int64', 'float64'])
            
            standardization = StandardScaler()
            
            scaled_data = DataFrame(standardization.fit_transform(stand_data))
            
            scaled_data.columns = stand_data.columns 
            
            mon_stand = self.client[self.data_base][f'{self.collection}_standard']
            
            # categorical
            cat_data = data_frame_raw.select_dtypes(include='object')
            
            cat_data = get_dummies(cat_data)
            
            # concatenation
            send_df = concat([scaled_data, cat_data], axis=1)
            
            df_send = send_df.to_dict(orient='records')
            
            mon_stand.insert_many(df_send)
            
            self.check_occurrence.update_many({},
                                              {'$set': 
                                              {'pre_process': 1}}, 
                                              upsert=True, 
                                              array_filters=None)
        
        except Exception as error:
            print(f"\n\n{'*' * 50}\n\nDATA SCALING:\n\n{error}\n\n{'*' * 50}")
