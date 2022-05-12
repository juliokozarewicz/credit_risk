from pandas import DataFrame, read_csv, crosstab
from seaborn import countplot, heatmap
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
            plt.xlabel(f"{col.replace('_', ' ').lower()}", fontsize=15)
            plt.xticks(rotation = 8)
        
        plt.tight_layout()
        
        plt.savefig(f'1_results/6_categorical_attributes.jpeg')
        
        return


    def numeric_plot(self):
        """
        Plotting the information of the numeric variables.
        """
        
        df_numeric = DataFrame(self.data_frame).drop("_id", axis=1)
        df_numb = df_numeric.select_dtypes(include=['float64', 'int64'])
        
        fig, ax = plt.subplots(figsize=(18, 10), dpi=600)
        
        numb_plot = 0
        
        for col in df_numb:
            
            # count
            numb_plot += 1
            
            # plot
            plt.subplot(2, 4, numb_plot)
            
            plt.hist(x=df_numb[col],
                     density=True,
                     color=self.color1,
                     ec=self.color3) 
            
            plt.rcParams.update({'font.size': 11})
            plt.xlabel(f"{col.replace('_', ' ').lower()}", fontsize=15)
            plt.xticks(rotation = 8)
            plt.ticklabel_format(style='plain')
        
        plt.tight_layout() 
        plt.savefig(f'1_results/7_numeric_attributes.jpeg')
        
        return


    def correlation(self):
        """
        Information on the correlation between the variables.
        """
        
        df_correl = DataFrame(self.data_frame).drop(['_id'], axis=1).corr()
        
        plt.style.use(self.style_graph)
        fig, ax = plt.subplots(figsize=(18, 10), dpi=600)
        
        heatmap(df_correl, annot=True, cmap='Pastel2', linewidths=2)
        
        plt.rcParams.update({'font.size': 11})
        plt.xticks(rotation = 30) 
        plt.tight_layout() 
        plt.savefig(f'1_results/8_correlation.jpeg')
        
        return


    def insights(self):
        """
        Understanding of specific causes and effects within the context of the data.
        """
        
        df_insight = DataFrame(self.data_frame).drop(['_id'], axis=1)
        
        df_select = df_insight.groupby(by='loan_grade').median()
        
        lis_col_select = ['person_income', 'loan_amnt', 'loan_int_rate',
                                   'loan_status', 'loan_percent_income']
        
        df_select = df_select[lis_col_select]
        
        df_select.to_csv('1_results/9_insights.txt', sep='|')
        
        with open('1_results/9_insights.txt', 'r') as txt:
            txt = txt.readlines()
            txt.insert(1, f"{'|-' * (len(df_select.columns) - 1)}")
            txt[1] = f'{txt[1]}|-\n'
        
        with open('1_results/9_insights.txt', 'w') as txt2:
            for line in txt:
                txt2.write(line)
        
        loan_grade = crosstab(df_insight['loan_grade'],
                              df_insight['loan_status'],
                              margins=True)
        
        loan_grade.columns = ['not_default', 'default', 'all']
        
        percent_def = (loan_grade['default'] / loan_grade['all']) * 100
        
        percent_def = percent_def.map(lambda x: f'{x:.2f} %')
        
        loan_grade['percent_default'] = percent_def
        
        loan_grade.to_csv('1_results/9_insights_2.txt', 
                          sep='|', 
                          index='loan_grade',
                          float_format = '%.2f')
        
        with open('1_results/9_insights_2.txt', 'r') as txt:
            txt = txt.readlines()
            txt.insert(1, f"{'|-' * (len(loan_grade.columns))}")
            txt[1] = f'{txt[1]}|-\n'
        
        with open('1_results/9_insights_2.txt', 'w') as txt2:
            for line in txt:
                txt2.write(line)
        
        return
