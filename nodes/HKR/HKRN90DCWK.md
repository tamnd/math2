---
tag: HKRN90DCWK
kind: statement
role: theorem
name: Kolmogorov criterion for best approximation
msc: [41A50, 41A65]
uses: [7N4988HN3P, 0TVJZYB6SH, 0S1FJ8VEX9, 00YC1D652K]
about: [7N4988HN3P]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_theory
---

## Statement

Let $K$ be a [[compact|0TVJZYB6SH]] [[Hausdorff space|0S1FJ8VEX9]], and let $C(K)$ be the space of continuous functions $K \to \R$ with the supremum norm.
Let $V \subseteq C(K)$ be a [[linear subspace|00YC1D652K]], let $f \in C(K)$ and $p^* \in V$, and let
$$E = \set{x \in K : \abs{f(x) - p^*(x)} = \norm{f - p^*}}$$
be the set of extreme points of the error.
Then $p^*$ is a [[best approximation|7N4988HN3P]] of $f$ from $V$ if and only if
$$\min_{x \in E} \big( f(x) - p^*(x) \big) \, p(x) \le 0 \quad \text{for every } p \in V.$$

## Remarks

The idea of the proof: suppose some $p \in V$ has $(f - p^*) p > 0$ on $E$.
By compactness this product is positive on an open set $U \supseteq E$, and $\abs{f - p^*}$ stays below $\norm{f - p^*} - \eta$ for some $\eta > 0$ off $U$.
Then $\norm{f - p^* - t p} < \norm{f - p^*}$ for small $t > 0$, so $p^*$ is not best.
Conversely, if $q \in V$ has $\norm{f - q} < \norm{f - p^*}$, then $p = q - p^*$ satisfies $(f - p^*) p = (f - p^*)^2 - (f - p^*)(f - q) > 0$ on $E$.

Example: for $f(x) = x^2$ on $[0, 1]$, $V$ the lines and $p^*(x) = x - 1/8$, the set $E$ is $\set{0, 1/2, 1}$ with error signs $+, -, +$.
A line $p$ with $p(0) > 0$, $p(1/2) < 0$ and $p(1) > 0$ would have two zeros, so it does not exist, and the criterion shows $p^*$ is best.

For complex-valued functions the same criterion holds with $\operatorname{Re} \big( \overline{(f(x) - p^*(x))} \, p(x) \big)$ in place of the product.

## Explanations

### L1 human

A candidate approximation is best unless some correction pushes in the right direction at every point where the error is worst.
The criterion checks exactly this: there must be no $p$ that has the same sign as the error at all the worst points.

### L2 human

The criterion holds for every linear subspace, not only for polynomials or Haar subspaces.
For Haar subspaces it turns into the alternation property of the equioscillation theorem, because a function of a Haar subspace can follow any sign pattern with few sign changes.
It is a form of the first-order optimality condition for the convex function $p \mapsto \norm{f - p}$.
Similar criteria hold in other normed spaces with the norm's subdifferential in place of the product.
