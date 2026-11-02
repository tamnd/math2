---
tag: VC48WDWPV1
kind: concept
name: Kohn–Rossi cohomology
msc: [32V05, 32W10, 32V20]
sources:
  - url: https://en.wikipedia.org/wiki/CR_manifold
---

## Summary

Kohn–Rossi cohomology is the cohomology of the tangential Cauchy–Riemann complex $\bar\partial_b$ on a [[CR manifold|ZC78JKZX9S]].
It plays for CR manifolds the role that [[Dolbeault cohomology|Y3900T2EY5]] plays for complex manifolds.
Its degree $0$ group is the space of smooth [[CR functions|JFKYYK2CEB]], and the higher groups measure the obstruction to solving the equation $\bar\partial_b u = f$.

## Explanations

### L1 human

On a complex manifold one studies the equation $\bar\partial u = f$, and Dolbeault cohomology records when it cannot be solved.
A CR manifold, such as a real hypersurface in $\C^n$, has only part of the complex directions, so only the tangential part $\bar\partial_b$ of $\bar\partial$ makes sense on it.
Kohn–Rossi cohomology records when $\bar\partial_b u = f$ cannot be solved, given the necessary condition $\bar\partial_b f = 0$.
Take the unit sphere $S^{2n-1}$ in $\C^n$ with $n \ge 2$.
Its degree $0$ group consists of the boundary values of holomorphic functions on the ball that are smooth up to the boundary.
