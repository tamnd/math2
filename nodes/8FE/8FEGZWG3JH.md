---
tag: 8FEGZWG3JH
kind: definition
name: Fusion category
msc: [18M20, 18M10]
defines: D7NA6T33A7
uses: [M3MSQ3NKAE, A10WW8GEKR, Y9CZ3MTNF1, 04C5ZBG1WT, WYGRXCG2RN]
sources:
  - url: https://en.wikipedia.org/wiki/Fusion_category
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]].
A *fusion category* over $k$ is a [[monoidal category|M3MSQ3NKAE]] $(\mathcal{C}, \otimes, I)$ such that:

1. $\mathcal{C}$ is $k$-linear: every $\Hom(A, B)$ is a $k$-vector space, composition is $k$-bilinear, and $\otimes$ is $k$-bilinear on morphisms;
2. every $\Hom(A, B)$ is finite-dimensional;
3. $\mathcal{C}$ is semisimple: it is an [[abelian category|Y9CZ3MTNF1]] in which every object is a finite direct sum of simple objects;
4. $\mathcal{C}$ has only finitely many isomorphism classes of simple objects;
5. $\mathcal{C}$ is [[rigid|A10WW8GEKR]];
6. the unit object $I$ is simple.

Here an object is simple if it is nonzero and has no subobjects other than $0$ and itself.
Many authors assume that $k$ is algebraically closed.

## Remarks

Example: for a finite group $G$, the category $\mathrm{Rep}(G)$ of finite-dimensional complex [[representations|WYGRXCG2RN]] of $G$ is a fusion category over $\C$.
It is semisimple by Maschke's theorem, has finitely many irreducible representations up to isomorphism, the dual of a representation gives rigidity, and the trivial representation is simple.
Non-example: the category of finite-dimensional complex representations of the group $\Z$ satisfies clauses 1, 2, 5 and 6.
It is not semisimple, and it has infinitely many simple objects, one for each $\lambda \in \C^\times$.
Non-example: for a field $k$ of characteristic $p$ and a group $G$ of order divisible by $p$, $\mathrm{Rep}_k(G)$ fails clause 3 by the failure of Maschke's theorem.
If $X_1, \ldots, X_n$ are the simple objects, the fusion rules are the integers $N_{ij}^m$ with $X_i \otimes X_j \cong \bigoplus_m N_{ij}^m X_m$.
