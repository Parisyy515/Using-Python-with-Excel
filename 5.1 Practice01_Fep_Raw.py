import os

import pandas as pd

a = ['AAB', 'AHUT', 'AMR', 'BCS', 'CBP', 'CCS', 'CDC10', 'COL',
     'FUA30', 'FUM30', 'LBP', 'PPC1', 'SPCB', 'UOPC', 'W156', 'PCR']


def load_all(files):
    all_data = pd.DataFrame()

    # load all raw measure rate together and save in one excel sheet
    for file in files:
        if file.endswith('.xlsx'):
            df = pd.read_excel(file)
            df['filename'] = file
            all_data = all_data.append(df)
    all_data.to_excel('FEP_Raw_0.xlsx')

    # add header, file name, oragnize the key elements
    final = pd.read_excel('FEP_Raw_0.xlsx')
    final.columns = ['A', 'B', 'PlanCode', 'ReportMeasureID', 'E', 'F', 'G', 'H', 'I', 'J', 'MeasureID',
                     'L', 'M', 'N', 'O', 'Denominator', 'Numerator', 'R', 'S', 'T', 'Measure_Rate', 'V', 'W', 'Filename']
    final["Measure_Rate"] = final["Measure_Rate"]*100
    final['Flag'] = final['MeasureID'].apply(lambda x: 'Y' if x in a else 'N')
    f = final[['PlanCode', 'ReportMeasureID', 'MeasureID',
               'Denominator', 'Numerator', 'Measure_Rate', 'Filename', 'Flag']]
    stored = f.to_excel('FEP_Raw_1.xlsx')

    # filter on only the star measure by using the flag
    df1 = pd.read_excel('FEP_Raw_1.xlsx')
    df1 = df1.loc[df1['Flag'] == 'Y']

    # clean up
    to_drop = ['Flag', 'Unnamed: 0']
    df1.drop(columns=to_drop, inplace=True)
    df1.to_excel('FEP_Raw_1.xlsx')


def data_format(t):
    df_excel = pd.read_excel(t)
    df_excel.columns = ['', 'PlanCode', 'ReportMeasureID', 'MeasureID',
                        'Denominator', 'Numerator',  'Measure_Rate', 'Filename']
    df_excel['PopulationName'] = df_excel['PlanCode'].apply(lambda x: 'FEP PPO MD' if x == 190690
                                                            else 'FEP PPO DC')
    df_excel['ReportMonth'] = df_excel['Filename'].apply(lambda x: 'July 2020' if x[0:2] == '07'
                                                         else 'June 2020' if x[0:2] == '06'
                                                         else 'May 2020' if x[0:2] == '05'
                                                         else 'August 2020' if x[0:2] == '08' else 'other')
    df_excel['RunDate'] = df_excel['Filename'].apply(lambda x: '07/15/2020' if x[0:2] == '07'
                                                     else '06/15/2020' if x[0:2] == '06'
                                                     else '05/15/2020' if x[0:2] == '05'
                                                     else '08/15/2020' if x[0:2] == '08' else 'other')
    df_excel['SubmissionYear'] = '2021'
    df_excel['MeasurementYear'] = '2020'
    df_excel['Observed_Count'] = ''
    df_excel['Expected_Count'] = ''
    df_excel['OE_Ratio'] = ''
    df_excel['CurrentFlag'] = ''
    df_excel['Additional1'] = ''
    df_excel['Additional2'] = ''
    df_excel['Additional3'] = ''

    to_drop = ['PlanCode', '']
    df_excel.drop(columns=to_drop, inplace=True)

    # reorder the column in the final file
    df_excel = df_excel[['PopulationName', 'SubmissionYear', 'MeasurementYear', 'ReportMonth', 'RunDate', 'ReportMeasureID', 'MeasureID', 'Denominator',
                         'Numerator', 'Measure_Rate', 'Observed_Count', 'Expected_Count', 'OE_Ratio', 'CurrentFlag', 'Additional1', 'Additional2', 'Additional3']]
    df_excel.to_excel('FEP_Raw_Final.xlsx')


def main():
    # Step 1: grab all files name from the name.xlsx and load name into a list
    files = []
    wb = load_workbook('name.xlsx')
    ws = wb.active
    for row in ws.values:
        for value in row:
            files.append(value)

    # Step 2: load all files into one basic excel sheet
    load_all(files)

    # Step 3: format the one final excel sheet, clean up
    data_format('FEP_Raw_1.xlsx')
    os.remove('FEP_Raw_1.xlsx')
    os.remove('FEP_Raw_0.xlsx')


main()
