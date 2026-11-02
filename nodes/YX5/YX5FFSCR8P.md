---
tag: YX5FFSCR8P
kind: example
name: Exceptional Lie group G2
msc: ["22E15", "17B25", "22C05"]
instance_of: [AM7YJP8AR6]
uses: [1HRMT3DSX2, 0CGYNDCWRR, CZCWFPNS4N]
sources:
  - url: https://en.wikipedia.org/wiki/G2_(mathematics)
---

## Example

Let $\mathbb{O}$ be the [[octonions|1HRMT3DSX2]], the $8$-dimensional real normed division algebra.
The compact Lie group $G_2$ is the automorphism group of $\mathbb{O}$:
$$G_2 = \set{g \in GL(\mathbb{O}) : g(xy) = g(x)\, g(y) \text{ for all } x, y \in \mathbb{O}}.$$
It is a closed subgroup of $GL_8(\R)$, since it is cut out by polynomial equations, so it is a Lie group.
Each $g \in G_2$ fixes $1$ and preserves the octonion norm, so it maps the $7$-dimensional space $\operatorname{Im} \mathbb{O}$ of imaginary octonions to itself by a rotation.
This makes $G_2$ a closed subgroup of [[SO(7)|0CGYNDCWRR]], hence compact.

$G_2$ is a connected and simply connected [[simple Lie group|AM7YJP8AR6]] of dimension $14$ and rank $2$, with trivial centre.

## Remarks

$G_2$ is the smallest of the five exceptional compact simple Lie groups $G_2, F_4, E_6, E_7, E_8$.
Its Dynkin diagram has two nodes joined by a triple edge, and its root system has $12$ roots, of two lengths whose squares have ratio $3$.
It acts transitively on the unit sphere $S^6$ of $\operatorname{Im} \mathbb{O}$, with stabilizer isomorphic to [[SU(3)|CZCWFPNS4N]], so $G_2 / SU(3) \cong S^6$.
The name $G_2$ also denotes the complex simple Lie group of the same type and its noncompact split real form.
Riemannian $7$-manifolds whose holonomy group lies in $G_2$ are called $G_2$-manifolds.

## Explanations

### L1 human

The classical Lie groups come in infinite families of matrix groups, while $G_2$ is one of five exceptional groups outside those families.
It is the symmetry group of the octonions, the largest of the four normed division algebras.
It has dimension $14$, so a symmetry of the octonions is fixed by $14$ real parameters.
Every such symmetry is a rotation of the $7$ imaginary directions, but most rotations of those directions do not respect octonion multiplication.
