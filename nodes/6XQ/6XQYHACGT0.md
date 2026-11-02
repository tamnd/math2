---
tag: 6XQYHACGT0
kind: concept
name: Weighted polynomial approximation
msc: [41A81, 41A10]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_theory
---

## Summary

Weighted polynomial approximation measures the distance between a function and polynomials with a weight $w$, as in $\sup_x \abs{f(x) - p(x)} w(x)$ or in a weighted $L^p$ norm.
On unbounded sets such as $\R$ the weight must decay fast enough to make polynomials have finite norm.
A classical question, Bernstein's approximation problem, asks for which weights on $\R$ polynomials are dense in the corresponding space of continuous functions.
For the weights $e^{-\abs{x}^\alpha}$ the answer is yes exactly when $\alpha \ge 1$, and [[orthogonal polynomials|8TXASARQN1]] for such weights are a main tool.

## Explanations

### L1 human

On a closed bounded interval, every continuous function is a uniform limit of polynomials, by the [[Weierstrass approximation theorem|0JQE130DHW]].
On the whole real line this fails, because a nonconstant polynomial grows without bound.
A weight $w(x)$ that tends to $0$ quickly at infinity tames this growth, and one only asks that $(f - p) w$ be small.
For example, with $w(x) = e^{-x^2}$ every polynomial $p$ has $p(x) w(x) \to 0$ as $\abs{x} \to \infty$.
How fast the weight decays decides whether polynomials can approximate every function of the weighted space.
