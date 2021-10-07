from classes.paper_trade_class import account
from bot import collection


def exist(name):
    if collection.find_one({"_id": "paper_trading_accounts", name: {"$exists": True}}):
        return True
    return False


def newaccount(x):
    if exist(x):
        return "Account already Exists"
    newaccount = account(x)
    save(newaccount, x)
    return "Paper trading account created!"


def save(e, name):
    try:
        userdata = None
        if collection.find_one(
            {"_id": "paper_trading_accounts", name: {"$exists": True}}
        ):
            work = collection.update_one(
                {"_id": "paper_trading_accounts"},
                {
                    "$set": {
                        name: [
                            e.name,
                            e.balance,
                            e.portfolioValue,
                            e.coins,
                            e.recentTrades,
                        ]
                    }
                },
            )
            userdata = collection.find_one({"_id": "paper_trading_accounts"})
        else:
            work = collection.update(
                {"_id": "paper_trading_accounts"},
                {
                    "$set": {
                        name: [
                            e.name,
                            e.balance,
                            e.portfolioValue,
                            e.coins,
                            e.recentTrades,
                        ]
                    }
                },
            )
            userdata = collection.find_one({"_id": "paper_trading_accounts"})
    except Exception as e:
        print(e)


# save(test, "goth")
# test.balance = 7000
# save(test, "gothcow")
def load(name):
    try:
        if collection.find_one(
            {"_id": "paper_trading_accounts", name: {"$exists": True}}
        ):
            loadAccount = account(name)
            accountSave = collection.find_one({"_id": "paper_trading_accounts"})[name]
            print("account loaded " + str(accountSave))
            loadAccount.balance = accountSave[1]
            loadAccount.portfolioValue = accountSave[2]
            loadAccount.coins = accountSave[3]
            loadAccount.recentTrades = accountSave[4]
            return loadAccount
        print("acc doesnt exist")
        return "Account Doesnt Exist"

    except Exception as e:
        print(e)


# print("testingload")
# myacc = load("goth")
# print(myacc.portfolioValue)
# print(myacc.balance)
