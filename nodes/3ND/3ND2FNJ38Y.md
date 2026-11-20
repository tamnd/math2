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

Let $V$ be a vector space of finite dimension $n$ over a field $F$, and let $B$ be a [[bilinear form|0P799D6AMN]] on $V$.
Let $A$ be the matrix of $B$ in a basis, and let $L_B(u) = B(u, \cdot)$ and $R_B(v) = B(\cdot, v)$ be the maps $V \to V^*$.

1. The [[left radical|0KAN330PAH]] $\ker L_B$ and the right radical $\ker R_B$ both have dimension $n - \rank A$.
2. The following are equivalent:
   (a) $B$ is nondegenerate, that is, the left radical is $\{0\}$;
   (b) the right radical is $\{0\}$;
   (c) $A$ is invertible;
   (d) $L_B \colon V \to V^*$ is an isomorphism;
   (e) $R_B \colon V \to V^*$ is an isomorphism.
3. Let $W$ be a second space of finite dimension, and let $C \colon V \times W \to F$ be bilinear. If $v \mapsto C(v, \cdot)$ is injective on $V$ and $w \mapsto C(\cdot, w)$ is injective on $W$, then $\dim V = \dim W$ and both maps are isomorphisms onto the duals.

The [[proof|WCKDVAZMR2]] applies the rank-nullity theorem to the matrices $A^T$ and $A$.

## Remarks

### Why each hypothesis is needed

- Finite dimension is needed. On the space $V$ of finite sequences with basis $e_0, e_1, \dots$, let $B(e_i, e_{i + 1}) = 1$ and $B(e_i, e_j) = 0$ otherwise. Then the left radical is $\{0\}$, but $e_0$ lies in the right radical.
- In part 3 both injectivity conditions are needed. The pairing $F \times F^2 \to F$, $(a, w) \mapsto a w_1$, is injective on $F$, but $(0, 1)$ pairs to zero with all of $F$.

### Consequences

- The [[rank of a form|0SPYAGE7T0]] measures its degeneracy: $B$ is nondegenerate exactly when $\rank B = \dim V$.
- A nondegenerate form identifies $V$ with $V^*$. Each linear form is $B(u, \cdot)$ for exactly one $u$.
- The dimension formula $\dim W + \dim W^\perp = \dim V$ for [[orthogonal complements|M2JH84VEY9]] uses part 2.

### Converse

Each of the five conditions in part 2 implies the others, so the converse of each implication holds.
The converse of part 3 holds as well: if both maps are isomorphisms, both are injective.

### Generalizations

Over a commutative ring $R$ and a free module of finite rank, $L_B$ is an isomorphism exactly when $\det A$ is a unit of $R$.
For a [[sesquilinear form|054YEQ0Y8M]] the same criteria hold, with conjugate-linear maps into the dual.

## Explanations

### L1 human

There are several ways to test whether a form sees every nonzero vector.
We can look for an invisible vector, which pairs to zero with everything.
We can compute the determinant of the matrix of the form.
The statement says that all tests agree.

### L2 human

We test $B(x, y) = x^T A y$ on $\Q^2$ with $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$.

1. $\det A = 3 \neq 0$, so $A$ is invertible, and condition (c) holds.
2. By part 2, $B$ is nondegenerate, and both radicals are zero.
3. We check (d) directly: $L_B(e_1) = e_1^* + 2e_2^*$ and $L_B(e_2) = 3e_2^*$. These two linear forms are a basis of $V^*$.
4. So each linear form, for example $e_2^*$, is $L_B(u)$ for one $u$. Here $u = \frac13 e_2$.

The typical use is the matrix test (c), since a determinant is easy to compute.
A trap: the left and right radicals have the same dimension, but they can be different subspaces when $B$ is not reflexive.

### L3 human

The proof shows that the left and right radicals are the kernels of a linear map and of its dual map, which explains why they have the same dimension.
Part 3 is the finite-dimensional case of a perfect pairing, which appears in Poincaré duality, in Pontryagin duality and in the duality theory of algebraic groups.
In infinite dimension the right notion depends on a topology, and continuous dual spaces replace algebraic ones.
