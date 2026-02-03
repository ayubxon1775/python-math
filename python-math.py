# Pythonda mashqlar, topshiriqlar va misollar

################# O'zgaruvchilar
#  1 "Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring

# salom = 'Hello world'
# print(salom)

#  2 "xabar" deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring, keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.

# xabar = 'Assalomu aleykum'
# print(xabar)
# xabar = 'Hello world'
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

# radius = 5
# pi = 3.14159
# aylana_yuzi = pi * radius**2
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

# kocha = input("ko'chasini kiriting ")
# mahalla = input("mahallasini kiriting ")
# tuman = input("tumanini kiriting ")
# viloyat = input("viloyatini kiriting ")

# print(kocha + ' kochasi,\n'  +  mahalla + ' mahallasi, \n' +  tuman + ' tumani \n' + viloyat + ' viloyati \n' )  


# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang

# yangi_manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"

# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
# print(yangi_manzil.upper())
# print(yangi_manzil.lower())
# print(yangi_manzil.title())
# print(yangi_manzil.capitalize())


################# Sonlar

# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur

# son_kirit = int(input('Son kiriting >>> '))

# print(f'{son_kirit} ning kvadrati {son_kirit**2} ga teng')
# print(f'{son_kirit} ning kubi {son_kirit**3} ga teng')

# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur

# yosh = int(input('Yoshingizni kiriting: '))

# print(f"Siz {2026-yosh} da tug'ilgansiz")

# Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur

# son1 = int(input('1-sonni kiriting: '))
# son2 = int(input('2-sonni kiriting: '))

# print(f'{son1} + {son2} = {son1+son2}')
# print(f'{son1} - {son2} = {son1-son2}')
# print(f'{son1} * {son2} = {son1*son2}')
# print(f'{son1} / {son2} = {son1/son2}')

########### list (Ro'yxat)

# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting

ismlar = ['abdulbosit', 'akramjon', 'abdushohid', 'abdurrohman']

# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 

# print(f"Salom {ismlar[0].title()} bugun ko'rishamizmi")
# print(f"Salom {ismlar[1].title()} bugun ko'rishamizmi")
# print(f"Salom {ismlar[2].title()} bugun ko'rishamizmi")
# print(f"Salom {ismlar[0].title()} bugun ko'rishamizmi")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 

sonlar = [15, 1, -5, 2.2, 2.0, -3]

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi
# ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 

sonlar[0] = 18
sonlar[1] = 20
sonlar[2] = sonlar[3]
# print(f'{sonlar[0]*5}')
# print(f'{sonlar[1]+2}')
# print(f'{sonlar[2]*5}')
# print(f'{sonlar[3]*5}')

# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan
#  tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 

t_shaxslar = ['abu bakr', 'umar ibn hattob', 'Ali', 'Abu Ubayda']
z_shaxslar = ['Muhammad ali', 'Erdogan', 'Abror Muhtor ali'] 


# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:

t_shaxs = t_shaxslar.pop(0)
z_shaxs = z_shaxslar.pop(2)

# print(f"Men tarixiy shaxslardan {t_shaxs} bilan zamonaviy shaxslardan {z_shaxs} bilan suhbat qilishni istardim")

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi
#  bo'lgan do'stlaringizni kiriting. 

friends = []

friends.append('Abdushohid')
friends.append('Abdulbosit')
friends.append('Akramjon')
friends.append('Sobitxon')
friends.append('Abdurrohman')
print(friends)

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.

friends.remove('Abdurrohman') 
friends.remove('Sobitxon') 
print(friends)

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

friends.insert(0, 'Mutalli')
friends.append('Asatbek')
print(friends)


# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida
#  mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

Mehmonlar = []

Mehmonlar.append(friends.pop(0))
Mehmonlar.append(friends.pop(0))
Mehmonlar.append(friends.pop(0))
Mehmonlar.append(friends.pop(0))
Mehmonlar.append(friends.pop(0))



print(Mehmonlar)
print(f'Mehmonga kelganlar {Mehmonlar}')





