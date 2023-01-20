class Character:
    def __init__(self):
        self.health = 100
        self.exp = 0
        self.level = 1
        self.attack = 10
        self.defense = 10
        self.exp_to_level = 50

   def battle(self, enemy):
        while self.health > 0 and enemy.health > 0:
            print("You are fighting a {}!".format(enemy.name))
            print("Your health: {}".format(self.health))
            print("What would you like to do? (fight/defend/heal)")
            action = input()
            if action == "fight":
                enemy.health -= self.attack
                print("You dealt {} damage to the enemy!".format(self.attack))
            elif action == "defend":
                self.defense += 5
                print("You defended and your defense increased to {}%".format(self.defense))
            elif action == "heal":
                self.health += 10
                print("You healed and regained 10 health!")
            enemy_action = enemy.attack()
            if enemy_action == "attack":
                self.health -= ((enemy.attack_power * (100 - self.defense))/100)
                print("The enemy attacked and dealt {} damage!".format((enemy.attack_power * (100 - self.defense))/100))
        if self.health > 0:
            self.exp += enemy.exp
            print("You defeated the enemy and gained {} exp!".format(enemy.exp))
            if self.exp >= self.exp_to_level:
                self.level += 1
                self.exp = self.exp - self.exp_to_level
                self.exp_to_level += (self.exp_to_level * 0.3)
                self.attack += 5
                self.defense += 5
                print("You leveled up to level {}!".format(self.level))
                print("EXP to next level: {}".format(self.exp_to_level))
        else:
            print("You were defeated!")
        enemy = self.spawn_enemy(enemy.name)
        return enemy
   def spawn_enemy(self, name):
        if name == "Goblin":
            return Enemy("Goblin", 50, 10, 5, 20)
        elif name == "Undead":
            return Enemy("Undead", 85, 15, 3, 30)
        elif name == "Wolf":
            return Enemy("Wolf", 75, 20, 0, 40)

class Enemy:
    def __init__(self, name, health, attack_power, defense, exp):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.exp = exp

    def attack(self):
        return "attack"
        
import random

goblin = player.spawn_enemy("Goblin")
undead = player.spawn_enemy("Undead")
wolf = player.spawn_enemy("Wolf")

while True:
    print("What would you like to do? (rest/see stats/wander)")
    action = input()
    if action == "rest":
        player.rest()
    elif action == "see stats":
        player.stats()
    elif action == "wander":
        encounter = random.random()
        if encounter < 0.3:
            goblin = player.battle(goblin)
        elif encounter < 0.5:
            undead = player.battle(undead)
        elif encounter < 0.6:
            wolf = player.battle(wolf)
        else:
            print("You found nothing important.")
