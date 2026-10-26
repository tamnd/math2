---
tag: 0YY06KP3ZQ
kind: statement
role: theorem
name: Quadratic reciprocity for the Jacobi symbol
msc: [11A15]
uses: [0XDB5AW7M1, 085MJS6907]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_symbol
    locator: Properties
---

## Statement

Let $m$ and $n$ be coprime positive odd integers.
Then
$$\left(\frac{m}{n}\right) \left(\frac{n}{m}\right) = (-1)^{\frac{m-1}{2} \cdot \frac{n-1}{2}},$$
where the symbols are [[Jacobi symbols|0XDB5AW7M1]].

## Remarks

The supplements also extend: for a positive odd $n$, $\left(\frac{-1}{n}\right) = (-1)^{(n-1)/2}$ and $\left(\frac{2}{n}\right) = (-1)^{(n^2-1)/8}$.
The proof uses the [[law of quadratic reciprocity|085MJS6907]] for each pair of prime factors.
With this law, one computes $\left(\frac{a}{n}\right)$ by an algorithm like the [[Euclidean algorithm|0TRNT4X7J0]], with no factorization.

## Explanations

### L1 human

The Jacobi symbol obeys the same reciprocity law as the Legendre symbol.
So you can flip the symbol, reduce the top number modulo the bottom number, and repeat.
This gives a fast way to compute Legendre symbols for large primes.
