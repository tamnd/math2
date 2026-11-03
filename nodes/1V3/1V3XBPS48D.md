---
tag: 1V3XBPS48D
kind: statement
role: theorem
name: K0 of a Dedekind domain
msc: [19A49, 13F05, 11R29]
uses: [7NPY2CN5KB, Q14JS2MA1C, HQA9YHDSH5, 1WTNGZ5T5A, WQ46BD3ARY]
about: [Q14JS2MA1C, WQ46BD3ARY]
sources:
  - url: https://en.wikipedia.org/wiki/Ideal_class_group
---

## Statement

Let $R$ be a [[Dedekind domain|7NPY2CN5KB]] with [[ideal class group|WQ46BD3ARY]] $\mathrm{Cl}(R)$.

1. Every [[finitely generated projective|HQA9YHDSH5]] $R$-module $P$ of [[rank|1WTNGZ5T5A]] $n \ge 1$ is isomorphic to $R^{n-1} \oplus I$ for some nonzero ideal $I$ of $R$.
2. For nonzero ideals $I$, $J$ and $n \ge 1$, $R^{n-1} \oplus I \cong R^{n-1} \oplus J$ exactly when $I$ and $J$ have the same class in $\mathrm{Cl}(R)$.
3. The map sending $[P]$ to $(n, \text{class of } I)$ for $P \cong R^{n-1} \oplus I$ as in 1, and $[0]$ to $(0, 0)$, extends to a group isomorphism $K_0(R) \cong \Z \oplus \mathrm{Cl}(R)$.
In particular $\tilde{K}_0(R) \cong \mathrm{Cl}(R)$.

## Remarks

The proof rests on two facts.
First, a finitely generated torsion-free module over a Dedekind domain is a direct sum of nonzero ideals, and each nonzero ideal is projective.
Second, for nonzero ideals $I$ and $J$ there is an isomorphism $I \oplus J \cong R \oplus IJ$.
Together they reduce every $P$ to the form $R^{n-1} \oplus I$, and the class of $I$ is recovered as the class of the top exterior power $\Lambda^n P \cong I$.
In $K_0(R)$ this gives $[I] + [J] = [R] + [IJ]$, which turns multiplication of ideal classes into addition.

Example: let $R = \Z[\sqrt{-5}]$, whose class group has order $2$, and $I = (2, 1 + \sqrt{-5})$.
The ideal $I$ is not principal, so $I$ is a projective module of rank $1$ that is not free.
Its class in $\tilde{K}_0(R)$ is nonzero, so $I$ is not even stably free.
Still $I \oplus I \cong R \oplus I^2 \cong R^2$ is free, because $I^2 = (2)$ is principal.

For a principal ideal domain, such as $\Z$, the class group is trivial and $K_0(R) \cong \Z$.

## Explanations

### L1 human

Over the integers every finitely generated projective module is free, so $K_0(\Z)$ only records the rank.
Over a Dedekind domain, such as a ring of integers in a number field, some ideals are not principal, and they give projective modules that are not free.
The theorem says that these ideals are the only source of non-freeness.
So $K_0$ of a Dedekind domain is the rank plus the ideal class group.

### L2 human

This is the basic link between algebraic K-theory and algebraic number theory.
The reduced group $\tilde{K}_0(\mathcal{O}_K)$ of the ring of integers of a number field $K$ is the class group, a finite group whose order is the class number.
The determinant $\det P = \Lambda^n P$ gives the map to the class group, which is the [[Picard group|3Z9DCWYXQZ]] of $R$.
Part 1 is often called Steinitz's theorem; it is also a case of [[Serre's splitting theorem|FH0VE9PQXJ]], since a Dedekind domain has dimension at most $1$.
