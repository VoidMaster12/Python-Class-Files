# movies.py - Price of tickets
# Matthew Raines

# This was created to calculate costs of tickets to go to the movies depending on
# the number of people going.

my_cost = 9.50
ask = True

while ask:
    try:
        ppl = int(input("How many people are going to the movies?\n"))
        ask = False
    except ValueError:
        print("Invalid number.\n")

if (ppl < 25) and (ppl > 0):
    cost = my_cost+(ppl-1)*12.00  # $12 is the individual cost for all but me.
elif (ppl >= 25):
    cost = ppl*7.25   # $7.25 is the individual cost for groups larger than 25.
elif (ppl == 0):
    cost=0

print(f"The total cost of the tickets is ${cost:.2f}")