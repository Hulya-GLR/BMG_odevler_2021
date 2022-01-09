sinav_sonuc = {"isim" :["Ayşe K.","Ahmet M.","Nuri C.","Nawar C.","Suzan T.","Ala B."],
"cinsiyet": ["Kadın","Erkek","Erkek","Erkek","Kadın","Kadın"],
"matematik":["60","40","97","45","56","95"],
"türkçe" : ["70","30","23","80","78","46"]
}
ortalamaKadin = sinav_sonuc["matematik"][1] + sinav_sonuc["matematik"][5] + sinav_sonuc["matematik"][6] / 3 
print(ortalamaKadin)

ortalamaErkek = sinav_sonuc["matematik"][2] + sinav_sonuc["matematik"][3]+ sinav_sonuc["matematik"][4]
print(ortalamaErkek)

maksKadin = max(sinav_sonuc["türkçe"][1],sinav_sonuc["türkçe"][5],sinav_sonuc["türkçe"][6])
print(maksKadin)

maksErkek = max(sinav_sonuc["türkçe"][2],sinav_sonuc["türkçe"][3],sinav_sonuc["türkçe"][4])
print(maksErkek)
