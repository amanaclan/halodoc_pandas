import pandas as pd 
import numpy as np 

#import data halodoc
#data_halodoc = 'data_halodoc.csv'
#df_halodoc = pd.read_csv(data_halodoc)
#df_halodoc = df_halodoc['PRODUCT_SKU']
#df_halodoc = df_halodoc.dropna(axis=0)
#df_halodoc = pd.to_numeric(df_halodoc, errors='coerce')

#import data apotik
data_apotik = 'xReport.csv'
df_apotik = pd.read_csv(data_apotik)

#drugs data non-database
obat_tambahan = 'obat_tambahan.csv'
df2 = pd.read_csv(obat_tambahan)

#clean Unnamed columns
df_apotik = df_apotik.drop(['Unnamed: 0','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 7',
                            'Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13',
                            'Unnamed: 15','Unnamed: 17','Unnamed: 18'],axis=1)
#rename new columns
df_apotik.columns = ['Kode Item','Nama Item','Stok','Harga Pokok']

#conver df_apotik type data to float
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

#Tambahkan obat yang diubah
#df_apotik = df_apotik.append(z,ignore_index=True)
df_apotik.to_excel('combined_alammedika_0000000000.xlsx', index=False, header=True)
print("Updating Halodoc Items Have Done. (^oo^)")
#print(df_apotik)
