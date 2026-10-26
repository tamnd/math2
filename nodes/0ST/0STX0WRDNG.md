---
tag: 0STX0WRDNG
kind: statement
role: theorem
name: Density of the rationals
msc: [26A03]
uses: [0A3GWZ86AY, 0NCJ5WXN6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Dense_order
    locator: Example
  - url: https://en.wikipedia.org/wiki/Archimedean_property
    locator: Equivalent definitions of Archimedean ordered field
---

## Statement

Let $x$ and $y$ be real numbers with $x < y$.
Then there is a [[rational number|0NCJ5WXN6Z]] $q$ with $x < q < y$.

## Remarks

Proof idea: choose $n$ with $1/n < y - x$ by the [[Archimedean property|0WH916TJNY]]. Then some fraction $m/n$ with $m \in \mathbb{Z}$ lies between $x$ and $y$.
Thus between two real numbers there are infinitely many rational numbers.
The [[irrationals are also dense|04J6G4H78J]].

## Explanations

### L1 human

Between any two different real numbers, however close, there is a fraction.
For example, between $\sqrt{2} = 1.41421\dots$ and $1.4143$ lies the fraction $1.41425 = 28285/20000$.
