---
tag: 9F0CPB14FQ
kind: definition
name: Permutation group
msc: [20B05, 20B07]
defines: ZDJQRKPWGA
uses: [05RWFKVTJ7, 0515A6D2Y1, 0X1JXT47GA, 0WCY42EV9V, 0P7G9NGG2G, 0151VYVX27, 0JZ27DMJ5D]
sources:
  - url: https://en.wikipedia.org/wiki/Permutation_group
---

## Definition

Let $\Omega$ be a set, and let $\operatorname{Sym}(\Omega)$ be the [[symmetric group|0515A6D2Y1]] of $\Omega$: the group of all bijections $\Omega \to \Omega$ under composition.
A *permutation group* on $\Omega$ is a [[subgroup|0X1JXT47GA]] $G$ of $\operatorname{Sym}(\Omega)$.
The *degree* of $G$ is the cardinality $\abs{\Omega}$.

## Remarks

Example: label the corners of a square $1, 2, 3, 4$ in cyclic order.
The eight symmetries of the square give the set $G = \set{e, (1\,2\,3\,4), (1\,3)(2\,4), (1\,4\,3\,2), (1\,3), (2\,4), (1\,2)(3\,4), (1\,4)(2\,3)}$.
It is closed under composition and inverses, because the composite of two symmetries of the square is again one.
So $G$ is a permutation group of degree $4$, isomorphic to the [[dihedral group|0JZ27DMJ5D]] of order $8$.

Non-example: the set $\set{e, (1\,2), (1\,3), (2\,3)}$ in $S_3$.
It contains $(1\,2)$ and $(1\,3)$ but not their product, which is a $3$-cycle, so it is not a subgroup.

A [[group action|0WCY42EV9V]] of a group $H$ on $\Omega$ is the same as a homomorphism $H \to \operatorname{Sym}(\Omega)$, and its image is a permutation group on $\Omega$.
The image is isomorphic to $H$ exactly when the action is [[faithful|0P7G9NGG2G]].
By [[Cayley's theorem|0151VYVX27]], the action of a group $H$ on itself by left multiplication is faithful, so $H$ is isomorphic to a permutation group on $H$.
