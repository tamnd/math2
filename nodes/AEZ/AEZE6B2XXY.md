---
tag: AEZE6B2XXY
kind: concept
name: Collectively compact operator approximation
msc: [45L05, 47A58, 65R20]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_operator
---

## Summary

A sequence of operators $K_n$ is a collectively compact approximation of an operator $K$ if $K_n \to K$ pointwise.
In addition, the images of the unit ball under all $K_n$ together must form a relatively compact set.
This weaker notion replaces norm convergence, which often fails for numerical methods such as the Nyström method.
It still gives the main conclusion when $I - K$ is invertible.
Then $I - K_n$ is invertible for large $n$, with uniformly bounded inverses, and the approximate solutions converge.
The theory was developed by P. M. Anselone for the numerical solution of integral equations.

## Explanations

### L1 human

In the Nyström method one replaces an integral by a weighted sum over finitely many points.
The resulting operators do not get close to the integral operator in the strongest sense, because a function can be large between the quadrature points.
But all of them smooth functions in the same uniform way, and that is enough for the approximate equations to have solutions close to the true one.
A simple example: with the rectangle rule, $(K_n\varphi)(x) = \frac{1}{n} \sum_{j=1}^n k(x, \frac{j}{n}) \varphi(\frac{j}{n})$ approximates $\int_0^1 k(x, t) \varphi(t) \, dt$.
