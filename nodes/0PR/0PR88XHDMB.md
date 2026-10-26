---
tag: 0PR88XHDMB
kind: statement
role: theorem
name: Dirichlet convolution of multiplicative functions is multiplicative
msc: [11A25]
uses: [0KH1N66QWW, 0AP80TT660]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_convolution
    locator: Properties
---

## Statement

Let $f$ and $g$ be [[multiplicative functions|0AP80TT660]].
Then their [[Dirichlet convolution|0KH1N66QWW]] $f * g$ is a multiplicative function.

## Remarks

Let $m$ and $n$ be coprime. The proof uses that each divisor of $mn$ is a unique product of a divisor of $m$ and a divisor of $n$.
With $f = \mathrm{id}_k \colon n \mapsto n^k$ and $g = \mathbf{1}$, the theorem gives the [[multiplicativity of the divisor function|04WC36XKV6]], since $\sigma_k = \mathrm{id}_k * \mathbf{1}$.
The Dirichlet inverse of a multiplicative function is also multiplicative.

## Explanations

### L1 human

Multiplicative functions stay multiplicative when you convolve them.
So a new function built from known ones by divisor sums keeps the property, and you can compute it from prime powers.
