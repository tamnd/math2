---
tag: 0RBQS1JJCR
kind: concept
name: Quadratic form
msc: ["15A63", "11E04"]
topics: [6TSCEW8QMK]
audience: ug1
uses: [0SQZMXB6GP, 2C3PAQ7H50, 0VR671PHE5]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Associated symmetric matrix
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: History
  - book: isbn:9780387728285
  - book: isbn:9780134860244
same_as:
  wikidata: Q736753
  wikipedia: Quadratic form
---

## Summary

A quadratic form is a polynomial in which every term has degree exactly two, such as $3x^2 - 4xy + y^2$.
After the linear functions it is the simplest kind of function on a vector space, and it describes squared lengths, energies, conic sections and the second-order behavior of a smooth function.
Let $F$ be a field and let $V$ be a vector space of finite dimension $n$ over $F$.
A *quadratic form* on $V$ is a map $Q \colon V \to F$ with two properties, as in [[the definition|0HZNE5QZDJ]]:
$$Q(av) = a^2 Q(v) \quad \text{for all } a \in F,\ v \in V, \qquad (u, v) \mapsto Q(u + v) - Q(u) - Q(v) \ \text{is bilinear}.$$
On $F^n$ these maps are exactly the [[homogeneous polynomials|2C3PAQ7H50]] of degree $2$, $Q(x) = \sum_{i \le j} c_{ij} x_i x_j$.
When the characteristic of $F$ is not $2$, each of them has the form $Q(x) = x^{\mathsf{T}} A x$ for exactly one [[symmetric matrix|0VR671PHE5]] $A$.

## Motivation

Many quantities in mathematics have degree two in the coordinates.
The squared length $x_1^2 + x_2^2 + x_3^2$ of a vector, the kinetic energy $\tfrac{1}{2} m v^2$ and the left side of the ellipse equation $x^2/4 + y^2 = 1$ are three of them.
Near a critical point, Taylor's formula makes a smooth function of several variables look like a constant plus a quadratic form, so the form decides whether the point is a minimum, a maximum or a saddle.

In each case the same two questions come up.
Can a change of coordinates remove the cross terms $x_i x_j$, and which coefficients are left after such a change?
The pages that follow answer these questions: [[diagonalization|0Z3FEWZ8HA]] removes the cross terms, and the answer to the second question depends on the field.
Over $\mathbb{C}$ only the rank is left, over $\mathbb{R}$ the [[signature|07EZA80NEH]] is left too, and over a finite field the [[discriminant|MZFRXECCMC]] is left.
For real forms the [[principal axis theorem|0PR5P9Z4KM]] does even better, with a rotation of the axes.

## Notation

We write $Q$ or $q$ for a quadratic form, and $b_Q(u, v) = Q(u + v) - Q(u) - Q(v)$ for its [[polar form|0HYFWKKY3C]].
Outside characteristic $2$, the [[associated symmetric bilinear form|0KRVRV5V80]] is $B = \tfrac{1}{2} b_Q$, and then $B(v, v) = Q(v)$.
The *matrix* of $Q$ in a basis $(e_1, \dots, e_n)$ is the matrix $A = (B(e_i, e_j))$ of $B$, so that $Q(x) = x^{\mathsf{T}} A x$ for the coordinate column $x$.
For a diagonal form $a_1 x_1^2 + \dots + a_n x_n^2$, many books write $\langle a_1, \dots, a_n \rangle$.

Two forms $Q$ on $V$ and $Q'$ on $V'$ are *equivalent*, or *isometric*, when $Q' = Q \circ T$ for a linear bijection $T \colon V' \to V$.
In matrices this says $A' = P^{\mathsf{T}} A P$ with $P$ invertible, so the two matrices are [[congruent|WJWNYSQKK8]].
Watch out for one notation from number theory: there $ax^2 + bxy + cy^2$ is written $[a, b, c]$, and some books use the matrix $\begin{pmatrix} 2a & b \\ b & 2c \end{pmatrix}$ of the polar form in place of the matrix of $B$.

## Remarks

### A first form and its matrix

