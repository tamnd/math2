---
tag: 4C6EBHFF3R
kind: concept
name: Linear algebra without determinants
msc: ["15A18", "15-01", "97H60"]
topics: [VKVAJ94SKZ]
audience: ug1
uses: [Y7PBW8VD4Q, 0BQAA2BK3Q, 00KDZRW4C0, 03NDVCSHSB]
sources:
  - book: isbn:9783031410253
    locator: Preface
  - book: isbn:9783031410253
    locator: Chapter 5
  - book: isbn:9783031410253
    locator: Chapter 9
  - book: isbn:9783319110790
    locator: Chapter 10
  - book: isbn:9780135367971
    locator: Chapter 5
  - book: isbn:9780134860244
    locator: Chapter 4
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenvalues and the characteristic polynomial
---

## Summary

Linear algebra without determinants is a way to build the theory of [[eigenvalues|0BQAA2BK3Q]] that explains why they exist before any [[determinant|00KDZRW4C0]] appears.
Axler set it out in the article "Down with determinants!" in the *American Mathematical Monthly* 102 (1995) and in his textbook *Linear Algebra Done Right*.
The eigenvalues come from polynomials in the operator, and in later editions from the [[minimal polynomial|03NDVCSHSB]], instead of from the characteristic polynomial $\det(A - \lambda I)$.
The main structure theorems, from the existence of an eigenvalue to the spectral theorem, are proved first, and the determinant is defined at the end as a volume.

## Motivation

In a determinant-first course, a number $\lambda$ is an eigenvalue of $A$ when $\det(A - \lambda I) = 0$.
The test is quick for a $2 \times 2$ matrix, but its proof needs the whole theory of determinants, and many students find that theory hard to see through.
Axler asked whether the theory of eigenvalues needs determinants at all.
The answer is no.
One count of dimensions and the fundamental theorem of algebra already prove that every operator on a nonzero complex space has an eigenvalue, and the proof shows where the eigenvalue comes from.

## Notation

The space of linear operators on $V$ is $\mathcal{L}(V)$.
A polynomial $p(z) = a_0 + a_1 z + \dots + a_m z^m$ gives the operator
$$p(T) = a_0 I + a_1 T + \dots + a_m T^m.$$
The minimal polynomial of $T$ is the monic polynomial $p$ of least degree with $p(T) = 0$.
Watch out for the sign convention: some books write the characteristic polynomial as $\det(A - \lambda I)$ and others as $\det(\lambda I - A)$, and the two differ by the factor $(-1)^n$.

## Remarks

### The proof that an eigenvalue exists

Let $V \neq 0$ be a complex vector space of dimension $n$, let $T \in \mathcal{L}(V)$, and pick any $v \neq 0$.
The $n + 1$ vectors $v, Tv, \dots, T^n v$ live in a space of dimension $n$, so they are linearly dependent.
That means $p(T) v = 0$ for some nonzero polynomial $p$ of degree at most $n$.
The polynomial $p$ is not a constant, since $a_0 v = 0$ with $v \neq 0$ forces $a_0 = 0$.
By the [[fundamental theorem of algebra|0JP0W07Y9A]] it factors as $p(z) = c (z - \lambda_1) \cdots (z - \lambda_m)$ with $c \neq 0$, so
$$c (T - \lambda_1 I) \cdots (T - \lambda_m I) v = 0.$$
A product of injective operators is injective, so some factor $T - \lambda_j I$ is not injective, and that $\lambda_j$ is an eigenvalue.

### The proof with numbers

Take the quarter turn $T(x, y) = (-y, x)$ on $\mathbb{C}^2$ and $v = (1, 0)$.
Apply $T$ twice:
$$T v = (0, 1), \qquad T^2 v = (-1, 0) = -v.$$
So $T^2 v + v = 0$, and the polynomial is $p(z) = z^2 + 1 = (z - i)(z + i)$.
The vector $w = (T + iI) v = (i, 1)$ is nonzero, and the other factor sends it to $0$.
Check: $T(i, 1) = (-1, i) = i \, (i, 1)$, so $i$ is an eigenvalue with the eigenvector $(i, 1)$.

