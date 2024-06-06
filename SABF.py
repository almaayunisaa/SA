# Algoritma Brute Force
import csv
import pandas as pd
from operator import itemgetter
import time

data_BF=pd.read_csv(r"C:\Users\Alma\Documents\Kulyah\DataBF.csv")
data_BF=data_BF.drop('delisting_date', axis=1)
data_BF=data_BF.dropna()
nama_perusahaan=pd.read_csv(r"C:\Users\Alma\Documents\Kulyah\archive\List Emiten\all.csv")

def BF(data_BF):
    list_HargaLokal=[]
    list_Kenaikan=[]
    idxAwal=0
    idxAkhir=14
    i=0
    while i<len(data_BF):
        list_HargaLokal=[]
        code=data_BF.iloc[i]['Code']
        idxAkhir=idxAwal+14

        # Menghitung moving average per 15 data terurut datenya
        while idxAkhir<len(data_BF) and (data_BF.iloc[i]['Code'])==(data_BF.iloc[idxAkhir]['Code']):
            total_Harga=(data_BF[idxAwal:idxAkhir]['close'].sum())/15
            list_HargaLokal.append(total_Harga)
            idxAwal=idxAwal+1
            idxAkhir=idxAkhir+1

        hargaSaham=(data_BF.iloc[idxAkhir-1]['close'])
        kenaikan=0
        idxAwal_cek=0
        idxAkhir_cek=1

        #Hitung kenaikan per moving average
        while idxAkhir_cek<len(list_HargaLokal):
            if list_HargaLokal[idxAwal_cek]<list_HargaLokal[idxAkhir_cek]:
                kenaikan=kenaikan+1
            idxAwal_cek=idxAwal_cek+1
            idxAkhir_cek=idxAkhir_cek+1

        
        list_Kenaikan.append((code, kenaikan, hargaSaham))
        idxAwal=idxAkhir+1
        i=idxAkhir+1

    list_Kenaikan.sort(key=itemgetter(1), reverse=True)
    return (list_Kenaikan[:10])

def main():
    print("Masukkan Budget :")
    budget=float(input())
    print()
    namaHasil=[]
    start=time.time()
    codeHasil=BF(data_BF)
    end=time.time()
    for i in range(len(codeHasil)):
        namaHasil.append((nama_perusahaan[nama_perusahaan['code']==codeHasil[i][0]].values[0]))
    
    print("Top 10 Perusahaaan yang dapat dipilih")
    for i in range(len(namaHasil)):
        print("Nama Perusahaan               : ", namaHasil[i][1])
        print("Lembar (maksimal)             : ", int(budget/codeHasil[i][2]), " lembar")
        print("Harga Saham (yang terdata)    : ", codeHasil[i][2])
        print()
    print("Waktu :", (end-start)*1000)

main()


        
        