Take $Q(x, y) = x^2 + 3xy + 2y^2$ on $\mathbb{R}^2$.
Doubling both variables multiplies every term by $4$, so $Q(2, 2) = 4 + 12 + 8 = 24 = 4 \cdot Q(1, 1)$.
To write $Q$ with a symmetric matrix, put the coefficients of the squares on the diagonal and split the coefficient $3$ of $xy$ into two halves:
$$x^2 + 3xy + 2y^2 = \begin{pmatrix} x & y \end{pmatrix} \begin{pmatrix} 1 & 3/2 \\ 3/2 & 2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}.$$
Check: the product is $x^2 + \tfrac{3}{2} xy + \tfrac{3}{2} yx + 2y^2$, which is $Q$.
In general the off-diagonal entries are $a_{ij} = a_{ji} = \tfrac{1}{2} c_{ij}$, and [[the form x² + xy|V5AKNSKQNG]] works this out with entries $\tfrac{1}{2}$.

### Why every form is a polynomial

The two conditions of the definition force a polynomial.
Fix a basis $(e_1, \dots, e_n)$ and use the rule $Q(u + v) = Q(u) + Q(v) + b_Q(u, v)$ again and again, one basis vector at a time.
Together with $Q(x_i e_i) = x_i^2 Q(e_i)$ this gives
$$Q\Bigl(\sum_i x_i e_i\Bigr) = \sum_i Q(e_i)\, x_i^2 + \sum_{i < j} b_Q(e_i, e_j)\, x_i x_j.$$
So the coefficient of $x_i^2$ is $Q(e_i)$, and the coefficient of $x_i x_j$ is $b_Q(e_i, e_j)$.
Conversely, every monomial $x_i x_j$ scales by $a^2$ and has the bilinear polar form $x_i y_j + y_i x_j$, so every sum $\sum_{i \le j} c_{ij} x_i x_j$ is a quadratic form.

### More examples

The squared length $x_1^2 + \dots + x_n^2$ on $\mathbb{R}^n$ has matrix $I_n$, and it is the main example of a [[positive definite form|0RP20HFYM3]].
The Minkowski form $x^2 + y^2 + z^2 - t^2$ on $\mathbb{R}^4$ takes positive, negative and zero values.
On $2 \times 2$ matrices, [[the determinant ad − bc|BQQZX1QS4S]] is a quadratic form on a space of dimension $4$.
On $n \times n$ matrices, $Q(X) = \operatorname{tr}(X^2)$ is a quadratic form, because $Q(aX) = a^2 Q(X)$ and
$$\operatorname{tr}\bigl((X + Y)^2\bigr) - \operatorname{tr}(X^2) - \operatorname{tr}(Y^2) = \operatorname{tr}(XY) + \operatorname{tr}(YX) = 2 \operatorname{tr}(XY),$$
which is bilinear in $X$ and $Y$.
Over the field $\mathbb{F}_2$ with two elements, $Q(x, y) = xy$ is a quadratic form, but [[no symmetric bilinear form gives it|ZEGSCCVGZF]].

### What it is not

The map $Q(x, y) = x^2 + y$ on $\mathbb{R}^2$ is not homogeneous: $Q(0, 2) = 2$, but $2^2 Q(0, 1) = 4$.
The map $Q(x) = x^3$ on $\mathbb{R}$ fails the same condition, since $Q(2) = 8$ and $2^2 Q(1) = 4$.
The second condition is needed too.
[[The function x⁴/(x² + y²)|AN5RQ78DD8]] satisfies $Q(av) = a^2 Q(v)$, but its polar form is not bilinear, so it is not a quadratic form.

### The rules you can use

Taking $a = 0$ and $a = -1$ in the first condition gives $Q(0) = 0$ and $Q(-v) = Q(v)$.
The polar form is symmetric, and $b_Q(v, v) = Q(2v) - 2Q(v) = 2Q(v)$.
If $T \colon W \to V$ is linear, then $Q \circ T$ is a quadratic form on $W$, so the restriction of $Q$ to a subspace is again a quadratic form.
Under a change of basis with matrix $P$, the matrix $A$ becomes $P^{\mathsf{T}} A P$, by [[the change of basis rule for bilinear forms|0SPYAGE7T0]].
Outside characteristic $2$, quadratic forms and [[symmetric bilinear forms|0AXZNE5XNH]] [[correspond one to one|VN9AG8JKYT]], and every quadratic form has [[a diagonal form|0Z3FEWZ8HA]] $a_1 x_1^2 + \dots + a_n x_n^2$ in a suitable basis.

