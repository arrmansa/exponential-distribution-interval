import random

p = 0.0000001
chunk_n = 10000
chunk_p = lambda p, n : 1 - (1 - p)**n

def get_output(n, p, probe_number):
    value = (1-p)**n
    probability_part = 0
    for index in range(n):
        probability_part = ((1-p)**index)*p
        if value + probability_part < probe_number:
            value += probability_part
        else: 
            break
    return index + 1

count = 0
number = random.random()
while number < 1 - chunk_p(p, chunk_n):
    number = random.random()
    count += chunk_n
    
count += get_output(chunk_n, p, number)
print(count)
