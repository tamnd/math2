---
tag: QB3Q5FBJ08
kind: concept
name: Mixed volume
msc: [52A39]
sources:
  - url: https://en.wikipedia.org/wiki/Mixed_volume
same_as:
  wikidata: Q4424496
  wikipedia: Mixed volume
---

## Summary

Let $K_1, \dots, K_r$ be nonempty compact convex sets of $\R^n$ and $\lambda_i \ge 0$.
The volume of the [[Minkowski sum|SXS6D87PHE]] $\lambda_1 K_1 + \cdots + \lambda_r K_r$ is a homogeneous polynomial of degree $n$ in the $\lambda_i$.
Its coefficients are the mixed volumes $V(K_{i_1}, \dots, K_{i_n})$.
Mixed volumes unify volume, surface area, mean width and many other measurements of convex bodies.
They satisfy deep inequalities, above all the [[Alexandrov–Fenchel inequality|D3AVHVYQW9]].

## Explanations

### L1 human

Blow up two convex shapes by factors $\lambda$ and $\mu$ and add them.
The area of the result is $A(K) \lambda^2 + 2 V(K, L) \lambda \mu + A(L) \mu^2$, a quadratic expression.
The middle coefficient $V(K, L)$ is the mixed area of $K$ and $L$: it measures how the two shapes interact.
When $L$ is the unit disk, $V(K, L)$ is half the perimeter of $K$.
So perimeter, and in higher dimensions surface area, are special mixed volumes.
