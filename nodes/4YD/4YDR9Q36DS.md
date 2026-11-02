---
tag: 4YDR9Q36DS
kind: statement
role: theorem
name: Iwasawa decomposition of a Lie group
msc: ["22E46", "22E15"]
uses: [XJS07AJ50Y, A5JB9JQKR0, DK87YN458D, H3QX1ZFC8K]
about: [XJS07AJ50Y]
sources:
  - url: https://en.wikipedia.org/wiki/Iwasawa_decomposition
same_as:
  wikidata: Q750099
  wikipedia: Iwasawa decomposition
---

## Statement

Let $G$ be a connected [[semisimple Lie group|XJS07AJ50Y]] with finite center and Lie algebra $\mathfrak{g}$.
Let $\mathfrak{g} = \mathfrak{k} \oplus \mathfrak{p}$ be the Cartan decomposition for a Cartan involution, as in the [[Cartan decomposition|A5JB9JQKR0]].
Let $K$ be the connected subgroup with Lie algebra $\mathfrak{k}$.
Let $\mathfrak{a} \subseteq \mathfrak{p}$ be a maximal abelian subspace.
For a linear form $\lambda \ne 0$ on $\mathfrak{a}$, put $\mathfrak{g}_\lambda = \set{X \in \mathfrak{g} : [H, X] = \lambda(H) X \text{ for all } H \in \mathfrak{a}}$, and let $\Sigma$ be the set of $\lambda$ with $\mathfrak{g}_\lambda \ne 0$, the restricted roots.
Fix $H_0 \in \mathfrak{a}$ with $\lambda(H_0) \ne 0$ for all $\lambda \in \Sigma$, put $\Sigma^+ = \set{\lambda \in \Sigma : \lambda(H_0) > 0}$ and $\mathfrak{n} = \bigoplus_{\lambda \in \Sigma^+} \mathfrak{g}_\lambda$.
Let $A$ and $N$ be the connected subgroups of $G$ with Lie algebras $\mathfrak{a}$ and $\mathfrak{n}$.
Then $A$ is abelian, $N$ is [[nilpotent|DK87YN458D]], both are closed and simply connected, and the map
$$K \times A \times N \to G, \quad (k, a, n) \mapsto kan,$$
is a diffeomorphism.

## Remarks

On the Lie algebra level, $\mathfrak{g} = \mathfrak{k} \oplus \mathfrak{a} \oplus \mathfrak{n}$ as vector spaces; this follows from the restricted root space decomposition and the fact that $\theta$ maps $\mathfrak{g}_\lambda$ to $\mathfrak{g}_{-\lambda}$.
One then shows that $AN$ is a closed simply connected solvable subgroup, and that $K \times AN \to G$ is a bijective local diffeomorphism.

Example: $G = \mathrm{SL}_n(\R)$ with $K = \mathrm{SO}(n)$.
Here $A$ is the group of diagonal matrices with positive entries and determinant $1$, and $N$ is the group of upper triangular matrices with $1$ on the diagonal.
The decomposition $g = kan$ is the Gram–Schmidt process applied to the columns of $g$, also known as the QR decomposition.

## Explanations

### L1 human

Every element of a semisimple Lie group is, in exactly one way, a rotation times a scaling times a shear.
For matrices, the scaling is a positive diagonal matrix and the shear is an upper triangular matrix with ones on the diagonal.
This is what Gram–Schmidt orthogonalisation does to the columns of an invertible matrix.

### L2 human

The Iwasawa decomposition shows that $G/K$ is diffeomorphic to the solvable group $AN$.
So the symmetric space $G/K$ is a solvable Lie group with a left-invariant metric.
The subgroup $MAN$, with $M$ the centralizer of $\mathfrak{a}$ in $K$, is the minimal parabolic subgroup.
Inducing to $G$ the representations of $MAN$ that are trivial on $N$ gives the principal series representations.
The dimension of $\mathfrak{a}$ is the real rank of $G$.
