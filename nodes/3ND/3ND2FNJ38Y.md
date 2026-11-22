---
tag: 3ND2FNJ38Y
kind: statement
role: proposition
name: Criteria for a nondegenerate bilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
about: [01NHFZF2SK]
uses: [0KAN330PAH, ZVMJAF7D53, 0W4FSW1TVB, 0TZAG60ZYT, 00889YD15K, ACDFDABVQK]
sources:
  - url: https://en.wikipedia.org/wiki/Degenerate_bilinear_form
    locator: Nondegenerate forms
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Non-degenerate bilinear forms
---

## Statement

In finite dimension, five tests for nondegeneracy of a bilinear form agree, and the two radicals of any bilinear form have the same dimension.

Let $V$ be a vector space of finite dimension $n$ over a field $F$, and let $B$ be a [[bilinear form|0P799D6AMN]] on $V$.
Let $A$ be the matrix of $B$ in a basis of $V$.
Let $L_B, R_B \colon V \to V^*$ be the linear maps $L_B(u) = B(u, \cdot)$ and $R_B(v) = B(\cdot, v)$.

1. The [[left radical|0KAN330PAH]] $\ker L_B$ and the right radical $\ker R_B$ both have dimension $n - \operatorname{rank} A$.
2. The following five conditions are equivalent.

- (a) $B$ is nondegenerate, that is, the left radical is $\{0\}$.
- (b) The right radical is $\{0\}$.
- (c) The matrix $A$ is invertible.
- (d) The map $L_B \colon V \to V^*$ is an isomorphism.
- (e) The map $R_B \colon V \to V^*$ is an isomorphism.

3. Let $W$ be a second vector space of finite dimension over $F$, and let $C \colon V \times W \to F$ be bilinear. If the map $v \mapsto C(v, \cdot)$ from $V$ to $W^*$ and the map $w \mapsto C(\cdot, w)$ from $W$ to $V^*$ are both injective, then $\dim V = \dim W$ and both maps are isomorphisms.

The [[proof|WCKDVAZMR2]] applies the rank-nullity theorem to the matrices $A^{\mathsf{T}}$ and $A$.

## Remarks

### Why finite dimension is needed

Without finite dimension, the left and the right radical need not agree even in size.
Let $V$ be the space of finite sequences, with basis $e_0, e_1, e_2, \dots$, and define $B$ on the basis by $B(e_i, e_{i+1}) = 1$ and $B(e_i, e_j) = 0$ for all other pairs.
For $u = \sum_i x_i e_i$, the value $B(u, e_j)$ is $x_{j-1}$ for $j \ge 1$, so $B(u, \cdot) = 0$ forces every $x_i = 0$, and the left radical is $\{0\}$.
For $v = \sum_j y_j e_j$, the value $B(e_i, v)$ is $y_{i+1}$, and this never involves $y_0$.
So $e_0$ lies in the right radical, and condition (a) holds while (b) fails.

### Why both maps are needed in part 3

Injectivity on one side alone does not force equal dimensions.
The pairing $C \colon F \times F^2 \to F$, $C(a, w) = a w_1$, gives an injective map on $F$, because $a w_1 = 0$ for all $w$ forces $a = 0$.
But $w = (0, 1)$ pairs to zero with every $a$, so the map on $F^2$ is not injective, and indeed $\dim F = 1 \ne 2 = \dim F^2$.

### What it gives you

The matrix test (c) is the one you compute: one determinant decides nondegeneracy, and a change of basis $A \mapsto P^{\mathsf{T}} A P$ multiplies it by $(\det P)^2 \ne 0$, so the answer does not depend on the basis.
Part 1 says that the [[rank of the form|0SPYAGE7T0]] measures exactly how degenerate it is: $B$ is nondegenerate exactly when $\operatorname{rank} B = n$.
Condition (d) says that each linear form on $V$ is $B(u, \cdot)$ for exactly one $u$.
For example, with $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ on $\mathbb{Q}^2$, the coordinate form $e_2^*$ equals $L_B(u)$ for $u = \tfrac{1}{3} e_2$, since $B(e_2, y) = 3y_2$.
The [[dimension statement for orthogonal complements|M2JH84VEY9]] rests on condition (e).

### The converse and the generalizations

Each condition of part 2 implies each other one, so every converse in part 2 holds.
The converse of part 3 holds as well, since an isomorphism is injective.

Over a commutative ring $R$ and a free module of finite rank, $L_B$ is an isomorphism exactly when $\det A$ is a unit of $R$.
Here injectivity is weaker: the form $B(x, y) = 2xy$ on $\mathbb{Z}$ has $L_B$ injective but not surjective.
For a [[sesquilinear form|054YEQ0Y8M]] over $\mathbb{C}$ the same criteria hold, with the map $v \mapsto B(\cdot, v)$ now conjugate-linear.

## Explanations

### L1 human

There are several ways to test whether a form sees every nonzero vector.
You can look for an invisible vector that pairs to zero with everything, once from the left and once from the right.
You can also compute the determinant of the matrix of the form.
The statement says that in a finite-dimensional space all these tests give the same answer.
So for $x_1 y_1 + x_2 y_2$ on the plane, the determinant $1$ already tells you that no invisible vector exists.

### L2 human

We test $B(x, y) = x^{\mathsf{T}} A y$ on $\mathbb{Q}^2$ with $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$.
The determinant is $1 \cdot 3 - 2 \cdot 0 = 3 \ne 0$, so condition (c) holds, and by part 2 both radicals are zero.
We check condition (d) directly.
The row $i$ of $A$ lists the values $B(e_i, e_1), B(e_i, e_2)$, so
$$L_B(e_1) = e_1^* + 2e_2^*, \qquad L_B(e_2) = 3e_2^*.$$
These two linear forms are independent, so they are a basis of the $2$-dimensional space $V^*$, and $L_B$ is an isomorphism.
The matrix test needed one multiplication, while the direct check needed a basis of $V^*$, which is why (c) is the test used in practice.
Watch out: the two radicals have the same dimension, but for a form that is not reflexive they can be different subspaces.

### L3 human

The proof shows that $R_B$ is the dual map of $L_B$, once $V$ is identified with $V^{**}$.
So the left and right radicals are the kernels of a linear map and of its dual, and the equality of their dimensions is the equality of row rank and column rank.
Part 3 is the finite-dimensional case of a perfect pairing, an idea that returns in Poincaré duality in topology and in Pontryagin duality for abelian groups.
In infinite dimension the algebraic dual is too large, and a topology and the continuous dual take its place.
