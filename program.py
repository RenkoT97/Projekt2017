# Pobriši ime seznama v datoteki in pusti samo seznam!!
# rabiš seznam seznama, ne naborov! Sami oglati oklepaji!

with open('rezultati.txt') as dat1:
    with open('tabele_stolpcev.txt') as dat2:
        with open('tabele_vrstic.txt') as dat3:
            with open('tabele_operacij.txt') as dat4:
                def start():
                    a = random.randint(1, 10)
                    for a in range(10):
                        A = dat1.readline(a)
                        B = dat2.readline(a)
                        C = dat3.readline(a)
                        D = dat4.readline(a)
                import tkinter as tk
                okno = tk.Tk()
                def povej_mi_navodila():
                    print('Kenken je matematična uganka, ki jo je leta 2004 razvil japonski učitelj Tetsuya Miyamoto. Rešuje se tako...')
                def izpisi_kenken_za_resevanje():
                    for i in range(5):
                        for j in range(5):
                            tk.Button(text=D[i - 1][j - 1]).grid(row=i, column=j)
                okno.mainloop()














                def igraj():
                    st_vrstice = input('Izberite vrstico, v katero želite vpisati število! ')
                    st_stolpca = input('Izberite stolpec, v katerega želite vpisati število! ')
                    stevilo = input('Vpišite število! ')
#               def preveri_pravilnost():
#                    if A == ???:
#                       return ''
#                    else:
#                        return pobrisi??
