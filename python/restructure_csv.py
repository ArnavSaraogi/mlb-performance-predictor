"""
Turns stats_300.csv (downloaded from BaseballSavant) into out.csv.
Changes the csv from a long format to a wide format, with individual players representing 1 row with all their stats from 2021-2024.
Adds 3 columns for the OPS % change by year.
"""

import pandas as pd

stats_df = pd.read_csv('input_csvs/stats.csv')
babip_df = pd.read_csv('input_csvs/babip.csv')
hr_df = pd.concat([pd.read_csv('input_csvs/homeruns_2023.csv'), pd.read_csv('input_csvs/homeruns_2024.csv')])

stats_df = stats_df.pivot(index = ['player_id', 'last_name, first_name'], columns = 'year').dropna()
stats_df.columns = [f'{col[0]} ({col[1]})' for col in stats_df.columns]

babip_df = babip_df.pivot(index = ['player_id', 'last_name, first_name'], columns = 'year')
babip_df.columns = [f'{col[0]} ({col[1]})' for col in babip_df.columns]
babip_df = babip_df[babip_df.index.isin(stats_df.index)]
babip_df['babip_career'] = babip_df.mean(axis=1)
babip_df['babipdiff (2023)'] = babip_df['babip (2023)'] - babip_df['babip_career']
babip_df['babipdiff (2024)'] = babip_df['babip (2024)'] - babip_df['babip_career']

#Add HR Stat
hr_df = hr_df.pivot_table(index = 'player', columns = 'year', aggfunc = lambda x: '; '.join(x) if x.dtype == 'object' else x.sum()).dropna()
babip_df.columns = [f'{col[0]} ({col[1]})' for col in babip_df.columns]

hr_df.to_csv('test.csv')

stats_df[['babipdiff (2023)', 'babipdiff (2024)']] = babip_df[['babipdiff (2023)', 'babipdiff (2024)']]
stats_df['ops_change 2023-2024'] = stats_df[['on_base_plus_slg (2023)', 'on_base_plus_slg (2024)']].pct_change(axis = 1)['on_base_plus_slg (2024)']
stats_df['ops_change 2023-2024'] *= 100

stats_df.to_csv('out.csv')