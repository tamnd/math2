---
tag: CT2F31EDH8
kind: concept
name: Complexification and realification
aliases: [complexification, realification, linear-complex-structure]
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: grad
uses: [000AYPA9AJ, 05G2G0P224, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Complexification
    locator: Formal definition
  - url: https://en.wikipedia.org/wiki/Linear_complex_structure
    locator: Definition
  - book: isbn:9780387728285
    locator: Chapter 1
same_as:
  wikipedia: Complexification
---

## Summary

The complexification of a real [[vector space|000AYPA9AJ]] $V$ is the complex vector space $V_\C = V \times V$, with pairs $(u, w)$ written $u + iw$.
Scalar multiplication is $(a + bi)(u, w) = (au - bw, aw + bu)$, and $\dim_\C V_\C = \dim_\R V$.
Realification goes the other way: a complex space $W$, with scalars restricted to $\R$, is a real space $W_\R$ with $\dim_\R W_\R = 2 \dim_\C W$.
A complex structure on a real space $V$ is a real linear map $J$ with $J^2 = -I$; it makes $V$ a complex space.

## Motivation

Real matrices can have complex eigenvalues, such as the rotation $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ with eigenvalues $\pm i$.
The eigenvectors live in $\C^2 = (\R^2)_\C$, not in $\R^2$.
Complexification gives a fixed place for them, and many proofs for real spaces pass through it.

## Notation

We write $V_\C$, or $V \otimes_\R \C$, for the complexification, and $W_\R$ for the realification.
The [[tensor product|0BF2DE2SYK]] form $V \otimes_\R \C$ is the definition in many books and in Mathlib; it is isomorphic to $V \times V$ with the rule above.

## Remarks

### Examples

1. $(\R^n)_\C = \C^n$: the pair $(u, w)$ of real vectors is the complex vector $u + iw$.
2. $(M_n(\R))_\C = M_n(\C)$, and $(\R[x])_\C = \C[x]$.
3. Check of the rule for $V = \R$: $V_\C = \R \times \R$, and $i \cdot (1, 0) = (0 \cdot 1 - 1 \cdot 0, 0 \cdot 0 + 1 \cdot 1) = (0, 1)$, which is $i$.
4. Check of axiom 5 for $i \cdot i$: $i \cdot (i \cdot (u, w)) = i \cdot (-w, u) = (-u, -w) = (-1) \cdot (u, w)$.
5. The realification of $\C$ is $\R^2$, with basis $1, i$, and multiplication by $i$ is the complex structure $J(x, y) = (-y, x)$.
6. The realification of $\C^n$ is $\R^{2n}$, with basis $e_1, i e_1, \dots, e_n, i e_n$.

### Non-examples

1. $\R^2$ with the reflection $J(x, y) = (y, x)$ and $(a + bi) v = a v + b J v$ fails axiom 5, compatibility.
   Check: $i \cdot (i \cdot (1, 0)) = J(J(1, 0)) = (1, 0)$, but $(i \cdot i)(1, 0) = (-1, 0)$; the cause is $J^2 = I$, not $-I$.
2. $\R^3$ has no complex structure: if $J^2 = -I$, then $\det(J)^2 = \det(-I) = (-1)^3 = -1$, which no real number satisfies.
3. $\R$ with $z \cdot x = \abs{z} x$ for $z \in \C$ fails axiom 8, distributivity over scalars: $(1 + (-1)) \cdot 1 = 0$, but $1 \cdot 1 + (-1) \cdot 1 = 1 + 1 = 2$.

### Basic properties

1. If $b_1, \dots, b_n$ is a [[basis|0VTQTPQGAV]] of $V$ over $\R$, then $(b_1, 0), \dots, (b_n, 0)$ is a basis of $V_\C$ over $\C$; so $\dim_\C V_\C = \dim_\R V$.
2. If $w_1, \dots, w_m$ is a basis of $W$ over $\C$, then $w_1, i w_1, \dots, w_m, i w_m$ is a basis of $W_\R$ over $\R$; so $\dim_\R W_\R = 2 \dim_\C W$.
3. A finite-dimensional real space has a complex structure if and only if its [[dimension|05G2G0P224]] is even.
4. A real linear map $T$ extends to $T_\C(u + iw) = Tu + i Tw$, and $T_\C$ has the same matrix as $T$ in the basis of property 1.
5. $(V_\C)_\R \cong V \oplus V$, of real dimension $2 \dim_\R V$.

### History

Hamilton defined complex numbers as pairs of real numbers in the 1830s.
The complexification $V \times V$ applies the same construction to a real vector space.

### Common errors

1. $V_\C$ is not $V$: for $V = \R^2$, the space $V_\C = \C^2$ has real dimension $4$.
2. The dimension depends on the field: $\dim_\C \C^n = n$, but $\dim_\R \C^n = 2n$.
3. A complex structure must be real linear with $J^2 = -I$; a map with $J^2 = I$, such as a reflection, gives no complex structure.
4. Complexifying a realification does not give back the space: $(W_\R)_\C$ has complex dimension $2 \dim_\C W$.

## Explanations

### L1 human

Complexification lets a real space use complex numbers as scalars, by pairing two real vectors as a real part and an imaginary part.
Realification forgets the complex scalars and keeps only the real ones, so the dimension doubles.

### L2 human

Example: the rotation by $90$ degrees on $\R^2$ has no real eigenvector.
In $(\R^2)_\C = \C^2$, the vector $(1, -i)$ satisfies $J(1, -i) = (i, 1) = i (1, -i)$, so it is an eigenvector with eigenvalue $i$.
To compute a dimension after realification, double the complex dimension: $\dim_\R \C^3 = 6$.

### L3 human

A complex structure $J$ on $\R^{2n}$ is the same as an identification $\R^{2n} \cong \C^n$, and the set of such $J$ is the homogeneous space $\mathrm{GL}_{2n}(\R) / \mathrm{GL}_n(\C)$.
On $V_\C$, the map $u + iw \mapsto u - iw$ is a conjugate-linear involution, and its fixed points are $V$; conversely, a complex space with such a real structure is the complexification of its fixed space.
