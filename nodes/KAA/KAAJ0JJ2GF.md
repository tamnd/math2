---
tag: KAAJ0JJ2GF
kind: statement
role: theorem
name: Pfaff and Euler transformations
msc: ["33C05"]
uses: [463X5V31D9]
about: [463X5V31D9]
sources:
  - url: https://en.wikipedia.org/wiki/Hypergeometric_function
---

## Statement

Let $a, b, c \in \C$ with $c \notin \set{0, -1, -2, \ldots}$, and let ${}_2F_1$ be the [[hypergeometric function|463X5V31D9]] on $\C \setminus [1, \infty)$, with principal powers.
Then for all $z \in \C \setminus [1, \infty)$:

1. (Pfaff transformations)
$${}_2F_1(a, b; c; z) = (1 - z)^{-a} \, {}_2F_1\left(a, c - b; c; \frac{z}{z - 1}\right) = (1 - z)^{-b} \, {}_2F_1\left(c - a, b; c; \frac{z}{z - 1}\right).$$
2. (Euler transformation)
$${}_2F_1(a, b; c; z) = (1 - z)^{c - a - b} \, {}_2F_1(c - a, c - b; c; z).$$

## Remarks

The map $z \mapsto \frac{z}{z - 1}$ sends $\C \setminus [1, \infty)$ onto itself, so the right sides make sense.
For $\operatorname{Re} c > \operatorname{Re} b > 0$, the first Pfaff formula follows from [[Euler's integral representation|812THX456R]] by the substitution $t \mapsto 1 - t$, and the general case by analytic continuation in the parameters.
The second Pfaff formula is the first with $a$ and $b$ exchanged, and applying the two Pfaff formulas one after the other gives the Euler transformation.

Example: for $b = c$, the Euler transformation reads $(1 - z)^{-a} = (1 - z)^{-a} \, {}_2F_1(c - a, 0; c; z)$, which is true since ${}_2F_1(\cdot, 0; c; z) = 1$.

The Pfaff transformation turns the series at $z$ into a series at $\frac{z}{z - 1}$, which converges for $\operatorname{Re} z < \frac12$; this gives the continuation of ${}_2F_1$ to that half-plane.

## Explanations

### L1 human

The same hypergeometric function can be written in several different ways, with changed parameters, a changed variable, and a power of $1 - z$ in front.
These formulas let one pass from a series that converges slowly to one that converges fast, or to a region where the original series does not converge at all.

### L2 human

Together with the identity, the Pfaff and Euler transformations form a group of four expressions for the same solution of the hypergeometric equation.
Combined with the solutions at the other singular points, they give [[Kummer's 24 solutions|7QFW771QMA]].
The Euler transformation also explains the factor $(1 - z)^{c - a - b}$ that governs the behaviour of ${}_2F_1$ near $z = 1$.
