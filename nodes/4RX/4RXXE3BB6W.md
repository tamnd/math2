---
tag: 4RXXE3BB6W
kind: statement
role: theorem
name: Harish-Chandra embedding
msc: [32M15, "22E46"]
uses: [NT4797Z9H8, Y7Q2SNKG0C, 7JBRGCVJRB, DRYYK2WX0M]
about: [NT4797Z9H8, Y7Q2SNKG0C]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_symmetric_space
---

## Statement

Let $G$ be a connected noncompact simple real Lie group, contained in its simply connected [[complexification|DRYYK2WX0M]] $G_\C$.
Let $K \subset G$ be a maximal compact subgroup such that $X = G/K$ is a [[Hermitian symmetric space|NT4797Z9H8]].
Let $\mathfrak{g} = \mathfrak{k} \oplus \mathfrak{p}$ be the Cartan decomposition, and let $\mathfrak{p}_\C = \mathfrak{p}^+ \oplus \mathfrak{p}^-$ be the splitting into the $\pm i$ eigenspaces of the complex structure.
Put $P^\pm = \exp \mathfrak{p}^\pm$, and let $K_\C$ be the complexification of $K$ in $G_\C$.
Then:

1. Every $g \in G$ can be written uniquely as $g = p^+ k p^-$ with $p^\pm \in P^\pm$ and $k \in K_\C$.
2. The map $\zeta \colon X \to \mathfrak{p}^+$, $gK \mapsto \log p^+$, is a holomorphic embedding onto a bounded domain in the complex vector space $\mathfrak{p}^+ \cong \C^n$, where $n = \dim_\C X$.

## Remarks

The image is a [[bounded symmetric domain|Y7Q2SNKG0C]], the Harish-Chandra realization of $X$, and it is convex and circled.
The map extends to the Borel embedding of $X$ as an open subset of the compact dual $G_\C / K_\C P^-$.
In this picture $\zeta$ is the restriction of an affine chart $P^+ \cong \mathfrak{p}^+$ of the compact dual.
The same holds for semisimple $G$ by taking products.

Example: for $G = SU(1, 1)$ and $K = U(1)$ the Harish-Chandra realization of $G/K$ is the unit disc.
For $G = Sp(2n, \R)$ and $K = U(n)$, the space $G/K$ is the [[Siegel upper half-space|5PTYE97PF6]] $\mathbb{H}_n$, and the realization is the domain $\set{W : W^T = W,\ I - W^* W > 0}$, reached by the Cayley transform $Z \mapsto (Z - iI)(Z + iI)^{-1}$.

## Explanations

### L1 human

A Hermitian symmetric space of noncompact type is first defined abstractly, as a quotient of a Lie group.
The theorem says that it can always be drawn as a bounded region in $\C^n$.
So abstract symmetric spaces and concrete bounded symmetric domains are the same objects.

### L2 human

Together with the fact that bounded symmetric domains with the Bergman metric are Hermitian symmetric, this gives an equivalence between the two notions.
The embedding is the tool behind holomorphic discrete series representations and the analysis of automorphic forms on $G/K$.
It also explains why $X$ sits as an open subset inside its compact dual, as the disc sits inside the Riemann sphere.
