---
tag: 07VHQ31EYJ
kind: statement
role: theorem
name: Young's inequality for products
msc: [26D15]
uses: [0DRF0F3XC9]
sources:
  - url: https://en.wikipedia.org/wiki/Young%27s_inequality_for_products
    locator: Standard version for conjugate Hölder exponents
same_as:
  wikidata: Q910563
  wikipedia: Young's inequality for products
---

## Statement

Let $p, q > 1$ be real numbers with $\frac{1}{p} + \frac{1}{q} = 1$.
Then for all real $a, b \ge 0$,
$$a b \le \frac{a^p}{p} + \frac{b^q}{q}.$$
Equality holds if and only if $a^p = b^q$.

## Remarks

It is the weighted [[AM–GM inequality|0DRF0F3XC9]] for the numbers $a^p$ and $b^q$, with weights $1/p$ and $1/q$.
For $p = q = 2$ it is $a b \le (a^2 + b^2)/2$.
It is the main step in the proof of [[Hölder's inequality|0BKDAGMGX9]]. Mathlib states it as `Real.young_inequality`.

## Explanations

### L1 human

Young's inequality bounds a product by a sum of powers.
It splits the product in a way that depends on the pair of exponents $p$ and $q$.
