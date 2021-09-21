'''
Oppgave 2: Regning med løkker
'''

#2.1 og 2.2
user_input = int(input("Skriv et tall. 0 avslutter innlesingen: "))
my_list = list()

while user_input != 0:
    my_list.append(user_input)
    user_input = int(input("Skriv et tall. 0 avslutter innlesingen: "))

#2.3
for i, number in enumerate(my_list):
    print(f"my_list[{i}] = {number}")


#2.4
my_sum = 0
for number in my_list:
    my_sum += number

print(f"summen av alle tall = {my_sum}.")


#2.5
min_val = max_val = my_list[0] #initieres variablene

#min
for number in my_list:
    if number < min_val:
        min_val = number

assert min_val == min(my_list)
print(f"Det minste tallet er {min_val}")

#max
for number in my_list:
    if number > max_val:
        max_val = number

assert max_val == max(my_list)
print(f"Det største tallet er {max_val}")