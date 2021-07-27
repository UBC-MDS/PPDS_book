import pandas as pd

pd.set_option('display.max_rows', 100)

df = pd.read_csv('cereal.csv', index_col=0)

df = df.loc[:,['mfr','sugars']]

df.groupby('mfr').get_group('K')

candy = pd.read_csv('../../../../data/candybars.csv', index_col=0)
candy

candy2 = pd.read_csv('../../../../data/candybars2.csv', index_col=0)
candy2_sorted= candy2.sort_values('calories')
candy2_sorted

pd.concat([candy, candy2_sorted], axis=0).head(20)

df = pd.read_csv('cereal.csv')

# Read in the dataset 
hockey_players = pd.read_csv('../../../../data/canucks.csv')


# Display the dataframe
hockey_players.head()

list(hockey_players.columns)

columns_hockey = hockey_players.columns 

list(columns_hockey)

hockey_shape = hockey_players.shape

hockey_shape

hockey_players

df[['calories','fiber']]

penalty_players = hockey_players.loc[[10, 21, 2], ['Height', 'Weight', 'Salary', 'Country']]


penalty_players.shape

penalty_players.columns

penalty_players.index

star_players = hockey_players.loc[7:19, 'Player':'Country']

# Display it

star_players


star_players.shape

star_players.index

benched_players = hockey_players.loc[3:9]

# Display it

benched_players

benched_players.shape

rich_players = hockey_players.sort_values(by='Salary', ascending=False)

# Display it

rich_players

rich_players.index

