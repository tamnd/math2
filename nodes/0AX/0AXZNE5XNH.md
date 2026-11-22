---
tag: 0AXZNE5XNH
kind: concept
name: Symmetric bilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
specializes: [0SQZMXB6GP]
uses: [0SQZMXB6GP, 0QK6K857HS, 0VR671PHE5]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_bilinear_form
    locator: Formal definition
  - url: https://en.wikipedia.org/wiki/Symmetric_bilinear_form
    locator: lead section
  - book: isbn:9780387728285
    locator: Chapter 11
  - url: https://en.wikipedia.org/wiki/Sylvester%27s_law_of_inertia
    locator: lead section
same_as:
  wikidata: Q2100018
  wikipedia: Symmetric bilinear form
---

## Summary

A symmetric bilinear form is a pairing of vectors that does not care about the order of the two vectors.
It is the setting for lengths and right angles without any positivity, and it is the bilinear partner of a [[quadratic form|0RBQS1JJCR]].
Let $V$ be a vector space over a field $F$.
A [[bilinear form|0SQZMXB6GP]] $B$ on $V$ is *symmetric* when
$$B(u, v) = B(v, u) \qquad \text{for all } u, v \in V.$$
The [[formal definition|0744CN4MDA]] states the same condition.
When $V$ has finite dimension, $B$ is symmetric exactly when its [[matrix|0QK6K857HS]] in one basis, or in every basis, is a [[symmetric matrix|0VR671PHE5]].

## Motivation

In the plane, the angle from $u$ to $v$ has the same size as the angle from $v$ to $u$, and the [[dot product|0S52TNNTH9]] reflects this with $u \cdot v = v \cdot u$.
Many other pairings keep this symmetry but lose positivity.
The form $x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$ is the geometry of special relativity with one space dimension, and the trace form $\operatorname{tr}(XY)$ pairs square matrices.
A symmetric form is what these pairings share, and it gives a relation "$u$ is orthogonal to $v$" that reads the same in both directions.

Symmetric forms also come out of functions of degree $2$.
For $q(x) = x_1^2 + 3x_1 x_2$, the expression $q(x + y) - q(x) - q(y) = 2x_1 y_1 + 3x_1 y_2 + 3x_2 y_1$ is a symmetric bilinear form in $x$ and $y$.
The sub-area on [[quadratic forms|0RBQS1JJCR]] builds its whole theory on this link, and the [[orthogonal groups|0TKYAEJ8N7]] are the groups that keep a symmetric form.

## Notation

A space with a symmetric form is written $(V, B)$, and some books call it a quadratic space or an orthogonal space.
When $B$ has the diagonal matrix $\operatorname{diag}(a_1, \dots, a_n)$ in some basis, many books write $B \cong \langle a_1, \dots, a_n \rangle$.
Watch out for the clash with the angle brackets of an inner product: $\langle 1, -1 \rangle$ here names the form $x_1 y_1 - x_2 y_2$, not a pairing of the vectors $1$ and $-1$.

## Remarks

### Reading symmetry off the matrix

Take the form on $\mathbb{Q}^2$ with
$$B(x, y) = 2x_1 y_1 + 3x_1 y_2 + 3x_2 y_1 - x_2 y_2.$$
Its matrix collects the coefficient of $x_i y_j$ in place $(i, j)$:
$$A = \begin{pmatrix} 2 & 3 \\ 3 & -1 \end{pmatrix}.$$
The two entries off the diagonal agree, so $A^{\mathsf{T}} = A$ and $B$ is symmetric.
Check: $B(e_1, e_2) = 3$ and $B(e_2, e_1) = 3$.

The reason is the same in general.
If $B$ is symmetric, then $A_{ji} = B(e_j, e_i) = B(e_i, e_j) = A_{ij}$.
If $A^{\mathsf{T}} = A$, then $x^{\mathsf{T}} A y$ is a $1 \times 1$ matrix, so it equals its transpose $y^{\mathsf{T}} A^{\mathsf{T}} x = y^{\mathsf{T}} A x$, which is $B(y, x)$ by the [[correspondence theorem|ZVMJAF7D53]].
So the symmetric forms on an $n$-dimensional space match the symmetric $n \times n$ matrices, and they form a space of dimension $n(n + 1)/2$, one entry for each place on or above the diagonal.

