#Guess the secret number

secret = 7

input("Willkommen zum Guess the secret Number-Spiel.")

input("Deine Aufgabe: Rate eine Zahl zwischen 1 und 10.")

guess = input("Gib deinen Tipp ein: ")

print("Dein Tipp: "  + guess)

if guess == "7":
    print("YAY!Du hast die geheime Zahl erraten!")
else:
    print("Sorry! Du hast die geheime Zahl nicht erraten.")

