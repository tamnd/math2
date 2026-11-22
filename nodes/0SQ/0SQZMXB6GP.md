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

A bilinear form takes two vectors and returns one number, and it is linear in each vector when you hold the other one fixed.
The [[dot product|0S52TNNTH9]] is the first example, but signed areas, the geometry of relativity and pairings of matrices all have the same shape.
Let $F$ be a [[field|04C5ZBG1WT]] and let $V$ be a [[vector space|000AYPA9AJ]] over $F$.
A *bilinear form* on $V$ is a map $B \colon V \times V \to F$ such that for all $u, v, w \in V$ and all $a, b \in F$:
$$B(au + bv, w) = a B(u, w) + b B(v, w), \qquad B(u, av + bw) = a B(u, v) + b B(u, w).$$
The first rule is linearity in the first slot, and the second rule is linearity in the second slot.
The [[formal definition|0P799D6AMN]] states the same two conditions.

## Motivation

The dot product on $\mathbb{R}^n$ gives lengths and angles.
When you prove things about it, you mostly use one property: it is linear in each factor.
Positivity and symmetry are needed only for a few results.
So it pays to study all pairings that are linear in each factor, over any field, and to add the other properties only when a result needs them.

Many useful pairings are of this kind.
The number $x_1 y_2 - x_2 y_1$ is the signed area of the parallelogram spanned by two vectors of the plane.
The number $x_1 y_1 - x_2 y_2$ is the pairing of special relativity in one space dimension.
The number $\operatorname{tr}(XY)$ pairs two square matrices, and it returns in the theory of Lie algebras.
Later pages sort these forms into [[symmetric|0AXZNE5XNH]], [[alternating|0DGDS5XY84]] and [[sesquilinear|054YEQ0Y8M]] forms, and classify them by their matrices.

## Notation

Books write $B(x, y)$, $\langle x, y \rangle$, $(x, y)$ or $x \cdot y$, and the angle brackets usually mean a form that is fixed for the whole discussion.
The set of all bilinear forms on $V$ is written $\operatorname{Bil}(V)$, or $L^2(V; F)$ in some books.
A map $V \times W \to F$ on two different spaces that is linear in each slot is a *bilinear pairing*, and some books call it a bilinear form too.
In Mathlib the type is `LinearMap.BilinForm R M`, which is a linear map from `M` to the linear maps `M → R`, so `B u v` is the value.

## Remarks

### A first computation

On $\mathbb{Q}^2$ take
$$B(x, y) = x_1 y_1 + 2 x_1 y_2 + 3 x_2 y_2.$$
Fix $y$ and collect the terms by the coordinates of $x$:
$$B(x, y) = (y_1 + 2 y_2)\, x_1 + 3 y_2\, x_2.$$
For fixed $y$ this is a linear expression in $x_1$ and $x_2$, so $B$ is linear in the first slot.
In the same way, $B(x, y) = x_1\, y_1 + (2 x_1 + 3 x_2)\, y_2$ is linear in $y$ for fixed $x$.
So $B$ is a bilinear form, and it is the [[form with matrix $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$|N9CJZW5596]].
A sample value is $B((2, 1), (1, -1)) = 2 - 4 - 3 = -5$.
The test works for every formula of this kind: a polynomial in the coordinates is bilinear exactly when each of its terms contains one coordinate of $x$ and one coordinate of $y$.

### Four standard examples

The dot product $x \cdot y = x_1 y_1 + \dots + x_n y_n$ on $F^n$ is bilinear, because each term $x_k y_k$ is linear in $x$ and in $y$.
More generally, every $n \times n$ matrix $A$ over $F$ gives the form
$$B(x, y) = x^{\mathsf{T}} A y = \sum_{i, j} x_i A_{ij} y_j$$
on $F^n$, since a matrix product is linear in each factor.
The [[matrix of a bilinear form|0QK6K857HS]] shows that every form on a space of dimension $n$ looks like this in a basis.
The determinant of two columns, $B(x, y) = x_1 y_2 - x_2 y_1$, is bilinear and gives $B(x, x) = 0$ for every $x$, so it is [[alternating|0DGDS5XY84]].
The [[trace form on 2 by 2 matrices|CWKB533GHM]], $B(X, Y) = \operatorname{tr}(XY)$, is bilinear because the product $XY$ is bilinear and the trace is linear; the [[trace pairing on square matrices|4F7GWKTQ1H]] works for every size.

### What it is not

The [[map $x_1 y_1 + x_2$ on $\mathbb{R}^2$|5JPJW2GJR6]] is linear in $x$ for fixed $y$, but it is not linear in $y$: for $x = (0, 1)$ it gives $1$ at $y = 0$, and a linear map sends $0$ to $0$.
The map $(x, y) \mapsto \lVert x \rVert \, \lVert y \rVert$ on $\mathbb{R}^2$ fails additivity in $x$: with $x = e_1$, the values at $x$ and $-x$ are both $\lVert y \rVert$, but the value at $x + (-x) = 0$ is $0$.
The [[standard inner product on $\mathbb{C}^n$|TFZ8DYVJ1J]] is not bilinear over $\mathbb{C}$, because it is conjugate-linear in the second slot: $\langle x, i y \rangle = -i \langle x, y \rangle$.
It is a [[sesquilinear form|054YEQ0Y8M]] instead.

