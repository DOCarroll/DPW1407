'''
Daniel O'Carroll
1407DPW
Basic Python Quiz
'''

width = input("Enter a Width: ")
height = input("Enter a height: ")


def calc_area(w, h):
    area = w * h

    if w == h:
        shape = "square"
    else:
        shape = "rectangle"

    print "Your " + str(shape) + " is " + str(int(area)) + " square feet."

calc_area(width,height)
