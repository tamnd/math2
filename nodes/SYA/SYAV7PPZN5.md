---
tag: SYAV7PPZN5
kind: statement
role: proposition
name: Kelly criterion
msc: [91G10, 91A60, 94A17]
uses: [04DXAFN2ES, 0WQNRCNY3M, 0DFWHQ839T]
sources:
  - url: https://en.wikipedia.org/wiki/Kelly_criterion
same_as:
  wikidata: Q2065471
  wikipedia: Kelly criterion
---

## Statement

Consider a sequence of independent bets.
Each bet wins with probability $p \in (0, 1)$ and pays $b > 0$ per unit staked; otherwise the stake is lost, which happens with probability $q = 1 - p$.
A bettor with wealth $W_0 > 0$ stakes the same fraction $f \in [0, 1)$ of current wealth on every bet, so $W_N$ is the wealth after $N$ bets.
Then, almost surely,
$$\lim_{N \to \infty} \frac{1}{N} \ln \frac{W_N}{W_0} = G(f) = p \ln(1 + bf) + q \ln(1 - f).$$
If $bp > q$, the growth rate $G$ has a unique maximum on $[0, 1)$, at the *Kelly fraction*
$$f^* = \frac{bp - q}{b} = p - \frac{q}{b}.$$
If $bp \le q$, the maximum of $G$ on $[0, 1)$ is at $f = 0$.

## Remarks

Each bet multiplies wealth by $1 + bf$ or $1 - f$, so $\ln(W_N/W_0)$ is a sum of $N$ independent copies of a random variable with [[mean|0WQNRCNY3M]] $G(f)$.
The [[strong law of large numbers|0DFWHQ839T]] gives the limit.
The function $G$ is strictly concave, and $G'(f) = pb/(1 + bf) - q/(1 - f)$ vanishes exactly at $f = (bp - q)/b$.
Since $G'(0) = bp - q$, the maximum is interior exactly when $bp > q$.

Example: a coin that lands heads with probability $0.6$ and pays even money, $b = 1$.
Then $f^* = 0.6 - 0.4 = 0.2$, and $G(0.2) = 0.6 \ln 1.2 + 0.4 \ln 0.8 \approx 0.020$, so wealth grows by about $2\%$ per bet in the long run.
Betting the fraction $f = 0.5$ instead gives $G(0.5) = 0.6 \ln 1.5 + 0.4 \ln 0.5 \approx -0.034 < 0$, and wealth tends to $0$ almost surely, although each bet has positive expected gain.

Maximising $G(f)$ is the same as maximising the expected [[logarithm|04DXAFN2ES]] of wealth after one bet.
The criterion is named after John Kelly, who derived it in 1956.

## Explanations

### L1 human

If you have an edge in a repeated bet, how much of your money should you bet each time?
Bet too little and your money grows slowly; bet too much and a run of losses can wipe you out.
The Kelly fraction is the amount that makes your money grow fastest in the long run.
For even-money bets it is simply your edge: win probability minus loss probability.

### L2 human

The Kelly criterion is the rule of maximising expected log wealth.
It ties betting to information theory: Kelly's paper links the growth rate of a gambler's capital to the information rate of a communication channel.
In portfolio choice it is the growth-optimal portfolio, which is the optimal choice of an investor with logarithmic utility.
Since $G$ is concave, betting more than $f^*$ adds risk and lowers growth, so practitioners often bet only a fraction of $f^*$.
