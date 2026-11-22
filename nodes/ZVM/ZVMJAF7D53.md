---
tag: ZVMJAF7D53
kind: statement
role: proposition
name: Bilinear forms correspond to matrices and to linear maps into the dual
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
about: [0SQZMXB6GP, 0QK6K857HS, 07JBSZE0V4]
uses: [0P799D6AMN, 0P24YW565F, 0M856Q1AMZ, 0W6M3PSD08, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Coordinate representation
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Pairs of distinct vector spaces
---

## Statement

A bilinear form, a square matrix and a linear map into the dual space are three descriptions of the same thing.

Let $V$ be a vector space over a field $F$, and let $V^*$ be its [[dual space|0M856Q1AMZ]].
For a [[bilinear form|0P799D6AMN]] $B$ on $V$ define $L_B, R_B \colon V \to V^*$ by
$$L_B(u) = B(u, \cdot), \qquad R_B(v) = B(\cdot, v).$$

1. $L_B$ and $R_B$ are linear maps, and $B \mapsto L_B$ is a linear bijection from the space of bilinear forms on $V$ onto $\operatorname{Hom}(V, V^*)$.

Now let $V$ have a finite basis $(e_1, \dots, e_n)$ with [[dual basis|0W6M3PSD08]] $(e_1^*, \dots, e_n^*)$, and let $A$ be the [[matrix|0P24YW565F]] of $B$ in this basis.

2. If $x$ and $y$ are the coordinate vectors of $u$ and $v$, then $B(u, v) = x^{\mathsf{T}} A y$.
3. The map $B \mapsto A$ is a linear bijection from the space of bilinear forms on $V$ onto $M_n(F)$.
4. In the bases $(e_i)$ and $(e_i^*)$, the [[matrix|0YYMY95FWS]] of $L_B$ is $A^{\mathsf{T}}$ and the matrix of $R_B$ is $A$.

The [[proof|8HVW5T9CRS]] evaluates both sides on basis vectors.

## Remarks

### Why each hypothesis is needed

Part 1 needs no basis and no finite dimension: it only fixes one slot of the form.
Parts 2 to 4 need a finite basis, because a matrix has finitely many rows and columns.

Part 4 also needs the dual basis on the side of $V^*$.
In another basis of $V^*$ the map $L_B$ has a different matrix, and the clean answer $A^{\mathsf{T}}$ is lost.

Bilinearity is needed for $L_B$ to land in $V^*$ at all.
For the [[map $x_1 y_1 + x_2$|5JPJW2GJR6]], fixing $u = (0, 1)$ gives the constant function $1$ in the second slot, which is not a linear form.

### What it gives you

When $\dim V = n$, part 3 shows that the bilinear forms on $V$ form a space of dimension $n^2$.
For the form with matrix $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ on $\mathbb{Q}^2$, part 4 gives
$$L_B(e_1) = e_1^* + 2 e_2^*, \quad L_B(e_2) = 3 e_2^*, \qquad R_B(e_1) = e_1^*, \quad R_B(e_2) = 2 e_1^* + 3 e_2^*,$$
so $L_B$ has the columns $(1, 2), (0, 3)$ and $R_B$ has the columns $(1, 0), (2, 3)$, as the [[non-symmetric example|N9CJZW5596]] computes.

Three consequences follow at once.
A form is [[symmetric|0AXZNE5XNH]] exactly when $L_B = R_B$, which is exactly when $A = A^{\mathsf{T}}$.
The maps $L_B$ and $R_B$ have the same rank, because $A$ and $A^{\mathsf{T}}$ have the same [[rank|0ZC9YTXZRY]], and this common number is the rank of $B$.
The [[criteria for nondegeneracy|3ND2FNJ38Y]] follow from part 4, since $L_B$ is injective exactly when $A$ is invertible.

### The converse

The correspondences run both ways.
Each linear map $T \colon V \to V^*$ comes from exactly one form, namely $B(u, v) = T(u)(v)$.
Each matrix $A \in M_n(F)$ comes from exactly one form, namely $B(u, v) = x^{\mathsf{T}} A y$.

### Generalizations

For two spaces $V$ and $W$, the bilinear maps $V \times W \to F$ correspond to $\operatorname{Hom}(V, W^*)$ and to $\operatorname{Hom}(W, V^*)$, by the same two ways of fixing a slot.
If $\dim V = m$ and $\dim W = n$, their matrices are the $m \times n$ matrices $A_{ij} = B(e_i, f_j)$.
Over a commutative ring $R$ and a free module $R^n$, parts 1 to 4 hold word for word, but $L_B$ is bijective only when $\det A$ is a unit of $R$, not merely nonzero.

## Explanations

### L1 human

A bilinear form on the plane is the same thing as a table of four numbers.
It is also the same thing as a rule that turns each vector into a linear function.
The vector $u$ goes to the function "pair with $u$", which eats a second vector and returns a number.
All three descriptions carry the same information, so you can work with whichever is easiest.

### L2 human

Here is a typical use: decide whether a form has a nonzero vector $u$ with $B(u, v) = 0$ for all $v$.
By part 1 this asks whether $L_B$ has a nonzero kernel, and by part 4 it asks whether $A^{\mathsf{T}}$ is singular.
For $A = \begin{pmatrix} 1 & 2 \\ 3 & 6 \end{pmatrix}$ on $\mathbb{Q}^2$, the transpose $A^{\mathsf{T}} = \begin{pmatrix} 1 & 3 \\ 2 & 6 \end{pmatrix}$ has kernel spanned by $(3, -1)$.
Check: $B((3, -1), v) = (3, -1) A v = (3 - 3, 6 - 6) v = 0$ for every $v$.
The kernel of $R_B$, from $A y = 0$, is spanned by $(2, -1)$, a different line of the same dimension.
Watch out: many books define the map $V \to V^*$ through the other slot, and then its matrix is $A$ instead of $A^{\mathsf{T}}$.

### L3 human

Part 1 is the tensor-hom adjunction $\operatorname{Hom}(V \otimes V, F) \cong \operatorname{Hom}(V, \operatorname{Hom}(V, F))$.
For finite-dimensional $V$ it gives $\operatorname{Bil}(V) \cong V^* \otimes V^*$, and part 3 reads this isomorphism in the basis $e_i^* \otimes e_j^*$.
The change of basis law $P^{\mathsf{T}} A P$ of [[congruence|WJWNYSQKK8]] is the law of a map $V \to V^*$, and it differs from the law $P^{-1} A P$ of a map $V \to V$.
In infinite dimension, $L_B$ can be injective while $R_B$ is not, which is why the [[nondegeneracy criteria|3ND2FNJ38Y]] assume finite dimension.
