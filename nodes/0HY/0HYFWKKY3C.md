---
tag: 0HYFWKKY3C
kind: concept
name: Polar form of a quadratic form
msc: ["15A63", "11E04"]
topics: [6TSCEW8QMK]
audience: ug1
uses: [0RBQS1JJCR, 0SQZMXB6GP, 0AXZNE5XNH]
sources:
  - url: https://en.wikipedia.org/wiki/Polarization_of_an_algebraic_form
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
  - book: isbn:9780387728285
---

## Summary

A quadratic form takes one vector, and its polar form takes two.
The polar form measures how far the quadratic form is from being additive, and in most fields it lets you trade the quadratic form for a symmetric matrix.
Let $Q$ be a [[quadratic form|0RBQS1JJCR]] on a finite-dimensional vector space $V$ over a field $F$.
Its *polar form* is the map $b_Q \colon V \times V \to F$ given by
$$b_Q(u, v) = Q(u + v) - Q(u) - Q(v),$$
as in the [[definition|02STTYFBVY]].
It is a [[bilinear form|0SQZMXB6GP]] by the definition of a quadratic form, it is [[symmetric|0AXZNE5XNH]], and $b_Q(v, v) = 2Q(v)$.
When the characteristic of $F$ is not $2$, the half $B = \tfrac{1}{2} b_Q$ is the [[associated symmetric bilinear form|0KRVRV5V80]], with $B(v, v) = Q(v)$, and $Q \mapsto B$ is a [[bijection onto the symmetric bilinear forms|VN9AG8JKYT]].

## Motivation

Many uses of a quadratic form need two vectors at once.
Orthogonality, the matrix of the form and the test for nondegeneracy are all statements about pairs $(u, v)$.
The polar form recovers this two-vector object from $Q$.

The squared length is the model case.
For $Q(v) = \|v\|^2$ on $\mathbb{R}^n$ we get $b_Q(u, v) = \|u + v\|^2 - \|u\|^2 - \|v\|^2 = 2\, u \cdot v$, so the dot product is half the polar form of the squared length.
This is the [[polarization identity|05FKHRT0B4]] of inner product spaces.
Later pages use the polar form at every step: [[diagonalization|0Z3FEWZ8HA]] builds orthogonal bases for $B$, and the [[discriminant|MZFRXECCMC]] is the determinant of its matrix.

## Notation

We write $b_Q$ for $Q(u + v) - Q(u) - Q(v)$, without the factor $\tfrac{1}{2}$, because this map exists in every characteristic.
Outside characteristic $2$ we write $B$ or $B_Q$ for $\tfrac{1}{2} b_Q$.
Books do not agree here: some call $\tfrac{1}{2} b_Q$ the polar form, and others call $b_Q$ itself the polar form, so check the factor before you use a formula.
Outside characteristic $2$ a second formula gives the same $B$:
$$B(u, v) = \tfrac{1}{4}\bigl(Q(u + v) - Q(u - v)\bigr).$$

## Remarks

### A first computation

Take $Q(x, y) = 3x^2 - 2xy + y^2$, and let $u = (x, y)$ and $v = (x', y')$.
Expand $Q(u + v)$ and remove $Q(u)$ and $Q(v)$; only the mixed products survive:
$$b_Q(u, v) = 6xx' - 2(xy' + x'y) + 2yy'.$$
Half of it is $B(u, v) = 3xx' - xy' - x'y + yy'$, and the matrix of $B$ is $\begin{pmatrix} 3 & -1 \\ -1 & 1 \end{pmatrix}$.
Check: $B(u, u) = 3x^2 - 2xy + y^2 = Q(u)$.

### More examples

For [[the form x² + xy|V5AKNSKQNG]] the polar form is $2xx' + xy' + x'y$, and for [[the determinant on 2 × 2 matrices|BQQZX1QS4S]] it is $ad' + a'd - bc' - b'c$.
For $Q(x) = x^{\mathsf{T}} A x$ with $A$ symmetric, expanding $(x + y)^{\mathsf{T}} A (x + y)$ gives $b_Q(x, y) = x^{\mathsf{T}} A y + y^{\mathsf{T}} A x = 2\, x^{\mathsf{T}} A y$.
So $B(x, y) = x^{\mathsf{T}} A y$ when $2 \ne 0$, and the matrix of $b_Q$ is $2A$.

### The rules you can use

The polar form is symmetric, because the formula does not change when $u$ and $v$ are exchanged.
Its diagonal is $b_Q(v, v) = Q(2v) - 2Q(v) = 4Q(v) - 2Q(v) = 2Q(v)$.
It is compatible with linear maps: $b_{Q \circ T}(u, v) = b_Q(Tu, Tv)$, which follows by putting $Tu$ and $Tv$ into the formula.
Outside characteristic $2$, the form $Q$ and the form $B = \tfrac{1}{2} b_Q$ determine each other, by [[the correspondence theorem|VN9AG8JKYT]].

