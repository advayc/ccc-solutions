p = int(input()) 
n = int(input()) 
r = int(input())

day = 0
total_infected = n
newly_infected = n

while total_infected <= p:
    day += 1
    newly_infected *= r
    total_infected += newly_infected

print(day)
