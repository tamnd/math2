---
tag: 0ZD2CF6ZS0
kind: concept
name: Dual basis
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug1
specializes: [0KCQ9Y3QKA]
uses: [07JBSZE0V4, 0KCQ9Y3QKA, 04CYQHN6MC, 0R8X9XA83A]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_basis
    locator: Finite-dimensional vector spaces
  - url: https://en.wikipedia.org/wiki/Dual_basis
    locator: Examples
  - book: isbn:9783031410253
    locator: Section 3F
  - book: isbn:9780134860244
    locator: Section 2.6
same_as:
  wikidata: Q2297777
  wikipedia: Dual basis
---

## Summary

A basis lets us describe each vector by a list of coordinates, and the dual basis is the list of rules that compute those coordinates.
These rules are linear forms, and together they form a basis of the dual space.
Let $V$ be a finite-dimensional vector space over a field $F$ with a [[basis|0KCQ9Y3QKA]] $b_1, \dots, b_n$.
The *dual basis* is the family of [[linear forms|07YQ1C78G0]] $b_1^*, \dots, b_n^*$ in the [[dual space|07JBSZE0V4]] $V^*$ with
$$b_i^*(b_j) = \delta_{ij} = \begin{cases} 1 & \text{if } i = j, \\ 0 & \text{if } i \ne j. \end{cases}$$
Equivalently, $b_i^*$ reads off coordinate $i$: $b_i^*(a_1 b_1 + \dots + a_n b_n) = a_i$.
The [[formal definition|0W6M3PSD08]] states it, and the dual basis is a basis of $V^*$, so $\dim V^* = \dim V$.

## Motivation

The [[coordinates|04CYQHN6MC]] of a vector in a basis depend linearly on the vector: the coordinates of $u + v$ are the sums of the coordinates of $u$ and of $v$.
So each coordinate is a linear form, and the dual basis is the name of these forms.
With them, a vector and a form can both be expanded in the basis by evaluation, without solving equations:
$$v = \sum_{i=1}^n b_i^*(v)\, b_i, \qquad f = \sum_{i=1}^n f(b_i)\, b_i^*.$$

The dual basis appears wherever a problem gives values at some points and asks for a function.
Interpolation, quadrature rules and the components of tensors in physics are all expansions in a dual basis.
It also explains the [[change of dual basis rule|SXWX10HSB6]], by which forms change with the inverse transpose of the matrix that changes vectors.

## Notation

The dual basis of $b_1, \dots, b_n$ is written $b_1^*, \dots, b_n^*$, or $b^1, \dots, b^n$ with upper indices in physics and differential geometry.
The defining condition uses the Kronecker delta: $b_i^*(b_j) = \delta_{ij}$.
The notation $b_i^*$ is misleading in one way: $b_i^*$ depends on the whole basis, not only on the vector $b_i$.
Mathlib writes `Module.Basis.dualBasis`.

## Remarks

### A first computation

Take the basis $b_1 = (1, 1)$, $b_2 = (1, 2)$ of $\R^2$ and look for $b_1^*(x, y) = px + qy$.
The two conditions $b_1^*(b_1) = 1$ and $b_1^*(b_2) = 0$ read
$$p + q = 1, \qquad p + 2q = 0,$$
so $q = -1$ and $p = 2$, and $b_1^* = 2x - y$.
In the same way $b_2^* = -x + y$.
The [[worked example|YMRSMANN2E]] finds both forms at once as the rows of the inverse of the matrix with columns $b_1, b_2$, and it uses them to find the coordinates $(1, 2)$ of the vector $(3, 5)$.

For the standard basis $e_1, \dots, e_n$ of $F^n$, the dual basis is the family of coordinate forms $e_i^*(x) = x_i$, the [[rows of the identity matrix|EGJXHX96R9]].

### Values at points as a dual basis

On the space $P_2(\R)$ of polynomials of degree at most $2$, the three evaluations $p \mapsto p(0)$, $p \mapsto p(1)$ and $p \mapsto p(2)$ are the [[dual basis of the Lagrange basis|J8RDPQXN1Z]] for the nodes $0, 1, 2$.
So the expansion of a form in this dual basis is a formula in the three values $p(0), p(1), p(2)$.
For the integral over $[0, 2]$ it gives Simpson's rule,
$$\int_0^2 p(t)\,dt = \tfrac{1}{3} p(0) + \tfrac{4}{3} p(1) + \tfrac{1}{3} p(2),$$
which is exact for every $p$ of degree at most $2$.

### The rules you can use

