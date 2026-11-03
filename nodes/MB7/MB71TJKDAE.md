---
tag: MB71TJKDAE
kind: definition
name: Black–Scholes model
msc: [91G20, 60H30]
defines: FFT8TF6QP2
uses: [D48DR46B97, 22735FGJV6, ZFTNJ2YREG, 05AQE0QR0D, 858BHBY2BD, A1V152H2CA, CEHQSTM1NY]
sources:
  - url: https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model
---

## Definition

Let $W$ be a standard [[Wiener process|22735FGJV6]] on a probability space $(\Omega, \mathcal{F}, P)$ with its natural filtration.
Fix constants $r \in \R$, $\mu \in \R$ and $\sigma > 0$, and an initial price $S_0 > 0$.
The *Black–Scholes model* is the market in continuous time $t \in [0, T]$ with two assets:

1. a bond with price $B_t = e^{rt}$;
2. a stock whose price is the [[geometric Brownian motion|D48DR46B97]] $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$, that is $S_t = S_0 \exp\left( (\mu - \sigma^2/2) t + \sigma W_t \right)$.

Trading is continuous and frictionless, and any real amount of each asset can be held.

## Remarks

The model has a unique [[risk-neutral measure|858BHBY2BD]], under which $S$ has drift $r$ instead of $\mu$, and it is a [[complete market|A1V152H2CA]].
The price $V(t, S_t)$ of a European claim with payoff $g(S_T)$ solves the [[Black–Scholes equation|ZFTNJ2YREG]] with $V(T, S) = g(S)$.
For a call with strike $K$ and time to maturity $\tau = T - t > 0$, it is the *Black–Scholes formula*
$$C = S \, N(d_1) - K e^{-r\tau} N(d_2), \qquad d_{1,2} = \frac{\ln(S/K) + (r \pm \sigma^2/2) \tau}{\sigma \sqrt{\tau}},$$
where $N$ is the distribution function of the standard [[normal distribution|05AQE0QR0D]].

Example: $S = K = 100$, $r = 0$, $\sigma = 0.2$ and $\tau = 1$.
Then $d_1 = 0.1$ and $d_2 = -0.1$, so $C = 100 (N(0.1) - N(-0.1)) \approx 7.97$.

Non-example: a model in which the volatility is itself a random process is not a Black–Scholes model, since clause 2 requires a constant $\sigma$.
Such stochastic volatility models are in general incomplete.

The [[binomial model|CEHQSTM1NY]] with $u = e^{\sigma \sqrt{\Delta t}}$ and $d = 1/u$ converges to this model as the period length $\Delta t \to 0$.
