from creature import Creature


class human(Creature):
    pass

        

class monster:
    def __init__(self ,name="" , health=150 , attackdamage=70 , armor=100):
        self.is_alive = True
        self.health = health
        self.attackdamage = attackdamage
        self.armor = armor
        self.name = name
    def attack(self , multipleir):
        return int(self.attackdamage*multipleir)
    def decrease_health_m(self , amount_m ):
        if self.armor > 0:
            self.armor -= amount_m
            if self.armor < 0:
                self.health += self.armor
                self.armor = 0
            else:
                self.health -= amount_m
                if self.health <= 0:
                    self.is_alive = False

