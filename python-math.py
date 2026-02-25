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


######## lugat bilan ishlash

# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu 
# inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo).
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda,
# Samarqand viloyatida tug'ilgan


# otam = {
#     "ismi": 'Yunusxon',
#     "t_yil": 1979,
#     "t_shahar": 'Namangan',
#     'y_manzil': 'Sharshara MFY'
# }

# onam = {
#     "ismi": 'Muazzam',
#     "t_yil": 1981,
#     "t_shahar": 'Namangan',
#     'y_manzil': 'Sharshara MFY'
# }

# ukam = {
#     "ismi": 'Yaxyoxon',
#     "t_yil": 2003,
#     "t_shahar": 'Namangan',
#     'y_manzil': 'Barkamol avlod MFY'
# }

# singlim = {
#     "ismi": 'Zohida',
#     "t_yil": 2012,
#     "t_shahar": 'Namangan',
#     'y_manzil': 'Sharshara MFY'
# }

# print(f"Otamning ismi {otam['ismi']} {otam['t_yil']}-yilda {otam['t_shahar']} shahrida tug'ilgan. ")
# print(f"Onamning ismi {onam['ismi']} {onam['t_yil']}-yilda {onam['t_shahar']} shahrida tug'ilgan. ")
# print(f"Ukamning ismi {ukam['ismi']} {ukam['t_yil']}-yilda {ukam['t_shahar']} shahrida tug'ilgan. ")
# print(f"Singlimning ismi {singlim['ismi']} {singlim['t_yil']}-yilda {singlim['t_shahar']} shahrida tug'ilgan. ")

# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
#  Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

# taomlar = {
# 'Otam': 'Manti',
# 'Onam': 'Shashlik',
# 'Ukam': 'Somsa',
# 'Singlim1': 'kartoshka',
# 'Simglim2': 'Bilish'
# }
# print(f"Otamning sevimli taomi {taomlar['Otam']}")
# print(f"Onamning sevimli taomi {taomlar['Onam']}")
# print(f"Ukamning sevimli taomi {taomlar['Ukam']}")

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing

# lugat = {
#     'integer': 'butun son',
#     'float': 'onlik son',
#     'string': 'matn',
#     'if': 'agar shart',
#     'else': 'agar shart',
#     'function': 'funksiya',
#      'or': 'yoki taqqoslash operatori',
#      'and': 'va taqqoslash operatori',
#      'print': 'malumotni ekranga chiqaruvchi funksiya',
#      'boolean': 'togri yoki notogri ekanini korsatuvchi operator'
# }

# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan 
# chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

# soz_kirit = input('kalit soz kiriting: ').lower()
# print(lugat.get(soz_kirit, 'bunday soz mavjud emas'))



# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli 
# ko'rinishda chiqaring.

# tarjima = lugat.get(soz_kirit)
# if tarjima == None:
#     print('bunday soz mavjud emas')
# else:
#     print(f'{soz_kirit} sozi {lugat[soz_kirit]} deb tarjima qilinadi')


############ lugat elementlar bilan ishlash


# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
#  Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida
#  chiroyli qilib konsolga chiqaring. 

# lugatlar = {
#     'integer': 'butun son',
#     'float': 'onlik son',
#     'string': 'matn',
#     'if': 'agar shart',
#     'else': 'agar shart',
#     'function': 'funksiya',
#      'or': 'yoki taqqoslash operatori',
#      'and': 'va taqqoslash operatori',
#      'print': 'malumotni ekranga chiqaruvchi funksiya',
#      'boolean': 'togri yoki notogri ekanini korsatuvchi operator'
# }

# for lugat in sorted(lugatlar):
#     print(f'{lugat}-{lugatlar[lugat]}')


# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni,
#  keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 

# davlatlar = {
#     "O'zbekiston": 'Toshkent',
#     "AQSH": 'Washington',
#     "Rossiya": 'Moskva',
#     'Angliya': 'London',
#     'Fransiya': 'Paris'
# }
# print('Dunyo davlatlari')
# for davlat in sorted(davlatlar.keys()):
#     print(f'{davlat}')

# print('Davlatlarning poytaxti')
# for davlat in sorted(davlatlar.values()):
#     print(f'{davlat}')
  

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning
# poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa,
# "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

# dav_kirit = input('Qaysi davlatni poytaxtini bilishni istaysiz: ').title()

# capital = davlatlar.get(dav_kirit)
# if capital == None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')  
# else:
#     print(f'{dav_kirit} ning poytaxti {capital} shahri')


# taomlar = {
#     'osh': 15000,
#     'shashlik': 18000,
#     'somsa': 10000,
#     'qozonkabob': 20000,
#     'bishteks': 20000,
#     'lagmon': 22000,
#     'norin': 28000
# }
# print('3 ta buyurtma bering: ')
# buyurtmalar = []

