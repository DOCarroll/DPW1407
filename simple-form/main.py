'''
Danny O'Carroll
July 10th, 2014
Simple Form
'''
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_out())

        if self.request.GET:
            self.response.write(self.request.GET['fName'])
            self.response.write(self.request.GET['lName'])
            self.response.write(self.request.GET['eMail'])
            self.response.write(self.request.GET['payment'])


class Page(object):
    def __init__(self):
        self.header = '''
        <!DOCTYPE html>
        <html>
        <head>
        <title>Pizza Form</title>
        </head>
        <body>
        '''

        self.content = '''
        <h1>Pizza Form</h1>
        <form>
        <h3>Contact Info</h3>
        <input type="text" name="fName" id="fName" placeholder="First Name" />
        <input type="text" name="lName" id="lName" placeholder="Last Name" />
        <input type="text" name="eMail" id="eMail" placeholder="E-Mail Address" />
        <h3>Type of Pizza</h3>
        <input type="checkbox" id="Cheese" name="Cheese" /> Cheese
        <input type="checkbox" id="Pepperoni" name="Pepperoni" /> Pepperoni
        <input type="checkbox" id="Pineapple" name="Pineapple" /> Pineapple
        <h3>Payment Type</h3>
        <select name="payment" id="payment">
            <option name="Credit Card" >Credit Card</option>
            <option name="Cash">Cash</option>
            <option name="Paypal">Paypal</option>
        </select> <br/>
        <input type="submit">

        </form>
        '''

        self.close = '''
        </body>
        </html>
        '''
    def print_out(self):
        return self.header + self.content + self.close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
