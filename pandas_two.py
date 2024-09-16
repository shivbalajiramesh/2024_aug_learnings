import os

#print(os.getcwd())

os.chdir('C:\\Users\\shivbalaji.ramesh\\OneDrive - CES Limited\\Desktop\\python\\pandas_two')

#print(os.getcwd())

import pandas as pd

df = pd.read_csv('survey_results_public.csv')
#print(type(df.shape))
#print(df.info())

#print(df.head(5))
#print(df.columns.values)

s_df = pd.read_csv('survey_results_schema.csv')

#print(s_df.head(5))
#print(s_df.shape)
#print(s_df.info())

#print(s_df.loc[s_df['Column'] == 'Hobbyist'])


my_dict = {
    'First': ['Corey', 'Jane', 'John']
    ,'Last': ['Schafer', 'Doe', 'Doe']
    ,'Email': ['coreyschafer@email.com', 'jandoe@email.com', 'johndoe@email.com']
}

small_df = pd.DataFrame(my_dict)

print('\nHello World!\n')
'''
#print('\n')
#print(small_df)
#print('\n')

#print(type(small_df['Email']))

print('\n')

print(small_df[['First', 'Email']])

print('\n')

print(type(small_df.loc[0]))


print(df.head(3))

#print((df['Hobbyist'] == 'Yes')) #.value_counts())

#print(df.loc[0:3,'Respondent':'Hobbyist'])

print(small_df)

small_df.set_index('Email', inplace = True)

print(small_df)

small_df.reset_index(inplace = True)

print(small_df)

print(s_df)

print(s_df.loc[s_df['Column'] == 'MgrIdiot', 'QuestionText'])

print(s_df.sort_values('Column', ascending=False))

print(small_df['Last'].str.contains('Doe', case=False))

print(small_df.loc[small_df['Last'].str.contains('Doe', case=False)])

print(small_df.loc[~((small_df['Last'] == 'Doe') & (small_df['First'] == 'Jane'))])



print(s_df['Column'].str.contains('salary', case=False))

print(s_df.loc[s_df['Column'].str.contains('converted', case=False)])

print(df.loc[df['ConvertedComp'] > 100000, ['Country', 'LanguageWorkedWith', 'ConvertedComp']])

df2 = df.loc[df['ConvertedComp'] > 100000, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]

print(df2.loc[(df2['Country'] == 'United States') | (df2['Country'] == 'Canada') | (df2['Country'] == 'India')])


country_list = ['United States', 'India', 'Canada']

country_filter = df2['Country'].isin(country_list)

print(df2.loc[country_filter])



#print(small_df)

small_df.columns = ['first_name', 'last_name', 'email']

small_df.columns = [i.upper() for i in small_df.columns]

#print(small_df.columns.str.replace('_', '%'))

small_df.columns = [i.lower() for i in small_df.columns]

#print(small_df.columns[0])

new_df = small_df.rename({'first_name': 'f'})

print(new_df)


#print(small_df)

print(small_df)
print(small_df.loc[2, 'Last'])

small_df.loc[2, ['Last', 'Email']] = ['Smith', 'johnsmith@email.com']

print(small_df, '\n')

small_df['Email'] = small_df['Email'].str.upper()

print(small_df, '\n')

for i in small_df.itertuples():
    print(i[3])

print(small_df, '\n')

def update_email(em):
    return em.upper()

print(small_df['Email'].apply(update_email())) --Why we should not put paranthesis for update_email?

print(small_df['Email'].apply(lambda x:x.upper()))

small_df['Number_test'] = 1
small_df.loc[1, 'Number_test'] = 2
small_df.loc[2, 'Number_test'] = 3

print(small_df['Number_test'].apply(lambda x : x**2))
print(small_df, '\n')



print('\n', small_df, '\n')

#print(small_df['Email'].str.len())

#print(small_df['Email'].apply(len))

#print(small_df.apply(len))

#apply method works on individual elements in a pandas series and it works on individual series in a pandas dataframe

#applymap works only for dataframes
#print(small_df.applymap(len))
#print(small_df.applymap(str.lower))


print(small_df['First'].map({'Corey': 'Chris', 'Jane': 'Mary'}))
print(small_df['First'].replace({'Corey': 'Chris', 'Jane': 'Mary'}))

print(df.columns)
df.rename({'ConvertedComp': 'Salary'}, axis=1, inplace = True)
#df.rename(columns = {'ConvertedComp': 'Salary'}, inplace = True)
print(df.columns)

#print(df.head(3))

#df['Hobbyist'] = df['Hobbyist'].replace({'Yes': True, 'No': False})

#df['Hobbyist'] = df['Hobbyist'].map({'Yes': True, 'No': False})
#print(df.head(3))

print(df['WorkLoc'].unique())


print(small_df)

small_df['Name'] = small_df['First'] +' '+ small_df['Last']

print(small_df)

small_df.drop(columns=['Name'], inplace=True)

print(small_df)


small_df['Name'] = small_df['First'] +' '+ small_df['Last']
#print(small_df['Name'].str.split(expand=True))

#print(small_df['Name'].str.split(expand=True)[0])

small_df['F'] = small_df['Name'].str.split(expand=True)[0]
small_df['L'] = small_df['Name'].str.split(expand=True)[1]

#print(small_df)

avengers = {
    'First':['Tony', 'Steve']
    ,'Last':['Stark', 'Rogers']
    ,'Email': ['ironman@avengers.com', 'cap@avengers.com']
}
small_df2 = pd.DataFrame(avengers)
#print(small_df2)

#print(pd.concat([small_df, small_df2]))

newdf = pd.concat([small_df, small_df2])

newdf.reset_index(drop=True, inplace=True)

#print(newdf)

rows_to_drop = newdf.loc[newdf['Last'] == 'Doe'].index

newdf.drop(index=rows_to_drop, inplace=True)

print(newdf)


print(small_df)

print(small_df.sort_values(by = ['Last', 'First'], ascending = [False, True]))

#print(small_df.sort_index(ascending=True, axis=1))
'''


#print(df.sort_values(by = ['Country', 'ConvertedComp'], ascending=True)[['Country', 'ConvertedComp']])


#print(df['ConvertedComp'].nlargest(10))

#print(df.nlargest(10, 'ConvertedComp'))

print(df.nsmallest(10, 'ConvertedComp'))