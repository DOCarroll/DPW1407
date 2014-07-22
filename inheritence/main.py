import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #p = Page()
        f = FormPage()
        f.inputs = [{'type':'text', 'placeholder':'First Name', 'name':'fname'},
                {'type':'email', 'placeholder':'Email', 'name':'email'},
                {'type':'button', 'name':'submit', 'value':'Go'}]
        f.form_out()
        self.response.write(f.print_out)


class Page(object):
    _head = """<!DOCTYPE HTML>
    <head>
        <title>Inheritance Demo</title>
    </head>
    <body>"""
    _content = ''
    _close = """
    </body>
    </html>"""

    def __init__(self):
        pass

    def print_out(self):
        return self._head + self._content + self._close


class FormPage(Page):
    __inputs = ''
    _form_open = "<form method=\"GET\" action="" />"
    _form_close = "</form>"

    def __init__(self):
        #invoke constructor in parent/superclass
        Page.__init__(self)

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, i):
        self.__inputs = i

    def create_inputs(self):
        tot_inputs = ''
        #accept an array of dictionaries
        #use it to build out form <input> elements
        for i in self.__inputs:
            #for each item in our __inputs array
            tot_inputs += '<input type="'+i['type']+'" name="'+i['name']+'" '
            if 'placeholder' in i:
                tot_inputs += ' placeholder="' + i['placeholder'] + '"/>'
            if 'value' in i:
                tot_inputs += ' value="'+i['value']+'"'
            tot_inputs += ' />'
        return tot_inputs

    def form_out(self):
        self._content = self._form_open + self.create_inputs() + self._close




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
