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


