__author__ = 'dyju'

Wynik=[1,1]
suma=0

for i in range (2,40):
    Wynik.append(Wynik[i-1]+Wynik[i-2])
    if Wynik[i]<4000000:
        print (i, ". ", Wynik[i])