import oyun
oyun= oyun.oyun()
matris1=oyun.matrisolustur()
matris2=oyun.matrisolustur()
oyun.matrisdoldur(matris1)
oyun.matrisdoldur(matris2)


print("oyuncu 1")
for i in range(10):  # Matris ekrana yazdırılıyor.
    for j in range(10):
        print(matris1[i][j], end=" ")
    print()
print("----------------------------------------")
print("oyuncu 2")
for i in range(10):  # Matris ekrana yazdırılıyor.
    for j in range(10):
        print(matris2[i][j], end=" ")
    print()

canoyuncu1 = 11
canoyuncu2 = 11
oyunkontrol = True
i = 0
while oyunkontrol:
    if canoyuncu1 == 0:
        print("oyuncu 2 kazandı\n kalan can:", canoyuncu2)
        break

    elif canoyuncu2 == 0:
        print("oyuncu 1 kazandı\n kalan can:", canoyuncu2)
        break
    else:
        if (i % 2 == 0):
            oyuncu1 = oyun.oyun.oyna(matris2)
            if oyuncu1 == 1:
                canoyuncu2 = canoyuncu2 - 1
                print("gemi vuruldu....  \noyuncu 1 kalan can:", canoyuncu1, "\noyuncu 2 kalan can : ", canoyuncu2)
            else:
                print("karavana atış....\noyuncu 1 kalan can:", canoyuncu1, "\noyuncu 2 kalan can : ", canoyuncu2)
        else:
            oyuncu2 = oyun.oyun.oyna(matris1)
            if oyuncu2 == 1:
                canoyuncu1 = canoyuncu1 - 1
                print("gemi vuruldu....  \noyuncu 1 kalan can:", canoyuncu1, "\noyuncu 2 kalan can : ", canoyuncu2)
            else:
                print("karavana atış....\noyuncu 1 kalan can:", canoyuncu1, "\noyuncu 2 kalan can : ", canoyuncu2)