### Watch out

The most common error is to put the full coefficient of $x_i x_j$ into both entries $a_{ij}$ and $a_{ji}$.
For $x^2 + 3xy + 2y^2$ the matrix $\begin{pmatrix} 1 & 3 \\ 3 & 2 \end{pmatrix}$ gives $x^2 + 6xy + 2y^2$, which is a different form.
The correct entries are $\tfrac{3}{2}$.

A second error is to carry the formula $B(u, v) = \tfrac{1}{2}\bigl(Q(u + v) - Q(u) - Q(v)\bigr)$ into characteristic $2$.
There $\tfrac{1}{2}$ does not exist, and the [[polar form|0HYFWKKY3C]] page shows that a quadratic form then carries more information than any symmetric bilinear form.

### History

Questions about integers started the theory, for example Fermat's theorem on primes that are sums of two squares.
Gauss's Disquisitiones Arithmeticae of 1801 contains a large theory of binary quadratic forms $ax^2 + bxy + cy^2$ with integer coefficients.
Forms over the integers and over number fields now belong to number theory, in the topic on [[quadratic forms over local and global fields|NQC5CJZY4J]].

### Try it

First, find the symmetric matrix of $Q(x, y, z) = 2x^2 - 6xy + 4yz + z^2$.
The diagonal is $(2, 0, 1)$, the entries at $(1, 2)$ and $(2, 1)$ are $-3$, the entries at $(2, 3)$ and $(3, 2)$ are $2$, and the entries at $(1, 3)$ and $(3, 1)$ are $0$.

Second, is $Q(x, y) = (x + y)^2 - xy$ a quadratic form, and what is its matrix?
It expands to $x^2 + xy + y^2$, a homogeneous polynomial of degree $2$, so it is a quadratic form with matrix $\begin{pmatrix} 1 & 1/2 \\ 1/2 & 1 \end{pmatrix}$.

## Explanations

### L1 human

A quadratic form is a sum of terms that each have degree two, such as $3x^2 - 4xy + y^2$.
It has no constant term and no terms of degree one.
If you double every variable, the value is multiplied by four.
At $(1, 0)$ the form above gives $3$, and at $(2, 0)$ it gives $12 = 4 \cdot 3$.
At $(1, 1)$ it gives $3 - 4 + 1 = 0$, and at $(2, 2)$ it gives $12 - 16 + 4 = 0$ again.

### L2 human

Here is a typical use: write $Q(x, y, z) = 2x^2 - 6xy + 4yz + z^2$ with a symmetric matrix, so that matrix methods apply.
The coefficients of the squares go on the diagonal, and each cross coefficient is split into two equal halves:
$$A = \begin{pmatrix} 2 & -3 & 0 \\ -3 & 0 & 2 \\ 0 & 2 & 1 \end{pmatrix}.$$
Check: $x^{\mathsf{T}} A x = 2x^2 + 2(-3)xy + 2(2)yz + z^2$, which is $Q$.
After a change of variables $x = Py$ the matrix becomes $P^{\mathsf{T}} A P$, and the next pages choose $P$ so that this matrix is diagonal.
Watch out: the matrix with $-6$ at $(1, 2)$ and $0$ at $(2, 1)$ also gives $Q$, but it is not symmetric, so the theorems on symmetric matrices do not apply to it.

### L3 human

The definition by the polar form works over every commutative ring, also in characteristic $2$, and Mathlib states it that way as `QuadraticMap`, with `QuadraticForm R M` the case of values in $R$.
A pair $(V, Q)$ is a *quadratic space*.
The orthogonal sum makes the isometry classes of nondegenerate quadratic spaces into a monoid, and the [[Witt group|KFVY0RPGF2]] is built from it.
The later pages classify forms over $\mathbb{C}$, over $\mathbb{R}$ and over finite fields, and use the real case for conics and quadric surfaces.
Over $\mathbb{Q}$ the classification needs local invariants and the [[Hasse-Minkowski theorem|R8HCWA981S]], which belong to number theory.
