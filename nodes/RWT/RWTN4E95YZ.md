---
tag: RWTN4E95YZ
kind: definition
name: Noncommutative geometry
msc: [58B34, 46L87, 46L85]
defines: PS2MR7P299
uses: [NT564Y315M]
sources:
  - url: https://en.wikipedia.org/wiki/Noncommutative_geometry
---

## Definition

A *noncommutative space* is a [[C*-algebra|M2WFY1D3SZ]] $A$, possibly not commutative, often with extra structure such as a dense $*$-subalgebra or a spectral triple.
*Noncommutative geometry* is the study of such algebras with the methods of topology and geometry, through the following dictionary.

1. A locally compact Hausdorff space $X$ corresponds to the commutative C*-algebra $C_0(X)$ of continuous complex functions on $X$ that vanish at infinity.
2. By the [[commutative Gelfand–Naimark theorem|NT564Y315M]], every commutative C*-algebra is isomorphic to $C_0(X)$ for a locally compact Hausdorff space $X$, unique up to homeomorphism.
3. A notion of the geometry of $X$ that can be expressed through $C_0(X)$ alone is then defined for every C*-algebra by the same formula.

## Remarks

Example: the space $X$ is compact if and only if $C_0(X)$ has a unit.
So a unital C*-algebra is read as a "compact noncommutative space".
Another example: vector bundles over a compact space $X$ correspond to finitely generated projective $C(X)$-modules.
So these modules play the role of vector bundles for any unital C*-algebra, and this leads to [[operator K-theory|DQZ8S67ZE6]].

Non-example: the notion "a point of the space" does not carry over.
A point $x$ of $X$ gives the character $f \mapsto f(x)$ of $C_0(X)$, that is, a nonzero multiplicative linear functional.
The matrix algebra $M_2(\C)$ has no such functional.
Indeed, if $\varphi$ is one and $E_{ij}$ are the matrix units, then $\varphi(E_{11}) = \varphi(E_{12})\varphi(E_{21}) = \varphi(E_{22})$ and $\varphi(E_{11})\varphi(E_{22}) = \varphi(E_{11}E_{22}) = 0$, so $\varphi(I) = \varphi(E_{11}) + \varphi(E_{22}) = 0$.
Then $\varphi(a) = \varphi(I)\varphi(a) = 0$ for every $a$, a contradiction.

The approach of Alain Connes adds a [[spectral triple|FTQMQR3YS7]] to $A$ to describe metric and differential structure.
