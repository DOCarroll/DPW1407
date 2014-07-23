'''
Daniel O'Carroll
DPW1407
July 22nd, 2014
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        r = Rogue()
        self.response.write(r.health)


#Make an Abstract Class
class Hero(object):
    def __init__(self):
        self.__health = 200
        self.strength = 20
#Created a Getter to access health property
    @property
    def health(self):
        return self.__health







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
