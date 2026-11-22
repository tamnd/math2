---
tag: 0RP20HFYM3
kind: concept
name: Positive definite quadratic form
aliases: [positive-definite-quadratic-form]
msc: [15A63, "11E04"]
topics: [6TSCEW8QMK]
audience: ug1
specializes: [0RBQS1JJCR]
uses: [0RBQS1JJCR, 0KX66CZMBB, 0Z3FEWZ8HA, 0VGSYBWHV2]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_quadratic_form
    locator: lead section
  - url: https://understandinglinearalgebra.org/sec-quadratic-forms.html
  - book: isbn:9780321982384
inventory: [R63EXRT7EA]
---

## Summary

A positive definite form is a quadratic form that behaves like a squared length: it is positive at every vector except the zero vector.
These forms are exactly the forms that come from inner products, so they are the forms that give a geometry of lengths and angles.
Let $V$ be a finite-dimensional real vector space.
A [[quadratic form|0RBQS1JJCR]] $Q$ on $V$ is *positive definite* when
$$Q(v) > 0 \qquad \text{for every } v \in V \text{ with } v \ne 0.$$
The [[formal definition|00QN1N6MNT]] states this condition.
For $Q(x) = x^{\mathsf{T}} A x$ on $\mathbb{R}^n$ with $A$ symmetric, the condition says that $A$ is a [[positive definite matrix|0KX66CZMBB]].
In the language of [[signature|07EZA80NEH]], $Q$ is positive definite exactly when its inertia is $(p, q, r) = (n, 0, 0)$ with $n = \dim V$.

## Motivation

The squared length $x_1^2 + \dots + x_n^2$ is positive at every nonzero vector, and this property is what lets it measure size.
Many other forms share the property.
The kinetic energy of a system of masses, written in general coordinates of the positions, is one example.
The covariance form of random variables with no exact linear relation is another.
Each such form defines its own notion of length, so it is useful to decide from the coefficients whether a given form is positive definite.

The question also comes from calculus.
At a critical point of a smooth function of several variables, a positive definite second derivative form means a strict local minimum, as in [[the five types of forms|01RBSSGMY5]].
The tests of the sub-area on [[positive definite matrices|0KX66CZMBB]] answer the question for matrices, and this concept is the same idea seen from the side of the form.

## Notation

Books write $Q > 0$ for a positive definite form and $A \succ 0$ for its matrix.
The weaker condition $Q(v) \ge 0$ for all $v$ is written $Q \ge 0$ or $A \succeq 0$, and it is called positive semidefinite.
Some older books say "definite" alone and mean "positive definite", so check the convention of the book before you read a theorem.

## Remarks

### A first test by squares

Take $Q(x, y) = x^2 + xy + y^2$.
The cross term $xy$ is negative when $x$ and $y$ have opposite signs, so it is not obvious that $Q$ stays positive.
[[Completing the square|XNCV97HTZ8]] settles the question:
$$x^2 + xy + y^2 = \left( x + \tfrac{1}{2} y \right)^2 + \tfrac{3}{4} y^2.$$
Check: the square expands to $x^2 + xy + \tfrac{1}{4} y^2$, and adding $\tfrac{3}{4} y^2$ gives back $Q$.
Both terms are at least $0$, and their sum is $0$ only when $y = 0$ and then $x = 0$.
So $Q$ is positive definite, and [[the full example|TZETVDBJG9]] confirms it with eigenvalues and minors.

### Three more positive forms

The sum of squares $x_1^2 + \dots + x_n^2$ is positive definite, since a sum of squares is $0$ only when each term is $0$.
The form with matrix $\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$ is positive definite, because its eigenvalues are $3$ on $(1, -1)$ and $1$ on $(1, 1)$.
Its matrix has negative entries, so negative entries do not stop a form from being positive.

For a real matrix $M$ with independent columns, the form $Q(x) = \lVert Mx \rVert^2 = x^{\mathsf{T}} M^{\mathsf{T}} M x$ is positive definite.
It is a squared length, so it is at least $0$, and it is $0$ only when $Mx = 0$.
Independent columns mean that $Mx = 0$ forces $x = 0$.
This is the [[Gram matrix|0AM050KCAW]] construction, and it gives every positive definite form.

### What fails to be positive definite

The form $x^2$ on $\mathbb{R}^2$ is at least $0$ everywhere, but $Q(0, 1) = 0$ at a nonzero vector.
So it is positive semidefinite and not positive definite.
The form $x^2 - y^2$ fails more strongly, since $Q(0, 1) = -1 < 0$, and it is indefinite.
The form $2x^2 + 6xy + 4y^2$ has only positive coefficients, but [[it takes the value -2 at (3, -2)|HS1DY318PY]].

### Four tests that agree

Let $A$ be a real symmetric $n \times n$ matrix and $Q(x) = x^{\mathsf{T}} A x$.
The following conditions are equivalent, and each one gives a practical test.

