---
tag: DTNDR45FTH
kind: definition
name: Topos
msc: [18B25, 03G30]
defines: 6837RS7N82
uses: [A2DE66937D, PYSBNWCHCF, BFBNQ36QS8, RHWD8DY41R, NKP5TPQ79X]
sources:
  - url: https://en.wikipedia.org/wiki/Topos
---

## Definition

An *elementary topos* is a [[category|A2DE66937D]] $\mathcal{E}$ such that:

1. $\mathcal{E}$ has all finite limits (it is [[finitely complete|PYSBNWCHCF]]);
2. $\mathcal{E}$ is [[Cartesian closed|BFBNQ36QS8]]: for all objects $A$ and $B$ there is an [[exponential object|RHWD8DY41R]] $B^A$;
3. $\mathcal{E}$ has a [[subobject classifier|NKP5TPQ79X]] $\top \colon 1 \to \Omega$.

## Remarks

An equivalent definition asks for finite limits and power objects: for each object $A$, an object $PA$ with a natural bijection between subobjects of $B \times A$ and morphisms $B \to PA$; then $PA = \Omega^A$.
Every topos also has finite colimits, and its subobjects of any object form a Heyting algebra.
Example: $\mathbf{Set}$ is a topos: it has finite limits, the exponential $B^A$ is the set of functions $A \to B$, and $\set{0, 1}$ classifies subsets.
Example: for a group $G$, the category of $G$-sets is a topos with $\Omega = \set{0, 1}$ and trivial action.
Non-example: the category of real vector spaces fails clause 3.
Its terminal object is $0$, so the pullback of $\top$ along $\chi \colon X \to \Omega$ is $\ker \chi$.
If $\chi \colon \R \to \Omega$ classifies the zero subspace, then $\chi$ is injective, so $2\chi \ne \chi$, yet $\ker(2\chi) = 0$ too, and uniqueness fails.
Non-example: the category $\mathbf{Top}$ of topological spaces has finite limits but is not Cartesian closed, so it fails clause 2.
