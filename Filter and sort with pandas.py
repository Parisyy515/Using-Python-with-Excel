import pandas as pd
from openpyxl.workbook import workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Address',
              'City', 'State', 'Area Code', 'Income']
# read the existing csv file and update its column


df['Tax%'] = df['Income'].apply(
    lambda x: .15 if 10000 < x < 40000 else .2 if 40000 < x < 80000 else .25)
# apple a new column using lambda to define its value


df['Taxs Owed'] = df['Income']*df['Tax%']
# create a new column based on mutiple values from other columns
# print(df['Taxs Owed'])


to_drop = ['City', 'State', 'Area Code', ]
df.drop(columns=to_drop, inplace=True)
# print(df)
# list out the columns you would like to drop


df['Test Col'] = False
df.loc[df['Income'] < 60000, 'Test Col'] = True
print(df)
# create a new column [Test Col] and give its value to False, change this value based on another value in this dataset


print(df.groupby(['Test Col']).mean())
# group by the two unique value in ['Test Col']; mean function take the average of all data in one group

print(df.groupby(['Test Col']).mean().sort_values('Income'))
# add sort function to group
