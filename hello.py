from flask import Flask
from flask import request
from yahoo_finance import Share
# import converter
# from decimal import Decimal

app = Flask(__name__)

@app.route('/data')
def data():
    stockName = request.args.get('stockName')
    theObj = Share(stockName)
    stockPrice = theObj.get_price()
#    exchange = converter.convert(from_curr='usd', to_curr='sek', amount=float(stockPrice))
    return stockPrice

if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0")
