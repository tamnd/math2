---
tag: T5VW3PE7TZ
kind: statement
role: theorem
name: Baouendi–Trèves approximation theorem
msc: [32V10, "32E30"]
uses: [JFKYYK2CEB, ZC78JKZX9S, 07GNX8GCYP]
about: [JFKYYK2CEB]
sources:
  - url: https://en.wikipedia.org/wiki/CR_manifold
---

## Statement

Let $M$ be a smooth real submanifold of $\C^n$ that is generic, that is, $T_q M + J\, T_q M = T_q \C^n$ for every $q \in M$, where $J$ is multiplication by $i$.
Let $p \in M$.
Then there is a compact neighbourhood $K$ of $p$ in $M$ with the following property.
Let $f$ be a continuous [[CR function|JFKYYK2CEB]] on $M$.
Then there is a sequence $(P_k)$ of complex [[polynomials|07GNX8GCYP]] in $z_1, \dots, z_n$ such that $P_k \to f$ uniformly on $K$.

## Remarks

The theorem is due to M. S. Baouendi and F. Trèves, who proved it for locally integrable structures; the statement above is its form for embedded [[CR manifolds|ZC78JKZX9S]].
The proof convolves $f$ with the Gaussian kernel $e^{-\tau \sum_j (z_j - \zeta_j)^2}$ over a suitable totally real piece of $M$.
The result is an entire function of $z$.
The CR equations and Stokes' theorem show that it tends to $f$ on $K$ as $\tau \to \infty$.
Truncating the power series of these entire functions then gives polynomials.
The neighbourhood $K$ depends on $M$ and $p$ but not on $f$.
For example, let $M = \C^{n-1} \times \R \subset \C^n$.
Its CR functions are the functions holomorphic in $(z_1, \dots, z_{n-1})$ for each fixed real $z_n$.
The theorem says that they are local uniform limits of holomorphic polynomials in all $n$ variables.
The result is local: a CR function on all of $M$ need not be a uniform limit of polynomials on large compact subsets of $M$.

## Explanations

### L1 human

CR functions on a submanifold of complex space are defined by a system of differential equations, and they can be quite rough.
The theorem says that near each point they can nevertheless be approximated as closely as one wants by ordinary polynomials in the complex coordinates.
So every CR function is locally a limit of restrictions of holomorphic functions on the whole space.

### L2 human

This approximation theorem is a basic tool in the local theory of CR functions.
By the maximum principle, polynomials that converge uniformly on $K$ also converge uniformly on the polynomially convex hull $\widehat{K}$ of $K$.
So every continuous CR function on $M$ extends holomorphically to the interior of $\widehat{K}$, which gives a way to prove extension results such as the [[Lewy extension theorem|V2YCGHD719]].
The theorem also shows that CR functions in this sense are exactly the local uniform limits of restrictions of holomorphic functions.
