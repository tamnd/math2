---
tag: 7DH8HG1SXH
kind: definition
name: Wreath product
msc: ["20E22"]
defines: W1X984PKJ9
uses: [G5S1M9, 0WCY42EV9V, 0H3WZXCZNF, 00HF4RJ5QN]
sources:
  - url: https://en.wikipedia.org/wiki/Wreath_product
---

## Definition

Let $A$ and $G$ be [[groups|G5S1M9]], and let $G$ [[act|0WCY42EV9V]] on a set $\Omega$, written $(g, \omega) \mapsto g\omega$.
Let $A^\Omega$ be the group of all functions $f \colon \Omega \to A$ with the pointwise product, that is, the [[direct product|00HF4RJ5QN]] of $\abs{\Omega}$ copies of $A$.
For $g \in G$ and $f \in A^\Omega$, let $g \cdot f \in A^\Omega$ be the function $(g \cdot f)(\omega) = f(g^{-1}\omega)$.
This defines an action of $G$ on $A^\Omega$ by automorphisms.
The *wreath product* $A \wr_\Omega G$ is the [[semidirect product|0H3WZXCZNF]] $A^\Omega \rtimes G$ for this action.
Its elements are the pairs $(f, g)$ with $f \in A^\Omega$ and $g \in G$, and the product is
$$(f, g)(f', g') = (f \, (g \cdot f'), \; g g').$$
The subgroup $A^\Omega$ is the *base group*.
When $\Omega = G$ with the action by left multiplication, the group is the *regular wreath product*, written $A \wr G$.

## Remarks

The order of a finite wreath product is $\abs{A \wr_\Omega G} = \abs{A}^{\abs{\Omega}} \abs{G}$.

Example: let $A = C_2$ and let $G = C_2$ act on $\Omega = \set{1, 2}$ by swapping.
Then $A \wr_\Omega G$ has order $2^2 \cdot 2 = 8$.
It is isomorphic to the dihedral group of order $8$, the symmetry group of a square.
The base group $C_2 \times C_2$ consists of the identity, the half-turn and the reflections in the two diagonals.
The swap is the reflection in an axis through the midpoints of two opposite sides.

Non-example: the direct product $A^\Omega \times G$ has the same underlying set, but there $G$ does not move the functions at all.
Its multiplication differs from that of the wreath product when $A \ne 1$ and $G$ moves some point, because then $g \cdot f \ne f$ for some $g$ and $f$.

For $G = S_m$ acting on $\set{1, \dots, m}$, the group $S_k \wr S_m$ is the subgroup of $S_{km}$ that preserves a fixed partition of $km$ points into $m$ parts of size $k$.
The group $C_2 \wr S_n$ is the group of signed permutations, of order $2^n n!$.
For an infinite set $\Omega$, the group defined above is the *unrestricted* wreath product, built from all functions $\Omega \to A$.
The *restricted* wreath product uses only the functions with $f(\omega) = 1$ for all but finitely many $\omega$.
