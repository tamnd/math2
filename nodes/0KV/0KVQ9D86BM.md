---
tag: 0KVQ9D86BM
kind: statement
role: proposition
name: Variance under scaling
msc: [60A05]
uses: [007QED3E0Y, 0P7PTC8DDE]
sources:
  - url: https://en.wikipedia.org/wiki/Variance
    locator: Addition and multiplication by a constant
---

## Statement

Let $X$ be a real random variable with finite [[variance|007QED3E0Y]] and let $a \in \mathbb{R}$. Then
$$\operatorname{Var}(aX) = a^2 \operatorname{Var}(X).$$

## Remarks

Proof: $E[aX] = a E[X]$ by [[linearity of expectation|0P7PTC8DDE]]. So $(aX - E[aX])^2 = a^2 (X - E[X])^2$, and one takes expectations.
For the standard deviation, the formula becomes $\sigma_{aX} = |a| \, \sigma_X$.
In particular, $\operatorname{Var}(-X) = \operatorname{Var}(X)$.

## Explanations

### L1 human

If you measure in centimeters instead of meters, every value is multiplied by $100$. The variance is then multiplied by $100^2 = 10000$, because it is measured in squared units.
