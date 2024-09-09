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

# Monte Carlo Simulation for Option Pricing

The Monte Carlo simulation predicts an option’s price by simulating random price paths of the option. It takes into account the five existing variables from the Black-Scholes model, with the addition of three parameters:

| Symbol | Description                                                                                                             |
|--------|-------------------------------------------------------------------------------------------------------------------------|
| `μ`    | The drift rate, representing the expected return of the asset or the average rate of growth of the asset's price over time (In risk-neutral scenarios, \( r = μ \)) |
| `n`    | The number of time steps at which the price of an asset is updated                                                     |
| `M`    | The number of simulations                                                                                               |

## Steps in the Monte Carlo Simulation

1. **Simulation of Price Paths Using Geometric Brownian Motion (GBM):**

   GBM describes the random movement of financial assets, assuming that the percentage change in price follows a normal distribution and that the asset price follows a continuous-time stochastic process with constant drift and volatility. The GBM formula is:

   $dS_t = μ S_t \, dt + σ S_t \, dW_t$

   Where:
   - $S_t$ = asset price at the current time t
   - $dt$= infinitesimal change in time
   - $dW_t$ = infinitesimal random increment in the Wiener process (Brownian Motion), normally distributed with mean 0 and variance dt

2. **Discretizing GBM:**

   The total time to expiration T is divided into small time intervals Δt. For each time step, the asset price is updated using the discretized version of the GBM:

   $S_{t + Δt} = S_t \times \exp \left( \left( μ - \frac{σ^2}{2} \right) Δt + σ \sqrt{Δt} \times Z_t \right)$

   Where:
   - $μ - \frac{σ^2}{2}$ represents the drift of the stock price after accounting for volatility. Without this correction, the model would overestimate the growth rate of the stock price, especially under high volatility conditions.
   - $Z_t$ is a random variable that follows a normal distribution with mean 0 and variance 1, introducing uncertainty into the model.
   - $σ \sqrt{Δt}$scales the random variable to volatility, keeping the variance of price changes proportional to the time interval.

3. **Calculate the Option’s Payoff:**

   - **Call Option Payoff:** max($S_t$ - X, 0), where X  is the strike price. The profit earned is $S_t$ - X if $S_t$ > X ; otherwise, the payoff is 0.
   - **Put Option Payoff:** max(X - $S_t$, 0)

4. **Calculate the Discounted Payoff:**

   The value of money decreases over time due to market conditions or other factors. To account for this, use the risk-free interest rate to convert the payoff back to its present value:

   $Disc. Payoff = Payoff \times \exp(-r \times T)$

5. **Estimate the Option Price:**

   This involves averaging the discounted payoffs from all possible paths of the asset’s price:

   $OP = \frac{1}{N} \sum_{i=1}^{N} Payoff_i$






