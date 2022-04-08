# libs
from pandas import DataFrame
from pathlib import Path

# plot
from matplotlib import pyplot as plt


class Descriptive_stats:
    """
    Responsible for returning the descriptive statistics of the data.
    """

    def __init__(self, data_frame, main_variables,
                       style_graph="seaborn", 
                       color1="royalblue", 
                       color2="crimson", 
                       color3="darkorange", 
                       color4="black", 
                       color5="red"):
        
        # data
        self.data_frame = DataFrame(data_frame).drop("_id", axis=1)
        self.main_variables = main_variables
        
        # style
        self.style_graph = style_graph
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.color4 = color4
        self.color5 = color5
        
        # make dir
        Path('./1_results').mkdir(exist_ok=True)


    def describe_attributes(self):
        """
        Method responsible for describing the attributes of the database.
        """
        
        col_list = ''
        for col in self.data_frame.columns:
            col_list = col_list + f"{col}\n"
        
        with open('1_results/1_columns_name.txt', 'w') as desc_stat:
            desc_stat.write(col_list)
        
        return


    def graph_dependent_var(self):
        """
        *****
        """
        
        for col in self.data_frame:
            # config
            plt.style.use(self.style_graph)
            fig, ax = plt.subplots(1, 1, sharex=False, dpi=300)
            plt.rcParams.update({'font.size': 8})
            
            # df
            data_frame = self.data_frame.sort_values(by=col)
            
            # plot
            plot_data = data_frame[col].hist(color = self.color2,
                                        legend = False,
                                        bins = 'auto',
                                        rwidth = 0.7,
                                        figsize = (12, 6))
            
            # layout
            plt.title(f"{col.replace('_', ' ').upper()}")
            plt.xticks(rotation = 20)
            ax.ticklabel_format(scilimits=None)
            plt.tight_layout()
            
            # save
            plt.savefig(f"1_results/2_hist_{col}.jpg") 
        
        return


    def statistic_data(self):
        """
        *****
        """
        
        for col in self.data_frame:
                
                if self.data_frame[col].dtype == 'object':
                    pass
                
                else:
                    name_col = col
                    mean_col = self.data_frame[col].mean()
                    median_col = self.data_frame[col].median()
                    std_col = self.data_frame[col].std()
                    var_col = self.data_frame[col].var()
                    min_col = self.data_frame[col].min()
                    max_col = self.data_frame[col].max()
                    