1. $Q$ is positive definite.
2. Every eigenvalue of $A$ is positive, by [[the eigenvalue test|0HYC2RHD3M]].
3. Every leading principal minor of $A$ is positive, by [[Sylvester's criterion|0WKEF78PMV]].
4. Completing squares, as in [[the diagonalization theorem|0Z3FEWZ8HA]], gives $n$ positive coefficients, and [[Sylvester's law of inertia|0WFED3K3DQ]] makes this count independent of the method.
5. $A = R^{\mathsf{T}} R$ with $R$ upper triangular and with a positive diagonal, by [[the Cholesky decomposition|0WKG8CYY6A]].

For a $2 \times 2$ form $ax^2 + bxy + cy^2$ the minors test reads $a > 0$ and $ac - \tfrac{1}{4} b^2 > 0$.
For $x^2 + xy + y^2$ this is $1 > 0$ and $1 - \tfrac{1}{4} = \tfrac{3}{4} > 0$.

### The rules you can use

The sum of two positive definite forms is positive definite, since a sum of two positive numbers is positive.
A positive multiple $cQ$ with $c > 0$ is positive definite for the same reason.
The restriction of $Q$ to a subspace $W$ is positive definite on $W$, because the condition for $v \in W$ is one of the conditions for $v \in V$.
A form $Q$ is positive definite if and only if its [[polar form|0HYFWKKY3C]] $B(v, w) = \tfrac{1}{2}\bigl(Q(v + w) - Q(v) - Q(w)\bigr)$ is an [[inner product|0VGSYBWHV2]], and then $Q(v) = B(v, v)$ is the squared norm.

### Watch out

Do not judge a form by its diagonal entries.
Positive diagonal entries are necessary, because $Q(e_i) = a_{ii}$, but they are not enough: $2x^2 + 6xy + 4y^2$ has positive diagonal entries $2$ and $4$ and still takes negative values.

Do not use the leading minors to test for semidefinite forms.
The matrix $\operatorname{diag}(0, -1)$ has leading minors $0$ and $0$, which looks harmless, but $Q(0, 1) = -1$.
For semidefinite forms you need all principal minors, or the eigenvalues.

Do not forget the factor $\tfrac{1}{2}$ in the matrix.
The form $x^2 + xy + y^2$ has matrix $\begin{pmatrix} 1 & 1/2 \\ 1/2 & 1 \end{pmatrix}$, with determinant $\tfrac{3}{4}$.
With $1$ in place of $\tfrac{1}{2}$ the determinant would be $0$, and the minors test would give the wrong answer.

### Try it

First, decide whether $3x^2 - 2xy + y^2$ is positive definite.
Its matrix $\begin{pmatrix} 3 & -1 \\ -1 & 1 \end{pmatrix}$ has minors $3 > 0$ and $3 - 1 = 2 > 0$, so it is positive definite.

Second, find all $t$ for which $x^2 + 2txy + y^2$ is positive definite.
The minors are $1$ and $1 - t^2$, so the form is positive definite exactly when $-1 < t < 1$.

## Explanations

### L1 human

A positive definite form gives a positive number for every arrow except the zero arrow.
Its graph over the plane is a bowl whose lowest point is the origin.
The squared length $x^2 + y^2$ is the simplest example: at $(3, 4)$ it gives $25$.
The form $x^2 + xy + y^2$ is another bowl, a little squeezed, and at $(1, -1)$ it still gives $1 - 1 + 1 = 1$.

### L2 human

Here is a typical problem: for which numbers $k$ is $Q(x, y, z) = x^2 + y^2 + z^2 + 2kxy$ positive definite?
The matrix is
$$A = \begin{pmatrix} 1 & k & 0 \\ k & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
Its leading minors are $1$, then $1 - k^2$, then $\det A = 1 - k^2$, by expansion along the last row.
All three are positive exactly when $\lvert k \rvert < 1$.
Check with squares: $Q = (x + ky)^2 + (1 - k^2) y^2 + z^2$, and the coefficients $1$, $1 - k^2$ and $1$ are positive exactly when $\lvert k \rvert < 1$.
At $k = 1$ the form is $(x + y)^2 + z^2$, which is $0$ at $(1, -1, 0)$, so the boundary case is only semidefinite.
The typical use is this kind of parameter question, where one test by minors answers for all values at once.

### L3 human

The positive definite forms on $\mathbb{R}^n$ form an open convex cone in the space of all quadratic forms, and its closure is the cone of positive semidefinite forms.
The group $GL_n(\mathbb{R})$ acts on this cone by $A \mapsto P^{\mathsf{T}} A P$, and the action is transitive, because every positive definite form is congruent to $x_1^2 + \dots + x_n^2$.
So the cone is the space of all inner products on $\mathbb{R}^n$, and it is the quotient $GL_n(\mathbb{R}) / O_n(\mathbb{R})$.
Over $\mathbb{Z}$ and $\mathbb{Q}$, positive definite forms are the subject of the arithmetic theory of lattices and of the representation of integers by forms, which belongs to number theory.
