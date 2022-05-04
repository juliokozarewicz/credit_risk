from pymongo import MongoClient
from pandas import DataFrame
from numpy import percentile
from matplotlib import pyplot as plt


class Data_cleansing:
    """
    This class is responsible for pre-processing the data, here you will find 
    methods for handling missing data, outliers and other problems.

    syntax: Connection_mongodb(client = Database address,
                               data_base = Database name,
                               collection = Collection name,
                               filter = Data filter)
    """

    def __init__(self, client, data_base, collection, dict_filter={}):
        self.client = MongoClient(client)
        self.data_base = data_base
        self.collection = collection
        self.filter = dict_filter
        self.check_occurrence = self.client[self.data_base]['cleansing_status']

    def copy_db_bkp(self):
        """
        Data base backup.
        """
        
        try:
            bkp_check = self.check_occurrence.find()
            
            if DataFrame(bkp_check)['db_backup'].iloc[-1] == 1:
                return
        
        except:
            self.check_occurrence.update_many({},
                                              {'$set': 
                                              {'db_backup': 0}}, 
                                              upsert=True, 
                                              array_filters=None)
        
        try:
            db_copy = list(self.client[self.data_base][self.collection].find())
            
            collection_bkp = self.client[self.data_base][f'{self.collection}_bkp']
            
            collection_bkp.insert_many(db_copy)
            
            self.check_occurrence.update_many({},
                                              {'$set':
                                              {'db_backup': 1} },
                                              upsert=True,
                                              array_filters=None)
        except Exception as error:
            print(f"\n\n{'*' * 50}\n\n{error}\n\n{'*' * 50}")
        
        return


    def data_cleansing_nan(self):
        """
        Get data from mongodb and delete nan.
        """
        
        try:
            missing_check = self.check_occurrence.find()
            
            if DataFrame(missing_check)['missing_data'].iloc[-1] == 1:
                return
        
        except:
            self.check_occurrence.update_many({}, 
                                              {'$set': 
                                              {'missing_data': 0}}, 
                                              upsert=True, 
                                              array_filters=None)
        
        try:
            raw = self.client[self.data_base][self.collection]
            
            df_data = DataFrame(raw.find())
            
            null_list_id = []
            
            for col in df_data.columns: 
                col_id_nan = df_data[df_data[col].isnull()]['_id']
                
                for id_nan in col_id_nan:
                    null_list_id.append(id_nan)
            
            null_list_id = set(null_list_id)
            
            percent_remove = ( ( len(null_list_id) / len(df_data) ) * 100 )
            
            numb_del_percent = (
            
            f'About missing data removed from the original database:      \n\n'
            f'| TOTALS                     | VALUES                         \n'
            f'|----------------------------|--------------------------------\n'
            f'| Number of observations     | {len(df_data)}                 \n'
            f'| Number of missing data     | {len(null_list_id)}            \n'
            f'| Percentage of data removed | {percent_remove:.2f} %     \n\n\n' 
            
            )
            
            with open('1_results/0_data_cleansing_report.txt', 'w') as report:
                report.write(numb_del_percent)
            
            for id_select in null_list_id:
                raw.delete_one( {"_id" : id_select} )
            
            self.check_occurrence.update_many({},
                                              {'$set':
                                              {'missing_data': 1} },
                                              upsert=True,
                                              array_filters=None)
        
        except Exception as error:
            print(f"\n\n{'*' * 50}\n\n{error}\n\n{'*' * 50}")
        
        return


    def data_cleansing_outlier(self):
        """
        Get data from mongodb and delete outliers.
        """
        
        try:
            missing_check = self.check_occurrence.find()
            
            if DataFrame(missing_check)['outlier'].iloc[-1] == 1:
                return
        
        except:
            self.check_occurrence.update_many({},
                                              {'$set': 
                                              {'outlier': 0}}, 
                                              upsert=True, 
                                              array_filters=None)
        
        try:
            raw = self.client[self.data_base][self.collection]
            
            df_data = DataFrame(raw.find())
            
            outlier_list = []
            
            for col in df_data.columns:
                
                if df_data[col].dtype != 'object':
                    q1, q3 = percentile(df_data[col], [25 , 75])
                    
                    iqr = q3 - q1
                    
                    outl_select = df_data[ (df_data[col] < (q1 - 1.5 * iqr) ) | 
                                           (df_data[col] > (q3 + 1.5 * iqr) ) |
                                           (df_data['person_age'] > 60 ) ]
                    
                    for outlier_id in outl_select['_id']:
                        outlier_list.append(outlier_id)
            
            outlier_list = set(outlier_list)
            
            percent_remove = ( ( len(outlier_list) / len(df_data) ) * 100 )
            
            numb_del_percent = (
            
            f'About outliers removed from the original database:          \n\n'
            f'| TOTALS                     | VALUES                         \n'
            f'|----------------------------|--------------------------------\n'
            f'| Number of observations     | {len(df_data)}                 \n'
            f'| Number of outliers         | {len(outlier_list)}            \n'
            f'| Percentage of data removed | {percent_remove:.2f} %     \n\n\n' 
            
            )
            
            with open('1_results/0_data_cleansing_report.txt', 'a') as report:
                report.write(numb_del_percent)
            
            for id_select in outlier_list:
                raw.delete_one( {"_id" : id_select} )
            
            self.check_occurrence.update_many({},
                                              {'$set':
                                              {'outlier': 1} },
                                              upsert=True,
                                              array_filters=None)
            
            fig, ax = plt.subplots(figsize=(12, 6), dpi=600)
            plt.title('OUTLIERS REMOVED')
            
            # original data
            df_data.plot(x='person_age',
                         y='loan_amnt',
                         kind='scatter',
                         ax=ax,
                         color='darkslateblue',
                         alpha=0.15)
            
            # Outlier plot
            outl_select.plot(x='person_age',
                             y='loan_amnt',
                             kind='scatter',
                             ax=ax,
                             color='tomato',
                             alpha=0.15)
            
            plt.tight_layout()
            plt.savefig('1_results/0_outliers.jpeg')
        
        except Exception as error:
            print(f"\n\n{'*' * 50}\n\n{error}\n\n{'*' * 50}")

