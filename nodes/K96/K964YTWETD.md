---
tag: K964YTWETD
kind: definition
name: Cumulant
msc: ["60E10", "62E10"]
defines: 9F3ZTTT9HA
uses: [0PNRKMRC55, 0WQVXP7PDB, 0N2SP6K9ZC, 01XAHPADBA]
sources:
  - url: https://en.wikipedia.org/wiki/Cumulant
---

## Definition

Let $X$ be a real [[random variable|0PNRKMRC55]] such that $M(t) = E[e^{tX}]$ is finite for all $t$ in an open interval containing $0$.
Let $K(t) = \log M(t)$ be its [[cumulant generating function|0N2SP6K9ZC]] on that interval.
For $n \ge 1$, the *$n$-th cumulant* of $X$ is
$$\kappa_n(X) = K^{(n)}(0),$$
so that $K(t) = \sum_{n \ge 1} \kappa_n \frac{t^n}{n!}$ near $0$.

## Remarks

Writing $\mu = E[X]$ and $\mu_k = E[(X - \mu)^k]$, the first cumulants are $\kappa_1 = \mu$, $\kappa_2 = \mu_2 = \operatorname{Var}(X)$, $\kappa_3 = \mu_3$ and $\kappa_4 = \mu_4 - 3 \mu_2^2$.
If $X$ and $Y$ are independent, then $K_{X+Y} = K_X + K_Y$, so $\kappa_n(X + Y) = \kappa_n(X) + \kappa_n(Y)$.
Also $\kappa_n(cX) = c^n \kappa_n(X)$ for real $c$, and $\kappa_n(X + c) = \kappa_n(X)$ for $n \ge 2$.
Example: if $X$ is normal with mean $\mu$ and variance $\sigma^2$, then $K(t) = \mu t + \sigma^2 t^2 / 2$, so $\kappa_1 = \mu$, $\kappa_2 = \sigma^2$ and $\kappa_n = 0$ for $n \ge 3$.
Example: if $X$ is Poisson with mean $\lambda$, then $K(t) = \lambda(e^t - 1)$, so $\kappa_n = \lambda$ for all $n$.
Non-example: a Cauchy variable has $E[e^{tX}] = \infty$ for all $t \ne 0$, so the hypothesis fails and it has no cumulants.
When only $E[\abs{X}^n] < \infty$ is known, one defines $\kappa_1, \dots, \kappa_n$ instead from the expansion of $\log E[e^{itX}]$ at $0$, as $i^k \kappa_k$ for the coefficient of $t^k/k!$; the two definitions agree when both apply.
