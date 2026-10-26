---
tag: 0FEMF8JKAF
kind: statement
role: proposition
name: e as the limit of (1 + 1/n)^n
msc: [26A09]
uses: [0FM6N4R0VB, 0RMVS7RXZX]
sources:
  - url: https://en.wikipedia.org/wiki/E_(mathematical_constant)
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/E_(mathematical_constant)
    locator: Compound interest
---

## Statement

Let $e = \exp(1)$, where $\exp$ is the [[exponential function|0RMVS7RXZX]].
Then
$$\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e.$$
More generally, for each real number $x$,
$$\lim_{n \to \infty} \left(1 + \frac{x}{n}\right)^n = e^x.$$

## Remarks

Some texts take the limit as the definition of [[the number e|0MVCFMW7S4]]. The sequence $(1 + 1/n)^n$ is increasing and bounded above by $3$, so the [[monotone convergence theorem|0FM6N4R0VB]] gives the limit.
The first values are $2$, $2.25$, about $2.370$ and about $2.441$. The limit is $e \approx 2.71828$.
Jacob Bernoulli found this limit when he studied compound interest.
Mathlib states the general form as `Real.tendsto_one_add_div_pow_exp`.

## Explanations

### L1 human

Put one unit of money in a bank at $100\%$ yearly interest, paid $n$ times a year.
After one year you have $(1 + 1/n)^n$ units. As $n$ grows, this approaches $e$, and it never exceeds $e$.
