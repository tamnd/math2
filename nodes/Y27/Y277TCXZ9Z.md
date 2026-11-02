---
tag: Y277TCXZ9Z
kind: statement
role: theorem
name: Laguerre's method
msc: [65H04]
uses: [019MA1VTR2, 047SX3TD69, YWZQC5E54B, 09FTAET5Z4]
about: [019MA1VTR2]
sources:
  - url: https://en.wikipedia.org/wiki/Laguerre%27s_method
same_as:
  wikidata: Q1171964
  wikipedia: Laguerre's method
---

## Statement

Let $p$ be a polynomial of degree $n \ge 2$ with complex coefficients.
For a point $x$ with $p(x) \ne 0$, put
$$G = \frac{p'(x)}{p(x)}, \qquad H = G^2 - \frac{p''(x)}{p(x)}, \qquad a = \frac{n}{G \pm \sqrt{(n - 1)(nH - G^2)}},$$
where the sign is chosen so that the denominator has the larger absolute value.
*Laguerre's method* is the iteration $x_{k+1} = x_k - a$, with $G, H, a$ computed at $x = x_k$.
Then:

1. If $r$ is a [[root|019MA1VTR2]] of $p$ of [[multiplicity|047SX3TD69]] $1$, then for $x_0$ close enough to $r$ the iterates [[converge|YWZQC5E54B]] to $r$ with order $3$.
2. If all roots of $p$ are real, then for every real $x_0$ the iterates stay real and converge to a root of $p$.

## Remarks

The formula comes from a model of $p$ near $x$.
Assume that one root $r$ is at distance $a = x - r$, and that the other $n - 1$ roots all sit at a common distance $b$.
The identities $G = \sum_i \frac{1}{x - r_i}$ and $H = \sum_i \frac{1}{(x - r_i)^2}$ over the roots $r_i$ then give two equations for $a$ and $b$, whose solution is the formula above.
For polynomials with only real roots, a real starting point between two consecutive roots leads to one of these two roots.
A real starting point outside all roots leads to the nearest root on that side.
At a multiple root the convergence is only linear.
The square root can be non-real, so the method also finds the [[complex|09FTAET5Z4]] roots of real polynomials.

## Explanations

### L1 human

Laguerre's method is a root finder made for polynomials.
It pretends that one root is near and all the others are bunched together far away, and it solves this simplified picture exactly.
The answer is a very good next guess, and near a simple root the number of correct digits roughly triples at each step.

### L2 human

The method uses $p$, $p'$ and $p''$, which Horner's scheme evaluates cheaply.
Its convergence from almost any start makes it a robust choice for finding all roots one at a time, with deflation after each root.
Its behaviour on polynomials with only real roots is a rare case of guaranteed global convergence.
