---
tag: 0XM8BZD76G
kind: object
name: Coordinate space
msc: [15A03]
topics: [MVH97H8B2J]
audience: ug1
instance_of: [000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: lead section
---

## Description

The coordinate space is the space of lists of $n$ numbers, where you add two lists entry by entry and scale a list by scaling every entry.
It is the first vector space that everyone meets, and every finite-dimensional vector space can be moved into it by a choice of basis.

Let $F$ be a [[field|04C5ZBG1WT]] and let $n \ge 0$ be an integer.
The *coordinate space* $F^n$ is the set of all $n$-tuples $x = (x_1, \dots, x_n)$ with every entry $x_i$ in $F$.
Two tuples are equal when they agree in every position.
The sum and the scalar multiple are defined entry by entry:
$$(x_1, \dots, x_n) + (y_1, \dots, y_n) = (x_1 + y_1, \dots, x_n + y_n), \qquad a (x_1, \dots, x_n) = (a x_1, \dots, a x_n),$$
for $a \in F$.
With these operations $F^n$ is a [[vector space|000AYPA9AJ]] over $F$.
Its zero vector is $(0, \dots, 0)$, and the negative of $x$ is $(-x_1, \dots, -x_n)$.
Each axiom holds because it holds in $F$ in each position separately, and the [[worked check of the axioms|713F6AM1X1]] goes through them one by one.

## Remarks

### A first computation

Take $F = \mathbb{R}$ and $n = 3$, with $x = (2, -1, 5)$ and $y = (1, 0, -2)$.
To form $x + 3y$, first scale $y$ and then add entry by entry:
$$x + 3y = (2, -1, 5) + (3, 0, -6) = (5, -1, -1).$$
Check: the first entries give $2 + 3 \cdot 1 = 5$, the second give $-1 + 3 \cdot 0 = -1$, and the third give $5 + 3 \cdot (-2) = -1$.
Every computation in $F^n$ is of this kind: $n$ separate computations in $F$, done side by side.

### The main cases

For $F = \mathbb{R}$, the spaces $\mathbb{R}^2$ and $\mathbb{R}^3$ are the plane and ordinary space with a chosen origin and chosen axes, and their elements are the [[Euclidean vectors|0QN3D80AWP]] of school geometry.
For $F = \mathbb{C}$, the space $\mathbb{C}^n$ is the setting for eigenvalues and for quantum mechanics.
For a finite field the space is finite.
Over the field $\mathbb{F}_2 = \{0, 1\}$ with $1 + 1 = 0$, the space $\mathbb{F}_2^3$ has $2^3 = 8$ elements, and in it $(1, 1, 0) + (1, 1, 0) = (0, 0, 0)$.
For $n = 0$ there is one tuple, the empty one, so $F^0$ is the zero space.

### Rows and columns

A tuple is written in a row, but in matrix work we write the elements of $F^n$ as columns.
Then an $m \times n$ matrix $A$ and a column $x \in F^n$ give a product $Ax \in F^m$, and a system of linear equations reads $Ax = b$.
For example,
$$\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 4 \\ -1 \end{pmatrix} = \begin{pmatrix} 1 \cdot 4 + 2 \cdot (-1) \\ 0 \cdot 4 + 3 \cdot (-1) \end{pmatrix} = \begin{pmatrix} 2 \\ -3 \end{pmatrix}.$$
The row and the column are two pictures of the same element of $F^n$, and books choose one by convention.

### Why every finite-dimensional space looks like this

Take the space of real polynomials of degree at most $2$.
Each such polynomial $a + bx + cx^2$ is fixed by its three coefficients, so we can send it to the column $(a, b, c)$ of $\mathbb{R}^3$.
This map keeps sums and scalar multiples, and it is a bijection, so the two spaces have the same structure.
In general, an ordered [[basis|0KCQ9Y3QKA]] $v_1, \dots, v_n$ of a space $V$ sends each vector to its [[coordinate vector|04CYQHN6MC]] in $F^n$.
This gives the [[isomorphism with the coordinate space|059THXBRBB]], and that is why every finite-dimensional problem can be solved with columns and matrices.
The isomorphism depends on the basis: with the basis $1, 1 + x, x^2$ the polynomial $x$ goes to $(-1, 1, 0)$ and not to $(0, 1, 0)$.

### The field is part of the data

The same set can be a coordinate space over two fields, with two different dimensions.
The [[standard basis|0V7ZD6P7RK]] shows that $F^n$ has [[dimension|03GSZ8RTZJ]] $n$ over $F$, so $\mathbb{C}^2$ has dimension $2$ over $\mathbb{C}$.
As a real vector space $\mathbb{C}^2$ has dimension $4$, with the real basis $(1, 0)$, $(i, 0)$, $(0, 1)$, $(0, i)$.
So the statement "$\mathbb{C}^2$ has dimension $2$" is true only when we say which scalars we use.

### What it is not

The set $\mathbb{Z}^2$ of pairs of integers has the same entrywise addition, but it is not a vector space over $\mathbb{Q}$ or $\mathbb{R}$.
The product $\tfrac{1}{2} (1, 0) = (\tfrac{1}{2}, 0)$ leaves the set, and $\mathbb{Z}$ is not a field, so it cannot serve as the scalars either.
The closed quadrant of pairs $(x, y)$ with $x, y \ge 0$ is not a vector space under the operations of $\mathbb{R}^2$, because $(-1)(1, 0) = (-1, 0)$ leaves it.
Both sets fail because a scalar multiple leaves the set, while $F^n$ contains every scalar multiple of every element.

### Watch out

The plane $\mathbb{R}^2$ is not a subset of $\mathbb{R}^3$.
Its elements are pairs and the elements of $\mathbb{R}^3$ are triples, so $(1, 2)$ is not an element of $\mathbb{R}^3$.
The vectors $(x, y, 0)$ form a [[subspace|00YC1D652K]] of $\mathbb{R}^3$, and that subspace is isomorphic to $\mathbb{R}^2$.
The vectors $(x, 0, y)$ form a second such subspace, so "the plane inside space" depends on a choice.

### Try it

First, in $\mathbb{R}^4$ compute $2(1, 0, -1, 3) - (0, 4, 1, 1)$.
The answer is $(2, 0, -2, 6) - (0, 4, 1, 1) = (2, -4, -3, 5)$.

Second, how many vectors does $\mathbb{F}_3^2$ have, where $\mathbb{F}_3 = \{0, 1, 2\}$ with arithmetic modulo $3$?
Each of the two entries has $3$ choices, so there are $3^2 = 9$ vectors.

## Explanations

### L1 human

The coordinate space $\mathbb{R}^3$ is the collection of all lists of three real numbers, such as $(2, -1, 5)$.
You can think of each list as an arrow from the origin to a point in space.
To add two lists, add the numbers in the same position: $(1, 2, 3) + (4, 5, 6) = (5, 7, 9)$.
To scale a list, multiply every entry: $2 \cdot (1, 2, 3) = (2, 4, 6)$.
The rules for these operations are the rules of ordinary arithmetic, used once in each position.

### L2 human

Here is a typical use: decide whether $p = 3 + 2x - x^2$ is a combination of $q_1 = 1 + x$ and $q_2 = x + x^2$.
Move the problem into $\mathbb{R}^3$ by the coefficients, so that $p \mapsto (3, 2, -1)$, $q_1 \mapsto (1, 1, 0)$ and $q_2 \mapsto (0, 1, 1)$.
We need numbers $s$ and $t$ with
$$s (1, 1, 0) + t (0, 1, 1) = (s, s + t, t) = (3, 2, -1).$$
The first and the third entries give $s = 3$ and $t = -1$, and then the second entry is $3 + (-1) = 2$, as required.
So $p = 3 q_1 - q_2$.
Check: $3(1 + x) - (x + x^2) = 3 + 2x - x^2$.
The problem about polynomials became a small system of equations in $\mathbb{R}^3$, and this is the typical use of the coordinate space.

### L3 human

For any set $I$, the set $F^I$ of all functions $I \to F$ is a vector space under pointwise operations, and $F^n$ is the case $I = \{1, \dots, n\}$; the [[spaces of functions and sequences|0GZB2SN0PH]] study the general case.
For infinite $I$ the finitely supported functions form a smaller space $F^{(I)}$, the free vector space on $I$, and every vector space is isomorphic to one of these by the choice of a basis.
In the language of categories, $F^n$ is both the product and the coproduct of $n$ copies of the one-dimensional space $F$, that is, the [[direct sum|0XYYT5KNTX]] $F \oplus \dots \oplus F$.
Over a commutative ring $R$ in place of a field, the same tuples form the free module $R^n$, and much of linear algebra survives there.
