from pandas import DataFrame
from config import client, data_base, collection
from config import main_variables
from config import style_graph, palette, color1, color2, color3, color4, color5
from mongodb_connection import Connection_mongodb
from data_cleansing import Data_cleansing 
from descriptive import Descriptive_stats
from pathlib import Path
from exploratory_analysis import Exploratory_analysis, Hypotheses
from pre_process import Pre_processing


# make dir
# ----------------------------------------------------------------------------
Path('./1_results').mkdir(exist_ok=True)
# ----------------------------------------------------------------------------

# data cleansing
# ----------------------------------------------------------------------------
db_cleansing = Data_cleansing(

                    client,
                    data_base,
                    collection,
                    style_graph = style_graph,
                    palette = palette,
                    color1 = color1,
                    color2 = color2, 
                    color3 = color3,
                    color4 = color4, 
                    color5 = color5

)

db_cleansing.copy_db_bkp()
db_cleansing.data_cleansing_nan()
db_cleansing.box_plot()
db_cleansing.data_cleansing_outlier()
# ----------------------------------------------------------------------------

# data base entry
# ----------------------------------------------------------------------------
data_input = Connection_mongodb(

                    client, 
                    data_base,
                    collection

)

data_frame = data_input.all_data()
db_raw = DataFrame(data_frame)
# ----------------------------------------------------------------------------

# descriptive statistics
# ----------------------------------------------------------------------------
desc_stats = Descriptive_stats(

                    db_raw,
                    main_variables = main_variables,
                    style_graph = style_graph,
                    color1 = color1,
                    color2 = color2, 
                    color3 = color3,
                    color4 = color4, 
                    color5 = color5

)

desc_stats.sample_dataframe()
desc_stats.describe_attributes()
desc_stats.graph_dependent_var()
desc_stats.statistic_data()
# ----------------------------------------------------------------------------

# exploratory analysis
# ----------------------------------------------------------------------------
explorat_analysis = Exploratory_analysis(

                    db_raw,
                    main_variables = main_variables,
                    style_graph = style_graph,
                    palette = palette,
                    color1 = color1,
                    color2 = color2, 
                    color3 = color3,
                    color4 = color4, 
                    color5 = color5

)

explorat_analysis.categorical_plot()
explorat_analysis.numeric_plot()
explorat_analysis.correlation()
explorat_analysis.insights()
# ----------------------------------------------------------------------------

# Hypotheses
# ----------------------------------------------------------------------------
hip_test = Hypotheses(

                    db_raw, main_variables = main_variables,
                    style_graph = style_graph,
                    palette = palette,
                    color1 = color1,
                    color2 = color2, 
                    color3 = color3,
                    color4 = color4, 
                    color5 = color5

)

hip_test.h1()
hip_test.h2()
hip_test.h3()
hip_test.h4()
hip_test.h5()
hip_test.h6()
hip_test.h7()
hip_test.h8()
# ----------------------------------------------------------------------------

# pre process
# ----------------------------------------------------------------------------
pre_process = Pre_processing(

                    db_raw,
                    client, 
                    data_base,
                    collection

)

pre_process.data_scaling()
# ----------------------------------------------------------------------------
