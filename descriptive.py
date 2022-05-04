from pandas import DataFrame, read_csv
from matplotlib import pyplot as plt


class Descriptive_stats:
    """
    Responsible for returning the descriptive statistics of the data.

    Required parameters:
        data_frame: Data frame with the data.

    Optional parameters:
        main_variables: List with selected specific variables.
        style_graph: Name with chart layout.
        color1: Setting color for graphics.
        color2: Setting color for graphics.
        color3: Setting color for graphics.
        color4: Setting color for graphics.
        color5: Setting color for graphics.
    """

    def __init__(self, data_frame, **kwargs):  
        # data
        self.data_frame = DataFrame(data_frame).drop("_id", axis=1)
        
        # kwargs
        main_variables = kwargs.get('main_variables')
        style_graph = kwargs.get('style_graph')
        color1 = kwargs.get('color1')
        color2 = kwargs.get('color2')
        color3 = kwargs.get('color3')
        color4 = kwargs.get('color4')
        color5 = kwargs.get('color5')
        
        self.style_graph = "seaborn" if not style_graph else style_graph
        self.color1 = "royalblue" if not color1 else color1
        self.color2 = "crimson" if not color2 else color2
        self.color3 = "darkorange" if not color3 else color3
        self.color4 = "black" if not color4 else color4
        self.color5 = "red" if not color5 else color5
        
        if main_variables:
            self.main_variables = main_variables
        
        else:
            self.main_variables = self.data_frame.columns

    def sample_dataframe(self):
        """
        Generates a table with a sample of the data for quick visualization.
        """
        
        self.data_frame.sample(10).to_csv('1_results/1_sample_dataframe.txt', 
                                          sep='|', index=False)
        
        with open('1_results/1_sample_dataframe.txt', 'r') as txt:
            txt = txt.readlines()
            txt.insert(1, f"{'|-' * (len(self.data_frame.columns) - 1)}")
            txt[1] = f'{txt[1]}|-\n'
        
        with open('1_results/1_sample_dataframe.txt', 'w') as txt2:
            for line in txt:
                txt2.write(line)


    def describe_attributes(self):
        """
        Method responsible for describing the attributes of the database.
        """
        
        try:
            col_list = f'Attribute|Description\n|-|-\n'
            
            for col in self.data_frame.columns:
                col_list = col_list + f"|{col}|\n"
            
            with open('1_results/2_columns_name.txt', 'w') as desc_stat:
                desc_stat.write(col_list)
        
        except Exception as error:
            print(f"\n\n{'*' * 50}\n\n{error}\n\n{'*' * 50}")
        
        return


    def graph_dependent_var(self):
        """
        Method responsible for creating the graphs of the selected variables.
        """
        
        try:
            for col in self.main_variables:
                # config
                plt.style.use(self.style_graph)
                fig, ax = plt.subplots(1, 1, sharex=False, dpi=300)
                plt.rcParams.update({'font.size': 8})
                
                # df
                data_frame = self.data_frame.sort_values(by=col)
                
                # plot
                plot_data = data_frame[col].hist(color = self.color1,
                                            legend = False,
                                            bins = 'auto')
                
                # layout
                plt.title(f"{col.replace('_', ' ').upper()}")
                plt.xticks(rotation = 20)
                ax.ticklabel_format(scilimits=None)
                plt.tight_layout()
                
                # save
                plt.savefig(f"1_results/3_hist_{col}.jpg")
        
        except Exception as error:
            print(f"\n\n{'*' * 50}\n\n{error}\n\n{'*' * 50}")
        
        return


    def statistic_data(self):
        """
        Method responsible for creating a csv file with descriptive statistics 
        of numeric attributes.
        """
        
        try:
            
            df_stat_num = []
            
            for col in self.data_frame:
                
                if self.data_frame[col].dtype != 'object':
                    name_col = col
                    mean_col = self.data_frame[col].mean()
                    median_col = self.data_frame[col].median()
                    std_col = self.data_frame[col].std()
                    var_col = self.data_frame[col].var()
                    min_col = self.data_frame[col].min()
                    max_col = self.data_frame[col].max()
                    
                    stat_line = [name_col,
                                 mean_col,
                                 median_col,
                                 std_col,
                                 var_col,
                                 min_col,
                                 max_col]
                    
                    df_stat_num.append(stat_line)
            
            df_stat_num = DataFrame(df_stat_num)
            df_stat_num.columns = ["attributes",
                                   "mean",
                                   "median",
                                   "std",
                                   "variance",
                                   "lower",
                                   "higher"]
            
            # save
            df_stat_num.to_csv('1_results/4_descriptive_stats.txt',
                               sep = "|",
                               decimal = ".",
                               quotechar = '"',
                               index = False,
                               float_format = '%.2f')
            
            with open('1_results/4_descriptive_stats.txt', 'r') as txt2:
                txt2 = txt2.readlines()
                txt2.insert(1, f"{'|-' * (len(df_stat_num.columns) - 1)}")
                txt2[1] = f'{txt2[1]}|-\n'
            
            with open('1_results/4_descriptive_stats.txt', 'w') as txt3:
                for line in txt2:
                    txt3.write(line)
        
        except Exception as error:
            print(f"\n\n{'*' * 50}\n\n{error}\n\n{'*' * 50}")
        
        return

