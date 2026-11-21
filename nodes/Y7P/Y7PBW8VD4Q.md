---
tag: Y7PBW8VD4Q
kind: concept
name: "Linear algebra: overview"
msc: ["15-01", "15A03", "15A04", "15A06"]
topics: [VKVAJ94SKZ]
audience: ug1
uses: [000AYPA9AJ, 0NRYHJPQG2, 0VD9ZSWWJG, 0GT4WWGWH2]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_algebra
    locator: History
  - url: https://en.wikipedia.org/wiki/Linear_algebra
    locator: Vector spaces
  - book: isbn:9781733146678
    locator: Chapter 1
  - book: isbn:9783031410253
    locator: Chapter 1
  - url: https://understandinglinearalgebra.org/
---

## Summary

Linear algebra is the mathematics of problems in which twice the cause gives twice the effect.
Its objects are [[vector spaces|000AYPA9AJ]], the [[linear maps|0NRYHJPQG2]] between them, and the [[systems of linear equations|0GT4WWGWH2]] that these maps describe.
A vector space is a set with an addition and a multiplication by numbers that obey the usual rules of arithmetic.
A linear map $T$ respects both operations:
$$T(u + v) = T(u) + T(v), \qquad T(c v) = c \, T(v).$$
In finite dimension a choice of bases turns each linear map into a [[matrix|0VD9ZSWWJG]] and each linear system into one matrix equation $A x = b$.
Linear problems can be solved completely, and that is why so much of applied mathematics works by reducing a hard problem to a linear one.

## Motivation

Many laws of nature and of economics are linear, at least for small changes.
Kirchhoff's laws for an electric circuit, the balance of a chemical reaction, the fit of a line to data and a finite-difference model of heat flow all lead to systems of linear equations, often with thousands of unknowns.
A calculator that solves one equation at a time is of no use there.
What you need is a theory that says when a system has a solution, how many solutions it has, and how to find them in a fixed number of steps.

Linear algebra gives that theory by looking at one problem in three ways.
Take the system $x + 2y = 5$ and $3x + 4y = 6$.
As equations, you eliminate $x$ and solve.
As matrices, you write
$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 5 \\ 6 \end{pmatrix}$$
and invert the matrix.
As a linear map, you look for the vector that $T(x, y) = (x + 2y, \; 3x + 4y)$ sends to $(5, 6)$.
All three give $x = -4$ and $y = \tfrac{9}{2}$.
Check: $-4 + 9 = 5$ and $-12 + 18 = 6$.
The equations give the algorithms, the matrices give a compact notation for computing, and the maps give the theory that explains the answers.

## Notation

Vectors are written $u, v, w$, sometimes in bold, and scalars $a, b, c$ or $\lambda$.
The space $F^n$ holds the columns of length $n$ with entries in a field $F$, and $\mathbb{R}^n$ is the case $F = \mathbb{R}$.
The space of linear maps from $V$ to $W$ is $\mathcal{L}(V, W)$ or $\operatorname{Hom}(V, W)$, and $M_{m \times n}(F)$ is the space of $m \times n$ matrices.
Most modern books treat vectors as columns, so that a matrix acts on the left; some older books use rows and put the matrix on the right, and then every formula appears transposed.

## Remarks

### Where linear algebra appears

The same structure turns up far from the systems of equations that started the subject.
The rotation of the plane by a right angle, $T(x, y) = (-y, x)$, is a linear map with the matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
The derivative $p \mapsto p'$ is a linear map on the polynomials of degree at most $2$, a space of dimension $3$.
The solutions of the differential equation $y'' + y = 0$ form a vector space of dimension $2$ with the basis $\cos t, \sin t$.
The best line through a cloud of data points, found by [[least squares|0BYTQ4X1HC]], is a projection in $\mathbb{R}^n$.
The long-run behavior of a [[Markov chain|0G48PYM96Q]] is an eigenvector of its transition matrix, or of the transpose in the other convention, for the eigenvalue $1$.

### What is not linear

Linearity is a strong condition, and it helps to see where it stops.
The system $x^2 + y = 1$, $x + y = 0$ is not linear because of the square, and its solution set is not flat: it is the two points where a parabola meets a line.
The map $x \mapsto x + 1$ on $\mathbb{R}$ is not linear, since a linear map must send $0$ to $0$; it is an affine map, a linear map followed by a shift.
The integers $\mathbb{Z}$ are not a vector space over the rational numbers, because $\tfrac{1}{2} \cdot 1$ is not an integer; they form a module over the ring $\mathbb{Z}$, which the area on rings and modules studies.

### The first facts

