# Pobriši ime seznama v datoteki in pusti samo seznam!!
# rabiš seznam seznama, ne naborov! Sami oglati oklepaji!

with open('rezultati.txt') as dat1:
    with open('tabele.txt') as dat2:
        def start():
            a = random.randint(1, 10)
            for a in range(10):
                A = dat1.readline(a)
            for a in range(10):
                print(dat2.readline(a))
        def igraj():
            st_vrstice = input('Izberite vrstico, v katero želite vpisati število! ')
            st_stolpca = input('Izberite stolpec, v katerega želite vpisati število! ')
            stevilo = input('Vpišite število! ')
        def preveri_pravilnost():
            if A == 
