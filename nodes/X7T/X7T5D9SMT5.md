---
tag: X7T5D9SMT5
kind: statement
role: theorem
name: Lie algebra of a compact group is reductive
msc: ["22E15", 22C05, 17B05]
uses: [9TFC6ADC1C, VY0HXD3GC4]
about: [9TFC6ADC1C]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_Lie_algebra
---

## Statement

Let $G$ be a [[compact Lie group|9TFC6ADC1C]], and let $\mathfrak{g}$ be its [[Lie algebra|WKVBS76432]], with center $\mathfrak{z}$ and [[Killing form|TWVQT18JXE]] $B$.
Then:

1. $\mathfrak{g}$ is a [[reductive Lie algebra|T4S70DDW0A]]: $\mathfrak{g} = \mathfrak{z} \oplus [\mathfrak{g}, \mathfrak{g}]$ as Lie algebras, and $[\mathfrak{g}, \mathfrak{g}]$ is [[semisimple|EY9DN7QAX1]];
2. $B(X, X) \le 0$ for all $X \in \mathfrak{g}$, with equality exactly when $X \in \mathfrak{z}$.

## Remarks

The proof averages an inner product on $\mathfrak{g}$ over $G$ with the normalized [[Haar measure|VY0HXD3GC4]].
This gives an inner product invariant under $\mathrm{Ad}(G)$, so each $\operatorname{ad} X$ is skew-symmetric for it.
The orthogonal complement of an ideal is then an ideal, so $\mathfrak{g}$ is a direct sum of simple ideals and of the abelian ideal $\mathfrak{z}$.
For 2, the eigenvalues of the skew-symmetric map $\operatorname{ad} X$ are purely imaginary, so $B(X, X) = \tr\big((\operatorname{ad} X)^2\big) \le 0$, with equality only when $\operatorname{ad} X = 0$.

Example: for $G = \mathrm{U}(n)$, the Lie algebra $\mathfrak{u}(n)$ of skew-Hermitian matrices is $i\R \cdot I \oplus \mathfrak{su}(n)$, the center plus a simple ideal for $n \ge 2$.

Compactness is needed.
The group of affine maps $x \mapsto ax + b$ of $\R$ with $a > 0$ is a noncompact Lie group whose Lie algebra is solvable but not abelian, so it is not reductive.

## Explanations

### L1 human

The infinitesimal version of a compact group is very well behaved.
It splits into a commutative part and a part made of simple pieces, with no mixing between them.
The reason is that a compact group can be averaged over, which produces a symmetric inner product that the group respects.

### L2 human

The theorem is the first step of the structure theory of compact Lie groups.
A real Lie algebra with an inner product for which each $\operatorname{ad} X$ is skew-symmetric is called a compact Lie algebra.
The compact Lie algebras are exactly the reductive ones with negative semidefinite Killing form.
Conversely, each semisimple Lie algebra with negative definite Killing form is the Lie algebra of a compact Lie group, by Weyl's theorem that its simply connected group is compact.
Together with Weyl's unitary trick, this lets one move between compact groups and complex semisimple Lie algebras.
