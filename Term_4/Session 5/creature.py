class Creature:

    def __init__(self , health=100 , attackdamage=10 , name=""):
        self.is_alive = True
        self.name = name
        self.health = health 
        self.attackdamage = attackdamage
        attackdamage = 10 
    def attack(self , multipleir):
        return int(self.attackdamage*multipleir)
    def decrease_health_h(self, amount_h):
        self.health -= amount_h
        if self.health <= 0 :
            self.is_alive = False