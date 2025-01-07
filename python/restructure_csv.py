"""
Turns stats_300.csv into out.csv.
Changes the csv from a long format to a wide format, with individual players representing 1 row with all their stats from 2021-2024.
Adds 3 columns for the OPS % change by year.
"""

import pandas as pd

df = pd.read_csv('stats_300.csv')
df = df.pivot(index = ['player_id', 'last_name, first_name'], columns = 'year').dropna()
df.columns = [f"{col[0]} ({col[1]})" for col in df.columns]

df['ops_change 2021-2022'] = df[['on_base_plus_slg (2021)', 'on_base_plus_slg (2022)']].pct_change(axis = 1)['on_base_plus_slg (2022)']
df['ops_change 2021-2022'] *= 100
df['ops_change 2022-2023'] = df[['on_base_plus_slg (2022)', 'on_base_plus_slg (2023)']].pct_change(axis = 1)['on_base_plus_slg (2023)']
df['ops_change 2022-2023'] *= 100
df['ops_change 2023-2024'] = df[['on_base_plus_slg (2023)', 'on_base_plus_slg (2024)']].pct_change(axis = 1)['on_base_plus_slg (2024)']
df['ops_change 2023-2024'] *= 100

df.to_csv('out.csv')
