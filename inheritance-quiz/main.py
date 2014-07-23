'''
Daniel O'Carroll
DPW1407
July 22nd, 2014
'''

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        r = Rogue()
        self.response.write(r.print_info())


#Make an Abstract class
class Hero(object):
    def __init__(self):
        self.__health = 200
        self.strength = 20
#Created a Getter to access health property
    @property
    def health(self):
        return self.__health

    #create first method
    def calc_stamina(self):
        stamina = self.health + self.strength
        return stamina

    #create second method
    def print_info(self):
        return "Health: " + str(self.health) + " Strength: " + str(self.strength) + " Stamina: " + str(self.calc_stamina())


#create first subclass
class Rogue(Hero):
    def __init__(self):
        Hero.__init__(self)
        self.crit = 200
        self.__agility = 250
        self.energy = 25

    @property
    def agility(self):
        return self.__agility

    #create polymorphic method
    def calc_stamina(self):
        stamina = self.agility * self.crit
        return stamina


#create second subclass
class Warrior(Hero):
    def __init__(self):
        Hero.__init__(self)
        self.power = 200
        self.__rage = 10
        self.energy = 20

    @property
    def rage(self):
        return self.__rage

    def calc_stamina(self):
        stamina = self.power - self.rage
        return stamina



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