# for n in range(3):
#     buyurtmalar.append(input(f'{n+1}-taomni kiriting: '))

# for buyurtma in buyurtmalar:
#     if buyurtma in taomlar:
#         print(f'{buyurtma} {taomlar[buyurtma]} som')
#     else:
#         print(f'bizda {buyurtma} taomi yoq')


############## Nesting


# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni
# lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi
# ma'lumotni konsolga chiqaring.

# buxoriy = {
#     'ism': 'abu abdulloh muhammad ibn ismoil',
#     't_yil': 810,
#     't_shahar': 'Buxoro',
#     'yosh': 60,
#     'asarlar': ['al-jome as-sahih', 'al-adab al-mufrad', 'at-tarix as-sagir']
# }
# qodiriy = {
#     'ism': 'Abdulla Qodiriy',
#     't_yil': 1894,
#     't_shahar': 'Toshkent',
#     'yosh': 44,
#     'asarlar': ['Otkan kunlar', 'mehrobdan chayon', 'obid ketmon']
# }
# vohidov = {
#     'ism': 'Erkin Vohidov',
#     't_yil': 1936,
#     't_shahar': 'Fargona',
#     'yosh': 80,
#     'asarlar': ['Tong nafasi', 'Qoshiqlarim sizga', 'ozbegim', 'qiziquvchan matmusa']
# }
# navoiy = {
#     'ism': 'Alisher Navoiy',
#     't_yil': 1441,
#     't_shahar': 'Xirot',
#     'yosh': 60,
#     'asarlar': ['Xamsa', 'lison ut-tayr', 'mahbub al-qulub', 'munojot']
# }

# adabiyotchilar = [buxoriy, qodiriy, vohidov, navoiy]

# for adabiyot in adabiyotchilar:
#     print(f'{adabiyot['ism']} {adabiyot['t_yil']}-yilda '
#           f'{adabiyot['t_shahar']}da tavallud topgan. {adabiyot['yosh']} yil umr korgan')


# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
# For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

# for adabiyot in adabiyotchilar:
#     ism = adabiyot['ism']
#     asarlar = adabiyot['asarlar']
#     print(f'{ism} ning mashxur asarlar: ')
#     for asar in asarlar:
#         print(asar)

# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
# Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang. 
# Natijani konsolga chiqaring.

# dostlar = {
#     'ali': ['Terminator', 'Rambo', 'Titanic'],
#     'vali': ['Tenet', 'Inception', 'Interstellar'],
#     'hasan': ['Abdullajon', 'Bomba', 'Shaytanat'],
#     'husan': ['Mahallada duv duv gap', 'john wick',]
# }

# for kalit, qiymat in dostlar.items():
#     print(f'{kalit.title()} ning sevimli kinolari:')
#     for q in qiymat:
#         print(q)


# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni 
# lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

# davlatlar = {
#     "o'zbekiston":{
#         'poytaxt': 'Toshkent',
#         'hududi': 448978,
#         'aholi': 33_000_000,
#         'pul birligi': 'som'
#     },
#     "rossiya":{
#         'poytaxt': 'Moskva',
#         'hududi': 17098246,
#         'aholi': 144_000_00,
#         'pul birligi': 'rubl'
#     },
#     "aqsh":{
#         'poytaxt': 'Washington',
#         'hududi': 9631418,
#         'aholi': 327_000_000,
#         'pul birligi': 'dollor'
#     },
#     "malayziya":{
#         'poytaxt': 'Kuala-Lampur',
#         'hududi': 329750,
#         'aholi': 25_000_000,
#         'pul birligi': 'rinngit'
#     }
# }

# for davlat, info in davlatlar.items():
#     if davlat.lower() == 'aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f'\n {davlat} ning poytaxti {info['poytaxt'].title()}'
#           f'\n Hududi: {info['hududi']} kv.km'
#           f'\n Aholisi: {info['aholi']}'
#           f'\n Pul birligi {info['pul birligi']}'
#           )


# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas,
# foydalanuvchi so'ragan davlat haqida ma'lumot bering. 
# Agar davlat sizning lug'atingizda mavjud bo'lmasa, 
# "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

# davlat = input('Davlat nomini kiriting: ').lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['hududi']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")


######### while tsikli


# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
# Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating

# savol = "O'zingiz yoqtirgan kitoblarni kiriting: "
# savol += "(Dasturni to'xtatish uchun 'stop' so'zini yozing): "

# qiymat = ''
# while qiymat != 'stop':
#     qiymat = input(savol)
#     if qiymat != 'stop':
#         print(qiymat)


# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm,
# 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, 
# dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
# Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

