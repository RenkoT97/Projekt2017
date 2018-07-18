import tkinter as tk
import random
import sys
import os

def pretvori_dat_v_sez(ime_dat):
    seznam = []
    with open(ime_dat) as dat:
        for vrstica in dat:
            a = []
            b = vrstica.replace(' ', '').split('~')
            c = b[1:]
            d = c[:-1]
            for x in d:
                f = []
                e = x.split(',')
                for y in e:
                    f.append(y)
                a.append(f)
            seznam.append(a)
    return seznam

seznam1 = pretvori_dat_v_sez('Resitve.txt')
seznam2 = pretvori_dat_v_sez('barve_polj.txt')
seznam31 = pretvori_dat_v_sez('operacije.txt')

def zbrisi_x(seznam):
    sez = []
    for element in seznam:
        sez.append(element.replace('x', ''))
    return sez

def spremeni(seznam):
    sez = []
    for podseznam in seznam:
        sez.append(zbrisi_x(podseznam))
    return sez

def spremeni_seznam(seznam):
    sez = []
    for podseznam in seznam:
        sez.append(spremeni(podseznam))
    return sez

seznam3 = spremeni_seznam(seznam31)

št_kenkena = random.randint(0, 9)

barve = {'A': 'chocolate3', 'B': 'green yellow', 'C': 'RoyalBlue3', 'D': 'maroon1', 'E': 'NavajoWhite2', \
'F': 'lime green', 'G': 'DarkOrange1', 'H': 'Sienna1', 'I': 'DeepPink4', 'J': 'SkyBlue3', 'K': 'purple4', \
'L': 'SeaGreen1', 'M': 'gold', 'N': 'red3', 'O': 'LightPink3'}

okno = tk.Tk()

gumb1 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][0][0]])
gumb1.insert(0, seznam3[št_kenkena][0][0] + '           ')
gumb1.grid(row = 1, column = 0, ipady = 40)
gumb2 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][0][1]])
gumb2.insert(0, seznam3[št_kenkena][0][1] + '           ')
gumb2.grid(row = 1, column = 1, ipady = 40)
gumb3 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][0][2]])
gumb3.insert(0, seznam3[št_kenkena][0][2] + '           ')
gumb3.grid(row = 1, column = 2, ipady = 40)
gumb4 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][0][3]])
gumb4.insert(0, seznam3[št_kenkena][0][3] + '           ')
gumb4.grid(row = 1, column = 3, ipady = 40)
gumb5 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][0][4]])
gumb5.insert(0, seznam3[št_kenkena][0][4] + '           ')
gumb5.grid(row = 1, column = 4, ipady = 40)
gumb6 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][0][5]])
gumb6.insert(0, seznam3[št_kenkena][0][5] + '           ')
gumb6.grid(row = 1, column = 5, ipady = 40)

gumb7 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][1][0]])
gumb7.insert(0, seznam3[št_kenkena][1][0] + '           ')
gumb7.grid(row = 2, column = 0, ipady = 40)
gumb8 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][1][1]])
gumb8.insert(0, seznam3[št_kenkena][1][1] + '           ')
gumb8.grid(row = 2, column = 1, ipady = 40)
gumb9 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][1][2]])
gumb9.insert(0, seznam3[št_kenkena][1][2] + '           ')
gumb9.grid(row = 2, column = 2, ipady = 40)
gumb10 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][1][3]])
gumb10.insert(0, seznam3[št_kenkena][1][3] + '           ')
gumb10.grid(row = 2, column = 3, ipady = 40)
gumb11 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][1][4]])
gumb11.insert(0, seznam3[št_kenkena][1][4] + '           ')
gumb11.grid(row = 2, column = 4, ipady = 40)
gumb12 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][1][5]])
gumb12.insert(0, seznam3[št_kenkena][1][5] + '           ')
gumb12.grid(row = 2, column = 5, ipady = 40)

