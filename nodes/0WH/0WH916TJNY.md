---
tag: 0WH916TJNY
kind: statement
role: corollary
name: There is a natural number n with 1/n below any positive epsilon
msc: [26A03]
uses: [0A3GWZ86AY]
sources:
  - url: https://en.wikipedia.org/wiki/Archimedean_property
    locator: Ordered fields
---

## Statement

Let $\varepsilon$ be a real number with $\varepsilon > 0$.
Then there is a natural number $n \ge 1$ with $\dfrac{1}{n} < \varepsilon$.

## Remarks

Proof: since the [[reals are Archimedean|0A3GWZ86AY]], there is a natural number $n > 1/\varepsilon$. Then $n \ge 1$ and $1/n < \varepsilon$.
Thus $\inf \{1/n : n \ge 1\} = 0$. There are no positive infinitely small real numbers.
The same holds in each Archimedean ordered field.

## Explanations

### L1 human

The fractions $1, 1/2, 1/3, \dots$ get as small as you want.
For $\varepsilon = 0.001$, the number $n = 1001$ works, because $1/1001 < 0.001$.
