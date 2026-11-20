---
tag: 0ASHNYF7AG
kind: concept
name: Annihilator of a subspace
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug2
specializes: [00YC1D652K]
uses: [07JBSZE0V4, 00YC1D652K, 07YQ1C78G0]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Quotient spaces and annihilators
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Annihilators
  - book: isbn:9783031410253
    locator: Section 3F
  - book: isbn:9780134860244
    locator: Section 2.6
---

## Summary

Let $V$ be a vector space over a field $F$ and let $U$ be a [[subspace|00YC1D652K]] of $V$.
The annihilator of $U$ is the set $U^0 = \set{f \in V^* : f(u) = 0 \text{ for all } u \in U}$ of [[linear forms|07YQ1C78G0]] that vanish on $U$.
It is a subspace of the [[dual space|07JBSZE0V4]] $V^*$.
In finite dimension, $\dim U + \dim U^0 = \dim V$, and $U \mapsto U^0$ matches the subspaces of $V$ with those of $V^*$, reversing inclusions.

## Motivation

A subspace can be given by vectors that span it, or by linear equations that cut it out.
The annihilator collects all linear equations that hold on $U$.
For example, the plane $x + y + z = 0$ in $\R^3$ has the annihilator spanned by the form $x + y + z$.
Passing from $U$ to $U^0$ turns "parametric" descriptions into "equation" descriptions, and back.

## Notation

The annihilator is written $U^0$, $U^\circ$, $\operatorname{Ann}(U)$ or $U^\perp$.
The notation $U^\perp$ is also used for the orthogonal complement in an inner product space, which is a subspace of $V$, not of $V^*$.
For a subspace $X$ of $V^*$, the set $X_0 = \set{v \in V : f(v) = 0 \text{ for all } f \in X}$ is sometimes called the pre-annihilator.
Mathlib writes `Submodule.dualAnnihilator`.

## Remarks

### Examples

- [[The annihilator of a plane in R^3|5VNTTZGN1A]]: for $U = \set{x + y + z = 0}$, the annihilator is $U^0 = \R \cdot (x + y + z)$. For the line spanned by $(1, 2, 3)$, it is spanned by $-2x + y$ and $-3x + z$.
- [[The annihilator of the trace-zero matrices|5QM5REJ243]] is the line spanned by the trace.
- $\set{0}^0 = V^*$ and $V^0 = \set{0}$.

### Non-examples

- [[The orthogonal complement is not the annihilator|ENNMQ30X9F]]: in $\R^2$, the orthogonal complement of a line is a line in $\R^2$, and it depends on the inner product. The annihilator is a line in $(\R^2)^*$, and it needs no inner product.
- The set of forms $f$ on $\R^2$ with $f(1, 0) = 1$ is not the annihilator of any subspace. It does not contain the zero form, so it is not even a subspace of $(\R^2)^*$.

### Basic properties

- If $U \subseteq W$, then $W^0 \subseteq U^0$. Further, $(U + W)^0 = U^0 \cap W^0$ and $(U \cap W)^0 = U^0 + W^0$, in any dimension, by the [[lemma on annihilators|Z71CEX564V]].
- In finite dimension, $\dim U^0 = \dim V - \dim U$, by the theorem on the [[dimension of the annihilator|06Q1EFVH0Q]]. Also $U^0 \cong (V/U)^*$ and $V^*/U^0 \cong U^*$.
- The [[kernel of the dual map|7FA499AW3T]] is an annihilator: $\ker f^* = (\im f)^0$.
- If $U = \ker f$ for a nonzero form $f$, then $U^0 = Ff$; this is part 3 of the theorem on [[hyperplanes and linear forms|XR0EQN0H8T]].

### History

The annihilator is the linear-algebra form of a general idea: the set of things that "kill" a given set.
The same word is used for the [[annihilator in ring theory|HB4XDKJTW8]], and in harmonic analysis, where [[annihilator duality|YT42EZ7GQQ]] matches the closed subgroups of a locally compact abelian group with those of its dual group.

### Common errors

- Confusing $U^0 \subseteq V^*$ with the orthogonal complement $U^\perp \subseteq V$.
- Expecting $U \mapsto U^0$ to be onto the subspaces of $V^*$ in infinite dimension. On $F^{(\N)}$, the span $X$ of the coordinate forms is a proper subspace of $V^*$, but no subspace $U$ has $U^0 = X$.
- Getting the direction of inclusion wrong: a larger subspace has a smaller annihilator.

## Explanations

### L1 human

The annihilator of a subspace is the set of all linear equations that the subspace satisfies.
A plane through the origin in space satisfies one equation, up to a factor, so its annihilator is one-dimensional.
A line through the origin in space satisfies two independent equations, so its annihilator is two-dimensional.
In each case, the dimensions add up to $3$.

### L2 human

We find the annihilator of the line $U$ spanned by $(1, 2, 3)$ in $\R^3$.

1. A form $f = ax + by + cz$ lies in $U^0$ exactly when $f(1, 2, 3) = a + 2b + 3c = 0$.
2. The solutions are $(a, b, c) = b(-2, 1, 0) + c(-3, 0, 1)$.
3. So $U^0$ is spanned by $-2x + y$ and $-3x + z$, and $\dim U^0 = 2 = 3 - 1$.
4. The common kernel of these two forms is the set $y = 2x$, $z = 3x$, which is $U$ again.

The typical use is to write a subspace as the solution set of a linear system: a basis of $U^0$ gives a system of equations for $U$.
A trap: $U^0$ lives in $V^*$, so its elements are equations, not vectors.

### L3 human

In finite dimension, $U \mapsto U^0$ is an order-reversing bijection between the lattices of subspaces of $V$ and of $V^*$, which exchanges sums and intersections.
Under the identification of $U^0$ with $(V/U)^*$, the annihilator is the dual of the quotient, and $V^* / U^0 \cong U^*$ is the dual of the inclusion.
So annihilators express that duality turns subspaces into quotients and quotients into subspaces.
In a normed space, the annihilator of a subspace inside the continuous dual is the starting point of the duality between subspaces and quotients in functional analysis.
