kisiler = []
for kisi in kisiler:
  print(kisiler)

#listeye üç eleman ekleme
kisi1 = kisiler.append(input("1. Kişi: "))
kisi2 = kisiler.append(input("2. kişi: "))
kisi3 = kisiler.append(input("3. kişi: "))
print(kisiler)#listeyi yazdırma
uzunluk = len(kisiler) 
print("listenin uzunluğu: ",uzunluk) #listenin uzunlugunu yazdırma
print("listenin ikinci elemanı: ",kisiler[1]) #listenin ikinci elemanının yazdırma
kisiler.pop() #pop metodu içine index belirtilmezse son elemanı siler
print(kisiler)#listenin son halini yazdırdım