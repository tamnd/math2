---
tag: 01H6QKWGDH
kind: concept
name: Generalized eigenvector
msc: ["15A18"]
topics: [Z6S6PWMJPH]
audience: ug2
uses: [0N6960W0BV, 0J7H0YBFDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_eigenvector
    locator: Overview and definition
  - book: isbn:9783031410253
    locator: Chapter 8
  - book: isbn:9780134860244
    locator: Section 7.1
same_as:
  wikidata: Q970767
  wikipedia: Generalized eigenvector
---

## Summary

A generalized eigenvector is a vector that $T - \lambda$ does not send to zero at once, but sends to zero after a few steps.
These vectors repair the matrices that have too few eigenvectors, and they are the building blocks of the Jordan normal form.
Let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]] of a vector space $V$ over a field $F$, and let $\lambda \in F$.
A [[generalized eigenvector|0SAAHC36J9]] of $T$ for $\lambda$ is a vector $v \ne 0$ such that
$$(T - \lambda \id_V)^k v = 0 \quad \text{for some integer } k \ge 1.$$
The least such $k$ is the *rank* of $v$.
The generalized eigenvectors of rank $1$ are exactly the [[eigenvectors|0N6960W0BV]] for $\lambda$.

## Motivation

Some matrices do not have enough eigenvectors to make a basis.
The [[shear|SBDF8APDF7]] $S = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has only the line through $e_1$ as eigenvectors, so it is not [[diagonalizable|07SQCNV233]].
The vector $e_2$ is not an eigenvector, but $(S - I) e_2 = e_1$ is one, and so $(S - I)^2 e_2 = 0$.
If we allow higher powers of $S - I$, the vectors $e_1$ and $e_2$ together make a basis.

This repair always works when the characteristic polynomial splits, for example over $\C$.
Then $V$ has a basis of generalized eigenvectors, by the [[decomposition into generalized eigenspaces|0Z3GDY89T5]].
The [[Jordan normal form|085HQ5G5TE]] of the next sub-area arranges such a basis into chains.
In differential equations, the chains give the solutions of $x' = A x$ that contain factors $t e^{\lambda t}$, which appear exactly when $A$ has too few eigenvectors.

## Notation

We write $N_\lambda = T - \lambda \id_V$, or $N$ when $\lambda$ is fixed.
A *Jordan chain* of length $k$ is a list $v, N v, \dots, N^{k-1} v$ with $N^{k-1} v \ne 0$ and $N^k v = 0$.
Its last vector $N^{k-1} v$ is an eigenvector.
Some books list the chain in the other order, starting from the eigenvector, so check the order before you read off a matrix.
In Mathlib, the kernels $\ker N^k$ appear as `Module.End.genEigenspace`.

## Remarks

### A first chain

Take the shear $S$ and $\lambda = 1$.
Subtract the identity:
$$N = S - I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad N \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} y \\ 0 \end{pmatrix}.$$
Apply $N$ twice to any vector: the first step gives $(y, 0)$, and the second step gives $(0, 0)$.
So $N^2 = 0$, and every nonzero vector of $F^2$ is a generalized eigenvector for $1$.
A vector $(x, y)$ with $y = 0$ has rank $1$, and a vector with $y \ne 0$ has rank $2$.
For $e_2$ the chain is $e_2 \mapsto e_1 \mapsto 0$.

### Longer chains

For the [[Jordan block of size 3|1YGY396SAS]] with eigenvalue $2$, the map $N = J - 2I$ sends $e_3 \mapsto e_2 \mapsto e_1 \mapsto 0$.
So $e_3$ has rank $3$, $e_2$ has rank $2$, and $e_1$ is an eigenvector.

For the [[derivative on real cubic polynomials|7DGJWWZ8DW]] and $\lambda = 0$, a chain is
$$x^3 \mapsto 3x^2 \mapsto 6x \mapsto 6 \mapsto 0.$$
In the same way, every nonzero polynomial of degree $d \le 3$ is a generalized eigenvector for $0$ of rank $d + 1$.

The [[3 × 3 matrix with eigenvalues 1, 2, 2|18WSA33PKA]] has the generalized eigenvector $(0, 1, 0)$ for $2$, of rank $2$.
The [[matrix with the single eigenvalue 2|6918MS1QRN]] makes every nonzero vector of $\R^2$ a generalized eigenvector for $2$.

### Vectors that fail

The vector $(1, 1)$ is not a generalized eigenvector of $A = \operatorname{diag}(1, 2)$ for any scalar, as [[the sum of two eigenvectors|EWGV69Z2VZ]] shows.
For every $k \ge 1$,
$$(A - I)^k \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \qquad (A - 2I)^k \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} (-1)^k \\ 0 \end{pmatrix},$$
and $A - \lambda I$ is invertible for every other $\lambda$.
The zero vector is excluded by the definition, just as for eigenvectors.
The rotation of $\R^2$ by a right angle has no generalized eigenvectors over $\R$, because each one would produce a real eigenvector, as the next subsection shows.

