---
tag: MJMB7SH7SD
kind: statement
role: theorem
name: Theorem of the cube
msc: [14K05, 14C20]
uses: [HV6YBS0YDH, 7JCF2TE3V5, 9537RKBZPP, R7W03TXRS9]
about: [R7W03TXRS9, 7JCF2TE3V5]
sources:
  - url: https://en.wikipedia.org/wiki/Theorem_of_the_cube
same_as:
  wikidata: Q7782346
  wikipedia: Theorem of the cube
---

## Statement

Let $k$ be an algebraically closed field.
Let $X$ and $Y$ be complete [[varieties|HV6YBS0YDH]] over $k$, and let $Z$ be a variety over $k$.
Let $x_0 \in X$, $y_0 \in Y$ and $z_0 \in Z$ be closed points.
Let $L$ be a [[line bundle|7JCF2TE3V5]] on $X \times Y \times Z$.
Assume that the restrictions of $L$ to $\set{x_0} \times Y \times Z$, to $X \times \set{y_0} \times Z$ and to $X \times Y \times \set{z_0}$ are trivial.
Then $L$ is trivial.

## Remarks

The standard proof uses the seesaw principle, which detects triviality of a line bundle on a product from its restrictions to fibres.
It combines this with a reduction to the case where $Z$ is a curve.

Applied to an [[abelian variety|R7W03TXRS9]] $A$, the theorem gives a formula on $A \times A \times A$.
Let $p_i$ be the projections and $p_{ij} = p_i + p_j$, $p_{123} = p_1 + p_2 + p_3$ the sum maps to $A$.
For every line bundle $L$ on $A$, the line bundle
$$p_{123}^{*} L \otimes p_{12}^{*} L^{-1} \otimes p_{13}^{*} L^{-1} \otimes p_{23}^{*} L^{-1} \otimes p_1^{*} L \otimes p_2^{*} L \otimes p_3^{*} L$$
is trivial.
Let $t_x$ be translation by a point $x$ of $A$.
Pulling back along maps into $A \times A \times A$ gives the theorem of the square: $t_{x+y}^{*} L \otimes L \cong t_x^{*} L \otimes t_y^{*} L$ for all points $x, y$.
It also gives $[n]^{*} L \cong L^{(n^2 + n)/2} \otimes [-1]^{*} L^{(n^2 - n)/2}$ for multiplication by $n$.
So for a symmetric line bundle, with $[-1]^{*} L \cong L$, one gets $[n]^{*} L \cong L^{n^2}$.

## Explanations

### L1 human

A line bundle on a product of three spaces is trivial as soon as it is trivial on three coordinate "faces" through a common corner.
The name comes from this picture of a cube with three faces through one vertex.
For abelian varieties this turns into identities for line bundles under addition of points.

### L2 human

The theorem of the cube is a basic tool in the algebraic theory of abelian varieties.
The theorem of the square that follows from it gives a homomorphism $A \to \operatorname{Pic}(A)$, $x \mapsto t_x^{*} L \otimes L^{-1}$, which lands in the points of the [[dual abelian variety|HZXSESHC8P]].
For an ample $L$ this map is an isogeny, the polarization attached to $L$.
The formula $[n]^{*} L \cong L^{n^2}$ for symmetric $L$ is a key step in computing the degree of multiplication by $n$, and in the theory of heights.
