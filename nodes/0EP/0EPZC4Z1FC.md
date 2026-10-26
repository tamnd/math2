---
tag: 0EPZC4Z1FC
kind: statement
role: theorem
name: Central limit theorem
aliases: [clt, lindeberg-levy-central-limit-theorem]
msc: [60F05]
uses: [0AJN7WHBJZ, 0JDAQHWA9N, 07RXBVTVZB, 0FPWF7TTMB, 0MYDNRT7PP]
sources:
  - url: https://en.wikipedia.org/wiki/Central_limit_theorem
    locator: Classical CLT
same_as:
  wikidata: Q190391
  wikipedia: Central limit theorem
---

## Statement

Let $X_1, X_2, \dots$ be [[i.i.d.|0AJN7WHBJZ]] real random variables with mean $\mu$ and variance $\sigma^2$, where $0 < \sigma^2 < \infty$. Let $\bar{X}_n = (X_1 + \dots + X_n)/n$.
Then $\sqrt{n} \, (\bar{X}_n - \mu) / \sigma$ converges [[in distribution|0JDAQHWA9N]] to $\mathcal{N}(0, 1)$. That is, for each $x \in \mathbb{R}$,
$$\lim_{n \to \infty} P\left(\frac{X_1 + \dots + X_n - n\mu}{\sigma \sqrt{n}} \le x\right) = \Phi(x) = \int_{-\infty}^{x} \frac{1}{\sqrt{2\pi}} e^{-u^2/2} \, du.$$

## Remarks

A standard proof uses [[characteristic functions|0MYDNRT7PP]]. With $Y_i = (X_i - \mu)/\sigma$, $\varphi_{Y_1}(t) = 1 - t^2/2 + o(t^2)$, so $\varphi_{Y_1}(t/\sqrt{n})^n \to e^{-t^2/2}$.
[[Lévy's continuity theorem|0FPWF7TTMB]] then gives the convergence in distribution.
The Lindeberg and Lyapunov forms remove the condition that the $X_i$ have the same law. The Berry–Esseen theorem bounds the rate of convergence when $E[|X_1|^3] < \infty$.
The finite variance is necessary. Sums of i.i.d. Cauchy variables, scaled by $1/n$, stay Cauchy.

## Explanations

### L1 human

The central limit theorem explains why the bell curve is everywhere.
A sum of many small independent effects is approximately normal, whatever the law of each effect, as long as the variance is finite.