The dual basis is a basis of $V^*$, and this is the main step in the proof of the [[dimension of the dual space|00889YD15K]].
The two expansions in the Motivation hold because two linear maps that agree on a basis are equal, by the [[theorem on maps determined by a basis|0R8X9XA83A]].
If the basis vectors are the columns of an invertible matrix $P$ in $F^n$, then the dual forms are the rows of $P^{-1}$, since $P^{-1} P = I$ says that row $i$ of $P^{-1}$ applied to column $j$ of $P$ gives $\delta_{ij}$.
If a new basis is $c_j = \sum_i p_{ij} b_i$, then the new dual forms are $c_k^* = \sum_i q_{ik} b_i^*$ with $Q = (P^{-1})^{\mathsf{T}}$, by the [[change of dual basis lemma|SXWX10HSB6]].
Finally, the dual basis of $b_1^*, \dots, b_n^*$ in $V^{**}$ is the image of $b_1, \dots, b_n$ under the evaluation map of the [[double dual theorem|0ZJM9D7NPS]].

### What it is not

In infinite dimension there is no dual basis in the sense above.
The [[coordinate forms of an infinite basis|JCMJDY59CH]] are linearly independent in $V^*$, but they do not span $V^*$.
On the space of finitely supported sequences, the form that adds up all terms is not a finite combination of coordinate forms.

The form $b_1^*$ is also not determined by $b_1$ alone.
Keep $b_1 = (1, 1)$ and change $b_2$ from $(1, 2)$ to $(1, 0)$.
Then $b_1^*$ changes from $2x - y$ to $y$, since $y$ is $1$ at $(1, 1)$ and $0$ at $(1, 0)$.

### Watch out

The map $b_i \mapsto b_i^*$ is an isomorphism $V \to V^*$, but it depends on the whole basis.
On $\R^2$, the standard basis sends $(1, 1) = e_1 + e_2$ to the form $x + y$.
The basis $(1, 1), (1, 2)$ sends the same vector $(1, 1) = b_1$ to $2x - y$.
So no basis gives a preferred isomorphism, and the [[non-canonical isomorphism|A3CP855PNV]] works this out.

A second error is to change dual bases with $P$ or $P^{\mathsf{T}}$.
If every basis vector is doubled, $c_j = 2b_j$, then every coordinate is halved, so $c_j^* = \tfrac{1}{2} b_j^*$, and this matches $(P^{-1})^{\mathsf{T}} = \tfrac{1}{2} I$.

### History

Gibbs, in his vector analysis, used the reciprocal system of three vectors in space, which is the dual basis carried into space by the dot product.
In the tensor calculus of Ricci and Levi-Civita, published in 1900, the covariant and contravariant components of a vector are its coordinates in a dual basis and in a basis.

### Try it

First, find the dual basis of $b_1 = (1, 0)$, $b_2 = (1, 1)$ in $\R^2$.
The answer is $b_1^* = x - y$ and $b_2^* = y$; check that $x - y$ gives $1$ at $(1, 0)$ and $0$ at $(1, 1)$.

Second, use it to find the coordinates of $v = (3, 5)$ in this basis.
They are $b_1^*(v) = -2$ and $b_2^*(v) = 5$, and indeed $-2 \cdot (1, 0) + 5 \cdot (1, 1) = (3, 5)$.

## Explanations

### L1 human

A basis lets us describe each vector by a list of coordinates.
The dual basis is the list of rules that compute these coordinates.
The first rule returns the first coordinate, the second rule returns the second coordinate, and so on.
So each rule gives $1$ on its own basis vector and $0$ on the others.
For the basis $(1, 1), (1, 2)$ of the plane, the rule $2x - y$ gives the first coordinate.

### L2 human

In $F^n$ the dual basis comes from one matrix inversion.
Put the basis vectors $b_1, \dots, b_n$ as the columns of a matrix $P$ and compute $P^{-1}$.
Row $i$ of $P^{-1}$ is the form $b_i^*$, because entry $(i, j)$ of $P^{-1} P = I$ is row $i$ of $P^{-1}$ applied to $b_j$.

For $b_1 = (1, 1)$ and $b_2 = (1, 2)$ we get
$$P = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}, \qquad P^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix},$$
so $b_1^* = 2x - y$ and $b_2^* = -x + y$.
The typical use is to find coordinates, since the coordinate column of $v$ is $P^{-1} v$, whose entries are the values $b_i^*(v)$.
Watch out: the form $b_1^*$ is not the vector $b_1$ written as a row, since $(1, 1)$ as a row is $x + y$, which gives $3$ at $b_2$.

### L3 human

A basis of $V$ is the same as an isomorphism $F^n \to V$, and the dual basis is its inverse $V \to F^n$, read one coordinate at a time.
The change rule with $(P^{-1})^{\mathsf{T}}$ is why lower-index and upper-index quantities transform differently in tensor calculus.
With an inner product, each $b_i^*$ is represented by a vector $b^i$ with $\langle b^i, b_j \rangle = \delta_{ij}$, the reciprocal basis of crystallography.
In infinite dimension, a basis $B$ still gives an injective map $V \to V^*$ by $b \mapsto b^*$, but its image consists only of the forms that vanish on all but finitely many elements of $B$.
