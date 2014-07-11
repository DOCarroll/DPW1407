'''
Daniel O'Carroll
1407DPW
Basic Python Quiz
'''

width = input("Enter a Width: ")
height = input("Enter a height: ")

#Create Calc_Area function
def calc_area(w, h):
    area = w * h

    if w == h:
        shape = "square"
    else:
        shape = "rectangle"

    print "Your " + str(shape) + " is " + str(int(area)) + " square feet."

calc_area(width,height)


def count_down(number):
    for i in range(number, 0, -1):
        second = number - 1
        print str(int(number)) + " bottles of beer on the wall " + str(int(number)) + " bottles of beer.. Take one down, and pass it around. Now you have " + str(int(second)) + " bottles of beer on the wall!"
        number = number - 1


beer = input("Enter a number of Beer bottles: ")
count_down(beer)