# savol = 'yoshingizni kiriting: '
# savol += 'Dasturni toxtatish uchun "exit" yoki "quit" tugmasini boshing '

# while True:
#     qiymat = input(savol)

#     if qiymat == 'exit' or qiymat == 'quit':
#         print('dastur tugadi.')
#         break
#     qiymat = int(qiymat)
#     if qiymat <= 7:
#         print('sizga kirish narxi 2000 som')
#     elif  7 < qiymat < 18:
#         print('sizga kirish narxi 3000 som')
#     elif  18 <= qiymat <= 65:
#         print('sizga kirish narxi 10000 som')
#     else:
#         print('sizga kirish bepul')
    
# Quyidagi dasturda bir nechta mantiqiy xatolar bor. 
# Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?


# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")



########## while royxatlar va lugatlar

# ismlar = []

# print('Yaqin dostlaringizni royxatini tuzamiz ')

# n = 1
# while True:
#     savol = f'{n}-dostingizni ismini kiriting '
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input('Yana ism qoshasizmi (ha/yoq) ')
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break

# print('dostlarni royxati ')
# for ism in ismlar:
#     print(ism.title())

# print('dostlaringizni yoshini saqlaymiz ')
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input('Dostingizni ismini kiriting ')
#     yosh = input(f'{ism.title()}ning yoshini kiriting ')
#     dostlar[ism] = int(yosh)

#     javob = input('Yana malumot qoshasizmi (ha/yoq) ')
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f'{ism.title()} {yosh} yoshda')


# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']

# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)

# talabalar = ['hasan', 'husan', 'olim', 'botir']

# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()} ning bahosini kiriting: ")
#     print(f'{talaba.title()} baholandi ')
#     baholangan_talabalar[talaba] = baho

# for talaba, baho in baholangan_talabalar.items():
#     print(f'{talaba.title()}ning bahosi {baho}')



# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

# print('Mahsulotlarni kiriting: ')
# mahsulotlar = []
# n = 1
# while True:
#     savol = f'{n}-mahsulotni kiriting '
#     mahsulot = input(savol)
#     mahsulotlar.append(mahsulot)
#     javob = input('Yana maxsulot qoshasizmi (ha/yoq) ')
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break
# print('mahsulotlar royxati')
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

# print('E-bozor uchun mahsulot royxatlari va narxlari')

# mahsulotlar = {}
# ishora = True
# while ishora:
#     mahsulot = input('mahsulotni nomini kiriting: ')
#     narh = input(f'{mahsulot.title()}ning narxini kiriting ')
#     mahsulotlar[mahsulot] = int(narh)

#     javob = input('Yana mahsulot qoshasizmi (ha/yoq)')
#     if javob == "yo'q":
#         ishora = False
# print('Mahsulotlar va ularning narxi')
# for mahsulot, narh in mahsulotlar.items():
#     print(f'{mahsulot.title()} {narh} som')
    

# Yuqoridagi ikki dasturni jamlaymiz. 
# Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring 
# (tayyor ro'yxat ishlatishingiz mumkin). 
# Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda 
# "Bizda bu mahsulot yo'q" degan xabarni kor'sating.


# buyurtmalar = ['olma', 'shaftoli', 'sabzi', 'kartoshka', 'tarvuz', 'bodring', 'pomidor', 'behi']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f'{buyurtma.title()} - {narh} som')
#     else:
#         print(f'Bizda {buyurtma} yoq')


###################

# funksiya

# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def toliq_ism(ism, yosh,joriy_yil = 2026):
#     """Foydalanuvchi ism va tugilgan yilini chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi tugilgan yili: {joriy_yil-yosh}"
#           )
    
# toliq_ism('olim', 28)


# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing

# def kvadrat_kub(son):
#     """Sonning kvadrati va kubini chiqaruvchi funksiya"""
#     print(f'{son} sonini kvadrati {son**2}\n'
#           f'{son} sonini kubi {son**3}'
#           )
# kvadrat_kub(5)


# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

# def juft_toq(son):
#     """Sonni juft yoki toq ekanini aniqlovchi funksiya"""
#     if son % 2 == 0:
#         print(f'{son} juft son')
#     else:
#         print(f'{son} toq son')
    
# juft_toq(19)


# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

# def taqqoslash(son1, son2):
#     if son1 > son2:
#         print(son1)
#     elif son1 < son2:
#         print(son2)
#     else:
#         print('Sonlar teng')

# taqqoslash(15,15)

# Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya yozing.

# def daraja(x, y):
#     """Darajani chiqarib beruvchi dastur"""
#     print(f'{x} ning darajasi {x**y}')

# daraja(2,3)

# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.

# def daraja(x, y=2):
#     """Darajani chiqarib beruvchi dastur"""
#     print(f'{x} ning darajasi {x**y}')

