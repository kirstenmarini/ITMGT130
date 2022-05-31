'''
#ID Number: 194760
#Surname: SY
#Year and Course: 3 BS ITE
'''

#Item1
def relationship_status(from_member:str, to_member:str, social_graph:dict):
if from_member in social_graph[to_member]['following']:
    if to_member in social_graph[from_member]['following']:
        return "friends"
    else:
        return "follower"
elif to_member in social_graph[from_member]['following']:
    return "followed by"
else:
    return "no relationship"

#Item2
def tic_tac_toe(board:list):
    #Hor
    points = 0
    lastelement = "blank"
    for row in board:
        points = 0
        lastelement = "blank"
        for element in row:
            if lastelement == element:
                points = points + 1
            lastelement = element
        if points == 2:
            return(str(element))

    #Vert
    column = -1
    row = -1
    vert_board = [[],[],[]]
    while column < 2:
        column = column + 1
        while row < 2:
            row = row + 1
            element = board[row][column]
            list.append(vert_board[column],element)
        else:
            row = -1
    for row in vert_board:
        points = 0
        lastelement = "blank"
        for element in row:
            if lastelement == element:
                points = points + 1
            lastelement = element
        if points == 2:
            return(str(element))

    #Diagonals
    column = -1
    row = -1
    points = 0
    lastelement = "blank"
    diag_board = [[],[]]
    while column < 2:
        
        column = column + 1
        row = row + 1
        element = board[row][column]
        if lastelement == element:
            points = points + 1
        list.append(diag_board[0],element)
        if points == 2:
            return(str(element))
        lastelement = element

    column = -1
    row = 3
    points = 0
    lastelement = "blank"
    while column < 2:
        
        column = column + 1
        row = row - 1
        element = board[row][column]
        if lastelement == element:
            points = points + 1
        list.append(diag_board[1],element)
        if points == 2:
            return(str(element))
        lastelement = element

    #No winner
    return(str("No winner"))


#Item3
def eta(first_stop, second_stop, route_map):
