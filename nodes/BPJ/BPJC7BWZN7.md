---
tag: BPJC7BWZN7
kind: proof
name: Proof of the logarithm of a quotient
msc: [33B10]
proves: 0J7PHRBNNS
uses: [0044CPHJBV, 0K2FNY6DYV]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_logarithm
    locator: Definition and properties
---

## Proof

We write $x$ as the product of $x/y$ and $y$.

1. Let $x > 0$ and $y > 0$, and let $\ln$ be the [[natural logarithm|0044CPHJBV]]. Then $\frac{x}{y} > 0$, so $\ln \frac{x}{y}$ is defined.
2. We have $x = \frac{x}{y} \cdot y$, a product of two positive numbers.
3. By the [[logarithm of a product|0K2FNY6DYV]], $\ln x = \ln \frac{x}{y} + \ln y$.
4. Subtract $\ln y$ from both sides. This gives $\ln \frac{x}{y} = \ln x - \ln y$.

## Idea

Division by $y$ undoes multiplication by $y$. Since $\ln$ turns products into sums, it turns quotients into differences.
