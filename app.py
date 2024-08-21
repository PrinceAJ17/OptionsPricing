from flask import Flask, render_template, request
import numpy
from scipy.stats import norm

app=  Flask(__name__)

def call(S,X,T,r,sigma):
    d1 = (numpy.log(S/X)+(r+((sigma)**2)/2)*T)/sigma*numpy.sqrt(T)
    d2 = d1 - (sigma*numpy.sqrt(T))

    C = S*norm.cdf(d1) - ((X*numpy.exp(-r*T))*norm.cdf(d2))
    return C

def put(S,X,T,r,sigma):
    d1 = (numpy.log(S/X)+(r+((sigma)**2)/2)*T)/sigma*numpy.sqrt(T)
    d2 = d1 - (sigma*numpy.sqrt(T))

    P = ((X*numpy.exp(-r*T))*norm.cdf(-d2)) - (S*norm.cdf(-d1))
    return P


@app.route("/", methods=["POST", "GET"])
def index():
    call_price = 0.00
    put_price = 0.00

    if request.method == "POST":
        S = float(request.form["stockPrice"])
        X = float(request.form["strikePrice"])
        r = float(request.form["RFIR"])
        T = float(request.form["expiration"])
        sigma = float(request.form["volatility"])

        call_price = call(S,X,T,r,sigma)
        put_price = put(S,X,T,r,sigma)

    return render_template("index.html", call_price=round(call_price, 2), put_price=round(put_price, 2))

if __name__ == "__main__":
    app.run(debug=True)

