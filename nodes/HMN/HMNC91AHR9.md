---
tag: HMNC91AHR9
kind: definition
name: Binomial options pricing model
msc: [91G20, 91G60]
defines: CEHQSTM1NY
uses: [Q626SC54P7, 858BHBY2BD, A1V152H2CA, 0WCWA1KT3M]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_options_pricing_model
---

## Definition

Fix $N \ge 1$ periods, an initial stock price $S_0 > 0$, factors $0 < d < u$, and a riskless gross return $R > 0$ per period.
The *binomial options pricing model* is the market with two assets:

1. a riskless bond whose value grows by the factor $R$ each period;
2. a stock with $S_{n+1} \in \set{u S_n, d S_n}$ for $n < N$, each move having positive probability.

The model assumes $d < R < u$.
Let $q = (R - d)/(u - d)$.
The price of a claim with payoff $V_N = g(S_N)$ is defined by backward induction:
$$V_n = \frac{q \, V_{n+1}^{u} + (1 - q) \, V_{n+1}^{d}}{R}.$$
Here $V_{n+1}^u$ and $V_{n+1}^d$ are the values at the two successor nodes.

## Remarks

The condition $d < R < u$ is exactly the absence of [[arbitrage|Q626SC54P7]].
Then $q \in (0, 1)$, and $q$ is the up-probability of the unique [[risk-neutral measure|858BHBY2BD]], so the model is a [[complete market|A1V152H2CA]].
Under it the number of up moves has a [[binomial distribution|0WCWA1KT3M]], so
$$V_0 = R^{-N} \sum_{k=0}^N \binom{N}{k} q^k (1 - q)^{N - k} \, g\!\left(S_0 u^k d^{N - k}\right).$$

Example: $N = 1$, $S_0 = 100$, $u = 1.2$, $d = 0.9$, $R = 1$, and a call with strike $100$.
The payoffs are $20$ and $0$, and $q = 0.1/0.3 = 1/3$, so $V_0 = 20/3 \approx 6.67$.
The replicating portfolio holds $\Delta = 20/30 = 2/3$ shares and borrows $60$; it costs $200/3 - 60 = 20/3$, which agrees.

Non-example: with $u = 1.2$, $d = 0.9$ and $R = 1.25$, the condition $R < u$ fails.
Selling a share short and investing $S_0$ in the bond then yields at least $1.25 S_0 - 1.2 S_0 > 0$, an arbitrage.

The Cox–Ross–Rubinstein choice $u = e^{\sigma \sqrt{\Delta t}}$, $d = 1/u$ with period length $\Delta t$ gives the Black–Scholes price in the limit $\Delta t \to 0$.
