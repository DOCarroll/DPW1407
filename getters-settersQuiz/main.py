'''
Daniel O'Carroll
DPW1407
July 24th, 2014
Getters & Setters Quiz
'''

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        c = Counter()
        counter = 0
        self.response.write(counter)
        self.response.write(p.print_out())
        if self.request.GET:
            p.counter += 1
            c.counter += p.counter
            self.response.write((p.counter))


class Page(object):
    def __init__(self):
        self.counter = 2
        self.open = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Counting Up!</title>
        </head>
        <body>
    """
        self.content = """
        <a href="?{self.counter}">Count Up</a>
        """

        self.close = """
        </body>
        </html>
        """
        self.all = self.open + self.content + self.close + str(self.counter)

    def print_out(self):
        self.all.format(**locals())
        return self.all


class Counter(object):
    def __init__(self):
        self.__counter = 0

    @property
    def counter(self):
        return self.__counter

    def print_out(self):
        return self.__counter

    @counter.setter
    def counter(self, i):
        self.__counter = i
        self.print_out()





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