### More examples

The [[dot product|0S52TNNTH9]] on $F^n$ is symmetric, because $x_k y_k = y_k x_k$ in every field.
The [[trace form on 2 by 2 matrices|CWKB533GHM]] is symmetric, because $\operatorname{tr}(XY) = \operatorname{tr}(YX)$.
The [[form $x_1 y_1 - x_2 y_2$ on the real plane|X6C1Z0W252]] is symmetric, but $B(e_2, e_2) = -1$, and the nonzero vector $(1, 1)$ has $B(v, v) = 0$.
Every real [[inner product|0NB0AWGJBW]] is a symmetric form with $B(v, v) > 0$ for every $v \ne 0$, so the inner products are exactly the positive definite symmetric forms over $\mathbb{R}$.
The [[degenerate form on the rational 3-space|RZMEYX1YJT]] is symmetric too, and it has a whole line of vectors that are orthogonal to everything.

### What it is not

The [[form with matrix with rows (1, 2) and (0, 3)|N9CJZW5596]] is not symmetric, since $B(e_1, e_2) = 2$ but $B(e_2, e_1) = 0$.
The [[determinant form $x_1 y_2 - x_2 y_1$|8K74K4BF5H]] is not symmetric when $1 + 1 \ne 0$ in $F$, since it gives $1$ on $(e_1, e_2)$ and $-1$ on $(e_2, e_1)$.
The [[standard inner product on complex space|TFZ8DYVJ1J]] is not a symmetric bilinear form at all: it is conjugate-linear in the second slot, and swapping the slots conjugates the value.
Its conjugation-free cousin $x_1 y_1 + x_2 y_2$ on $\mathbb{C}^2$ is symmetric and bilinear, but it is [[not sesquilinear|2A38WWPDES]].

### The rules you can use

When $1 + 1 \ne 0$ in $F$, every bilinear form splits into a symmetric part and a [[skew-symmetric part|0DGDS5XY84]]:
$$B(u, v) = \tfrac12 \bigl(B(u, v) + B(v, u)\bigr) + \tfrac12 \bigl(B(u, v) - B(v, u)\bigr).$$
In the same characteristic, a symmetric form is fixed by its values on the diagonal, through the [[polar form|0HYFWKKY3C]] $B(u, v) = \tfrac12 \bigl(q(u + v) - q(u) - q(v)\bigr)$ with $q(v) = B(v, v)$.
Orthogonality for a symmetric form is a symmetric relation, so the form is [[reflexive|M0G958M917]], and it has one [[orthogonal complement|01TXN7ETH2]] for each subspace and one radical.
Finally, when $1 + 1 \ne 0$ and $V$ has finite dimension, $V$ has a basis of pairwise orthogonal vectors, so the matrix is [[congruent to a diagonal matrix|0Z3FEWZ8HA]].

### Diagonal form by congruence

