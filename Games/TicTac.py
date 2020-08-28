#    | |
#   ------
#    | |
#   ------
#    | |
def drawfield(field):
    for row in range(5):
        if row%2==0:
            practicalRow= int(row/ 2)
            for col in range(5):
                practicalCol = int(col/ 2)
                if col%2==0:
                    if col !=0:
                        print(field[practicalCol][practicalRow], end=" ")
                    else:
                        print(" ")
                else:
                     print("|", end=" ")
        else:
            print("-----------")

Player=1
currentField=[[" ", " ", " "," "],[" ", " ", " "],[" ", " ", " "]]
drawfield(currentField)
while(True):
    print("Player Turn:", Player)
    MoveRow = int(input("Please enter the row"))
    MoveCol = int(input("Please enter the col"))
    if Player==1:
        if currentField[MoveCol][MoveRow] == " ":
            currentField[MoveCol][MoveRow]="x"
            Player=2
    else:
        if currentField[MoveCol][MoveRow] == " ":
            currentField[MoveCol][MoveRow] = "o"
            Player=1
    drawfield(currentField)
