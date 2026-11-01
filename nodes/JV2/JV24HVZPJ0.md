---
tag: JV24HVZPJ0
kind: statement
role: lemma
name: Lindström–Gessel–Viennot lemma
msc: [05A15, 05C38, 15A15]
uses: [0KFYGSHHF5, 03NAMV1DHJ, 00KDZRW4C0, 02DKV69ZH0, 0310REJJY8]
about: [0KFYGSHHF5, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Lindstr%C3%B6m%E2%80%93Gessel%E2%80%93Viennot_lemma
same_as:
  wikidata: Q6552939
  wikipedia: Lindström–Gessel–Viennot lemma
---

## Statement

Let $G$ be a finite acyclic [[directed graph|0KFYGSHHF5]] whose edges carry weights in a [[commutative ring|0310REJJY8]].
The weight $\omega(P)$ of a directed [[path|03NAMV1DHJ]] $P$ is the product of the weights of its edges.
For vertices $a, b$, let $e(a, b) = \sum_P \omega(P)$, the sum over all paths $P$ from $a$ to $b$.
Let $a_1, \dots, a_n$ and $b_1, \dots, b_n$ be vertices of $G$ and let $M$ be the $n \times n$ matrix with entries $M_{ij} = e(a_i, b_j)$.
Let $\mathcal{F}$ be the set of all tuples $(\sigma, P_1, \dots, P_n)$, where $\sigma$ is a permutation of $\set{1, \dots, n}$ and $P_1, \dots, P_n$ are pairwise vertex-disjoint paths.
Here $P_i$ goes from $a_i$ to $b_{\sigma(i)}$ for each $i$.
Then
$$\det M = \sum_{(\sigma, P_1, \dots, P_n) \in \mathcal{F}} \sgn(\sigma) \prod_{i=1}^{n} \omega(P_i).$$

## Remarks

Expand the [[determinant|00KDZRW4C0]] by the Leibniz formula: it is a signed sum over all families of paths $P_i$ from $a_i$ to $b_{\sigma(i)}$, disjoint or not.
On the families that meet, define an involution as follows.
Take the smallest $i$ such that $P_i$ meets another path, and the first vertex $v$ on $P_i$ that lies on another path.
Take the smallest $j \ne i$ with $v \in P_j$, and swap the parts of $P_i$ and $P_j$ after $v$.
The involution keeps the product of weights and changes the [[sign|02DKV69ZH0]] of $\sigma$, so these terms cancel.

Often the vertices are placed so that only $\sigma = \id$ admits disjoint paths.
Then $\det M$ is the weighted number of families of disjoint paths from $a_i$ to $b_i$.

Example: in the grid $\Z^2$ with unit steps to the east and to the north and all weights $1$, take $a_1 = (0, 1)$, $a_2 = (1, 0)$, $b_1 = (1, 2)$, $b_2 = (2, 1)$.
The path counts are binomial coefficients, $M = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, and $\det M = 3$.
Of the $4$ pairs of paths $a_1 \to b_1$, $a_2 \to b_2$, exactly one meets (both pass through $(1, 1)$), and no disjoint pair goes $a_1 \to b_2$, $a_2 \to b_1$; so there are $3$ disjoint pairs.

## Explanations

### L1 human

Counting families of paths that never touch each other is hard to do directly.
The lemma says that a determinant does it for you: the entries count single paths, and the signs in the determinant cancel every family in which paths touch.
The trick is to swap the tails of two touching paths at their first meeting point.

### L2 human

The lemma is a standard way to turn a determinant into a count, or a count into a determinant.
It proves the Jacobi–Trudi formula for Schur functions, where semistandard tableaux become families of disjoint lattice paths.
It also counts plane partitions in a box and rhombus tilings of hexagons.
It is due to Lindström, and Gessel and Viennot brought it into enumerative combinatorics.
