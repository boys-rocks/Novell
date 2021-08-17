from classes.paper_trade_class import account, all
from helpers.save import save, load
def exist(x):
    listOfAll = load("all")
    if x in listOfAll.lis:
        return True
    else:
        return False  
def newaccount(x):
    listOfAll = load("all")
    print(listOfAll.number)
    if exist(x):
        return "Account already Exists"
    else:
        newaccount = account(x)
        listOfAll.lis.append(x)
        listOfAll.number += 1
        save(listOfAll, "all")
        save(newaccount, x)
        return "Paper trading account created!"
