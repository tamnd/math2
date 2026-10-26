---
tag: 0K2FNY6DYV
kind: statement
role: proposition
name: Logarithm of a product
msc: [33B10]
uses: [0044CPHJBV, 0E8HNVBCSP, 0RKW2X63YR]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_logarithm
    locator: Definition and properties
---

## Statement

For all real $x > 0$ and $y > 0$,
$$\ln(x y) = \ln x + \ln y.$$

## Remarks

By [[the sum rule for exp|0E8HNVBCSP]], $e^{\ln x + \ln y} = e^{\ln x} e^{\ln y} = x y$. Now [[take logarithms|0RKW2X63YR]].
So $\ln$ is a group isomorphism from $((0, \infty), \cdot)$ to $(\mathbb{R}, +)$.
Mathlib states it as `Real.log_mul`, for nonzero $x$ and $y$.

## Explanations

### L1 human

The logarithm turns multiplication into addition.
This property made logarithm tables useful for hand computation.
