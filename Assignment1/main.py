'''
Daniel O'Carroll
1407 DPW
Midlib
'''


#Create the String variables
first_name = raw_input('Enter your first Name: ')
last_name = raw_input('Enter your last Name: ')
gender = raw_input('Enter your gender, M or F: ')
your_life = ' '

#Create the number variables
age = raw_input('Enter your age: ')
web_experience = raw_input('Enter how many years have you been working with web development: ')
school = raw_input('Enter the number of years you have been in college: ')

#create an array
positions = ['Junior Software Engineer', 'Senior Software Engineer', 'CEO']
design_positions = ['Junior Designers', 'Senior Designer', 'CEO']

#create a dictionary
phones = {
    "junior": 'Blackberry',
    "senior": 'Windows HTC 8x',
    "ceo": 'iPhone 5s'
}

#create functions


def experience(age, school):
    life = age/school
    if life >= 3:
        your_life = 'I am sorry your life sucks'
    elif life < 3:
        your_life = 'Looks like you took care of business!'


for position in positions:
    print position
