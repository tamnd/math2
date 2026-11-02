---
tag: 58PZBP5FE1
kind: definition
name: Almost periodic sequence
msc: [39A24, 42A75]
defines: Z83P73MG91
uses: [0G9EKM0E15, Q3B6K9HYRG]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_periodic_function
---

## Definition

Let $(x_n)_{n \in \Z}$ be a two-sided [[sequence|0G9EKM0E15]] of complex numbers.
For $\varepsilon > 0$, an integer $p$ is an *$\varepsilon$-almost period* of the sequence if
$$\abs{x_{n+p} - x_n} < \varepsilon \quad \text{for all } n \in \Z.$$
The sequence is *almost periodic* if the following holds for every $\varepsilon > 0$.
There is an integer $L \ge 1$ such that every set of $L$ consecutive integers contains an $\varepsilon$-almost period.

## Remarks

Example: a [[periodic sequence|Q3B6K9HYRG]] with period $p$ is almost periodic.
Every multiple of $p$ is an $\varepsilon$-almost period for every $\varepsilon > 0$, and every set of $p$ consecutive integers contains a multiple of $p$, so $L = p$ works.

Non-example: let $x_n = 0$ for $n < 0$ and $x_n = 1$ for $n \ge 0$.
For $p > 0$ take $n = -1$, and for $p < 0$ take $n = 0$: in both cases $\abs{x_{n+p} - x_n} = 1$.
So for $\varepsilon = 1/2$ the only almost period is $0$, and no $L$ works.

Equivalent forms: a bounded sequence is almost periodic if and only if the set of its translates $(x_{n+p})_{n \in \Z}$, $p \in \Z$, is relatively compact for the supremum norm.
It is also equivalent that the sequence is a uniform limit on $\Z$ of trigonometric polynomials $\sum_{j=1}^{m} c_j e^{i \lambda_j n}$ with $c_j \in \C$ and $\lambda_j \in \R$.
An almost periodic sequence is bounded.