Take $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ over $\mathbb{Q}$.
Keep $f_1 = e_1$, since $B(e_1, e_1) = 1 \ne 0$.
A vector $y$ is orthogonal to $e_1$ when $B(e_1, y) = y_1 + 2y_2 = 0$, so take $f_2 = (-2, 1)$.
With $P$ the matrix with columns $f_1, f_2$, the new matrix is
$$P^{\mathsf{T}} A P = \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 2 & -3 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -3 \end{pmatrix}.$$
Check: $B(f_2, f_2) = 1 \cdot 4 + 2 \cdot 2 \cdot (-2) \cdot 1 + 1 \cdot 1 = 4 - 8 + 1 = -3$.
The eigenvalues of $A$ are $3$ and $-1$, not $1$ and $-3$, because [[congruence|WJWNYSQKK8]] is not similarity; only the signs match, by [[Sylvester's law of inertia|0WFED3K3DQ]].

### Watch out

The orthogonal basis needs $1 + 1 \ne 0$.
Over $\mathbb{F}_2$, take $B(x, y) = x_1 y_2 + x_2 y_1$, the polar form of $xy$, with matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
It is symmetric, and $B(v, v) = 2v_1 v_2 = 0$ for every $v$.
A diagonal matrix $P^{\mathsf{T}} A P$ would have the entries $B(f_i, f_i) = 0$ on its diagonal, so it would be the zero matrix of rank $0$, while $A$ has rank $2$.
So no orthogonal basis exists; the correct move in characteristic $2$ is to split off planes like this one, as in the [[classification of alternating forms|V8KKHKXXB3]].

A second trap: symmetric does not mean positive.
The form $x_1 y_1 - x_2 y_2$ is symmetric with $B(e_2, e_2) = -1$, so it is not an inner product.

### History

Sylvester published his law of inertia for real quadratic forms, and so for real symmetric forms, in 1852.

### Try it

First, is $B(x, y) = x_1 y_1 + x_1 y_2 + x_2 y_1$ on $\mathbb{R}^2$ symmetric, and is it an inner product?
Its matrix $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ is symmetric, but $B(e_2, e_2) = 0$ with $e_2 \ne 0$, so it is not an inner product.

Second, split $B(x, y) = x_1 y_2$ on $\mathbb{Q}^2$ into a symmetric part and a skew-symmetric part.
The parts are $\tfrac12 (x_1 y_2 + x_2 y_1)$ and $\tfrac12 (x_1 y_2 - x_2 y_1)$, and their sum is $x_1 y_2$.

## Explanations

### L1 human

A symmetric form takes two arrows and gives a number, and it gives the same number when you swap the arrows.
The dot product is the main example: $(1, 2) \cdot (3, 4) = 11 = (3, 4) \cdot (1, 2)$.
In the square table of numbers that describes the form, the entry in row $1$, column $2$ equals the entry in row $2$, column $1$.
Unlike the dot product, a symmetric form can give a negative number, or zero, when an arrow is paired with itself.

### L2 human

Here is a typical use: recover a symmetric form from its values on the diagonal.
Over $\mathbb{Q}$, suppose $q(x) = 2x_1^2 + 6x_1 x_2 - x_2^2$ and we want the symmetric $B$ with $B(v, v) = q(v)$.
The polar formula gives the entry off the diagonal:
$$B(e_1, e_2) = \tfrac12 \bigl(q(1, 1) - q(1, 0) - q(0, 1)\bigr) = \tfrac12 \bigl(7 - 2 + 1\bigr) = 3.$$
The diagonal entries are $q(e_1) = 2$ and $q(e_2) = -1$, so the matrix is $\begin{pmatrix} 2 & 3 \\ 3 & -1 \end{pmatrix}$, the form at the start of Remarks.
Check: $x^{\mathsf{T}} A x = 2x_1^2 + 3x_1 x_2 + 3x_2 x_1 - x_2^2 = q(x)$.
Watch out: the coefficient $6$ of $x_1 x_2$ splits into two entries $3$, not one entry $6$.
This is how a quadratic expression becomes a matrix that we can diagonalize.

### L3 human

Symmetric bilinear forms on $V$ are the linear forms on the symmetric square $\operatorname{Sym}^2 V$, and outside characteristic $2$ they match the [[quadratic forms|0RBQS1JJCR]] one to one.
Their classification up to [[congruence|WJWNYSQKK8]] depends on the arithmetic of the field: over $\mathbb{C}$ only the rank counts, over $\mathbb{R}$ rank and signature count, and over $\mathbb{Q}$ the question leads to the [[Hasse-Minkowski theorem|R8HCWA981S]] and to the [[Witt group|KFVY0RPGF2]].
The isometries of a nondegenerate symmetric form make the [[orthogonal group|0TKYAEJ8N7]].
In geometry, a pseudo-Riemannian metric on a manifold is a smooth choice of a nondegenerate symmetric form on each tangent space.
