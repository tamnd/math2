---
tag: GR2Q99RFWR
kind: proof
name: Proof that the exponential function is strictly increasing
msc: [33B10]
proves: 0KN2V7840E
uses: [0RMVS7RXZX, 0EX9GFJ0B3, 07ZMX4ANJS, 0P9BNBW2W3, 07J5X2T1ZX]
sources:
  - url: https://proofwiki.org/wiki/Exponential_is_Strictly_Increasing
    locator: Proof 2
---

## Proof

We use the sign of the derivative.

1. By [[the derivative of exp|0EX9GFJ0B3]], the [[exponential function|0RMVS7RXZX]] is differentiable on $\R$, and $\exp'(x) = \exp(x)$ for all real $x$.
2. [[Differentiable functions are continuous|07ZMX4ANJS]], so $\exp$ is continuous on $\R$.
3. By [[the positivity of exp|0P9BNBW2W3]] and step 1, $\exp'(x) = \exp(x) > 0$ for all real $x$.
4. The interval $I = \R$ has every point as an interior point. By steps 1 to 3, the theorem that a [[function with positive derivative is strictly increasing|07J5X2T1ZX]] applies to $\exp$ on $\R$.
5. So $x < y$ implies $\exp(x) < \exp(y)$.

## Idea

The slope of the exponential function at each point equals its value there, and this value is positive. A function whose slope is positive everywhere must rise, by the mean value theorem.
