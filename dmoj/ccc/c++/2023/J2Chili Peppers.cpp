n = int(input())

SHU_values = {
"Poblano": 1500,
"Mirasol": 6000,
"Serrano": 15500,
"Cayenne": 40000,
"Thai": 75000,
"Habanero": 125000
}

T = 0

for _ in range(n): 
    pepper_name = input()
    T += SHU_values[pepper_name] 

print(T)