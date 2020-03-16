import pandas as pd 
import numpy as np 
import xlsxwriter

#import data halodoc
#data_halodoc = 'data_halodoc.csv'
#df_halodoc = pd.read_csv(data_halodoc)
#df_halodoc = df_halodoc['PRODUCT_SKU']
#df_halodoc = df_halodoc.dropna(axis=0)
#df_halodoc = pd.to_numeric(df_halodoc, errors='coerce')

#import data apotik
df_apotik = pd.read_csv('xReport.csv', error_bad_lines=False, engine='python', delimiter=';')

#drugs data non-database
#obat_tambahan = 'obat_tambahan.csv'
#df2 = pd.read_csv(obat_tambahan)

#clean Unnamed columns
df_apotik = df_apotik.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 5','Unnamed: 5','Unnamed: 7'],axis=1)

#rename new columns
df_apotik.columns = ['Kode Item','Nama Item','Stok','Harga Pokok']

#convert decimal type of Harga Pokok to General
df_apotik['Harga Pokok'] = df_apotik['Harga Pokok'].astype(str).replace('\.','',regex=True)

#convert df_apotik type data to float
df_apotik['Kode Item'] = pd.to_numeric(df_apotik['Kode Item'], errors='coerce')
df_apotik['Harga Pokok'] = pd.to_numeric(df_apotik['Harga Pokok'], errors='coerce')
df_apotik['Stok'] = pd.to_numeric(df_apotik['Stok'], errors='coerce')

#clean Nan rows
df_apotik = df_apotik.dropna(axis=0)

#clean row index by 13
#df_apotik = df_apotik.drop([13],axis=0)

#clean value 0 in Harga Pokok column
df_apotik = df_apotik[df_apotik['Harga Pokok']!=0]

#reset index dataframe
df_apotik = df_apotik.reset_index(drop=True)

#replace pim-tra-col cheery
stok_pim_cherry = df_apotik.at[1734,"Stok"]
harga_pim_cherry = df_apotik.at[1734,"Harga Pokok"]
df_apotik =df_apotik.replace({"Kode Item": 2849},{"Kode Item":'HVJY2221'})
df_apotik.at[1635,"Stok"]=stok_pim_cherry
harga_pim_lem = df_apotik.at[1635,"Harga Pokok"]=harga_pim_cherry

#Adding other drugs
#df_apotik = df_apotik.append(z,ignore_index=True)
df_apotik.to_excel('combined_alammedika_0000000000.xlsx', index=False, header=True, encoding='utf-8', engine='xlsxwriter')
print("Updating Halodoc Items Have Done. (^oo^)")
#print(df_apotik.head(10))