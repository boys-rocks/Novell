import requests
from helpers import logHelper
symbolNamePairs = {
    'BITCOIN':'BTC',
    'ETHEREUM':'ETH',
    'DOGECOIN':'DOGE',  
}
class settings():
    def __init__(self):
        self.endpoint = "https://api.binance.com"
setting = settings()
def request(method, path, params=None):
    try:
        resp = requests.request(method, setting.endpoint + path, params = params)
        data = resp.json()
        return data
    except Exception as e:
        logHelper.logger.warning(f"Exception caught in requests function: {e}")
        
def getPrice(symbol):
    symbol = symbol.upper()
    if symbol in symbolNamePairs.keys():
        symbol = symbolNamePairs[symbol]
    try:
        data = request("GET", "/api/v3/ticker/price", {"symbol":symbol+"USDT"})
        price = str(data['price'])
        return price
    except Exception as e:
        logHelper.logger.warning(f"Exception caught in getPrice function: {e}")

