---
tag: N6JC6KNXJJ
kind: statement
role: theorem
name: Complete reducibility of representations of compact groups
msc: [22C05, 22D10]
uses: [EVHCE5VR6Y, VY0HXD3GC4, WYGRXCG2RN, FX3NEFYFFN, 0ACX5QT8TE, 0NB0AWGJBW]
about: [EVHCE5VR6Y, WYGRXCG2RN]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_group
---

## Statement

Let $G$ be a [[compact group|EVHCE5VR6Y]], let $V$ be a finite-dimensional complex vector space, and let $\rho \colon G \to GL(V)$ be a continuous [[representation|WYGRXCG2RN]].
Then:

1. there is an [[inner product|0NB0AWGJBW]] on $V$ such that $\ip{\rho(g)u}{\rho(g)v} = \ip{u}{v}$ for all $g \in G$ and $u, v \in V$;
2. $V$ is a direct sum $V = V_1 \oplus \cdots \oplus V_k$ of [[irreducible|FX3NEFYFFN]] subrepresentations.

## Remarks

For part 1, take any inner product $\ip{\cdot}{\cdot}_0$ on $V$ and average it with the normalised [[Haar measure|VY0HXD3GC4]]: $\ip{u}{v} = \int_G \ip{\rho(g)u}{\rho(g)v}_0 \, dg$.
Invariance of the Haar measure makes this inner product $G$-invariant, and it is positive definite because the integrand is positive when $u = v \ne 0$.
For part 2, the orthogonal complement of an [[invariant subspace|0ACX5QT8TE]] for an invariant inner product is again invariant, and induction on $\dim V$ finishes the proof.
For a finite group the Haar integral is the average over the group, and the theorem is Maschke's theorem over $\C$.
Compactness is needed: the representation of $\R$ on $\C^2$ given by $t \mapsto \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}$ has the invariant line $\C e_1$.
It has no invariant complement, since for $t \ne 0$ the only eigenvectors of the matrix are the multiples of $e_1$.
The same proof works for real representations, with a real inner product.

## Explanations

### L1 human

A representation of a compact group always breaks into irreducible pieces that do not interact.
The reason is that one can average over the group, which is possible because the group is compact.
Averaging gives a way of measuring lengths and angles that the group does not change, and then perpendicular pieces stay perpendicular.

### L2 human

The theorem reduces the study of finite-dimensional representations of compact groups to irreducible ones, which are then classified by characters through the [[Schur orthogonality relations|ETNDTECY97]].
For compact connected Lie groups, the irreducible representations are described by highest weights and the [[Weyl character formula|230F5FXPMQ]].
[[Weyl's unitary trick|DDQ2WBQ9GB]] transfers the theorem to complex semisimple Lie groups and Lie algebras, which are not compact.
The [[Peter–Weyl theorem|6VC9QE39XH]] extends the result to unitary representations on infinite-dimensional Hilbert spaces.
