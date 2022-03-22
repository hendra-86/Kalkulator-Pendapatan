import os   #import library os

#cetak kata ""Program Penghitung Pendapatan Per Tahun"
print("Program Penghitung Pendapatan Per Tahun")

#tempat menyimpan array pendapatan per bulan
pendapatan=[]
#dekalarasi total = 0
total=0

#================ code untuk melakukan looping, yg dimana akan melooping sebanyak 12 kali dan menginputkan pendapatan
for i in range(0,12):
    bulan = input(f"Masukkan Pendapatan pada bulan ke-{i+1} = ")
    pendapatan.append(bulan)    #memasukkan hasil inputan ke array
    total=float(total)+float(bulan) #rumus menghitung total
    os.system('cls')    #clear screen

j=1 #deklarasi j=1

#looping lagi untuk mencetak hasil yg ada di array
for i in pendapatan:
    
    print(f"Pendapatan Pada Bulan ke - {j}",i)
    j+=1
print("Total pendapatan dalam 1 tahun = ",total)    #cetak total

rata_per_tahun = float(total) / float(12)   #rumus rata-rata per tahun memakai tipe data float
print("Rata - rata per tahun = ", rata_per_tahun)   #cetak hasil rata-rata per tahun

persen_per_tahun = (float(12) / float(total)) * 100 #rumus persentase rata-rata pertahun
print("Persentase pendapatan pertahun = ", persen_per_tahun, "%")   #cetak hasil persentase rata2 pertahun

#perulangan while
while(True):
    pilih_bulan = input("pilih pendapatan bulan ke berapa = ")  #menginputkan pemilihan bulan ke berapa
    pilih_bulan=int(pilih_bulan)    #deklarasi pilih_bulan ke integer
    pilih_bulan-=1  #pilih_bulan - 1
    hasil_bulan = pendapatan[pilih_bulan]   #mengambil nilai pada array sesuai inputan
    persen_per_bulan = (float(hasil_bulan)/float(total))*100    #rumus menghitung persentase pendapatan per bulan
    pilih_bulan+=1  #pilih_bulan + 1
    print(f"Hasil persentase pendapatan pada bulan ke - {pilih_bulan} = ", persen_per_bulan, "%")   #cetak hasil persentase per bulan
    jawab=input("Mau menghitung ulang persentase per bulan (y/n) : ")   #menginputkan y/n untuk terus mengecek atau berhenti 
    #apabila memilih y or Y maka program akan melooping lagi pada looping while
    if(jawab=="y" or jawab=="Y"):
        continue
    #apabila memilih huruf selain y or Y maka program berhenti
    else:
        break