A few results carry most of the subject.
Every vector space has a basis, and in finite dimension all bases have the same size, the [[dimension|03GSZ8RTZJ]].
A linear map is fixed by its values on a basis, because every vector is a combination of basis vectors and the map respects combinations.
The [[rank-nullity theorem|0W4FSW1TVB]] says that for $T : V \to W$ with $V$ of finite dimension,
$$\dim V = \dim \ker T + \dim \operatorname{im} T.$$
A square system $A x = b$ has exactly one solution for every $b$ when $A$ is [[invertible|0EB9N0S33C]], and this happens exactly when $\det A \neq 0$.

### A map of the sub-areas

The sub-areas follow the usual order of a two-semester course.
The [[vectors in the plane and in space|VKVAJ94SKZ]] come first, with lengths, angles and the dot and cross products.
Then [[systems of linear equations|DXSXFVDMXQ]], [[matrices|Y1ESNQ2V52]] and [[invertible matrices|P8J6QR66TJ]] give the computational core.
The abstract theory follows: [[vector spaces|MVH97H8B2J]], [[linear maps|9080WQTZ3M]], [[direct sums and quotients|QHKTJ89V6S]], [[matrices of linear maps|S6559D61BP]] and [[duality|9K7FFF26QR]].
The study of one operator comes next, with [[determinants|DTBK11SR77]], [[eigenvalues|6R1D6QPY3S]], [[diagonalization|Z6S6PWMJPH]] and the [[canonical forms|GEBYZKYV3D]].

Lengths and angles return in the second half.
The [[inner product spaces|1D4JTZ9VS3]] generalize the dot product, and they lead to [[orthogonality and least squares|8GQVME4SZZ]], the [[spectral theorems|3YM9EK6VMB]], the [[isometries|AZS5BPF5H3]] and the [[singular value decomposition|SS4EVPKT3A]].
The [[bilinear forms|DYAK7YMK7B]] and [[quadratic forms|6TSCEW8QMK]] drop the condition of positivity, and the [[applications|K0FNC6CWZN]] close the area.

### Neighboring areas

Three areas continue where this one stops.
[[Matrix theory and multilinear algebra|WMBK7M313V]] studies matrices for their own sake, with norms, inequalities and tensors.
[[Functional analysis|AFJZYWP3WQ]] is linear algebra in infinite dimension, where topology enters through [[Hilbert spaces|HM2HHE3J51]] and [[Banach spaces|06GZ956657]].
[[Numerical analysis|FJEK0GMJ2J]] asks how to compute solutions, factorizations and eigenvalues fast and with small rounding errors.

### History

The method of elimination for linear systems appears in the Chinese text *The Nine Chapters on the Mathematical Art*.
Cramer published his rule for square systems in 1750, long before matrices existed.
Grassmann studied spaces of any dimension in 1844, Sylvester introduced the word "matrix" in 1850, and Cayley set out the algebra of matrices in 1858.
Peano gave the axioms of a vector space in 1888.

### Watch out

The most common loss in a first course is to treat a matrix as a table of numbers only and forget the map that it stands for.
For example, a student who knows that $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ is a quarter turn can see at once that its fourth power is $I$, with no multiplication at all.
A second loss is to compute a number, such as a determinant, without its meaning, here the factor by which areas change.
The essay on [[common errors|79YPKR857M]] collects more traps of this kind.

## Explanations

### L1 human

Linear algebra is the mathematics of straight lines, flat planes and their analogues in more dimensions.
It solves many equations at the same time.
For example, $x + 2y = 5$ and $3x + 4y = 6$ have the one solution $x = -4$ and $y = 4.5$.
It also describes the motions that keep straight lines straight, such as rotations, reflections and stretches.
Computers use it to draw three-dimensional pictures on a flat screen, to rank web pages and to compress images.

### L2 human

A first course walks through the three views in turn.
It starts with systems and elimination, and it describes the set of all solutions of a system.
Then it writes each system as $A x = b$, and it learns the product and the inverse of matrices.
Next it abstracts to vector spaces and linear maps, with bases and dimension.
After that it studies one map in detail, through its eigenvalues and eigenvectors, and it adds lengths and angles through inner products.

The typical problem turns into $A x = b$ or into $A v = \lambda v$.
Watch out: a calculation in coordinates depends on the basis.
Only some answers, such as the rank, the determinant and the eigenvalues of a map, stay the same in every basis, and those are the answers that describe the map itself.

### L3 human

From the point of view of algebra, linear algebra is the theory of modules over a field, and many of its results survive over a principal ideal domain with small changes.
The classification of one operator on a finite-dimensional space up to change of basis is the structure theorem for finitely generated modules over the polynomial ring $F[x]$.
The finite-dimensional vector spaces and the linear maps form a basic example of an abelian category with a duality, in which every object is isomorphic to its double dual.
Representation theory, differential geometry and quantum mechanics are all built on the linear structure of their objects.
