import csv
import pandas as pd
from operator import itemgetter
import time

data_Greedy=pd.read_csv(r"C:\Users\Alma\Documents\Kulyah\DataBF.csv")
data_Greedy=data_Greedy.drop('delisting_date', axis=1)
data_Greedy=data_Greedy.dropna()

data_Greedy=data_Greedy[data_Greedy['date'].str[:4]=='2019']
data_Greedy = data_Greedy.groupby('Code').apply(lambda x: x.head(1)).reset_index(drop=True)
nama_perusahaan=pd.read_csv(r"C:\Users\Alma\Documents\Kulyah\archive\List Emiten\all.csv")

def GreedyHarga(data_Greedy):
    hasil_frekuensi=[]
    hasil=[]
    Harga_Greedy=data_Greedy.sort_values(by='frequency', ascending=False) # Mencari frekuensi pasar terbesar
    for i in range(300):
        hasil_frekuensi.append((Harga_Greedy.iloc[i]['close'], Harga_Greedy.iloc[i]['Code']))
    hasil_frekuensi=sorted(hasil_frekuensi, key=itemgetter(0)) # Mencari harga saham paling rendah
    for i in range(10):
        hasil.append((hasil_frekuensi[i][0], hasil_frekuensi[i][1]))
    return hasil

def GetHargaSahamNew(code):
    data_Greedy=pd.read_csv(r"C:\Users\Alma\Documents\Kulyah\DataBF.csv")
    data_Greedy=data_Greedy.drop('delisting_date', axis=1)
    data_Greedy=data_Greedy.dropna()
    data_Greedy = data_Greedy[(data_Greedy['Code'] == code)]
    if not data_Greedy[(data_Greedy['date'].str[:4] == '2024')].empty:
        data_Greedy = data_Greedy[(data_Greedy['date'].str[:4] == '2024')]
    elif not data_Greedy[(data_Greedy['date'].str[:4] == '2023')].empty:
        data_Greedy = data_Greedy[(data_Greedy['date'].str[:4] == '2023')]
    elif not data_Greedy[(data_Greedy['date'].str[:4] == '2022')].empty:
        data_Greedy = data_Greedy[(data_Greedy['date'].str[:4] == '2022')]
    elif not data_Greedy[(data_Greedy['date'].str[:4] == '2021')].empty:
        data_Greedy = data_Greedy[(data_Greedy['date'].str[:4] == '2021')]
    elif not data_Greedy[(data_Greedy['date'].str[:4] == '2020')].empty:
        data_Greedy = data_Greedy[(data_Greedy['date'].str[:4] == '2020')]
    elif not data_Greedy[(data_Greedy['date'].str[:4] == '2019')].empty:
        data_Greedy = data_Greedy[(data_Greedy['date'].str[:4] == '2019')]
    return data_Greedy.iloc[-1, 6]

def main():
    print("Masukkan Budget :")
    budget=float(input())
    print()
    namaHasil=[]
    hargaHasil=[]
    start=time.time()
    result=GreedyHarga(data_Greedy)
    end=time.time()
    for i in range(len(result)):
        namaHasil.append(nama_perusahaan[nama_perusahaan['code']==result[i][1]]['name'].values[0])
        hargaHasil.append(GetHargaSahamNew(result[i][1]))
    
    print("Top 10 Perusahaaan yang dapat dipilih")
    for i in range(len(namaHasil)):
        print("Nama Perusahaan               : ", namaHasil[i])
        print("Lembar (maksimal)             : ", int(budget/hargaHasil[i]), " lot")
        print("Harga Saham (terbaru)         : ", hargaHasil[i])
        print()
    print("Waktu :", (end-start)*1000)

main()