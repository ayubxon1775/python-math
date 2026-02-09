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

# ismlar = ['abdulbosit', 'akramjon', 'abdushohid', 'abdurrohman']

# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 

# print(f"Salom {ismlar[0].title()} bugun ko'rishamizmi")
# print(f"Salom {ismlar[1].title()} bugun ko'rishamizmi")
# print(f"Salom {ismlar[2].title()} bugun ko'rishamizmi")
# print(f"Salom {ismlar[0].title()} bugun ko'rishamizmi")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 

# sonlar = [15, 1, -5, 2.2, 2.0, -3]

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi
# ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 

# sonlar[0] = 18
# sonlar[1] = 20
# sonlar[2] = sonlar[3]
# print(f'{sonlar[0]*5}')
# print(f'{sonlar[1]+2}')
# print(f'{sonlar[2]*5}')
# print(f'{sonlar[3]*5}')

# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan
#  tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 

# t_shaxslar = ['abu bakr', 'umar ibn hattob', 'Ali', 'Abu Ubayda']
# z_shaxslar = ['Muhammad ali', 'Erdogan', 'Abror Muhtor ali'] 


# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:

# t_shaxs = t_shaxslar.pop(0)
# z_shaxs = z_shaxslar.pop(2)

# print(f"Men tarixiy shaxslardan {t_shaxs} bilan zamonaviy shaxslardan {z_shaxs} bilan suhbat qilishni istardim")

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi
#  bo'lgan do'stlaringizni kiriting. 

# friends = []

# friends.append('Abdushohid')
# friends.append('Abdulbosit')
# friends.append('Akramjon')
# friends.append('Sobitxon')
# friends.append('Abdurrohman')
# print(friends)

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.

# friends.remove('Abdurrohman') 
# friends.remove('Sobitxon') 
# print(friends)

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

# friends.insert(0, 'Mutalli')
# friends.append('Asatbek')
# print(friends)


# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida
#  mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

# Mehmonlar = []

# Mehmonlar.append(friends.pop(0))
# Mehmonlar.append(friends.pop(0))
# Mehmonlar.append(friends.pop(0))
# Mehmonlar.append(friends.pop(0))
# Mehmonlar.append(friends.pop(0))

# print(Mehmonlar)
# print(f'Mehmonga kelganlar {Mehmonlar}')

##############  Royxatlar bilar ishlash

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# davlatlar = ["O'zbekiston", "Qozog'iston", "Turkiya", "Qirg'iziston", "Kanada", "AQSH", "Britaniya"]

# print(davlatlar)

# Ro'yxatning uzunligini konsolga chiqaring

# print(len(davlatlar))

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring

# tartib_davlatlar = sorted(davlatlar)
# print(tartib_davlatlar)

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring

# tartib_davlatlar = sorted(davlatlar, reverse=True)
# print(tartib_davlatlar)

# Asl ro'yxatni qaytadan konsolga chiqaring

# print(davlatlar)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring

# davlatlar.reverse()
# print(davlatlar)


# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha,
#  keyin esa alifboga teskari tartibda konsolga chiqaring.

# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)


# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing

# sonlar = list(range(120,1200, 2))
# print(sonlar)

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring

# yigindi = sum(sonlar)
# print(yigindi)

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring

# eng_katta = max(sonlar)
# eng_kichik = min(sonlar)

# print(f'{eng_katta}-{eng_kichik}={eng_katta-eng_kichik}')

# Ro'yxatdagi elementlar sonini hisoblang

# print(len(sonlar))


# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring

# boshidan = sonlar[:20]
# ortasidan = sonlar[530:550]
# oxiridan = sonlar[-20:]

# print(boshidan)
# print(ortasidan)
# print(oxiridan)

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting

# taomlar = ['osh', 'shashlik','manti', 'somsa', 'shorva']
# print(taomlar)

# nonushta degan yangi ro'yxatga taomlardan nusxa oling

# nonushta = taomlar[:]
# print(nonushta)

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing

# nonushta.remove('somsa')
# nonushta.remove('manti')
# nonushta.remove('shashlik')
# nonushta.append('mastava')
# nonushta.append('qaymoq')

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# print(nonushta)
# print(taomlar)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring
# va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.

# nonushta = tuple(nonushta)
# nonushta[0] = 'qaymoq va non'
# print(nonushta)



############# For takrorlash operatori



# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing

ismlar = ['ayubxon', 'abdulbosit', 'akramjon','abdushohid', 'abdurahmon']

# for ism in ismlar:
    # print(f'{ism.title()} bugun dachaga boramizmi')

# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha
# marta takrorlanganini yozing)

# print(f'kod {len(ismlar)} marta takrorlandi')

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan
#  konsolga chiqaring.

# for n in range(11, 100,2):
    # print(f'{n} ning kubi {n**3} ga teng')

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling.
# Natijani konsolga chiqaring.

# kinolar = []
# for n in range(5):
#     kinolar.append(input(f"o'zingiz yoqtirgan {n+1} ta kino nomini kiriting: "))

# print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har 
# bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

# suhbat = int(input('bugun nechta odam bilan suhbatlashdingiz: '))
# suhbatdosh = []
# for n in range(suhbat):
#     suhbatdosh.append(input(f'{n+1}-suhbat qilgan odamingiz kim edi: '))
# print(suhbatdosh)

########## if-else

#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining 
# birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.

cars = ['toyoto', 'mazda', 'hyundai', 'gm', 'kia']

# for car in cars:
#     if car == 'gm':
        # print(car.upper())
    # else:
        # print(car.title())


# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 

# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())


# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, 
# Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. 
# Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.

# login = input('login ismini kiriting: ')

# if login.lower() == 'admin':
#     print("Hush kelibsiz, Admin Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login}!")

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, 
# "Sonlar teng" ekan degan yozuvni konsolga chiqaring.

# x = float(input('1-sonni kiriting '))
# y = float(input('2-sonni kiriting '))
# if x==y: print('sonlar teng')


# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", 
# agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 

# sonkirit = float(input('son kiriting: '))

# if sonkirit < 0:
#     print('manfiy')
# else:
#     print('musbat')

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini 
# hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 

# sonkirit = float(input('son kiriting: '))

# if sonkirit > 0:
#     print(f'{sonkirit ** (1/2)}')
# else:
#     print('musbat son kiriting')


########## bir nechta shartlarni tekshirish

# Quyidagi dasturlarni alohida fayllarga yozing va bajaring:

# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa
#  "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

# son_kirit = float(input('juft son kiriting: '))

# if son_kirit % 2 == 0:
#     print('Rahmat')
# else:
#     print('bu son juft emas')

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:


# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul

# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm

# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# yosh = float(input('yoshingizni kiriting: '))

# if yosh <= 4 or yosh >= 60:
#     price = 0
# elif yosh <= 18: 
#     price = 10000
# elif yosh > 18:
#     price = 20000

# print(f'sizga kirish narxi {price}')

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki
#  katta/kichikligi haqida xabarni chiqaring

# x = float(input('1-sonni kiriting: '))
# y = float(input('2-sonni kiriting: '))

# if x == y:
#     print(f'{x} == {y}')
# elif x > y:
#     print(f'{x} > {y}')
# elif x < y:
#     print(f'{x} < {y}')

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan
# savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar
# ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda,
# "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

# mahsulotlar = ['anor', 'olma', 'behi', 'kartoshka', 'sabzi', 'tarvuz', 'piyoz', "go'sht", 'anjir', 'uzum']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []

# for n in range(5):
#     savat.append(input(f'{n+1}-mahsulotni kiriting '))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print('dokonimizda quyidagi mahsulotlar yoq:')
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print('siz soragan barcha mahsulotlar dokonimizda bor')

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
#  Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga,
#  do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. 
#  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor"
#  degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.



# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing.
#  Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni
#  foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda 
# bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, 
# foydalanuvchi!" xabarini chiqaring.

# foydalanuvchilar = ['anvar', 'komil', 'ahror', 'bekzod', 'usmon']
# yangi_login = input("Yangi login kiriting ")

# if yangi_login in foydalanuvchilar:
#     print(f"{yangi_login} login band, yangi login tanlang")
# else:
#     print('hush kelibsiz foydalanuvchi')

# Foydalanuvchidan biror butun son kiritishni so'rang.
# Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga 
# qoldiqsiz bo'linishini konsolga chiqaring. 

# son_kirit = float(input('istalgan sonni kiriting '))

# for n in range(2,10):
#     if son_kirit % n == 0:
#         print(f'{son_kirit} soni {n} ga qoldiqsiz bolinadi')
