---
tag: YE87R5CDJY
kind: statement
role: theorem
name: Bieberbach theorems
msc: [20H15, 52C22]
uses: [7KTJKFQT2N, 0H3YY8CPKH, 087VJM5Q77, 0WJX8MGG37, 0CB0DX5BVV, 0DTXBQPA2S, 08MG7H8JW5, 0JF0TVYGWT]
about: [7KTJKFQT2N]
sources:
  - url: https://en.wikipedia.org/wiki/Space_group
---

## Statement

Let $n \ge 1$, and let crystallographic groups be as in [[crystallographic group|7KTJKFQT2N]].

1. Let $\Gamma$ be a crystallographic group of dimension $n$ and let $T$ be the subgroup of [[translations|087VJM5Q77]] in $\Gamma$. Then $T$ is a [[free abelian group|0WJX8MGG37]] of rank $n$ whose elements span $\R^n$, and $T$ is a [[normal subgroup|0CB0DX5BVV]] of finite [[index|0DTXBQPA2S]] in $\Gamma$.
2. Let $\Gamma_1$ and $\Gamma_2$ be crystallographic groups of dimension $n$. If $\Gamma_1$ and $\Gamma_2$ are [[isomorphic|08MG7H8JW5]] as abstract groups, then there is a bijective [[affine map|0JF0TVYGWT]] $\alpha \colon \R^n \to \R^n$ with $\Gamma_2 = \alpha \Gamma_1 \alpha^{-1}$.
3. For each $n$, there are only finitely many crystallographic groups of dimension $n$ up to isomorphism.

## Remarks

The proof of part 1 uses a commutator estimate.
If two isometries have linear parts close to the identity, their commutator has a linear part closer still.
Discreteness then forces enough elements to be pure translations.
Part 3 follows from part 1, because the finite quotient $\Gamma / T$ acts faithfully on $T \cong \Z^n$.
There are finitely many finite subgroups of $\mathrm{GL}_n(\Z)$ up to conjugacy, and each gives finitely many extensions.

Example: in dimension $1$ there are two crystallographic groups up to isomorphism.
They are the translations $x \mapsto x + k$ with $k \in \Z$, and the infinite dihedral group of all maps $x \mapsto \pm x + k$ with $k \in \Z$.
In both, the translation subgroup is $\Z$, of index $1$ and $2$.

The compactness of the quotient is necessary.
The translations $(x, y) \mapsto (x + k, y)$ with $k \in \Z$ form a discrete group of isometries of $\R^2$ whose translations span only a line.

## Explanations

### L1 human

Every crystal pattern in $n$-dimensional space repeats along $n$ independent directions.
Its symmetry group is mostly made of translations, with only finitely many kinds of extra rotations and reflections on top.
Two such symmetry groups that look the same as abstract groups really are the same, after a change of coordinates.
And in each dimension the list of possible crystal symmetry groups is finite.

### L2 human

Part 3 is the reason why there are exactly $17$ [[wallpaper groups|MY3CBHARYQ]] in the plane and $219$ space groups in dimension $3$ up to affine conjugacy.
A torsion-free crystallographic group acts freely on $\R^n$, and its quotient is a compact flat Riemannian manifold.
So the theorems say that each compact flat manifold is finitely covered by a torus, and that there are finitely many of them in each dimension up to affine equivalence.
The argument behind part 1 is close to the proof of the [[Jordan–Schur theorem|XT6EEXPD4P]] on finite groups of matrices.
