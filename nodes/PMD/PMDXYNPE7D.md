---
tag: PMDXYNPE7D
kind: definition
name: Sub-Gaussian distribution
msc: ["60E15", "60E05"]
defines: X9R1PCKJ0R
uses: [0PNRKMRC55, 0WQVXP7PDB, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Sub-Gaussian_distribution
---

## Definition

Let $X$ be a real [[random variable|0PNRKMRC55]].
$X$ is *sub-Gaussian* if there is a constant $K > 0$ such that
$$P(\abs{X} \ge t) \le 2 e^{-t^2 / K^2} \qquad \text{for all } t \ge 0.$$
A distribution on $\R$ is sub-Gaussian if a random variable with this distribution is sub-Gaussian.

## Remarks

Up to changing $K$ by a constant factor, the condition is equivalent to each of the following: $E[e^{X^2/K^2}] \le 2$; and $(E[\abs{X}^p])^{1/p} \le K \sqrt{p}$ for all $p \ge 1$.
If $E[X] = 0$, it is also equivalent to a bound on the [[moment-generating function|0WQVXP7PDB]]: there is $\sigma > 0$ with $E[e^{\lambda X}] \le e^{\lambda^2 \sigma^2 / 2}$ for all real $\lambda$.
In this last form one says that $X$ is sub-Gaussian with variance proxy $\sigma^2$.
Example: if $X$ is [[normal|05AQE0QR0D]] with mean $0$ and variance $\sigma^2$, then $E[e^{\lambda X}] = e^{\lambda^2 \sigma^2 / 2}$, so $X$ is sub-Gaussian with variance proxy $\sigma^2$.
Example: by Hoeffding's lemma, if $a \le X \le b$ and $E[X] = 0$, then $E[e^{\lambda X}] \le e^{\lambda^2 (b - a)^2 / 8}$, so $X$ is sub-Gaussian with variance proxy $(b - a)^2 / 4$.
Non-example: an [[exponential|0E99F51GVB]] variable with rate $1$ has $P(X \ge t) = e^{-t}$, and $e^{-t} \le 2 e^{-t^2/K^2}$ fails for large $t$, whatever $K$ is.
If $X_1, \dots, X_n$ are independent and centred with variance proxies $\sigma_i^2$, then $X_1 + \dots + X_n$ has variance proxy $\sigma_1^2 + \dots + \sigma_n^2$.
