annee = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12] 

annee.pop(9)
annee.pop(9)
annee.pop(9)
annee.append("Octobre")
annee.append("Novembre")
annee.append("Decembre")
print (annee)


moisDeLannee = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre')

print (moisDeLannee[3])


if "Mars" in moisDeLannee :
  print("Mars")

age = {"pierre" : 35 , "paul" : 32 , "Jacques" : 27 , "andre" : 23 , "david" : 22, "veronique" : 21, "sylvie" : 30, "damien" : 37} 

print ("l'age de sylvie est ")
print (age["sylvie"])

if "jean" in age:
  print ("jean est ici ")
else:
  print ("pas la ") 


club = {
  "pierre durand":(1986,1.72,70),
  "victor dupont":(1987,1.89,57),
  "paul dupuis":(1989,1.60,92),
  "jean rieux":(1985,1.88,77)
  }

nomSportif = input()
dateNaissSportif = club[nomSportif][0]
poidsSportif = club[nomSportif][2]
tailleSportif = club[nomSportif][1]


phrase = 'Le sportif nommé %s est né en %s, sa taille est de %sm et son poids est de %skg'

print (phrase %(nomSportif,dateNaissSportif, tailleSportif, poidsSportif))






