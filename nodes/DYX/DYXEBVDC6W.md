---
tag: DYXEBVDC6W
kind: statement
role: theorem
name: Levi–Malcev decomposition
msc: ["22E15", 17B05]
uses: [7JBRGCVJRB, 9CNSVFQ801, XJS07AJ50Y, Y1YPE6PM52]
about: [7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Levi_decomposition
---

## Statement

Let $G$ be a connected and simply connected real [[Lie group|7JBRGCVJRB]] with Lie algebra $\mathfrak{g}$.
Let $\mathfrak{r}$ be the radical of $\mathfrak{g}$, its largest solvable ideal, and let $R$ be the connected Lie subgroup of $G$ with Lie algebra $\mathfrak{r}$.
Then the following hold.

1. The subgroup $R$ is closed, normal, simply connected and [[solvable|9CNSVFQ801]].
2. There is a closed, simply connected, [[semisimple|XJS07AJ50Y]] Lie subgroup $S$ of $G$ such that $G = R \rtimes S$, that is, $G = RS$ and $R \cap S = \set{e}$.
3. If $S'$ is a second subgroup as in 2, then $S' = x S x^{-1}$ for some $x \in R$.

A subgroup $S$ as in 2 is a *Levi subgroup* of $G$.

## Remarks

The proof starts from the Levi decomposition of the Lie algebra, $\mathfrak{g} = \mathfrak{r} \rtimes \mathfrak{s}$ with $\mathfrak{s}$ a semisimple subalgebra.
The quotient $G/R$ is simply connected with Lie algebra $\mathfrak{s}$, so the connected subgroup $S$ with Lie algebra $\mathfrak{s}$ maps isomorphically onto $G/R$.
Thus $S$ is the image of a continuous section of $G \to G/R$, which gives 2.
Part 3 comes from Malcev's theorem that two Levi subalgebras are conjugate by $\exp(\operatorname{ad} z)$ for some $z$ in $\mathfrak{r}$; then $x = \exp z$ works.

Example: the group $G$ of affine maps $v \mapsto Av + b$ of $\R^2$ with $A \in \mathrm{SL}_2(\R)$ has radical the translations $R \cong \R^2$ and Levi subgroup $\mathrm{SL}_2(\R)$.
This $G$ is not simply connected; its [[universal cover|Y1YPE6PM52]] is $\R^2 \rtimes \widetilde{\mathrm{SL}}_2(\R)$.

Simple connectedness is needed for 2.
For a general connected Lie group, a Levi subgroup $S$ still exists and $G = RS$, but $R \cap S$ need not be trivial, and $S$ need not be closed.

## Explanations

### L1 human

Every connected Lie group is built from two kinds of pieces.
One piece is solvable, close to a group of upper triangular matrices.
The other piece is semisimple, like a group of rotations or $\mathrm{SL}_n$.
The theorem says that, for simply connected groups, the group is exactly a twisted product of one piece of each kind.

### L2 human

The decomposition reduces many questions about Lie groups to two separate theories.
Solvable groups are studied by induction on dimension, using Lie's theorem and the structure of nilpotent groups.
Semisimple groups are studied with root systems, the Cartan and Iwasawa decompositions, and Weyl groups.
The Lie algebra version is due to Levi, and the conjugacy statement to Malcev.
