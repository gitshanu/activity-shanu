t=1
print("Input for team 1")
while t<=2:
    team_scored = int(input("Enter the total runs scored by Team 1: "))
    team_faced = int(input("Enter the total overs faced by Team : "))
    team_conceded = int(input("Enter the total runs conceded by Team : "))
    team_bowled= int(input("Enter the total overs bowled by Team : "))
    if t==1:
        team1_Nrr = (team_scored / team_faced) - (team_conceded / team_bowled)
        print("Input for team 2")
    else:
        team2_Nrr = (team_scored / team_faced) - (team_conceded / team_bowled)
    t+=1
if team1_Nrr > team2_Nrr:
    print("Team 1 has a higher Net Run Rate and tops the points table.")
elif team2_Nrr > team1_Nrr:
    print("Team 2 has a higher Net Run Rate and tops the points table.")
else:
    print(" Match Tie")
