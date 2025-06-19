# Hornet_test.py - Testing hornet boss move attacks

# Imports turtle and random

import random
import turtle

# circle_fill: Given a radius, draws and fills a circle. Returns nothing.
# Causes an error if the radius isn't a number.

def circle_fill(rad):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0+rad,0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()


# needle_attack: 

def needle_attack(hp):
    turtle.pencolor("white")
    turtle.speed(0)
    dir = random.randint(1,4)
    if dir == 1:
        turtle.goto(-100,0)
        dodge = "left"
    elif dir == 2:
        turtle.goto(0,100)
        dodge = "up"
    elif dir == 3:
        turtle.goto(100,0)
        dodge = "right"
    elif dir == 4:
        turtle.goto(0,-100)
        dodge = "down"
    turtle.goto(0,0)
    turtle.clear()
    evade = input("Quickly enter the direction Hornet leapt to to avoid the attack! ")
    evade = evade.lower().strip()

    if evade == dodge:
        print("You dodged the attack in time...")
    else:
        print("You failed to dodge the attack.")
        hp -= 100

    turtle.pencolor("yellow")
    turtle.speed(10)
    return hp

# shaw:

def shaw(hp):
    print("You can dodge down for a chance to heal...")
    print("Or you can dodge left for a lower chance of being hit!")
    turtle.pencolor("white")
    turtle.speed(0)
    circle_fill(50)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.pencolor("yellow")
    evade = random.randint(1,5)
    dir = input("Quickly! Will you dodge left or down? ")
    dir = dir.lower().strip()
    if dir == "left" and evade <= 4:
        print("You managed to barely escape Hornet's needle...")
        turtle.goto(-50,0)
    elif dir == "down" and evade <= 2:
        print("You dodge the attack, and heal!")
        hp += 75
        turtle.goto(0,-50)
    elif dir == "down" and evade <= 3:
        print("You avoid the initial attack, but Hornet follows up with a needle strike!")
        hp = needle_attack(hp)
    else:
        print("You are hit by the attack!")
        hp -= 100
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.speed(10)
    turtle.clear()
    return hp

# hornet: 

def hornet(stats):
    base_hp = stats[0]*30
    dmg = stats[1]*10
    enemy_hp = 3300
    
    while enemy_hp > 0:
        print("Hornet attacks!")
        dmg = stats[1]*10
        enemy_hp = 3300
        hp = stats[0]*30

        while hp > 0:
            print(f"Hornet's health is {enemy_hp:.2f} and your health is {hp:.2f}.\n")
            move = input("Attack, charge, or heal: ")
            move = move.lower().strip()
            miss = random.randint(1,10)

        # Your move
            
            if miss > 8:
                print("Hornet's quick movement causes you to miss!")
            elif move == "attack":
                enemy_hp -= dmg
                print("You manage to hit Hornet!")
            elif move == "charge":
                dmg = dmg*1.5
                print("You have charged your attack power!")
            elif move == "heal":
                hp += stats[2]*5.5
                if hp > base_hp:
                    hp = base_hp
                print("You have healed.")
            else:
                print("Invalid command!")
        
        # Hornet's move

            move = random.randint(1,9)

            if move <= 5:
                print("Hornet attacks with her needle!\n")
                hp = needle_attack(hp)
            elif move <= 7:
                print("Hornet has used her silk to heal!\n")
                enemy_hp += 300
                if enemy_hp > 3300:
                    enemy_hp = 3300
            else:
                print("Hornet shaws and swings her needle in a circle around her!\n")
                hp = shaw(hp)
                if hp > base_hp:
                    hp = base_hp
            
            if enemy_hp <= 0:
                stats[3] += 20
                # stats = lvl_up(stats)
                print("You defeated hornet!")
                break
            elif hp <= 0:
                print ("YOU DIED\n")
    return stats


#----MAIN PROGRAM----

# Sets us stats and compiles into a list.

vigor = 14
strength = 14
faith = 10
enemy_def = 0

stats=[vigor,strength,faith,enemy_def]

# Sets up the turtle colors

turtle.bgcolor("black")
turtle.pencolor("yellow")
turtle.pensize(2)

turtle.setheading(90)

stats = hornet(stats)