gumb13 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][2][0]])
gumb13.insert(0, seznam3[št_kenkena][2][0] + '           ')
gumb13.grid(row = 3, column = 0, ipady = 40)
gumb14 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][2][1]])
gumb14.insert(0, seznam3[št_kenkena][2][1] + '           ')
gumb14.grid(row = 3, column = 1, ipady = 40)
gumb15 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][2][2]])
gumb15.insert(0, seznam3[št_kenkena][2][2] + '           ')
gumb15.grid(row = 3, column = 2, ipady = 40)
gumb16 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][2][3]])
gumb16.insert(0, seznam3[št_kenkena][2][3] + '           ')
gumb16.grid(row = 3, column = 3, ipady = 40)
gumb17 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][2][4]])
gumb17.insert(0, seznam3[št_kenkena][2][4] + '           ')
gumb17.grid(row = 3, column = 4, ipady = 40)
gumb18 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][2][5]])
gumb18.insert(0, seznam3[št_kenkena][2][5] + '           ')
gumb18.grid(row = 3, column = 5, ipady = 40)

gumb19 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][3][0]])
gumb19.insert(0, seznam3[št_kenkena][3][0] + '           ')
gumb19.grid(row = 4, column = 0, ipady = 40)
gumb20 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][3][1]])
gumb20.insert(0, seznam3[št_kenkena][3][1] + '           ')
gumb20.grid(row = 4, column = 1, ipady = 40)
gumb21 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][3][2]])
gumb21.insert(0, seznam3[št_kenkena][3][2] + '           ')
gumb21.grid(row = 4, column = 2, ipady = 40)
gumb22 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][3][3]])
gumb22.insert(0, seznam3[št_kenkena][3][3] + '           ')
gumb22.grid(row = 4, column = 3, ipady = 40)
gumb23 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][3][4]])
gumb23.insert(0, seznam3[št_kenkena][3][4] + '           ')
gumb23.grid(row = 4, column = 4, ipady = 40)
gumb24 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][3][5]])
gumb24.insert(0, seznam3[št_kenkena][3][5] + '           ')
gumb24.grid(row = 4, column = 5, ipady = 40)

gumb25 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][4][0]])
gumb25.insert(0, seznam3[št_kenkena][4][0] + '           ')
gumb25.grid(row = 5, column = 0, ipady = 40)
gumb26 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][4][1]])
gumb26.insert(0, seznam3[št_kenkena][4][1] + '           ')
gumb26.grid(row = 5, column = 1, ipady = 40)
gumb27 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][4][2]])
gumb27.insert(0, seznam3[št_kenkena][4][2] + '           ')
gumb27.grid(row = 5, column = 2, ipady = 40)
gumb28 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][4][3]])
gumb28.insert(0, seznam3[št_kenkena][4][3] + '           ')
gumb28.grid(row = 5, column = 3, ipady = 40)
gumb29 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][4][4]])
gumb29.insert(0, seznam3[št_kenkena][4][4] + '           ')
gumb29.grid(row = 5, column = 4, ipady = 40)
gumb30 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][4][5]])
gumb30.insert(0, seznam3[št_kenkena][4][5] + '           ')
gumb30.grid(row = 5, column = 5, ipady = 40)

gumb31 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][5][0]])
gumb31.insert(0, seznam3[št_kenkena][5][0] + '           ')
gumb31.grid(row = 6, column = 0, ipady = 40)
gumb32 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][5][1]])
gumb32.insert(0, seznam3[št_kenkena][5][1] + '           ')
gumb32.grid(row = 6, column = 1, ipady = 40)
gumb33 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][5][2]])
gumb33.insert(0, seznam3[št_kenkena][5][2] + '           ')
gumb33.grid(row = 6, column = 2, ipady = 40)
gumb34 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][5][3]])
gumb34.insert(0, seznam3[št_kenkena][5][3] + '           ')
gumb34.grid(row = 6, column = 3, ipady = 40)
gumb35 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][5][4]])
gumb35.insert(0, seznam3[št_kenkena][5][4] + '           ')
gumb35.grid(row = 6, column = 4, ipady = 40)
gumb36 = tk.Entry(okno, bg = barve[seznam2[št_kenkena][5][5]])
gumb36.insert(0, seznam3[št_kenkena][5][5] + '           ')
gumb36.grid(row = 6, column = 5, ipady = 40)

