import pandas as pd
pd.set_option('display.max_columns', None)
data = pd.read_excel('nba_league_leaders.xlsx', engine='openpyxl')
print(data.sample(5))
