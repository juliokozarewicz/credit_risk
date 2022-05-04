from pandas import DataFrame, read_csv
from seaborn import histplot, countplot
from matplotlib import pyplot as plt


class Exploratory_analysis:
    """
    Responsible for returning graphs and information provided by an exploratory analysis.

    Required parameters:
        data_frame: Data frame with the data.

    Optional parameters:
        main_variables: List with selected specific variables.
        style_graph: Name with chart layout.
        pallete: Color pallete.
        color1: Setting color for graphics.
        color2: Setting color for graphics.
        color3: Setting color for graphics.
        color4: Setting color for graphics.
        color5: Setting color for graphics.
    """

    def __init__(self, data_frame, **kwargs):  
        
        # data
        self.data_frame = data_frame
        
        # kwargs
        main_variables = kwargs.get('main_variables')
        style_graph = kwargs.get('style_graph')
        palette = kwargs.get('palette')
        color1 = kwargs.get('color1')
        color2 = kwargs.get('color2')
        color3 = kwargs.get('color3')
        color4 = kwargs.get('color4')
        color5 = kwargs.get('color5')
        
        self.style_graph = "seaborn" if not style_graph else style_graph
        self.palette = "muted" if not palette else palette
        self.color1 = "royalblue" if not color1 else color1
        self.color2 = "crimson" if not color2 else color2
        self.color3 = "darkorange" if not color3 else color3
        self.color4 = "black" if not color4 else color4
        self.color5 = "red" if not color5 else color5
        
        if main_variables:
            self.main_variables = main_variables
        
        else:
            self.main_variables = self.data_frame.columns
        


    def categorical_plot(self):
        """
        Plotting the information of the categorical variables.
        """
     
        df_categorical = DataFrame(self.data_frame).drop("_id", axis=1)
        df_cat = df_categorical.select_dtypes(exclude=['float64', 'int64'])
        
        fig, ax = plt.subplots(figsize=(18, 10), dpi=600)
        
        numb_plot = 0
        
        for col in df_cat:
            # count
            numb_plot += 1
            
            # plot
            plt.subplot(2, 2, numb_plot)
            
            countplot(x=df_cat[col], 
                      order = df_cat[col].value_counts().index,
                      palette=self.palette)
             
            plt.rcParams.update({'font.size': 11})
            plt.xlabel(f"{col.replace('_', ' ').title()}", fontsize=15)
            plt.xticks(rotation = 8)
        
        plt.tight_layout()
        
        plt.savefig(f'1_results/5_categorical_attributes.jpeg')
