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


            wm = WeatherModel(zip)
            #instance of weather model
            wv = WeatherView()
            wv.dos = wm.dos
            # this passes the data from the model to the view

            #pass subview to larger view
            f.additional_view = wv.content

        self.response.write(f.print_out())


class WeatherView(object):
    def __init__(self):
        self.__dos = []
        self.content = ''

    @property
    def dos(self):
        pass

    @dos.setter
    def dos(self, arr):
        self.__dos = arr
        self.create_display()

    def create_display(self):
        for do in self.__dos:
            self.content += "Day: " + do.day
            self.content += " (" + do.date + ' )'
            self.content += " High: " + do.high + "    Low: " + do.low
            self.content += "<img src=\"images/" + do.code + '.png" />'
            self.content += "<br />"
            print self.content



class WeatherModel(object):
    '''This is a model class. It is sending a request to the yahoo API and
    getting the XML from the API. It then sorts it into a data object.'''
    def __init__(self, z):
        self.url = "http://xml.weather.yahoo.com/forecastrss?p="

        #load in info from the API
        #build request - format the official request
        request = urllib2.Request(self.url+z)

        #create an object that fetches pages from server
        opener = urllib2.build_opener()

        #tell object to fetch response
        self.data = opener.open(request)

        self.parse()

    def parse(self):
        #convert this into xml object data that python understands
        #parse the info
        xmldoc = minidom.parse(self.data)
        forecast = xmldoc.getElementsByTagName("yweather:forecast")
        #organize data into Weather Data Object
        self.__dos = []
        for item in forecast:
            do = WeatherDataObject()
            do.day = item.attributes['day'].value
            do.date = item.attributes['date'].value
            do.high = item.attributes['high'].value
            do.low = item.attributes['low'].value
            do.code = item.attributes['code'].value
            do.description = item.attributes['text'].value
            #this will add the finished data object into the array
            self.__dos.append(do)


    @property
    def dos(self):
        return self.__dos


class WeatherDataObject(object):
    '''This class is just a big associtive array for holding the info we need'''
    def __init__(self):
        self.high = 0
        self.low = 0
        self.code = 0
        self.description = ''
        self.date = ''
        self.day = ''


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
    additional_view = ''

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
        self._content = self._form_open + self.create_inputs() + self._close + self.additional_view
        return Page.print_out(self)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
