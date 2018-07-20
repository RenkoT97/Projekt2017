import tkinter as tk
import random
import sys
import os

def pretvori_dat_v_sez(ime_dat):
    with open(ime_dat) as dat:
        datoteka = dat.readlines()
        seznam = [[[crka.strip() for crka in crke.split(',') if crka.strip() not in [" ", ","]] for crke in vrstica.split("~")[1:-1] if vrstica.strip()] for vrstica in datoteka]
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

st_kenkena = random.randint(0, 9)

barve = {'A': 'chocolate3', 'B': 'green yellow', 'C': 'RoyalBlue3', 'D': 'maroon1', 'E': 'NavajoWhite2', \
'F': 'lime green', 'G': 'DarkOrange1', 'H': 'Sienna1', 'I': 'DeepPink4', 'J': 'SkyBlue3', 'K': 'purple4', \
'L': 'SeaGreen1', 'M': 'gold', 'N': 'red3', 'O': 'LightPink3'}

okno = tk.Tk()

seznam_vhodov = []
for i in range(6):
    podsez = []
    for j in range(6):
        vhod = tk.Entry(okno, bg = barve[seznam2[st_kenkena][i][j]])
        vhod.insert(0, seznam3[st_kenkena][i][j] + '           ')
        vhod.grid(row = i + 1, column = j, ipady = 40)
        podsez.append(vhod)
    seznam_vhodov.append(podsez)

def resitve():
    sez = []
    seznam = seznam1[st_kenkena]
    for element in seznam:
        for podelement in element:
            sez.append(podelement)
    return sez

def preberi_resitve():
    pridobljene_resitve = []
    for i in range(6):
        podsez = []
        for j in range(6):
            podsez.append(seznam_vhodov[i][j].get())
        pridobljene_resitve.append(podsez)
    nov_sez = []
    for element in pridobljene_resitve:
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

def preveri_resitve():
    if preberi_resitve() == resitve():
        return 'Čestitke! Pravilno ste izpolnili kenken!'
    else:
        return 'Vaša rešitev je žal napačna.'

def okno_preveri_resitve():
    okno2 = tk.Tk()
    resitve = tk.Label(okno2, text = preveri_resitve(), bg = 'papayawhip', font = 'slant')
    resitve.pack()
    okno2.mainloop()
    
gumb_za_preverjanje_resitev = tk.Button(okno, text = 'Preveri rešitve', command = okno_preveri_resitve, cursor = 'hand2', activebackground = 'wheat', bg = 'papayawhip', width = '16')
gumb_za_preverjanje_resitev.grid(row = 0, column = 1)
gumb_za_preverjanje_resitev.pack

besedilo_navodila = 'Kenken je matematična uganka, ki jo je leta 2004 razvil japonski učitelj Tetsuya Miyamoto. \n Rešuje se ga tako, da se v vsako vrstico in stolpec dolžine n napiše prvih n različnih naravnih \n števil, v vsako polje iste barve pa taka števila, da iz njih s pripadajočo operacijo dobimo \n rezultat, napisan v polju.'

def povej_mi_navodila():
    okno3 = tk.Tk()
    navodila = tk.Label(okno3, text = besedilo_navodila, bg = 'papayawhip', font = 'slant', justify = 'left')
    navodila.pack()
    okno3.mainloop()

gumb_za_navodila = tk.Button(okno, text = 'Povej mi navodila', command = povej_mi_navodila, cursor ='hand2', activebackground = 'wheat', bg = 'papayawhip', width = '16')
gumb_za_navodila.grid(row = 0, column = 0)
gumb_za_navodila.pack

def zacni_še_enkrat():
    python = sys.executable
    os.execl(python, python, * sys.argv)

gumb_za_nov_kenken = tk.Button(okno, text = 'Nov kenken', command = zacni_še_enkrat, cursor = 'hand2', activebackground = 'wheat', bg = 'papayawhip', width = '16')
gumb_za_nov_kenken.grid(row = 0, column = 2)
gumb_za_nov_kenken.pack

def izhod():
    okno.destroy()

gumb_za_izhod = tk.Button(okno, text = 'Izhod', command = izhod, cursor = 'hand2', activebackground = 'wheat', bg = 'papayawhip', width = '16')
gumb_za_izhod.grid(row = 0, column = 3)
gumb_za_izhod.pack

okno.mainloop()
