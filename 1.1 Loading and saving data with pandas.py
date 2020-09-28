import pandas as pd
from openpyxl.workbook import workbook

df_excel = pd.read_excel('regions.xlsx')
df_csv = pd.read_csv('Names.csv')
df_txt = pd.read_csv('data.txt')
# panda can read cvs file or excel file

df_txt = pd.read_csv('data.txt', delimiter='\t')
# panda read text file, seperate by '\t'

df_csv = pd.read_csv('Names.csv', header=None)
# outline a header when there is not one
# in the parenthesis, we need to specify the file directory, include only file name when file is located in working directory)

print(df_csv)
# print out the file for the

df_csv.columns = ['First', 'Last', 'Address',
                  'City', 'State', 'Area Code', 'Income']
df_csv.to_excel('Modified.xlsx')
# update the columns header in exsiting csv file and save it into a new excel file
