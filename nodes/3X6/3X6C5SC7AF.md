---
tag: 3X6C5SC7AF
kind: statement
role: theorem
name: Durand–Kerner method
msc: [65H04]
uses: [07EXVNF9VP, 019MA1VTR2, 0BDX4MBKT4, 0JP0W07Y9A, YWZQC5E54B, 09FTAET5Z4]
about: [019MA1VTR2]
sources:
  - url: https://en.wikipedia.org/wiki/Durand–Kerner_method
same_as:
  wikidata: Q1299016
  wikipedia: Durand–Kerner method
---

## Statement

Let $p$ be a [[monic polynomial|0BDX4MBKT4]] of degree $n \ge 2$ with [[complex|09FTAET5Z4]] coefficients, whose roots $r_1, \dots, r_n$ are pairwise distinct.
The *Durand–Kerner method*, also called the Weierstrass method, updates $n$ approximations $z_1^{(k)}, \dots, z_n^{(k)}$ simultaneously by
$$z_i^{(k+1)} = z_i^{(k)} - \frac{p\big(z_i^{(k)}\big)}{\prod_{j \ne i} \big(z_i^{(k)} - z_j^{(k)}\big)}, \qquad i = 1, \dots, n.$$
Then there is $\delta > 0$ such that, if $\abs{z_i^{(0)} - r_i} < \delta$ for all $i$, the iterates are defined and $z_i^{(k)} \to r_i$ for each $i$, with quadratic [[convergence|YWZQC5E54B]].

## Remarks

The update is [[Newton's method|07EXVNF9VP]] applied to the system of $n$ equations in $n$ unknowns that says that $\prod_i (x - z_i) = p(x)$ as polynomials.
Equivalently, it is Newton's method for the coefficients of the factorization, and the Jacobian of this system is invertible exactly when the $z_i$ are distinct.
This explains the local quadratic convergence at simple roots.
The [[fundamental theorem of algebra|0JP0W07Y9A]] guarantees that $p$ has $n$ complex roots counted with multiplicity.
A usual start takes $z_i^{(0)} = w^{i-1}$ for a complex number $w$ that is neither real nor a root of unity, for example $w = 0.4 + 0.9 \sqrt{-1}$.
With such starts the method usually converges in practice, but the theorem above is only local.
At multiple roots the convergence is only linear.

## Explanations

### L1 human

Instead of hunting one root at a time, the Durand–Kerner method moves $n$ guesses at once, one for each root.
Each guess is pushed by a Newton-like step, in which the other guesses play the role of the other roots.
The guesses spread out and settle on the $n$ roots together.

### L2 human

The method avoids deflation, which can lose accuracy when roots are removed one by one.
Each step costs $O(n^2)$ operations.
The Aberth method is a refinement with cubic local convergence.
