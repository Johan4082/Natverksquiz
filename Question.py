import random
from random import shuffle

question_list = [
    "1. Hur många bitar är en byte? ", "8",
    "2. Hur många lager är det i Osi-modellen ", "7",
    "3. Hur många bitar är en ipv4 adress? ", "32",
    "4. Vilket kommando används, för att se om det finns kontakt mellan enheter? ", "ping",
    "5. Är TCP en förkortning av Transmission Control Protocol? ", "ja",
    "6  Är Von Neumann ett namn på en Laptop? ", "nej",
    "7. Är Ubuntu en Windows distrubition? ", "nej",
    "8. Är talet 0x54EF skrivet i hexadecimalform? ", "ja",
    "9. Är python ett filsystem? ", "nej",
    "10 Säljer Macintosh äpplen? ", "nej",
]


points = 0
current = 0
quiz = 1
a = "ja"

print("Välkommen till mitt Nätverksquiz")

while quiz < 11:


    question = input(question_list[current])

    if question == question_list[current+1]:
        print("Det är rätt!")

        current = current + 2
    else:
        print("Det är fel!")
        current = current + 2
    quiz = quiz + 1

    a = input("Vill du fortsätta?" "Ja/Nej ")
    if a == "Nej":
        quit()


print("Bra jobbat!" "Du fick" + str((quiz/10) * 100) + "%.")

