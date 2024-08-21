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


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        S = round(float(request.form["stockPrice"]),2)
        X = round(float(request.form["strikePrice"]),2)
        r = round(float(request.form["RFIR"]),2)
        T = round(float(request.form["expiration"]),2)
        sigma = round(float(request.form["volatility"]),2)

        call_price = call(S, X, T, r, sigma)
        put_price = put(S, X, T, r, sigma)
    else:
        S = 150.00
        X = 100.00
        r = 0.05
        T = 1.00
        sigma = 0.20

        call_price = call(S, X, T, r, sigma)
        put_price = put(S, X, T, r, sigma)

    return render_template(
        "index.html",
        call_price=round(call_price, 2),
        put_price=round(put_price, 2),
        stockPrice=f"{S:.2f}",
        strikePrice=f"{X:.2f}",
        RFIR=f"{r:.2f}",
        expiration=f"{T:.2f}",
        volatility=f"{sigma:.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)