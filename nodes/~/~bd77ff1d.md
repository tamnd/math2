---
tag: ~bd77ff1d
kind: statement
role: theorem
name: Sum of a finite geometric progression
aliases: [finite-geometric-series]
msc: [05A19]
uses: [~a5a82956]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_progression
    locator: Geometric series
---

## Statement

Let $x$ be a real number with $x \neq 1$, and let $n$ be a natural number.
Then
$$\sum_{k=0}^{n-1} x^k = 1 + x + x^2 + \dots + x^{n-1} = \frac{x^n - 1}{x - 1}.$$

## Remarks

The same formula holds for $x$ in any field, for example for complex numbers, when $x \neq 1$.
For $x = 1$, the sum is $n$.
A short proof: $(x - 1)(1 + x + \dots + x^{n-1}) = x^n - 1$, because the other terms cancel.

## Explanations

### L1 human

In a geometric progression, you get each term from the one before by multiplying by the same number $x$.
For $x = 2$, the formula gives $1 + 2 + 4 + 8 = 2^4 - 1 = 15$.
Multiply the sum by $x$ and subtract the sum: almost all terms cancel, and only $x^n - 1$ stays.
