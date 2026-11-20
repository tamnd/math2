---
tag: 0HYFWKKY3C
kind: concept
name: Polar form of a quadratic form
msc: [15A63, "11E04"]
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

Let $Q$ be a [[quadratic form|0RBQS1JJCR]] on a vector space $V$ over a field $F$.
The *polar form* of $Q$ is the map $b_Q \colon V \times V \to F$ with
$$b_Q(u, v) = Q(u + v) - Q(u) - Q(v).$$
By the definition of a quadratic form, $b_Q$ is a [[bilinear form|0SQZMXB6GP]], and it is [[symmetric|0AXZNE5XNH]] with $b_Q(v, v) = 2Q(v)$.
When the characteristic of $F$ is not $2$, many books call $B = \frac12 b_Q$ the polar form; it is the [[associated symmetric bilinear form|0KRVRV5V80]], with $B(v, v) = Q(v)$.
Outside characteristic $2$, the map $Q \mapsto \frac12 b_Q$ is [[a bijection from quadratic forms to symmetric bilinear forms|VN9AG8JKYT]].
So each question about $Q$ becomes a question about a symmetric matrix.

## Motivation

A quadratic form is a function of one vector, but many of its uses need two vectors.
Orthogonality, the matrix of the form and the tests for nondegeneracy are statements about pairs $(u, v)$.
The polar form recovers this two-vector object from $Q$.
For the squared length $Q(v) = \norm{v}^2$ on $\R^n$, it gives $b_Q(u, v) = 2\, u \cdot v$, so the dot product is half the polar form of the squared length.
This is the [[polarization identity|05FKHRT0B4]] of inner product spaces.

## Notation

- We write $b_Q$ for $Q(u + v) - Q(u) - Q(v)$, without the factor $\frac12$. This form exists in every characteristic.
- Outside characteristic $2$ we write $B$ or $B_Q$ for $\frac12 b_Q$.
- The factor varies between books: some use $\frac12 b_Q$ and call it the polar form, others use $b_Q$ itself. This page writes the factor each time.
- Another formula outside characteristic $2$ is $B(u, v) = \frac14 \bigl( Q(u + v) - Q(u - v) \bigr)$.

## Remarks

### Examples

- For $Q(x, y) = x^2 + xy$ on $\R^2$, [[the polar form|V5AKNSKQNG]] is $b_Q(u, v) = 2xx' + xy' + x'y$.
- For [[the determinant on $2 \times 2$ matrices|BQQZX1QS4S]], the polar form is $ad' + a'd - bc' - b'c$.
- For the squared length on $\R^n$, $b_Q(u, v) = 2 \sum_i u_i v_i$, and $B$ is the dot product.
- For $Q(x) = x^T A x$ with $A$ symmetric and $2 \ne 0$ in $F$, $b_Q(x, y) = 2\, x^T A y$, so $B(x, y) = x^T A y$.
- Over the field $\F_2$, the form $Q(x) = x^2$ has $b_Q(u, v) = 2uv = 0$. So [[its polar form is zero|ZEGSCCVGZF]], although $Q \ne 0$.

### Non-examples

- [[The bilinear form $u_1 v_2$ on $\R^2$|WW5X7DHHQ6]] is not the polar form of any quadratic form, because it is not symmetric.
- The function $Q(u + v) - Q(u) - Q(v)$ for $Q(x) = x^3$ on $\R$ is $3u^2 v + 3uv^2$. It is not bilinear, because $Q$ is not a quadratic form.

### Basic properties

- $b_Q$ is symmetric, because the formula does not change when $u$ and $v$ are exchanged.
- $b_Q(v, v) = Q(2v) - 2Q(v) = 4Q(v) - 2Q(v) = 2Q(v)$.
- So, in characteristic $2$, $b_Q(v, v) = 0$ for all $v$: the polar form is alternating.
- Outside characteristic $2$, $Q$ and $B = \frac12 b_Q$ determine each other, by [[the correspondence theorem|VN9AG8JKYT]].
- The matrix of $B$ in a basis is the symmetric matrix of $Q$. The matrix of $b_Q$ is twice that matrix.
- The polar form is compatible with linear maps: $b_{Q \circ T}(u, v) = b_Q(Tu, Tv)$.

### History

The method of passing from a homogeneous polynomial to a symmetric multilinear form is called polarization.
The Wikipedia article on the polarization of an algebraic form treats the quadratic case as its first example.
We found no source in this node for the first use of the term, so we give no date.

### Common errors

- Students forget the factor $\frac12$ and use $b_Q$ as the matrix of $Q$. Then $x^T (\text{matrix of } b_Q) x = 2Q(x)$, not $Q(x)$.
- Students divide by $2$ in characteristic $2$. There $b_Q(v, v) = 0$, and $Q$ cannot be recovered from $b_Q$.
- Students think that every symmetric bilinear form in characteristic $2$ is a polar form. Polar forms are alternating there, so the form $uv$ on $\F_2$ is not one.

## Explanations

### L1 human

A quadratic form gives one number for each vector.
The polar form gives one number for each pair of vectors.
It measures how far $Q$ is from being additive: it is the error $Q(u + v) - Q(u) - Q(v)$.
For the squared length in the plane, $u = (1, 0)$ and $v = (1, 1)$ give $5 - 1 - 2 = 2$, which is twice the dot product $u \cdot v = 1$.

### L2 human

Worked example: we compute the polar form of $Q(x, y) = 3x^2 - 2xy + y^2$ and its matrix.

1. For $u = (x, y)$ and $v = (x', y')$, $b_Q(u, v) = 6xx' - 2(xy' + x'y) + 2yy'$.
2. Half of it is $B(u, v) = 3xx' - xy' - x'y + yy'$.
3. The matrix of $B$ is $\begin{pmatrix} 3 & -1 \\ -1 & 1 \end{pmatrix}$.
4. Check: $B(u, u) = 3x^2 - 2xy + y^2 = Q(u)$.

The typical use: $u$ and $v$ are orthogonal for $Q$ when $B(u, v) = 0$.
Here $(1, 0)$ and $(1, 3)$ are orthogonal, since $B = 3 - 3 = 0$.
A trap: orthogonality for $Q$ is not orthogonality for the dot product; $(1, 0) \cdot (1, 3) = 1 \ne 0$.

### L3 human

Polarization is the passage from a homogeneous polynomial of degree $d$ to a symmetric $d$-linear form, and it needs division by $d!$.
For $d = 2$ the obstruction is the prime $2$, and in characteristic $2$ quadratic forms and symmetric bilinear forms are different objects.
There the polar form of a quadratic form is alternating.
An alternating form can be nondegenerate only in even dimension, so in odd dimension the polar form is always degenerate.
The general theory of symmetric and alternating bilinear forms is in the topic on [[bilinear and sesquilinear forms|DYAK7YMK7B]].
