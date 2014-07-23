import webapp2
import urllib2
from xml.dom import minidom


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #p = Page()
        f = FormPage()
        f.inputs = [{'type':'text', 'placeholder':'Zip Code', 'name':'zip'},
                {'type':'button', 'name':'submit', 'value':'Get Weather'}]
        #if there is key value pairs in the url request do stuff
        if self.request.GET:
            zip = self.request.GET['zip']
            #load in info from the API
            #build request - format the official request
            request = urllib2.Request("http://xml.weather.yahoo.com/forecastrss?p="+zip)

            #create an object that fetches pages from server
            opener = urllib2.build_opener()

            #tell object to fetch response
            data = opener.open(request)


            #parse the info
            xmldoc = minidom.parse(data)

            titles = xmldoc.getElementsByTagName("title")
            print titles[0].firstChild.nodeValue

            image = xmldoc.getElementsByTagName('image')
            print image


        else:
            self.response.write(f.print_out())


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
    __inputs = []
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
                tot_inputs += ' placeholder="' + i['placeholder'] + '"'
            if 'value' in i:
                tot_inputs += ' value="'+i['value']+'"'
            tot_inputs += ' />'
        return tot_inputs

    def print_out(self):
        self._content = self._form_open + self.create_inputs() + self._close
        return Page.print_out(self)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
