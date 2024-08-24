from flask import Flask, render_template, request
import numpy as np
import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt  # Import matplotlib for plotting




app = Flask(__name__)

def call(S,X,T,r,sigma):
    d1 = (np.log(S/X)+(r+((sigma)**2)/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - (sigma*np.sqrt(T))

    C = S*norm.cdf(d1) - ((X*np.exp(-r*T))*norm.cdf(d2))
    return C

def put(S,X,T,r,sigma):
    d1 = (np.log(S/X)+(r+((sigma)**2)/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - (sigma*np.sqrt(T))

    P = ((X*np.exp(-r*T))*norm.cdf(-d2)) - (S*norm.cdf(-d1))
    return P

def getFormValue(form, nameOfInput, defaultValue):
    if (form.get(nameOfInput)):
        return round(float(form[nameOfInput]),2)
    else:
        return defaultValue


@app.route("/", methods=["GET"])
def index():
    S = 150.00
    X = 100.00
    r = 0.05
    T = 1.00
    sigma = 0.20

    call_price = call(S, X, T, r, sigma)
    put_price = put(S, X, T, r, sigma)

    MinSP = S*0.8
    MaxSP = S*1.2
    minVol = sigma*0.5
    maxVol = sigma*1.5
    return render_template(
        "index.html",
        call_price=f"${round(call_price, 2):.2f}",
        put_price=f"${round(put_price, 2):.2f}",
        stockPrice=f"{S:.2f}",
        strikePrice=f"{X:.2f}",
        RFIR=f"{r:.2f}",
        expiration=f"{T:.2f}",
        volatility=f"{sigma:.2f}",
        minStockPrice=f"{MinSP:.2f}",
        maxStockPrice=f"{MaxSP:.2f}",
        minVolatility=f"{minVol:.2f}",
        maxVolatility=f"{maxVol:.2f}"
    )


@app.route("/calc", methods=["POST"])
def calc():
    S = getFormValue(request.form,"stockPrice", 150.00)
    X = getFormValue(request.form,"strikePrice", 100.00)
    r = getFormValue(request.form,"RFIR", 0.05)
    T = getFormValue(request.form,"expiration", 1.00)
    sigma = getFormValue(request.form,"volatility",0.20)

    call_price = call(S, X, T, r, sigma)
    put_price = put(S, X, T, r, sigma)

    MinSP = getFormValue(request.form,"minStockPrice",S*0.8)
    MaxSP = getFormValue(request.form,"maxStockPrice",S*1.2)

    minVol = getFormValue(request.form,"minVolatility", sigma*0.5)
    maxVol = getFormValue(request.form,"maxVolatility", sigma*1.5)

    return render_template(
        "index.html",
        call_price=f"${round(call_price, 2):.2f}",
        put_price=f"${round(put_price, 2):.2f}",
        stockPrice=f"{S:.2f}",
        strikePrice=f"{X:.2f}",
        RFIR=f"{r:.2f}",
        expiration=f"{T:.2f}",
        volatility=f"{sigma:.2f}",
        minStockPrice=f"{MinSP:.2f}",
        maxStockPrice=f"{MaxSP:.2f}",
        minVolatility=f"{minVol:.2f}",
        maxVolatility=f"{maxVol:.2f}"
    )

@app.route("/heatmap", methods=["POST"])
def heatmap():
    S = getFormValue(request.form,"stockPrice", 150.00)
    X = getFormValue(request.form,"strikePrice", 100.00)
    r = getFormValue(request.form,"RFIR", 0.05)
    T = getFormValue(request.form,"expiration", 1.00)
    sigma = getFormValue(request.form,"volatility",0.20)

    call_price = call(S, X, T, r, sigma)
    put_price = put(S, X, T, r, sigma)

    MinSP = getFormValue(request.form,"minStockPrice",S*0.8)
    MaxSP = getFormValue(request.form,"maxStockPrice",S*1.2)

    minVol = getFormValue(request.form,"minVolatility", sigma*0.5)
    maxVol = getFormValue(request.form,"maxVolatility", sigma*1.5)

    stockRange = np.round(np.linspace(MinSP, MaxSP, 10),2)
    volRange = np.round(np.linspace(minVol, maxVol, 10),2)


    call_prices = np.zeros((len(stockRange), len(volRange)))
    put_prices = np.zeros((len(stockRange), len(volRange)))

    for i, vol in enumerate(volRange):
        for j, stock in enumerate(stockRange):
            call_prices[j, i] = round(call(stock, vol),2)
            put_prices[j, i] = round(put(stock, vol),2)

# Create heatmap for call prices
    plt.figure(figsize=(10, 8))  # Set the figure size
    sns.heatmap(call_prices, cmap="Blues", annot=True, xticklabels=stockRange, yticklabels=volRange)
    plt.title('Call Prices Heatmap')
    plt.xlabel('Stock Price')
    plt.ylabel('Volatility')
    plt.show() 

if __name__ == "__main__":
    app.run(debug=True)