#from tkinter import *
#fenster = Tk()
#fenster.title (" Willkommen bei ihrem Tool für die Ausrechnung des Wohnfläche ")
#eingaben = []
Liste_zimmer = []
Berechnung = 0
schleife_seite = "Ja"
Zimmer = int
 
#while schleife == "Ja":
while schleife_seite == "Ja": 
    print("Bitte Geben sie die Bezeichnung zu dem Raumes an")
    name_zimmer = input()
    temp_zimmer = 0
    schleife = "Ja"
    Max_m2 = 0 

    while schleife == "Ja":
        print (" Bitte Geben sie die erste  seite  bzw.  Größe des Zimmers an ")
        größe_zimmer = int(input())
        temp_zimmer = (temp_zimmer + größe_zimmer)
        print(" Gibt es noch eine Seite ")
        abfrage_seite = input()
        if abfrage_seite == "Nein":
            schleife = "Nein"
            größe_zimmer = temp_zimmer * 2
            Räume = (name_zimmer + str(größe_zimmer))
            Max_m2 = Max_m2 + größe_zimmer
            Liste_zimmer.append(Räume)     
    print ("Gibt es noch ein weiteres Zimmer")
    abfrage1 = input() 
    if abfrage1 == "Nein":
        schleife_seite = "Nein"  
        
    #abfrage = (input())
    if abfrage1 == "Nein":
         schleife = "Nein"


Berechnung = Liste_zimmer
for each in Liste_zimmer:
    print()
print ("Für ihre Zimmer wurden Insgesamt", Berechnung," in Größe angegebenM^2", "Berechnet", " Die Generelle M2 liegt bei", Max_m2)