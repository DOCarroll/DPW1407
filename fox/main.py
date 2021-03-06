'''
Daniel O'Carroll
July 22nd, 2014
DPW1407
'''
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Reference the Subclasses in the main so they can be pushed into an array
        p = Page()
        bear = Bear()
        wolf = Wolf()
        fox = Fox()
        #Create Array to Store Animals
        animals = [bear, wolf, fox]
        #Detect a request
        if self.request.GET:

            a = self.request.GET['animal']
            #Check for the animal keyword, and populate accordingly
            if a == "fox":
                p.animal = fox
                self.response.write(p.update())
            elif a == "wolf":
                p.animal = wolf
                self.response.write(p.update())
            elif a == "bear":
                p.animal = bear
                self.response.write(p.update())
        else:
            self.response.write(p.update())


#create a class that will populate the page with html
class Page(object):
    def __init__(self):
        self.animal = AbstractAnimal()
        self.open = '''
<!DOCTYPE html>
<html>
    <head>
        <title>What Does the Fox Say?</title>
        <link rel="stylesheet" type="text/css" href="css/main.css"  />
    </head>
<body>'''

        self.nav = '''
<ul>
    <a href="?animal=fox"><li class='leftLi'>Red Fox</li></a>
    <a href="?animal=wolf"><li>Arctic Wolf</li></a>
    <a href="?animal=bear"><li>Polar Bear</li></a>
</ul>'''

        self.content = '''
        <div class="content">
<h1>{self.animal.name}</h1>
<img src="{self.animal.image}"/>
<p>{self.animal.phylum}</p>
<p>{self.animal.animal_class}</p>
<p>{self.animal.order}</p>
<p>{self.animal.family}</p>
<p>{self.animal.genus}</p>
<p>{self.animal.life}</p>
<p>{self.animal.habitat}</p>
<p>{self.animal.location}</p>
<p>{self.animal.sound}</p>
</div>
        '''

        self.close = '''
</body>
</html>'''
        self.all = self.open + self.nav + self.content + self.close

    #create a print method
    def update(self):
            self.all = self.all.format(**locals())
            return self.all


#create the Abstract Animal Class
class AbstractAnimal(object):
    def __init__(self):
        self.name = ''
        self.phylum = ''
        self.animal_class = ''
        self.order = ''
        self.family = ''
        self.genus = ''
        self.image = ''
        self.life = ''
        self.habitat = ''
        self.location = ''
        #create the method to set the sound of the animal
        def create_sound():
            self.sound = ''
            return self.sound
        create_sound()


#Create First Animal
class Fox(AbstractAnimal):
    def __init__(self):
        AbstractAnimal.__init__(self)
        self.name = 'Red Fox'
        self.phylum = 'Phylum: Chordata'
        self.animal_class = 'Class: Mammalia'
        self.order = 'Order: Carnivora'
        self.family = 'Family: Canidae'
        self.genus = 'Genus: Vulpes'
        self.image = 'css/images/redfox.jpg'
        self.life = 'Life Span: 5 Years'
        self.habitat = 'Habitat: Forests, Deserts, Mountains, and Grasslands'
        self.location = 'Location: All over the world'
        self.create_sound()

    #Set the Sound of the animal with the method
    def create_sound(self):
        self.sound = 'Sound: "Ring ding ding ding'
        return self.sound


#Create Second Animal
class Wolf(AbstractAnimal):
    def __init__(self):
        AbstractAnimal.__init__(self)
        self.name = 'Arctic Wolf'
        self.phylum = 'Phylum: Chordata'
        self.animal_class = 'Class: Mammalia'
        self.order = 'Order: Carnivora'
        self.family = 'Family: Canidae'
        self.genus = 'Genus: Canis'
        self.image = 'css/images/arcticwolf.jpg'
        self.life = 'Life Span: 7 to 10 years'
        self.habitat = 'Habitat: Tundras, snowy places '
        self.location = 'Location: Arctic, most of Northern Hemisphere'

        #set the second sound
        def create_sound():
            self.sound = 'Sound: "AAWWWOOOOOOOOOO!!!"'
            return self.sound
        create_sound()


#Create Third Animal
class Bear(AbstractAnimal):
    def __init__(self):
        AbstractAnimal.__init__(self)
        self.name = 'Polar Bear'
        self.phylum = 'Phylum: Chordata'
        self.animal_class = 'Class: Mammalia'
        self.order = 'Order: Carnivora'
        self.family = 'Family: Ursidae'
        self.genus = 'Genus: Ursus'
        self.image = 'css/images/polarbear.jpg'
        self.life = 'Life Span: 15 to 18 Years'
        self.habitat = 'Habitat: Icey snowy places'
        self.location = 'Location: The entire Arctic Region'
        self.sound = ''

        def create_sound():
            self.sound = 'Sound: "GRARAWWWRRRRRR!"'
            return self.sound
        create_sound()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
