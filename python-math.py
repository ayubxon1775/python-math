# Pythonda mashqlar, topshiriqlar va misollar

################# O'zgaruvchilar
#  1 "Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring

salom = 'Hello world'
# print(salom)

#  2 "xabar" deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring, keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.

xabar = 'Assalomu aleykum'
# print(xabar)
xabar = 'Hello world'
# print(xabar)

#  3'class' den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va konsolga chiqaring (siz kutgan natija chiqdimi?)

    # O'zgaruvchiga class deb nom berib bolmaydi chunki u maxsus kalit soz
# class = 'salom'
# print(class)

#  4
# radius = 5
# pi = 3.14159
# aylana_yuzi = pi * radius**2
# print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)

radius = 5
pi = 3.14159
aylana_yuzi = pi * radius**2
# print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)


############## String methodlar

# Quyidagi o'zgaruvchilarni yarating: 

# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor" 
# viloyat="Samarqand"

# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor" 
# viloyat="Samarqand"

# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati

# print(kocha + ' kochasi ' +  mahalla + ' mahallasi ' +  tuman + ' tumani ' + viloyat + ' viloyati ' )  

# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.

# kocha = input("ko'chasini kiriting ")
# mahalla = input("mahallasini kiriting ")
# tuman = input("tumanini kiriting ")
# viloyat = input("viloyatini kiriting ")

# print(kocha + ' kochasi ' +  mahalla + ' mahallasi ' +  tuman + ' tumani ' + viloyat + ' viloyati ' )  

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing

kocha = input("ko'chasini kiriting ")
mahalla = input("mahallasini kiriting ")
tuman = input("tumanini kiriting ")
viloyat = input("viloyatini kiriting ")

# print(kocha + ' kochasi,\n'  +  mahalla + ' mahallasi, \n' +  tuman + ' tumani \n' + viloyat + ' viloyati \n' )  


# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang

yangi_manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"

# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
print(yangi_manzil.upper())
print(yangi_manzil.lower())
print(yangi_manzil.title())
print(yangi_manzil.capitalize())





