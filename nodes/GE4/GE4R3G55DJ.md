---
tag: GE4R3G55DJ
kind: definition
name: Grothendieck–Witt group
msc: [19G12, "11E81", 19G38]
defines: KG8D0N6712
uses: [0RBQS1JJCR, 5FDMY7PDYY, 0F6ES3BRYP, CCB8VNQCV0, KFVY0RPGF2]
sources:
  - url: https://en.wikipedia.org/wiki/Witt_group
---

## Definition

Let $F$ be a field whose [[characteristic|0F6ES3BRYP]] is not $2$.
A quadratic space over $F$ is a finite-dimensional vector space with a nondegenerate [[quadratic form|0RBQS1JJCR]].
Let $M(F)$ be the set of isometry classes of quadratic spaces over $F$.
It is a commutative monoid under orthogonal sum $\perp$, with the zero space as identity.
The *Grothendieck–Witt group* $GW(F)$ is the [[Grothendieck group|5FDMY7PDYY]] of the monoid $M(F)$.
Its elements are formal differences $[q_1] - [q_2]$ of quadratic spaces.
The tensor product of quadratic spaces makes $GW(F)$ a commutative ring with unit $[\langle 1 \rangle]$.

## Remarks

Here $\langle a_1, \ldots, a_n \rangle$ denotes the diagonal form $a_1 x_1^2 + \cdots + a_n x_n^2$, with all $a_i \in F^\times$.
By Witt cancellation, a consequence of [[Witt's theorem|CCB8VNQCV0]], the monoid $M(F)$ is cancellative, so $M(F) \to GW(F)$ is injective.
The dimension gives a ring homomorphism $\dim \colon GW(F) \to \Z$.
Let $H = \langle 1, -1 \rangle$ be the hyperbolic plane; the multiples of $[H]$ form an ideal, and $GW(F)/\Z[H]$ is the [[Witt ring|KFVY0RPGF2]] $W(F)$.
Example: $GW(\R) \cong \Z \oplus \Z$, via the numbers of positive and of negative entries in a diagonalization, by Sylvester's law of inertia.
Non-example: in $W(\R)$ the classes of the zero space and of $H$ agree, but in $GW(\R)$ they differ, since $\dim H = 2$.
