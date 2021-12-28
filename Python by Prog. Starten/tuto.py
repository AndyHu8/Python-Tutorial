#Python Tuto #1 Dein erstes Programm
#Python und IDE installieren
#Projekt erstellen (Python-Datei erstellen und mit IDE öffnen)

#Hallo Welt
print("Hallo Welt")

#Python Tuto #2 Zahlen in Py
print(10, -7, 7 + 4)
print((3 + 2) * (2 + 3))
print(3.4)

#Python Tuto #3 Strings in Py
print("Ein String")
print("Das" + "Dies")
print('''Mehr
        zeilig''')

#Python Tuto #4 Variablen
age = 20
print(age)

#Python Tuto #5 Datyentypen
print("String" + "Verkettung")
print(10 + 3)
#print(10 + "String") #Geht nicht

#Python Tuto #6 input()-Funktion
print("Start")
inputName = input()
print("Ich heiße " + inputName)
print("Ende")

#Python Tuto #7 Type-Casting-Funktionen
value1 = input("Erste Zahl: ")
value2 = input("Zweite Zahl: ")
print(int(value1) + int(value2))

#Python Tuto #8 Zuweisungsoperator
example = 22
example += 22

#Python Tuto #9 Vergleichsoperator und bool
print(1 < 5)
print(1 <= 5)
print(1 != 5)
wahr = True
falsch = False

#Python Tuto #10 If-Anweisung
age = int(input("Dein Alter: "))

if age < 18:
    print("Du bist minderjährig")

#Python Tuto #11 Elif und Else Zweige
if age < 18:
    print(16)
elif age == 18:
    print(18)
else:
    print(20)

#Python Tuto #12 Logische Operatoren
if (age == 18) and (example == 22):
    print(18, 22)

#Python Tuto #13 While-Schleife
while 0 < 10:
    print("0 ist immer kleiner als 10")

#Python Tuto #14 Einführung Listen
nummern = [3, 5, 15, 17, 20]
nichtNurNummern = [3, 5, 15, 17, 20, "Andy"]

#Python Tuto #15 Zugriff auf Listen
nichtNurNummern2 = [3, 5, 15, 17, 20, "Andy"]
print(nichtNurNummern2[0])

#Python Tuto #16 For-Schleife
for element in nichtNurNummern:
    print(element)

#Python Tuto #17 For-Schleife als Zählerschleife
for element in range(1, 10, 2): #Start- und Endwert und Schrittweite
    print(element)

#Python Tuto #18 Funktionen
def say_hello():
    print("Hallo")
say_hello()

#Python Tuto #19 Funktionen mir Para
def say_hello2(name):
    print("Hallo " + name)
say_hello2("Andy")

#Python Tuto #20 Funktionen mit Rückgabe
def maximum(a, b):
    if a < b:
        return b
    else:
        return a
zahl = maximum(3, 7)
print(zahl)

#Python Tuto #21 Objektorientierung (Konzept)
#OOP: Darstellung von Daten (Welt besteht aus komplexen Objekten)
#Eigene Datentypen erstellen

#Python Tuto #22 Klassen und Objekten
class Car:
    def __init__(self):
        self.hersteller = ""
        self.ps = 0
        self.farbe = ""
car1 = Car()
car1.hersteller = "BMW"

#Python Tuto #23 Self Parameter
#Referenz auf ein Objekt => Self überliefert die Referenz de ausführenden Objekt

#Python Tuto #24 Methoden in Klassen
class Car2:
    def __init__(self):
        self.hersteller = ""
        self.ps = 0
        self.farbe = ""
        self.x_pos = 5
        self.y_pos = 5

    def drive(self, x, y):
        self.x_pos += x
        self.y_pos += y
car2 = Car2
car2.drive(5, 5)