### The rules you can use

If $v$ has rank $k$ for $\lambda$, then $N^{k-1} v$ is nonzero and $N$ sends it to $0$, so it is an eigenvector.
So a generalized eigenvector for $\lambda$ exists only when $\lambda$ is an [[eigenvalue|0BQAA2BK3Q]].

The vectors of a Jordan chain are linearly independent.
Suppose that $c_0 v + c_1 N v + \dots + c_{k-1} N^{k-1} v = 0$.
Apply $N^{k-1}$: every term except the first contains $N^j v$ with $j \ge k$, so $c_0 N^{k-1} v = 0$ and $c_0 = 0$.
Then apply $N^{k-2}$ to get $c_1 = 0$, and go on in the same way.

The chain lies in the [[generalized eigenspace|0AJ035ZTZE]] of $\lambda$, so the rank is at most its dimension.
By the [[dimension of the generalized eigenspace|PHZ684KGWS]], that dimension is the [[algebraic multiplicity|0FY42N02DV]] of $\lambda$.
Generalized eigenvectors for distinct eigenvalues are linearly independent, by the [[kernels lemma|ACBNK1VFVG]], because $(t - \lambda)^k$ and $(t - \mu)^l$ are coprime when $\lambda \ne \mu$.

### Watch out

A generalized eigenvector for $\lambda$ is not an eigenvector of $T^k$.
For the shear, $e_2$ is a generalized eigenvector for $1$, but
$$S^2 e_2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix},$$
which is not a multiple of $e_2$.
The correct move is to take powers of $T - \lambda$, not of $T$.
The two ideas agree only for $\lambda = 0$.

A second trap is to add generalized eigenvectors for different eigenvalues.
The sum $e_1 + e_2$ for $\operatorname{diag}(1, 2)$ above is the failing case.

### History

Camille Jordan published the normal form that carries his name in his treatise on substitutions of 1870.
Each block of that form is the matrix of $T$ on one chain of generalized eigenvectors.

### Try it

First, let $A = \begin{pmatrix} 5 & 1 \\ 0 & 5 \end{pmatrix}$ and find the rank of $(3, 2)$ for $\lambda = 5$.
The vector $(A - 5I)(3, 2) = (2, 0)$ is not zero, and $(A - 5I)^2 = 0$, so the rank is $2$.

Second, find the rank of $1 + x^2$ for the derivative $D$ on real cubic polynomials.
We get $D(1 + x^2) = 2x$, then $D^2(1 + x^2) = 2$, then $D^3(1 + x^2) = 0$, so the rank is $3$.

## Explanations

### L1 human

An eigenvector is a direction that a matrix only stretches.
Some matrices, like the shear, have too few such directions.
A generalized eigenvector is a vector that becomes zero after we subtract the stretch and apply the result a few times.
For the shear, the vector $(0, 1)$ goes to $(1, 0)$ after one step and to $(0, 0)$ after two steps.
So it is a generalized eigenvector of rank $2$, and together with $(1, 0)$ it fills the plane.

### L2 human

Solve $x' = A x$ with $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$.
The only eigenvalue is $2$, and $A - 2I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has the kernel $\R e_1$.
So $e^{2t} e_1$ is one solution, but we need a second one.

The vector $e_2$ is a generalized eigenvector of rank $2$, with $(A - 2I) e_2 = e_1$.
Try the chain solution
$$x(t) = e^{2t} \big( e_2 + t \, e_1 \big) = e^{2t} \begin{pmatrix} t \\ 1 \end{pmatrix}.$$
Differentiate with the product rule:
$$x'(t) = e^{2t} \begin{pmatrix} 2t + 1 \\ 2 \end{pmatrix}, \qquad A x(t) = e^{2t} \begin{pmatrix} 2t + 1 \\ 2 \end{pmatrix}.$$
Check: the two sides agree, so $x$ is a solution, and it is independent of $e^{2t} e_1$.
The problem shows the typical use: an eigenvector gives a pure exponential, and each further step of a chain adds one power of $t$.

### L3 human

Make $V$ a module over $F[t]$ by letting $t$ act as $T$.
The generalized eigenvectors for $\lambda$, together with $0$, form the $(t - \lambda)$-primary part of this module.
When the characteristic polynomial does not split, the [[primary decomposition theorem|49ZHBMYKVE]] uses the vectors killed by a power of an irreducible factor $p(T)$ instead.
In infinite dimension the rank can be unbounded, as for the derivative on all polynomials.
The sub-area on canonical forms turns chains into cyclic subspaces and proves the Jordan normal form from them.
