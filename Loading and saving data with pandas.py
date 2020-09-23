import pandas as pd
from openpyxl.workbook import workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Address',
              'City', 'State', 'Area Code', 'Income']
# read the existing scv file and update its column

print(df.columns)
# print all columns

print(df['First'])
# print out its first column header being New1

print(df[['First', 'Last']])
# print out its two column using double square bracket

print(df['First'][0:2])
# print out its first column and the first 5 rows of records using slicing

wanted_value = df[['First', 'Last', 'Address']]
stored = wanted_value.to_excel('First3Column.xlsx')
# select the first three columns and save it in a new file


print(df.loc[df['City'] == 'Riverside'])
# identify rows on the singular value in the column using data frame location function
print(df.loc[(df['City'] == 'Riverside') & (df['First'] == 'John')])
# identify rows on the singular value in the column using data frame location function with mutiple condition
