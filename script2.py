# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# pd.set_option('display.max_columns', None)

# data = pd.read_excel('nba_league_leaders.xlsx')

# data.sample(5)

# data_number = int(input("Please enter number of data you want : "))
# data.sample(data_number)

import pandas as pd
pd.set_option('display.max_columns', None)
data = pd.read_excel('nba_league_leaders.xlsx', engine='openpyxl')
data.sample(5)
