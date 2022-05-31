'''
#ID Number: 194760
#Surname: SY
#Year and Course: 3 BS ITE
'''

#Item1
def factorial(x:int):
    import math
    nfac = math.factorial((x))
    return(nfac)

#Item2
def classify_grade(number_grade):
    if number_grade <= 100 and number_grade >= 92:
        return 'A'

    elif number_grade <= 91.9 and number_grade >= 86:
        return 'B+'

    elif number_grade <= 85.9 and number_grade >= 80:
        return 'B'

    elif number_grade <= 79.9 and number_grade >= 74:
        return 'C+'

    elif number_grade <= 73.9 and number_grade >= 67:
        return 'C'

    elif number_grade <= 66.9 and number_grade >= 60:
        return 'D'

    elif number_grade <= 59.9 and number_grade >= 0:
        return 'F'

    else:
        return 'Error. Check your input again.'

#Item3
def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    return ((item_quantity_1*item_weight_1)+(item_quantity_2*item_weight_2))/(item_quantity_1+item_quantity_2)

#Item4
def string_sum(string):
    sum = 0
    for element in string:
        if isinstance(element, int) or element.isdigit():
            sum += int(element)
    return(sum)

#Item5
def distance(x_1, y_1, x_2, y_2):
    import math

    x_dist = abs(x_2 - x_1)
    y_dist = abs(y_2 - y_1)
    return math.sqrt(x_dist + y_dist)

#Item6
def make_change(amount:int):
    amt = amount * 100
    amt1 = int(amt//100)
    amt = amt%100
    amt2 = int(amt//25)
    amt = amt%25
    amt3 = int(amt//10)
    amt = amt%10
    amt4 = int(amt//5)
    amt = amt%5
    amt5 = int(amt//1)
    return("1P:{"+str(amt1)+"}/25C:{"+str(amt2)+"}/10C:{"+str(amt3)+"}/5C:{"+str(amt4)+"}/1C:{"+str(amt5)+"}")