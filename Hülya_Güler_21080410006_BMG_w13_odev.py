
def ogrenciKayıt(ogrenciSayac):
  sinav_sonuc = []

  sinav_sonuc.append({"isim":"Ayşe K.", "Cinsiyet":"K", "Matematik":"60", "Türkçe":"70"})
  sinav_sonuc.append({"isim":"Ahmet M.", "Cinsiyet":"E", "Matematik":"40", "Türkçe":"30"})
  sinav_sonuc.append({"isim":"Nuri C.", "Cinsiyet":"E", "Matematik":"97", "Türkçe":"23"})
  sinav_sonuc.append({"isim":"Nawar T.", "Cinsiyet":"E", "Matematik":"10", "Türkçe":"10"})
  sinav_sonuc.append({"isim":"Suzan T.", "Cinsiyet":"K", "Matematik":"56", "Türkçe":"78"})
  sinav_sonuc.append({"isim":"Nawar T.", "Cinsiyet":"K", "Matematik":"10", "Türkçe":"10"})
  sinav_sonuc.append({"isim":"Ala B.", "Cinsiyet":"K", "Matematik":"95", "Türkçe":"46"})
  



  for ogrenci in range(ogrenciSayac):
    isim = input("isim:")
    cinsiyet = input("cinsiyet:")
    Matematik = input("Matematik:")
    Türkçe = input("Türkçe:")
    sinav_sonuc.append({"isim":isim, "cinsiyet":cinsiyet, "Matematik":Matematik, "Türkçe":Türkçe })
  return sinav_sonuc



ogrenciSayac = input("Kaç öğrenci eklemek istersiniz:")
ogrenci = ogrenciKayıt(int(ogrenciSayac))
print("students:")
print(ogrenci)
