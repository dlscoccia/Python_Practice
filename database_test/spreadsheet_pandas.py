#!/usr/bin/python3
import pandas as pd

excel_csv_path = "~/Repositories/Python-Test/database_test/contratos.csv"
df = pd.read_csv(excel_csv_path)
# df_info = df.info()
# print(df_info)
# print(df.describe())
# max = df['metros_lineal'].describe()
#print(max)

# group_df = df.groupby(['motor_speed']).max()
# print(group_df['pm'])

'''
Following will return every column of df with profile_id == 4
'''
terbys = df[df['marmolero'] == "TERBYS"]
print(terbys)

roberto = df[df['marmolero'] == "ROBERTO"]
print(roberto)

df.plot(kind='bar', stacked=True, title="The title of my graph")