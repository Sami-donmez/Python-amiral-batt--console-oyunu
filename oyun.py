class oyun:

    @staticmethod
    def  matrisolustur():
        matris = []
        satir = 10
        sutun = 10
        for i in range(satir):           # Kullanıcının istediği boyutta matris oluşturuyor.
                matris += [[0] *sutun]

        for i in range(satir):           #Kullanıcıdan matrise değer atanıyor.
            for j in range(sutun):
                matris[i][j] = 0
        return matris
    def matrisdoldur(self,matris):
        kontrol=True
        gemikontrol=0
        while kontrol:
            if gemikontrol==11:
                return matris
            else:
                gemitip=str(input("gemi seç \n 1-Fırkateyn(1 birim x 4 adet)\n 2-Denizaltı(2 birim x 2 adet)\n 3-kruvazör (3birim x 1 adet)"))
                if gemitip != "":
                    if int(gemitip)<4 and int(gemitip)>0:
                        birim=0
                        adet=0
                        if int(gemitip)==1:
                            birim=1
                            adet=4
                        elif int(gemitip)==2:
                            birim = 2
                            adet = 2

                        else :
                           adet = 1
                           birim= 3

                        for i in range(0,adet):
                            print(i+1," gemi yerleştiriyorsunuz")
                            for j in range(0,birim):
                                hsatir=str(input("satır numarası giriniz(0-9)"))
                                hsutun=str(input("sutun numarasi giriniz(0-9)"))
                                if(hsatir!="" and hsutun!=""):
                                    hsatir=int(hsatir)
                                    hsutun=int(hsutun)
                                    if(int(hsatir)<10 and int(hsatir)>=0 and int(hsutun)<10 and int(hsutun)>=0):
                                        if(matris[hsutun][hsatir]==0):
                                            matris[hsatir][hsutun]=1
                                            gemikontrol+=1
                                        else:
                                            print("hata (",hsatir,",",hsutun,") kordinatlarında gemi var")
                                            birim=birim+1# daha sonra bak
                                else:
                                    print("lütfen düzgün doldurunun")
     
                    else:
                        print("Hata seçim yaptınız")
                else:
                    print("hatalı giriş yaptınız")

    def oyna(matris):
        skontrol=True
        while skontrol:
            ssatir=str(input("hedef satır numarası giriniz(0-9)"))
            ssutun=str(input("hedefsutun numarasi giriniz(0-9)"))
            if(ssatir!="" and ssutun!=""):
                ssatir=int(ssatir)
                ssutun=int(ssutun)
                if(int(ssatir)<10 and int(ssatir)>=0 and int(ssutun)<10 and int(ssutun)>=0):
                    if(matris[ssutun][ssatir]==0):
                        return 0
                    else:
                        matris[ssutun][ssatir]=0
                        return 1
                else:
                    print("lütfen düzgün doldurunun")