### Where the proof fails

The argument needs a field in which every polynomial has a root.
Over $\mathbb{R}$ the same quarter turn of $\mathbb{R}^2$ has no eigenvalue at all, because $z^2 + 1$ has no real root, and no vector in the plane keeps its direction under a quarter turn.
Determinant-free also does not mean that determinants are absent.
Axler defines them late, in chapter 9 of the fourth edition, and uses them for volume.

### What the approach proves

The same method gives, without determinants, the main theorems on one operator.
Every operator on a finite-dimensional complex space has an [[upper triangular|0N4XY7Z3NN]] matrix in some basis.
The [[spectral theorem|06J4PXRG22]] and the [[Jordan form|085HQ5G5TE]] follow.
The eigenvalues of $T$ are exactly the zeros of the minimal polynomial.
The [[characteristic polynomial|0VSSPAFM2C]] is defined from the eigenvalues and their multiplicities, and it agrees with $\det(zI - T)$ once determinants are available.

### What is gained and what is lost

The gain is a proof that shows why an eigenvalue exists, proofs that work for operators and not only for matrices, and less weight on one long computation.
The loss is the quick test $\det(A - \lambda I) = 0$ for small matrices, and [[Cramer's rule|0977KZ6PQB]].
The meaning of the determinant as a signed volume, and its role in the change of variables of multiple integrals, also comes late.
Older books, such as Hoffman and Kunze or Friedberg, Insel and Spence, treat determinants first, and their chapters on eigenvalues use $\det(A - \lambda I)$ throughout.
In numerical practice neither route is used: the eigenvalues of a large matrix come from iterative methods such as the QR algorithm, not from the roots of a polynomial.

### History

Determinants are older than matrices.
Seki and Leibniz used them in the 17th century, and Cramer published his rule in 1750.
For a long time textbooks defined eigenvalues through determinants.
Axler's article of 1995 and his book made the determinant-free route common in proof-based courses.

### Watch out

The approach does not avoid polynomials; it uses polynomials in $T$ in an essential way.
It also does not work over every field: the existence of an eigenvalue needs an algebraically closed field such as $\mathbb{C}$, as the real quarter turn shows.

## Explanations

### L1 human

An eigenvector of a transformation is a direction that the transformation only stretches, without turning it.
Many books find these directions with a special number, the determinant.
Axler found a way to prove that such directions exist without this number.
His proof uses one fact about polynomials: every polynomial equation, such as $z^2 + 1 = 0$, has a solution among the complex numbers.

### L2 human

Here are both routes for the matrix $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
The determinant route expands one determinant:
$$\det(A - \lambda I) = (2 - \lambda)^2 - 1 = (\lambda - 1)(\lambda - 3),$$
so the eigenvalues are $1$ and $3$.
The polynomial route starts with $v = (1, 0)$ and applies $A$ twice, which gives $A v = (2, 1)$ and $A^2 v = (5, 4)$.
These three vectors in the plane are dependent, and a short search finds the relation:
$$A^2 v - 4 A v + 3 v = (5 - 8 + 3, \; 4 - 4 + 0) = (0, 0).$$
So $p(z) = z^2 - 4z + 3 = (z - 1)(z - 3)$, and both routes give $1$ and $3$.

The polynomial route is the one to use in proofs about operators, and the determinant route is the one to use for a small matrix by hand.
Watch out: the polynomial depends on $v$.
For an eigenvector such as $v = (1, 1)$ the relation $A v - 3 v = 0$ already holds, and the polynomial of least degree is $z - 3$, which finds only one eigenvalue.

### L3 human

The polynomial route is the module view of linear algebra.
The operator $T$ makes $V$ a module over $\mathbb{C}[z]$, with $z$ acting as $T$, and the minimal polynomial generates the annihilator of that module.
The structure theorem for modules over a principal ideal domain then gives the canonical forms, as in the sub-area on [[canonical forms|GEBYZKYV3D]].
The determinant stays the right tool for volume, orientation and the exterior algebra, as in the sub-area on [[determinants|DTBK11SR77]].
