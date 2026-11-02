---
tag: S36T7TR7AG
kind: definition
name: Hereditary ring
msc: ["16E60", "16E10"]
defines: 89VBQH8HNS
uses: [0B1261B5ED, 5N2CJZ47D4, BFFA03GE3V]
sources:
  - url: https://en.wikipedia.org/wiki/Hereditary_ring
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity.
The ring $R$ is *left hereditary* if every [[left ideal|5N2CJZ47D4]] of $R$ is a [[projective module|BFFA03GE3V]] as a left $R$-module.
It is *right hereditary* if every right ideal is projective as a right $R$-module.
It is *hereditary* if it is both left and right hereditary.

## Remarks

Example: the ring $\Z$ is hereditary.
Each ideal is $n\Z$ for some $n \ge 0$; it is $0$ or isomorphic to $\Z$ through $x \mapsto x/n$, so it is free and hence projective.
Non-example: the ring $\Z/4\Z$ is not hereditary.
It is a local ring, so its projective modules are free.
The ideal $2\Z/4\Z$ has $2$ elements, while a nonzero free $\Z/4\Z$-module has at least $4$, so this ideal is not projective.
Equivalent forms: $R$ is left hereditary if and only if every submodule of a projective left $R$-module is projective.
This holds if and only if the left [[global dimension|GWA0T1WKCN]] of $R$ is at most $1$.
For a ring that is Noetherian on both sides, left and right hereditary are equivalent.
An integral domain is hereditary if and only if it is a [[Dedekind domain|7NPY2CN5KB]].
The path algebra of a finite quiver without oriented cycles over a field is hereditary.
