print("Enter runs scored by each player in 60 balls : ")
player_1 = int(input("Player 1 : "))
player_2 = int(input("Player 2 : "))
player_3 = int(input("Player 3 : "))

print("\n STRIKE RATE INDEX - ")
print("Player 1 -",(player_1/60)*100)
print("Player 2 -",(player_2/60)*100)
print("Player 3 -",(player_3/60)*100)

print("\n Runs scored if players played 60 more balls : ")
print("Player 1 -",player_1*2)
print("Player 2 -",player_2*2)
print("Player 3 -",player_3*2)

print("\n Maximum number of sixes each player could have hit : ")
print("Player 1 -",player_1//6)
print("Player 2 -",player_2//6)
print("Player 3 -",player_3//6)
