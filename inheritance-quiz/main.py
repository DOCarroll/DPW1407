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
        power = 50





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
