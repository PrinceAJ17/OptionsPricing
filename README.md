# OptionsPricing

**OptionsPricing** is a web application that allows users to calculate the fair value of an option using two popular pricing models:

1. **Black-Scholes model**
2. **Monte Carlo simulation**

These models help retail investors estimate the value of a call or put option based on various market conditions and assumptions.

---


## Pricing Models

### 1. Black-Scholes Model

The **Black-Scholes model** is a deterministic formula that calculates the price of options using a deterministic formula. It uses five main parameters:

| Symbol   | Description                                                                                |
|----------|--------------------------------------------------------------------------------------------|
| `S`      | Current price of the underlying asset                                                      |
| `X`      | Strike price (price at which an individual would have the right to buy or sell an option)  |
| `T`      | Time left until an option expires (in years)                                               |
| `σ`      | Volatility is the measure of how much the price of an asset is supposed to change          |
| `r`      | Risk-free interest rate would be the theoretical returns on risk free investments          |

#### Formula

The Black-Scholes formula for a call option (`C`) and a put option (`P`) is:

C = $SN(d_1) - Xe^{-rT}N(d_2)$

P = $Xe^{-rT}N(-d_2) - SN(-d_1)$

Where:

$d_1 = \frac{\ln\left(\frac{S}{X}\right) + \left(r + \frac{σ²}{2}\right)T}{σ\sqrt{T}}, \quad d_2 = d_1 - σ\sqrt{T}$

$N(d_1)$ and $N(d_2)$ gives the probability that a standard normal variable will be less than d, reflecting the likelihood of the option finishing in-the-money, that is:
- If the option is a call then the right to buy an option would be at a lower price compared to market price (X << S)
- If the option is a put then the right to sell the option would be at a higher price compared to market price (X >> S)

### 2. Monte Carlo Simulation
The Monte Carlo simulation predicts an options price by simulating random price paths of an option. It takes into account of the 5 existing variables from the Black-Scholes model with an additional 3 parameters: 

| Symbol   | Description                                                                                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------|
| `μ`      | The drift rate which would be the expected return of the asset or the avg. rate of growth of the asset's price over time (In risk neutral scenarios r = μ)|
| `n`      | This would be the time steps at which the price of an asset would be updated                                 |
| `M`      | Number of Simulations                                                                                                   |

The Monte Carlo Simulation follows these steps:

1) Simulation of price paths are generated using the Geometric Brownian Motion (GBM):

This describes the random movement of financial assets. It will assume that the percentage change in price follows a normal distribution and that the asset price follows a continuous-time stochastic process with constant drift and volatility. GBM is an example of a stochastic process where random variables are indexed over a period of time. The GBM formula is as follows:

$dS_t = μ S_t dt + σ S_t dW_t$

Where:

$S_t$ = asset price at the current time t
dt = Infinitesmal (to allow for a continuous process) changes in time
$dW_t$ = An infinitesimal random increment in the Wiener process (Brownian Motion), normally distributed with mean 0 and variance dt

2) Discretizing GBM:
The total time to expiration T is divided into small time intervals Δt. For each time step, the asset price is updated using the discretized version of the GBM:

$S_{t + \Delta t} = S_t \times \exp \left( \left( \mu - \frac{\sigma^2}{2} \right) \Delta t + \sigma \sqrt{\Delta t} \times Z_t \right)$

Where:

$\mu - \frac{\sigma^2}{2}$ represents the drift of the stock price after accounting for volatility. Without this correction, the model would overestimate the growth rate of the stock price, especially under high volatility conditions.

$Z_t$ would be the random variable introduced that follows a normal distribution with mean of 0 and variance of 1. This introduces the uncertainity in the model.

$\sigma \sqrt{\Delta t}$ allows for the random variable to be scaled to the volatility and keeping the variance of change in price (increments) proportional to the time interval.

3) Calculate the options payoff:

Call option payoff: max($S_t$ - X, 0) where X is the strike price so the profit earned will be $S_t$ - X if $S_t$ > X, if not then payoff is 0.

Put option payoff: max(X - $S_t$, 0)

4) Calculate discounted payoff:

Value of money would decrease over time possibly due to market conditions or other factors so to account for this you use this risk-free interest rate to convert the payoff back to real time value.

Disc. Payoff = Payoff $\times exp( -r \times T)$

5) Estimate the option price:

This involves averaging the discounted payoffs produced from all the possible paths of an asset's price.

OP = $\frac{1}{N} \sum_{i=1}^{N} \text{Payoff}_i$





