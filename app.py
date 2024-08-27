from flask import Flask, render_template, request
import numpy as np
import seaborn as sns
from scipy.stats import norm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Directory to save heatmap images
app.config['HEATMAP_FOLDER'] = 'static/heatmaps'

# Ensure the directory exists
os.makedirs(app.config['HEATMAP_FOLDER'], exist_ok=True)


# Default values
S = 150.00
X = 100.00
r = 0.05
T = 1.00
sigma = 0.20
minSP = 120
maxSP = 180
minVol = 0.1
maxVol = 0.3
colorPalette = "RdYlGn"

def call(S, X, T, r, sigma):
    d1 = (np.log(S/X)+(r+((sigma)**2)/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - (sigma*np.sqrt(T))
    C = S*norm.cdf(d1) - ((X*np.exp(-r*T))*norm.cdf(d2))
    return C

def put(S, X, T, r, sigma):
    d1 = (np.log(S/X)+(r+((sigma)**2)/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - (sigma*np.sqrt(T))
    P = ((X*np.exp(-r*T))*norm.cdf(-d2)) - (S*norm.cdf(-d1))
    return P

def getFormValue(form, nameOfInput, defaultValue):
    if form.get(nameOfInput):
        return round(float(form[nameOfInput]), 2)
    else:
        return defaultValue

def generateHeatMap(prices, stockrange, volrange, title, colorpal, filename):
    plt.figure(figsize=(10,8))
    sns.heatmap(prices, cmap=colorpal, annot=True, xticklabels=np.round(stockrange, 2), yticklabels=np.round(volrange, 2), fmt=".2f")
    plt.title(title)
    plt.xlabel("Stock Price")
    plt.ylabel("Volatility")
    heatmap_path = os.path.join(app.config['HEATMAP_FOLDER'], filename)
    plt.savefig(heatmap_path)
    plt.close()


@app.route("/", methods=["GET"])
def index():
    call_price = call(S, X, T, r, sigma)
    put_price = put(S, X, T, r, sigma)

    stockRange = np.round(np.linspace(minSP, maxSP, 10), 2)
    volRange = np.round(np.linspace(minVol, maxVol, 10), 2)

    call_prices = np.zeros((len(stockRange), len(volRange)))
    put_prices = np.zeros((len(stockRange), len(volRange)))

    mappedMinSP = minSP
    mappedMaxSP = maxSP

    mappedMinVol = minVol
    mappedMaxVol = maxVol

    for i, vol in enumerate(volRange):
        for j, stock in enumerate(stockRange):
            call_prices[i, j] = call(stock, X, T, r, vol)
            put_prices[i, j] = put(stock, X, T, r, vol)

    generateHeatMap(call_prices, stockRange, volRange, "Call Prices Heatmap",colorPalette, "call_prices_heatmap.png")
    generateHeatMap(put_prices, stockRange, volRange, "Put Prices Heatmap",colorPalette,"put_prices_heatmap.png")

    return render_template(
        "index.html",
        call_heatmap='call_prices_heatmap.png',
        put_heatmap='put_prices_heatmap.png',
        call_price=f"${round(call_price, 2):.2f}",
        put_price=f"${round(put_price, 2):.2f}",
        stockPrice=f"{S:.2f}",
        strikePrice=f"{X:.2f}",
        RFIR=f"{r:.2f}",
        expiration=f"{T:.2f}",
        volatility=f"{sigma:.2f}",
        minStockPrice=f"{minSP:.2f}",
        maxStockPrice=f"{maxSP:.2f}",
        minVolatility=f"{minVol:.2f}",
        maxVolatility=f"{maxVol:.2f}",
        mappedMinVolatility=f"{mappedMinVol:.2f}",
        mappedMaxVolatility=f"{mappedMaxVol:.2f}",
        mappedMinStockPrice=f"{mappedMinSP:.2f}",
        mappedMaxStockPrice=f"{mappedMaxSP:.2f}",
        heatmapColors=f"{colorPalette}"
    )

@app.route("/calc", methods=["POST"])
def calc():
    S = getFormValue(request.form, "stockPrice", 150.00)
    X = getFormValue(request.form, "strikePrice", 100.00)
    r = getFormValue(request.form, "RFIR", 0.05)
    T = getFormValue(request.form, "expiration", 1.00)
    sigma = getFormValue(request.form, "volatility", 0.20)

    call_price = call(S, X, T, r, sigma)
    put_price = put(S, X, T, r, sigma)

    minSP = S * 0.8
    maxSP =  S * 1.2

    minVol = sigma * 0.5
    maxVol =  sigma * 1.5

    mappedMinSP = getFormValue(request.form, "mappedMinStockPrice", minSP)
    mappedMaxSP = getFormValue(request.form, "mappedMaxStockPrice", maxSP)

    mappedMinVol = getFormValue(request.form, "minVolatility", minVol)
    mappedMaxVol = getFormValue(request.form, "maxVolatility", maxVol)

    stockRange = np.round(np.linspace(mappedMinSP, mappedMaxSP, 10), 2)
    volRange = np.round(np.linspace(mappedMinVol, mappedMaxVol, 10), 2)

    call_prices = np.zeros((len(stockRange), len(volRange)))
    put_prices = np.zeros((len(stockRange), len(volRange)))

    for i, vol in enumerate(volRange):
        for j, stock in enumerate(stockRange):
            call_prices[i, j] = call(stock, X, T, r, vol)
            put_prices[i, j] = put(stock, X, T, r, vol)
    
    colorPalette = request.form.get("heatmapColors", "RdYlGn")

    generateHeatMap(call_prices, stockRange, volRange, "Call Prices Heatmap", colorPalette, "call_prices_heatmap.png")
    generateHeatMap(put_prices, stockRange, volRange, "Put Prices Heatmap", colorPalette, "put_prices_heatmap.png")

    return render_template(
        "index.html",
        call_heatmap='call_prices_heatmap.png',
        put_heatmap='put_prices_heatmap.png',
        call_price=f"${round(call_price, 2):.2f}",
        put_price=f"${round(put_price, 2):.2f}",
        stockPrice=f"{S:.2f}",
        strikePrice=f"{X:.2f}",
        RFIR=f"{r:.2f}",
        expiration=f"{T:.2f}",
        volatility=f"{sigma:.2f}",
        minStockPrice=f"{minSP:.2f}",
        maxStockPrice=f"{maxSP:.2f}",
        minVolatility=f"{minVol:.2f}",
        maxVolatility=f"{maxVol:.2f}",
        mappedMinVolatility=f"{mappedMinVol:.2f}",
        mappedMaxVolatility=f"{mappedMaxVol:.2f}",
        mappedMinStockPrice=f"{mappedMinSP:.2f}",
        mappedMaxStockPrice=f"{mappedMaxSP:.2f}",
        heatmapColors=f"{colorPalette}"
    )


if __name__ == "__main__":
    app.run(debug=True)