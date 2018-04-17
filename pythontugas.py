#PROGRAM MENGHITUNG NILAI MAHASISWA
print "\n PROGRAM PYTHON MENGHITUNG NILAI MAHASISWA \n<><><><><><><><><><><><><><><><><><><><><><><><><><><>\n"
nama  = raw_input("masukan nama anda : ")
uas   = input(" masukkan nilai UAS anda : ")
uts   = input("masukkan nilai UTS anda : ")
quis  = input("masukkan nilai Quis anda : ")
final = input (" masukkan nilai final anda :")
print "\n HASIL NILAI AKHIR MAHASISWA \n<><><><><><><><><><><><><><><><><><><><><><><><>\n"
print "NAMA ANDA ADALAH        : %s"%nama
print "NILAI UAS ANDA ADALAH   : %d"%uas
print "NILAI UTS ANDA ADALAH   : %d"%uts
print "NILAI QUIS ANDA ADALAH  : %d"%quis
print "NILAI FINAL ANDA ADALAH : %d"%final

nilai = uas+uts+quis+final
print "JUMLAH NILAI ANDA SENUA : %d"%nilai
print "NILAI HURUF ANDA ADALAH : "

if nilai >= 80 :
    print "A"

elif nilai >= 70 :
    print "B"

elif nilai >= 60 :
    print "C"

elif nilai >= 40 :
    print "D"

elif nilai <= 30 :
    print "E"

if nilai <= 60 :
    print "KETERANGAN : TIDAK LULUS"
else :
    print "KETERANGAN : LULUS"

