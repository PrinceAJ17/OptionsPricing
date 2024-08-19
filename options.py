import numpy
from scipy.stats import norm

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


S = 100  # Current stock price
X = 150  # Strike price
T = 1    # Time to expiration (in years)
r = 0.05 # Risk-free interest rate (5%)
sigma = 0.2 # Volatility (20%)

callPrice = call(S,X,T,r,sigma)
putPrice = put(S,X,T,r,sigma)

print(f"Call price is: {callPrice}")
print(f"Put price is {putPrice}")