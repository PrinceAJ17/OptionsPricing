from flask import Flask, render_template, request
import numpy
from scipy.stats import norm


app=  Flask(__name__)

def call(S,X,T,r,sigma):
    d1 = (numpy.log(S/X)+(r+((sigma)**2)/2)*T)/(sigma*numpy.sqrt(T))
    d2 = d1 - (sigma*numpy.sqrt(T))

    C = S*norm.cdf(d1) - ((X*numpy.exp(-r*T))*norm.cdf(d2))
    return C

def put(S,X,T,r,sigma):
    d1 = (numpy.log(S/X)+(r+((sigma)**2)/2)*T)/(sigma*numpy.sqrt(T))
    d2 = d1 - (sigma*numpy.sqrt(T))

    P = ((X*numpy.exp(-r*T))*norm.cdf(-d2)) - (S*norm.cdf(-d1))
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



if __name__ == "__main__":
    app.run(debug=True)