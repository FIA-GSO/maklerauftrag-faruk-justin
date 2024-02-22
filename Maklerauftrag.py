#from tkinter import *
#fenster = Tk()
#fenster.title (" Willkommen bei ihrem Tool für die Ausrechnung des Wohnfläche ")
#eingaben = []
Liste_zimmer = []
Berechnung = 0
schleife = "Ja"
schleife_seite = "Ja"
Zimmer = int
#while schleife == "Ja":
while schleife_seite == "Ja": 
    print("Bitte Geben sie die Bezeichnung zu dem Raumes an")
    name_zimmer = input()
    while schleife == "Ja":
        print (" Bitte Geben sie eine seite  bzw.  Größe des Zimmers an ")
        größe_zimmer = int(input())
        Zimmer = (größe_zimmer * 2)
        print(" Gibt es noch eine Seite ")
        abfrage_seite = input()
        if abfrage_seite == "Nein":
            schleife = "Nein"
    print ("Gibt es noch ein weiteres Zimmer")
    Räume = (name_zimmer + str(größe_zimmer))
    abfrage1 = input()
    if abfrage1 == "Nein":
        schleife_seite = "Nein"  
       
    #abfrage = (input())
    #if abfrage == "Nein":
        # schleife = "Nein"
    Liste_zimmer.append(Räume)

Berechnung = (Liste_zimmer * 2)
print ("Für ihre Zimmer wurden Insgesamt", Berechnung," in Größe angegebenM^2", "Berechnet")