# daraja(2)

# def son_ol(son):
#     for n in range(1,10):
#         if son % n == 0:
#             print(f'{son} {n} ga qoldiqsiz bolinadi')
        
# son_ol(70)

##################

# qiymat qaytaruvchi funksiya

# def toliq_ism_yasa(ism, familiya, otasining_ismi = ''):
#     """Toliq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f'{ism} {familiya} {otasining_ismi}'
#     else:
#         toliq_ism = f'{ism} {familiya}'
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa('ayubxon', 'axmatxonov', 'yunusxon ogli')
# talaba2 = toliq_ism_yasa('olim', 'hakimov')

# print(f'darsga kelmagan talabalar: {talaba1}, {talaba2}')


# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {
#         'kompaniya': kompaniya,
#         'model': model,
#         'rang': rangi,
#         'korobka': korobka,
#         'yil': yili,
#         'narh': narhi
#     }
#     return avto

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)

# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud mashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = 'Nomalum'
#     print(f'{avto['rang']} {avto['model']}. Narhi : {narh}')


# def oraliq(min, max, qadam=1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min+=qadam
#     return sonlar

# print(oraliq(0,10,2))
# print(oraliq(10,21))


# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {
#         'kompaniya': kompaniya,
#         'model': model,
#         'rang': rangi,
#         'korobka': korobka,
#         'yil': yili,
#         'narh': narhi
#     }
#     return avto

# print('saytimizdagi avtolar royxatini shakllantiring ')
# avtolar = []

# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting ",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")

#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))

#     javob = input('Yana avto qoshasizmi (ha/yoq)')
#     if javob == 'no':
#         break
# print('Salonimizdagi avtolar')
# for avto in avtolar:
#     print(f'{avto['rang']} {avto['model']}, {avto['korobka']}. Narhi: {avto['narh']}')



# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi,
# email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi
# funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
# Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar
# degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.

# def user_info(ism, familiya, t_yil, t_joy, email_mazil, t_raqam='None'):
#     user = {
#         'ism': ism,
#         'familiya': familiya,
#         't_yil': t_yil,
#         't_joy':t_joy,
#         'email_manzil': email_mazil,
#         't_raqam': t_raqam, 
#         'yosh': 2026-t_yil 
#     }
#     return user

# print('Talabalar royxatini shakllantiring ')
# talabalar = []
# while True:
#     print('Quyidagi malumotlarni kiriting: ', end='')
#     ism = input('ismini kiriting ').title()
#     familiya = input('familiya kiriting ').title()
#     t_yil = int(input('tugilgan yilini kiriting '))
#     t_joy = input('tugilgan joyini kiriting ').title()
#     email_mazil = input('email manzilini kiriting ').title()
#     t_raqam = input('telefon raqamini kiriting ')

#     talabalar.append(user_info(ism, familiya, t_yil, t_joy, email_mazil, t_raqam))    

#     javob = input('Yana malumot kiritasizmi(ha/yoq) ')
#     if javob == 'yoq':
#         break
# print('Talabalar royxati ')
# for talaba in talabalar:
#     print(f'{talaba['ism']} {talaba['familiya']}. {talaba['yosh']} yoshda')


# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

# def son_ol(son1, son2, son3):
#     max = son1
#     if son2 >= max:
#         max = son2
#     if son3 >= max:
#         max = son3
#     return max

# sonlar = son_ol(5,18,9)
# print(sonlar)


# Foydalanuvchidan son qabul qilib, 
# shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  
# Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik 
# Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi. 

# def fibonachchi(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1) 
#         else:
#             sonlar.append(sonlar[x-1] + sonlar[x-2])
#     return sonlar
    
# print(fibonachchi(10))

##############

# funksiya va royxatlar

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f'Talaba {ism.title()}ning bahosi ')
#         baholar[ism] = baho
#     return baholar

# talabalar = ['ali', 'vali', 'ahmad', 'usmon']
# baholar = bahola(talabalar[:])
# print(talabalar)


# Matnlardan iborat ro'yxat qabul qilib, 
# ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing. 


# def katta_harf(ismlar):
#     for i in range(len(ismlar)):
#         ismlar[i] = ismlar[i].title()
#     return ismlar

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)


# Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring

# def katta_harf(ismlar):
#     for i in range(len(ismlar)):
#         ismlar[i] = ismlar[i].title()
#     return ismlar

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harf(ismlar[:])
# print(ismlar)
# print(yangi_ismlar)



# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va 
# asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.


# talabalar = ['ali', 'vali', 'hasan', 'husan']
# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f'Talaba {ism.title()}ning bahosi ')
#         baholar[ism] = baho
#     return baholar

# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)