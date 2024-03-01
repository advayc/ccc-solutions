players = int(input())
gold_team_counter = 0

for i in range(players):
    points = int(input())
    fouls = int(input())
    
    stars = 5 * points - 3 * fouls        

    if stars > 40:
        gold_team_counter += 1

output = str(gold_team_counter)
if gold_team_counter == players:
    output += '+'

print(output)