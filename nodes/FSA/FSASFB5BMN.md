---
tag: FSASFB5BMN
kind: definition
name: Buekenhout geometry
msc: ["51E24", 51A05]
defines: 4W27TKGQWR
uses: [FGKNAFNHA3, ZT9A6JK8QF, PCT2HY9AAZ]
sources:
  - url: https://en.wikipedia.org/wiki/Buekenhout_geometry
---

## Definition

Let $I$ be a finite set, the set of types.
Let $X$ be a set with a reflexive and symmetric relation $*$, called incidence.
Let $\tau \colon X \to I$ be a map, called the type function.
The triple $(X, *, \tau)$ is a *Buekenhout geometry* (or *geometry*) over $I$ if:

1. if $x * y$ and $\tau(x) = \tau(y)$, then $x = y$;
2. every flag, that is, every set of pairwise incident elements of $X$, is contained in a flag $C$ with $\tau(C) = I$.

## Remarks

A flag $C$ with $\tau(C) = I$ is a *chamber*; by clause 1 it has exactly one element of each type.
The number $\abs{I}$ is the rank.
A geometry of rank $2$ is the same as an [[incidence structure|FGKNAFNHA3]] whose flags extend, such as a projective plane or a [[generalized polygon|PCT2HY9AAZ]].
The residue of a flag $F$ is the geometry of the elements incident with all of $F$ and not in $F$, over the types not met by $F$.
The *Buekenhout diagram* records, for each pair of types $i \ne j$, the class of the rank $2$ residues of type $\set{i, j}$.
Tits buildings give geometries whose diagrams are Coxeter diagrams.

Example: let $\mathcal{P}$ be an $n$-dimensional [[projective space|ZT9A6JK8QF]].
Take $X$ to be the set of its subspaces of dimension $0, 1, \dots, n - 1$, let $\tau$ be the dimension, and let $x * y$ mean $x \subseteq y$ or $y \subseteq x$.
Clause 1 holds since two distinct subspaces of the same dimension are not contained in each other.
Clause 2 holds since every chain of subspaces can be refined to a chain with one subspace of each dimension.

Non-example: take the lines of a projective plane, all of one type, with $x * y$ meaning that $x$ and $y$ meet.
Any two lines meet, so two distinct incident elements have the same type and clause 1 fails.
