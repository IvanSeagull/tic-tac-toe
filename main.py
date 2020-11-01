var = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def showDeck():
    print(f'\n{var[0]} | {var[1]} | {var[2]}')
    print('---------')
    print(f'{var[3]} | {var[4]} | {var[5]}')
    print('---------')
    print(f'{var[6]} | {var[7]} | {var[8]}\n')


def Select(who):
    x = int(input("Enter position?\n"))
    if checkPos(x, who):
        var[x-1] = who

        showDeck()
        if checkWin(who):
            if who=="X":
                Select('0')
            else:
                Select('X')

def checkPos(pos, who):
    if var[pos-1]==pos:
        return True
    else:
        print("Cant go there, try again")
        Select(who)

def checkWin(who):
    if var[0] == var[1] and var[1]==var[2]:
        print(f'{who} won')
    elif var[3] == var[4] and var[4]==var[5]:
        print(f'{who} won')
    elif var[6] == var[7] and var[7]==var[8]:
        print(f'{who} won')
    elif var[0] == var[4] and var[4]==var[8]:
        print(f'{who} won')
    elif var[2] == var[4] and var[4]==var[6]:
        print(f'{who} won')
    else:
        return True

if __name__ == '__main__':
    showDeck()
    Select("X")
