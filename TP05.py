"""def afficher3fois(x):
  print (str (x) + str(x)+ str (x))
afficher3fois("x")

def tripler(x):
  return (str(x) + str(x) + str(x))
print (tripler("x"))"""

""""def ligneCar(n, ca):
  return (ca[0:n])

chaine = "janvier fevrier mars"
n = input("oui")
print (ligneCar(int(n), chaine))"""

nf = input("choix oui ")
f = open(nf + ".txt", "x")

t = ("janvier", "fevrier","mars", "avril", "mai", "juin", "juillet", "Aout", "septembre", "octobre", "novembre", "decembre")

for x in range (0, 12):
  f.write(t[x], "\n
")
f.close()
  
  


