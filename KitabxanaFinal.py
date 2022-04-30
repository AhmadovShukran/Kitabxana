import re
from googlesearch import search
import wikipedia
kitablar={'Akıl Oyunlarının Gölgesinde':['Sherlock Holmes',469] , 'Sir Arthur':[ 'Conan Doyle', 396],' Dalga': ['Ricky Yancey', 462],'Senin İçin Enginar Sakladım':['Salim Nizam',471],'Karantina':['Beyza Alkoç', 446],'Kayıp Kızlar':['Megan Miranda', 460],'Küçük Mucizeler':['Betül Güçlü', 323 ],'Tuhaf Çocuklar': ['Ransom Riggs', 399],'Asansör': ['Beyza Alkoç',370],'Ruhlar Akademisi':['Gabriella Poole', 239],'Kuralsız':['Şule Terzi',485],'Aldanış':['James Morgan',380],'Lacivert Safir':['T.Y Mazer',428],'Oyunbozan':['James Dashner', 318],'Kaygısız':['M.D Hasani',454]}
istifadeciler={'AZE15245793':['Nicat Zeynalov','514422122',0],'AZE14525787':['Kamal Kerimli','559855587',2]}
list1=[]
list2=[]
wikipedia_lang="az"

def kitab_goturmek():
    kitab_secmek=input("Kitab goturmek isteyirsiz?(beli/xeyr)(he/yox)(yes/no) ")
    list3=[]
    k=1
    while True :
        if kitab_secmek.lower()=="he" or kitab_secmek.lower()=="beli" or kitab_secmek.lower()=="yes":
            while True:
                kitab_sual=input("Kitabin adin daxil edin: ")
                if kitab_sual:
                    for i in kitablar.keys():
                        g=re.compile(kitab_sual+".+",re.I)
                        h=g.findall(i)
                        list3.extend(h)
                    print("Sizin sorgunuza uygun "+str(len(list3))+"Kitab tapildi")
                    for i in list3:
                        print(str(k)+str(i)+str(kitablar[i]))
                        k=k+1
                    if len(list3)>0:
                        m=int(input("Hansi kitabi goturmek isteyirsizse nomresin yazin . Istemirsizse 0 yazin."))
                        if m:
                            while True:
                                vaxt=input("Nece gunluk goturmek isteyisiz?")
                                try:
                                    vaxt=int(vaxt)
                                    break
                                except:
                                    print("Zamani dogru qeyd edin.. Ve ya Gun Sayini Artirin(min. 5Gun)")
                                if vaxt>5:
                                    continue
                                else:
                                    break
                            print("Kitabin 1 gunluk kiraye haqqi 0.20AZN dir.Siz hal hazirda ",str(vaxt*0.20),"AZN odemelisiz.")
                            print(kitablar[list3[m-1]][0],"Dunya Alimleri subut etmisdirki 1 ktab vereqinin oxunmasi ucun 1 deqiqe 1 sehifesi ucun ise 30 saniye vaxt lazim olur. Size bu kitabi oxumaq ucun",str(kitablar[list3[m-1]][1]*2),"deqiqe gundelik texminen ",str((kitablar[list3[m-1]][1]*2)/vaxt),'Deqiqe Lazim olacaq. ')
                            while True:
                                secim_100=input("Kitabi Almaq Isteyirsizse-1\n Hesabdan Cixmaq Ve Kitabi Legv Etmek isteyirsizse - 2 \n Yazin:")
                                if secim_100=="1":
                                    print("Xos oxumalar.")
                                    break
                                elif secim_100=="2":
                                    break
                                else:
                                    print("Duzgun Cavab Verin..")
                    else:
                        print("Bele bir kitab tapilmadi...\nAvtomatik olaraq hesabdan cixdiniz")
                        break
                    break
                break
            break
        else:
            print("Isteyinizi Dogru Qeyd edin..")
            break
def hesab_acmaq_funk():
    while True:
        hesab_acmaq=input("Hesab acmaq isteyirsiz? ")
        if hesab_acmaq.lower()=="he" or hesab_acmaq.lower()=="yes" or hesab_acmaq.lower()=="beli":
            while True:
                hesab_sorgu_1=input("Adinizi Daxil Edin: ")
                hesab_sorgu_2=input("Soyadinizi Daxil Edin: ")
                if hesab_sorgu_1.isalpha() and hesab_sorgu_2.isalpha():
                    break

                else:
                    print("Ad ve Soyad Yalniz Herf Ola Biler")
            while True:
                hesab_sorgu_3=input("Nomrenizi Daxil edin: ")
                try:
                    if hesab_sorgu_3==int(hesab_sorgu_3):
                        break
                    break
                except:
                    print("Nomre Yalnzi reqem ola biler")
            while True:
                hesab_sorgu_4=input("Vesiqnizin Seriya NomresiniDaxil edin: ")
                try:
                    if hesab_sorgu_4==int(hesab_sorgu_4):
                        break
                    break
                except:
                    print("Vesiqenin Seriya Nomresi Yalniz Reqem Ola Biler")
            if ("AZE"+hesab_sorgu_4) in istifadeciler.keys():
                print("Bu Hesab Artiq Movcuddur"+str(istifadeciler["AZE"+hesab_sorgu_4]))
                kitab_goturmek()
                break
            else:
                continue
            deyisken="AZE"+str(hesab_sorgu_4)
            istifadeciler.setdefault("AZE"+str(hesab_sorgu_4))
            list1.append((hesab_sorgu_1+" "+hesab_sorgu_2))
            list1.append(str(hesab_sorgu_3))
            istifadeciler[deyisken]=list1
            kitab_goturmek()
            break
        elif hesab_acmaq.lower()=="yox" or hesab_acmaq.lower()=="no" or hesab_acmaq.lower()=="xeyr":
            print("Sagolun.Proqramdan cixdiniz...")
            break
        else:
            print("Duzgun Cavab Qeyd edin: ")