### What it is not

[[The bilinear form u₁v₂ on ℝ²|WW5X7DHHQ6]] is not the polar form of any quadratic form, because it is not symmetric: it gives $1$ on $(e_1, e_2)$ and $0$ on $(e_2, e_1)$.
For $Q(x) = x^3$ on $\mathbb{R}$, the expression $Q(u + v) - Q(u) - Q(v) = 3u^2 v + 3uv^2$ is not bilinear, and this is because $x^3$ is not a quadratic form.

### Characteristic 2

In characteristic $2$ the diagonal rule gives $b_Q(v, v) = 2Q(v) = 0$ for every $v$, so the polar form is alternating.
Then $Q$ cannot be recovered from $b_Q$.
Over $\mathbb{F}_2$, the form $Q(x) = x^2$ has $b_Q(u, v) = 2uv = 0$, the same polar form as the zero form, as [[the example over F₂|ZEGSCCVGZF]] shows.
The same example shows that $xy$ on $\mathbb{F}_2^2$ is $B(v, v)$ for no symmetric bilinear form $B$.
So in characteristic $2$ a quadratic form carries more information than its polar form, and the two must be kept apart.

### Watch out

A common error is to use the matrix of $b_Q$ as the matrix of $Q$.
For $Q(x, y) = x^2 + y^2$ the matrix of $b_Q$ is $2I_2$, and $(x, y)\, 2I_2\, (x, y)^{\mathsf{T}} = 2x^2 + 2y^2 = 2Q$, not $Q$.
The matrix of $Q$ is the matrix of $B = \tfrac{1}{2} b_Q$, here $I_2$.
A second error is to think that every symmetric bilinear form in characteristic $2$ is a polar form: the form $uv$ on $\mathbb{F}_2$ has $1 \cdot 1 = 1 \ne 0$ on the diagonal, so it is not alternating and not a polar form.

### History

Gauss wrote binary forms in the Disquisitiones Arithmeticae of 1801 as $ax^2 + 2bxy + cy^2$, with an even middle coefficient.
That convention avoids the halves that appear in the symmetric matrix of a form with an odd middle coefficient.
The general passage from a homogeneous polynomial to a symmetric multilinear form is called polarization, and the quadratic case is its first instance.

### Try it

First, find the polar form of $Q(x, y) = xy$ on $\mathbb{R}^2$ and its matrix $B$.
The polar form is $xy' + x'y$, so $B = \tfrac{1}{2} b_Q$ has the matrix $\begin{pmatrix} 0 & 1/2 \\ 1/2 & 0 \end{pmatrix}$.

Second, for $Q(x, y) = 3x^2 - 2xy + y^2$, find a vector $v$ with $B((1, 0), v) = 0$.
From the formula above, $B((1, 0), (x', y')) = 3x' - y'$, so $v = (1, 3)$ works.

## Explanations

### L1 human

A quadratic form gives one number for each vector, and its polar form gives one number for each pair of vectors.
The polar form is the error in additivity, $Q(u + v) - Q(u) - Q(v)$.
For the squared length in the plane, $u = (1, 0)$ and $v = (1, 1)$ give $5 - 1 - 2 = 2$.
That is twice the dot product $u \cdot v = 1$.

### L2 human

Here is a typical use: orthogonality for a form.
Two vectors $u$ and $v$ are orthogonal for $Q$ when $B(u, v) = 0$.
For $Q = 3x^2 - 2xy + y^2$, the vectors $(1, 0)$ and $(1, 3)$ are orthogonal, since
$$B\bigl((1, 0), (1, 3)\bigr) = 3 \cdot 1 \cdot 1 - 1 \cdot 3 - 0 \cdot 1 + 0 \cdot 3 = 0.$$
In the basis $(1, 0), (1, 3)$ the form has no cross term: $Q(s(1, 0) + t(1, 3)) = 3s^2 + 6t^2$.
Check: at $s = 0$, $t = 1$ the vector is $(1, 3)$, and $Q(1, 3) = 3 - 6 + 9 = 6$.
Watch out: orthogonality for $Q$ is not orthogonality for the dot product, because $(1, 0) \cdot (1, 3) = 1 \ne 0$.

### L3 human

Polarization sends a homogeneous polynomial of degree $d$ to a symmetric $d$-linear form, and to recover the polynomial from the form you divide by $d!$.
For $d = 2$ the only obstruction is the prime $2$, so in characteristic $2$ quadratic forms and symmetric bilinear forms are different objects.
There the polar form is alternating, and an alternating form can be nondegenerate only in even dimension, so in odd dimension the polar form is always degenerate.
The general theory of symmetric and [[alternating bilinear forms|0DGDS5XY84]] is in the topic on [[bilinear and sesquilinear forms|DYAK7YMK7B]].
