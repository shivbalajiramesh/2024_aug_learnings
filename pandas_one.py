import pandas as pd
import os

path = os.getcwd()
print(f"Before {path}")
os.chdir('C:\\Users\\shivbalaji.ramesh\\OneDrive - CES Limited\\Desktop\\python\\pandas')
path = os.getcwd()
print(f"After {path}")


df = pd.read_csv('pokemon_data.csv')

'''
print('\n')
print(df.head(3))
print('\n')
print(df.tail(3))
print('\n')
print(df.columns)
print('\n')
print(df.columns[0:5])
print('\n')
print(df[['Name', 'Speed']])
print('\n')
print(df['Name'][0:5])
print('\n')
print(df.iloc[[1,5,6]])
print('\n')
print(df.iloc[1:8])
print('\n')
# Specific Location iloc[R, C]
print(df.iloc[1,5])
print('\n')
print(df.head(3))
print('\n')
#for index, row in df.iterrows():
#    print (index, row[['Name', 'Speed', 'Type 1']])
print('\n')
for i in df.itertuples():
    print (i[0:3])

print('\n')
print(df.describe())
print('\n')
print(df[df['Type 1'] == 'Fire'])

print(df.head(3))
print(df.sort_values(['Name', 'Type 2']))


print(df)
df2 = df
df2['Total'] = df['HP'] + df['Attack']
print(df2)

df2 = df
df3 = df2.drop(columns=['Generation', 'Legendary'])
print(df3)



df2 = df
df2['Total'] = df.loc[:, 'HP':'Speed'].sum(axis=1)


cols = list(df.columns.values)

#print(cols[0: 4])

df3 = df2[cols[0:4] + [cols[-1]] + cols[4:12]]
#print(df3)


try:
    df3.to_cs('new_file_two.')
except Exception as e:
    print(e)
else:
    print('New file created')
finally:
    print('This process is done.')

#print(df.head(30))

#print(type(df['Type 1'] == 'Grass'))
#print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])

#print(df.loc[~df['Name'].str.contains('Mega')])
'''

#print(df)

#print(df.groupby(['Type 1']).sum('HP')['HP'])

print(df[['HP','Attack']].min())