def rešitve():
    sez = []
    seznam = seznam1[št_kenkena]
    for element in seznam:
        for podelement in element:
            sez.append(podelement)
    return sez

def preberi_rešitve():
    pridobljene_rešitve = [[gumb1.get(), gumb2.get(), gumb3.get(), gumb4.get(), gumb5.get(), gumb6.get()], \
    [gumb7.get(), gumb8.get(), gumb9.get(), gumb10.get(), gumb11.get(), gumb12.get()], \
    [gumb13.get(), gumb14.get(), gumb15.get(), gumb16.get(), gumb17.get(), gumb18.get()], \
    [gumb19.get(), gumb20.get(), gumb21.get(), gumb22.get(), gumb23.get(), gumb24.get()], \
    [gumb25.get(), gumb26.get(), gumb27.get(), gumb28.get(), gumb29.get(), gumb30.get()], \
    [gumb31.get(), gumb32.get(), gumb33.get(), gumb34.get(), gumb35.get(), gumb36.get()]]
    nov_sez = []
    for element in pridobljene_rešitve:
        for podelement in element:
            if '+' in podelement or '-' in podelement or '*' in podelement or ':' in podelement:
                for znak in podelement:
                    if znak in '*:+-':
                        mesto = podelement.index(znak)
                        nov = podelement[(mesto + 1):]
                        nov_sez.append(nov.replace(' ', ''))
            else:
                nov_sez.append(podelement.replace(' ', ''))
    return nov_sez

def preveri_rešitve():
    if preberi_rešitve() == rešitve():
        return 'Čestitke! Pravilno ste izpolnili kenken!'
    else:
        return 'Vaša rešitev je žal napačna.'

def okno_preveri_rešitve():
    okno2 = tk.Tk()
    rešitve = tk.Label(okno2, text = preveri_rešitve(), bg = 'papayawhip', font = 'slant')
    rešitve.pack()
    okno2.mainloop()
    
gumb_za_preverjanje_rešitev = tk.Button(okno, text = 'Preveri rešitve', command = okno_preveri_rešitve, cursor = 'hand2', activebackground = 'wheat', bg = 'papayawhip', width = '16')
gumb_za_preverjanje_rešitev.grid(row = 0, column = 1)
gumb_za_preverjanje_rešitev.pack

besedilo_navodila = 'Kenken je matematična uganka, ki jo je leta 2004 razvil japonski učitelj Tetsuya Miyamoto. \n Rešuje se ga tako, da se v vsako vrstico in stolpec dolžine n napiše prvih n različnih naravnih \n števil, v vsako polje iste barve pa taka števila, da iz njih s pripadajočo operacijo dobimo \n rezultat, napisan v polju.'

def povej_mi_navodila():
    okno3 = tk.Tk()
    navodila = tk.Label(okno3, text = besedilo_navodila, bg = 'papayawhip', font = 'slant', justify = 'left')
    navodila.pack()
    okno3.mainloop()

gumb_za_navodila = tk.Button(okno, text = 'Povej mi navodila', command = povej_mi_navodila, cursor ='hand2', activebackground = 'wheat', bg = 'papayawhip', width = '16')
gumb_za_navodila.grid(row = 0, column = 0)
gumb_za_navodila.pack

def začni_še_enkrat():
    python = sys.executable
    os.execl(python, python, * sys.argv)

gumb_za_nov_kenken = tk.Button(okno, text = 'Nov kenken', command = začni_še_enkrat, cursor = 'hand2', activebackground = 'wheat', bg = 'papayawhip', width = '16')
gumb_za_nov_kenken.grid(row = 0, column = 2)
gumb_za_nov_kenken.pack

def izhod():
    okno.destroy()

gumb_za_izhod = tk.Button(okno, text = 'Izhod', command = izhod, cursor = 'hand2', activebackground = 'wheat', bg = 'papayawhip', width = '16')
gumb_za_izhod.grid(row = 0, column = 3)
gumb_za_izhod.pack

okno.mainloop()
