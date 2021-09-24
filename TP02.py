# def TP02():
 # print ("4.1 accès aux éléments d'une chaine")
 # ch = "Esope reste ici et se repose"
 # len(ch)

print ("4.1 accès aux éléments d'une chaine")

ch = "Esope reste ici et se repose"
print (ch)

print (ch [22:28])

print ("c")
print (ch [13])

tempDeg = "24°"
vent = "12km/h"
humidite = "45%"
meteo = f"aujourd’hui, il fait {tempDeg} , la vitesse du vent est {vent} ,l’humidité est {humidite}"


print (meteo)


d = 'aujourd’hui, il fait beau , la vitesse du vent est faible ,l’humidité est correcte' 

a = "romain"
b = "yoyan"
c = "oui"

print (a + b + c)

print ("cette chaine de contient " +str (len(a))+ " caracteres et celle-ci contient " + str(len(b)) + " caracteres par contre")


a1 = "age {} " .format(21)
b1 = "numero secu {} " .format(21313)
c1 = "code bancaire {} " .format(123)

print (a1 + b1 + c1)

