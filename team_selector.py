import random

players = ["Samwell", "Jorah", "Robb", "Joffrey", "Sansa",
           "Bran", "Ygritte", "Walder", "Sandor", "Grey Worm",
           "Viserys", "Drogon", "Viserion", "Rhaegal",
           "Jon", "Tyrion", "Jaime", "Cersei", "Daenerys",
           "Robert", "Qyburn", "Ramsey", "Theon", "Varys"]

print("Welcome to the Game of Thrones team allocator! Which tean would YOU choose?")

while True:
    random.shuffle(players)
    
    team1 = players[:len(players)//2]
    print("Team 1 Captain: " + random.choice(team1))
    print("Team 1: ")
    for player in team1:
        print(player)
    
    team2 = players[len(players)//2:]
    print("\nTeam 2 Captain: " + random.choice(team2))
    print("Team 2: ")
    for player in team2:
        print(player)
    
    response = input("Pick the teams again? Type yes or no: ")
    if response == "no":
        response = input("Which team are YOU picking? 1 or 2: ")
        if response == "1":
            print("Oooof good choice!")
        else:
            print("Interesting choice!")
        print("Thank you for using the Game of Thrones team allocator!")
        break

