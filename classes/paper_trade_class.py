from helpers.getPrice import getCost


class account:
    def __init__(self, name):
        self.name = name
        self.balance = 100000.00
        self.portfolioValue = 100000.00
        self.coins = {}
        self.recentTrades = []

    def updateBalance(self, change):
        self.balance += change

    def updateCoin(self, symbol, change):
        self.coins[symbol] += change

    def updatePortfolioPrice(self):
        keys = list(self.coins.keys())
        values = list(self.coins.values())
        i = 0
        total = 0
        for each in keys:
            print(each)
            print(values[i])
            cost_and_coin = getCost(str(each), float(values[i]))
            total += cost_and_coin[0]
            i += 1
        self.portfolioValue = total + self.balance

    def buy(self, symbol, amount):
        cost_and_coin = getCost(symbol, amount)
        if self.balance >= cost_and_coin[0]:
            self.recentTrades.append(
                {
                    "side": "buy",
                    "symbol": cost_and_coin[1],
                    "amount": amount,
                    "value": cost_and_coin[0],
                }
            )
            self.updateBalance(-cost_and_coin[0])
            if cost_and_coin[1] in self.coins:
                self.updateCoin(cost_and_coin[1], amount)
            else:
                self.coins[cost_and_coin[1]] = amount
            return (
                str(amount)
                + " "
                + cost_and_coin[1]
                + " purchased for "
                + str(cost_and_coin[0])
            )
        else:
            print("Insufficient Funds")
            return "Insufficient Funds"

    def sell(self, symbol, amount):
        if self.coins[symbol]:
            if self.coins[symbol] >= amount:
                cost_and_coin = getCost(symbol, amount)
                self.recentTrades.append(
                    {
                        "side": "sell",
                        "symbol": symbol,
                        "amount": amount,
                        "value": cost_and_coin[0],
                    }
                )
                self.updateBalance(cost_and_coin[0])
                self.updateCoin(symbol, -amount)
                return str(amount) + " " + symbol + " sold for " + str(cost_and_coin[0])
            else:
                print("Insufficient " + symbol)
                return "Insufficient " + symbol
        else:
            print("Insufficient " + symbol)
            return "Insufficient " + symbol


class all:
    def __init__(self):
        self.number = 0
        self.lis = []
