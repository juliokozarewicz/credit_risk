# local
from mongodb_connection import data_frame
from descriptive import Descriptive_stats
from config import main_variables
from config import style_graph, color1, color2, color3, color4, color5


# data base entry
# ----------------------------------------------------------------------------
db_raw = data_frame
# ----------------------------------------------------------------------------

# descriptive statistics
# ----------------------------------------------------------------------------
desc_stats = Descriptive_stats(db_raw,
                               main_variables = main_variables,
                               style_graph = style_graph,
                               color1 = color1, 
                               color2 = color2, 
                               color3 = color3, 
                               color4 = color4, 
                               color5 = color5)

desc_stats.describe_attributes()
desc_stats.graph_dependent_var()
desc_stats.statistic_data()
# ----------------------------------------------------------------------------
