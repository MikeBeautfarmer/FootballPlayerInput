class FootballPlayer:
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards, games):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.games = games


print("Gib die Daten für den Fussballspieler ein!")

f_name = input("Gib den Vornamen an: ")
l_name = input("Gib den Nachnamen an: ")
height = input("Gib die Spielergröße an: ")
weight = input("Gib das Gewicht des Spielers an: ")
goals = input("Gib die Tore das Spielers an: ")
y_cards = input("Gib die gelben Karten an: ")
r_cards = input("Gib die roten Karten an: ")
g_played = input("Gib die Gesamtspielanzahl des Spielers an: ")

new_player = FootballPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight),
                            goals=int(goals), yellow_cards=int(y_cards), red_cards=int(r_cards), games=int(g_played)
                            )

with open("footballplayers.txt", "w") as football_file:
    football_file.write(str(new_player.__dict__))

print("Player successfully entered!")
print("Player's data: {0}".format(new_player.__dict__))