### The rules you can use

Each rule follows from linearity in one slot.
A form vanishes when either slot is zero, $B(0, y) = B(x, 0) = 0$, because a linear map sends $0$ to $0$.
The forms on $V$ form a vector space under $(B + B')(x, y) = B(x, y) + B'(x, y)$ and $(cB)(x, y) = c B(x, y)$.
When $\dim V = n$, a form is fixed by its $n^2$ values $B(e_i, e_j)$ on a [[basis|0KCQ9Y3QKA]], so this vector space has dimension $n^2$.
A form is also the same thing as a linear map $V \to V^*$ into the [[dual space|07JBSZE0V4]], $u \mapsto B(u, \cdot)$, by the [[correspondence with linear maps into the dual|ZVMJAF7D53]].
The main classes of forms are the symmetric, the alternating and the [[nondegenerate|01NHFZF2SK]] forms.

### Watch out

A bilinear form is not a linear map on the product space $V \times V$.
If you double both vectors, the value is multiplied by $4$:
$$B(2x, 2y) = 2 B(x, 2y) = 4 B(x, y).$$
A linear map on $V \times V$ would only double it.
A bilinear form also need not be symmetric: for $B(x, y) = x_1 y_2$ on $F^2$ we get $B(e_1, e_2) = 1$ but $B(e_2, e_1) = 0$.
And it need not be positive: $x_1 y_1 - x_2 y_2$ gives $-1$ on the pair $(e_2, e_2)$, so no length comes from it.

### History

Frobenius studied bilinear forms and their transformations in a paper of 1878 on linear substitutions and bilinear forms.
There he treated a bilinear form through the square array of its coefficients, which is the matrix of the form.

### Try it

First, decide whether $B(x, y) = 3 x_1 y_2 - x_2 y_1 + x_2 y_2$ on $\mathbb{R}^2$ is bilinear, and compute $B((1, 2), (0, 1))$.
Every term has one coordinate of $x$ and one of $y$, so it is bilinear, and the value is $3 - 0 + 2 = 5$.

Second, decide whether $B(x, y) = x_1 y_1 + x_2^2 y_2$ is bilinear.
It is not, because $B(2x, y) = 2x_1 y_1 + 4 x_2^2 y_2$, which differs from $2B(x, y)$ when $x_2 y_2 \ne 0$.

## Explanations

### L1 human

A bilinear form is a rule that takes two arrows and gives one number.
If you double the first arrow, the number doubles.
If you double the second arrow, the number also doubles.
The dot product is the main example: $(1, 2)$ and $(3, 4)$ give $1 \cdot 3 + 2 \cdot 4 = 11$.
The rule $x_1 y_2 - x_2 y_1$ is another one, and for $(1, 2)$ and $(3, 4)$ it gives $4 - 6 = -2$, which is the area of the parallelogram of the two arrows with a sign.

### L2 human

Here is a typical use: a form turns a question about vectors into arithmetic with a matrix.
Take the form above, $B(x, y) = x_1 y_1 + 2 x_1 y_2 + 3 x_2 y_2$, and ask which vectors $y$ satisfy $B(e_1, y) = 0$.
Put $x = e_1 = (1, 0)$:
$$B(e_1, y) = y_1 + 2 y_2.$$
So the answer is the line $y_1 = -2 y_2$, spanned by $(-2, 1)$.
Now ask the same question with the slots swapped, $B(y, e_1) = 0$:
$$B(y, e_1) = y_1.$$
The answer is the line $y_1 = 0$, a different line.
So "orthogonal to $e_1$" depends on the slot, because this form is not symmetric.
Watch out for this whenever a form is not symmetric; the page on [[reflexive forms|M0G958M917]] says exactly when the slot does not matter.

### L3 human

A bilinear form on $V$ is a linear map $V \otimes V \to F$, so the space of forms is $(V \otimes V)^*$, and it equals $V^* \otimes V^*$ when $V$ is finite-dimensional.
Seen as a linear map $V \to V^*$, a form makes nondegeneracy and orthogonal complements into statements about [[duality|07JBSZE0V4]].
The group $GL(V)$ acts on forms by $(gB)(x, y) = B(g^{-1}x, g^{-1}y)$, and in matrices this action is [[congruence|WJWNYSQKK8]].
The stabilizer of a nondegenerate symmetric form is an [[orthogonal group|0TKYAEJ8N7]], and the stabilizer of a nondegenerate alternating form is a [[symplectic group|X12FS2JAP0]].
Over a ring in place of a field, bilinear forms on modules lead to lattices and to the arithmetic of [[quadratic forms|0RBQS1JJCR]].
