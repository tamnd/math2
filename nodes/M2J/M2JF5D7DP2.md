---
tag: M2JF5D7DP2
kind: definition
name: Variance reduction
msc: [65C05]
defines: A01GEGWKVB
uses: [HWP11G3HTN, 0WQNRCNY3M, 0477R9PYAE]
sources:
  - url: https://en.wikipedia.org/wiki/Variance_reduction
---

## Definition

Let $q$ be a real number.
Let $Y$ be a random variable with finite [[variance|0477R9PYAE]] and [[expected value|0WQNRCNY3M]] $\mathbb E Y = q$, used in a plain [[Monte Carlo method|HWP11G3HTN]] for $q$.
A *variance reduction* for this method is a random variable $Z$ such that:

1. $\mathbb E Z = q$;
2. $\operatorname{Var} Z < \operatorname{Var} Y$;
3. independent copies of $Z$ can be generated.

The Monte Carlo method then uses the average $\frac1n \sum_{i=1}^n Z_i$ of independent copies of $Z$ instead of the average of copies of $Y$.

## Remarks

Example: $q = \int_0^1 e^u\, du = e - 1$ and $Y = e^U$ with $U$ uniform on $(0, 1)$, so $\operatorname{Var} Y = \frac{e^2 - 1}{2} - (e - 1)^2 \approx 0.2420$.
Take $Z = \frac12 \bigl(e^U + e^{1 - U}\bigr)$.
Clause 1 holds because $1 - U$ is also uniform, clause 3 is clear, and a direct computation gives $\operatorname{Var} Z = \frac{e^2 - 1 + 2e}{4} - (e - 1)^2 \approx 0.0039$, so clause 2 holds.
Non-example: $Z = 1 + U + \frac12 U^2$, the Taylor polynomial of $e^U$, has variance about $0.189 < 0.2420$, but $\mathbb E Z = \frac53 \ne e - 1$, so clause 1 fails and the estimate is biased.
A fair comparison also counts the cost.
If one copy of $Z$ costs $c$ times as much as one copy of $Y$, the reduction pays off when $c \operatorname{Var} Z < \operatorname{Var} Y$.
In the example $c = 2$ and $2 \cdot 0.0039 < 0.2420$.
Some techniques, such as stratified sampling, change the whole estimator rather than one sample.
For them one compares the variances of two estimators of the same cost.
