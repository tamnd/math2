---
tag: 0SQZMXB6GP
kind: concept
name: Bilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
specializes: [0443XNARDV]
uses: [04C5ZBG1WT, 000AYPA9AJ, 0NRYHJPQG2]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Coordinate representation
  - book: isbn:9780387728285
    locator: Chapter 11
same_as:
  wikidata: Q837924
  wikipedia: Bilinear form
---

## Summary

Let $F$ be a [[field|04C5ZBG1WT]] and let $V$ be a [[vector space|000AYPA9AJ]] over $F$.
A bilinear form on $V$ is a map $B \colon V \times V \to F$ that is linear in each slot when the other slot is fixed.
So $B(au + bv, w) = aB(u, w) + bB(v, w)$ and $B(u, av + bw) = aB(u, v) + bB(u, w)$ for all $u, v, w \in V$ and $a, b \in F$.
The [[formal definition|0P799D6AMN]] states the same conditions.
Bilinear forms matter because they measure pairs of vectors: lengths, angles, areas, energies and dualities all come from them.

## Motivation

The [[dot product|0S52TNNTH9]] on $\R^n$ gives lengths and angles.
Most algebraic facts about it use only one property: it is linear in each factor.
Other useful pairings have the same property but no positivity.
The determinant $x_1 y_2 - x_2 y_1$ of two vectors in the plane gives a signed area.
The form $x_1 y_1 - x_2 y_2$ gives the geometry of special relativity in one space dimension.
The [[trace|07PTPSZPME]] $\tr(XY)$ pairs two square matrices.
A bilinear form is the common frame for all these pairings, over any field.

## Notation

- Common symbols are $B(x, y)$, $\langle x, y \rangle$, $(x, y)$ and $x \cdot y$.
- The set of bilinear forms on $V$ is written $\operatorname{Bil}(V)$ or $L^2(V; F)$ in some books.
- In Mathlib the type is `LinearMap.BilinForm R M`, which is a linear map $M \to (M \to R)$.
- A bilinear map $V \times W \to F$ on two different spaces is a bilinear pairing. Some books also call it a bilinear form.

## Remarks

### Examples

- The [[dot product|0S52TNNTH9]] $x \cdot y = \sum_k x_k y_k$ on $F^n$ is bilinear, because each term $x_k y_k$ is linear in $x$ and in $y$.
- For each $n \times n$ matrix $A$ over $F$, the map $B(x, y) = x^T A y$ on $F^n$ is bilinear, because matrix products are linear in each factor.
- The [[trace form on $2 \times 2$ matrices|CWKB533GHM]] $B(X, Y) = \tr(XY)$ is bilinear, because the product is bilinear and the trace is linear.
- The [[form with matrix $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$|N9CJZW5596]] on $\Q^2$ is bilinear but not symmetric.
- The determinant form $x_1 y_2 - x_2 y_1$ on $F^2$ is bilinear and [[alternating|0DGDS5XY84]].
- The [[trace pairing|4F7GWKTQ1H]] and the zero form $B(x, y) = 0$ are bilinear forms too.

### Non-examples

- The [[map $x_1 y_1 + x_2$ on $\R^2$|5JPJW2GJR6]] is not bilinear: it is not linear in $y$, since $y = 0$ does not give $0$.
- The map $(x, y) \mapsto \norm{x} \, \norm{y}$ on $\R^2$ is not bilinear: it is not additive in $x$, since $\norm{x} + \norm{-x} \neq \norm{0}$ for $x \neq 0$.
- The [[standard inner product on $\C^n$|TFZ8DYVJ1J]] is not bilinear over $\C$: it is conjugate-linear in the second slot, so it is a [[sesquilinear form|054YEQ0Y8M]].

### Basic properties

- $B(0, y) = 0$ and $B(x, 0) = 0$, because a linear map sends $0$ to $0$.
- The bilinear forms on $V$ form a vector space over $F$ under the pointwise sum and scalar multiple.
- If $\dim V = n$, a form is fixed by its $n^2$ values $B(e_i, e_j)$ on a [[basis|0KCQ9Y3QKA]]. These values make the [[matrix of the form|0QK6K857HS]], so the space of forms has dimension $n^2$.
- A bilinear form is the same as a linear map $V \to V^*$ into the [[dual space|07JBSZE0V4]], by the [[correspondence with linear maps into the dual|ZVMJAF7D53]].
- The main special classes are [[symmetric forms|0AXZNE5XNH]], [[alternating forms|0DGDS5XY84]] and [[nondegenerate forms|01NHFZF2SK]].

### Common errors

- A bilinear form is not a linear map on $V \times V$. For example, $B(2x, 2y) = 4B(x, y)$, not $2B(x, y)$.
- A bilinear form need not be symmetric. The order of the two slots matters for the form $x_1 y_2$.
- A bilinear form need not be positive. The form $x_1 y_1 - x_2 y_2$ gives $-1$ on the pair $((0, 1), (0, 1))$.

## Explanations

### L1 human

A bilinear form is a rule that takes two vectors and gives one number.
If we double the first vector, the number doubles.
If we double the second vector, the number also doubles.
The dot product is the main example: $(1, 2)$ and $(3, 4)$ give $1 \cdot 3 + 2 \cdot 4 = 11$.
Other rules, such as $x_1 y_2 - x_2 y_1$, measure signed areas instead of lengths.

### L2 human

We check that $B(x, y) = x_1 y_1 + 2x_1 y_2 + 3x_2 y_2$ on $\Q^2$ is a bilinear form.

1. Fix $y$. Then $B(x, y) = (y_1 + 2y_2)x_1 + 3y_2 x_2$, which is a linear function of $x$.
2. Fix $x$. Then $B(x, y) = x_1 y_1 + (2x_1 + 3x_2)y_2$, which is a linear function of $y$.
3. So $B$ is bilinear. Its matrix is $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$, and $B(x, y) = x^T A y$.
4. A sample value is $B((2, 1), (1, -1)) = 2 - 4 - 3 = -5$.

The typical use is to turn a geometric question into a matrix question with $B(x, y) = x^T A y$.
A trap: "linear in each slot" is weaker than "linear on $V \times V$".
The form above gives $B(2x, 2y) = 4B(x, y)$.

### L3 human

A bilinear form on $V$ is an element of $(V \otimes V)^*$, and so the space of forms is $V^* \otimes V^*$ when $V$ is finite-dimensional.
Equivalently it is a linear map $V \to V^*$, and this view makes nondegeneracy and orthogonal complements statements about [[duality|07JBSZE0V4]].
The group $GL(V)$ acts on forms by $(gB)(x, y) = B(g^{-1}x, g^{-1}y)$, and the classification of forms up to this action is the theory of [[congruence|WJWNYSQKK8]].
The stabilizers of special forms are the classical groups: the [[orthogonal group|0TKYAEJ8N7]] of a symmetric form and the [[symplectic group|X12FS2JAP0]] of an alternating form.
Over a ring in place of a field, bilinear forms on modules lead to lattices and to the arithmetic of [[quadratic forms|0RBQS1JJCR]].