while True:
    hesab_1=input("Hesabiniz varmi(he/yox)(beli/xeyr)(yes/no): ")
    if hesab_1.lower()=="he" or hesab_1.lower()=="yes" or hesab_1.lower()=="beli":
        while True:
            hesab_2=input("Kitabxana iscisisinizse-1 ve ya oxucusunuzsa-2 yazin: ")
            if hesab_2=="2":
                while True:
                    sexsiyyet_yoxlama=(input("Sexsiyyet vesiqnizin seriya nomresini daxil edin: "))
                    if sexsiyyet_yoxlama=="admin123":
                        print("Admin Panele Xos Geldiniz. \n Kitabxanada olan ümumi kitabların sayını öyrənmək üçün 1 yazın. \n Kitabxanadan istifadə edən oxucuların sayını öyrənmək üçün 2 yazın. \n Kitabxanaya yeni kitab əlavə etmək üçün 3 yazın. \n Oxucu hesabını silmək üçün 4 yazın.")
                        admin_sual=input("Seciminizi Edin...")
                        while True:
                            if admin_sual=="1":
                                list_admin=[]
                                for i in kitablar.keys():
                                    list_admin.append(i)
                                print(len(list_admin))
                                break
                            elif admin_sual=="2":
                                list_admin2=[]
                                for i in istifadeciler.keys():
                                    list_admin2.append(i)
                                print(len(list_admin2))
                                break
                            elif admin_sual=="3":
                                while True:
                                    kitab_name=input("Kitabin Adini daxil edin: ")
                                    kitab_list=[]
                                    kitab_yazici=input("Yazicinin Adii daxil edin: ")
                                    kitab_sehife=input("Kitabin Sehifelerinin Sayi: ")
                                    try:
                                        kitab_sehife=int(kitab_sehife)
                                        break
                                    except:
                                        print("Sehifede Yalniz Reqem Ola Biler")
                                    kitab_list.append(kitab_yazici)
                                    kitab_list.append(kitab_sehife)
                                    print(kitablar[kitab_name])
                                    break
                            elif admin_sual=="4":
                                oxucu_sil=input(" Hansi Oxucunun Hesabini Silmek Isteyirsizse \n Vesiqesinin Seriya Nomresini Yazin")
                                while True:
                                    try:
                                        oxucu_sil=int(oxucu_sil)
                                        break
                                    except:
                                        print("Seriya Nomresi Yalniz Reqem Ola Biler...")
                                    if "AZE"+oxucu_sil in istifadeciler.keys():
                                        istifadeciler.remove("AZE"+oxucu_sil)
                                        break
                                    else:
                                        dogrulama=input("Bele Bir Hesab Tapilmadi")
                            else:
                                print("Duzgun eded daxil edin..")

                    elif sexsiyyet_yoxlama!="admin123":
                        while True:
                            try:
                                sexsiyyet_yoxlama=int(sexsiyyet_yoxlama)
                                break
                            except:
                                print("Isteyinizi Dogru Qyed edin...")
                                sexsiyyet_yoxlama
                        deyisken2="AZE"+str(sexsiyyet_yoxlama)
                        if deyisken2 in istifadeciler.keys():
                            print(istifadeciler[deyisken2])
                            kitab_goturmek()
                        elif deyisken2 not in istifadeciler.keys():
                            print("Bele bir hesab tapilmadi..")
                            hesab_acmaq_funk()
                            break
                        break
                    break
                break
            elif hesab_2=="1":
                while True:
                    sexsiyyet_yoxlama=input("Sexiyyetin seriya nomresini daxil edin: ")
                    try:
                        sexsiyyet_yoxlama=int(sexsiyyet_yoxlama)
                    except:
                        print("Isteyinizi Dogru Qyed edin...")
                        sexsiyyet_yoxlama
                    deyisken2="AZE"+str(sexsiyyet_yoxlama)
                    if deyisken2 in istifadeciler.keys():
                        print(istifadeciler[deyisken2])
                        while True:
                            isci_sual=input("Her Hansi Yazici Haqqinda Melumat Toplamaq Isteyirsizse 1 \n Kitab Haqqinda Google-da Cixanlari Isteyirsizse 2 yazin:")
                            if isci_sual=="1":
                                while True:
                                    yazici=input("Yazicinin Adini Daxil edin: ")
                                    try:
                                        wikipedia.summary(yazici)
                                        print(wikipedia.summary(yazici))
                                        break
                                    except:
                                        print("Bele bir melumat yoxdur")
                                    break
                                break
                            elif isci_sual=="2":
                                while True:
                                    kitab_ad=input("Kitabin Adini Daxil edin: ")
                                    try:
                                        search(kitab,num=10,start=2,pause=1)
                                        for i in search(kitab,num=10,start=2,pause=1):
                                            print(i)
                                        break
                                    except:
                                        print("Bele Bir Kitab Yoxdur..")
                                        break
                                    break
                                break
                            break
                        break

                    elif deyisken2 not in istifadeciler.keys():
                        print("Bele bir hesab tapilmadi..")
                        hesab_acmaq_funk()
                        break
                    break
                break
            else :
                print("Duzgun Secim Edin..")
    elif hesab_1.lower()=="yox" or hesab_1.lower()=="no" or hesab_1.lower()=="xeyr":
        hesab_acmaq_funk()
    else:
        print("Isteyinizi dogru qeyd edin: ")

