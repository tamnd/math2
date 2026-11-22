---
tag: 0Z3FEWZ8HA
kind: statement
role: theorem
name: Diagonalization of a quadratic form
msc: ["11E04", "15A63"]
topics: [6TSCEW8QMK]
audience: ug1
about: [0RBQS1JJCR, 0AXZNE5XNH]
uses: [0HZNE5QZDJ, 05Q4JD6XEH, VN9AG8JKYT, NZJDNC6EP6]
proofs: [PP93XQZ6WR, BDT6XBCRDJ]
formal:
  - system: lean4
    library: mathlib
    decl: QuadraticForm.equivalent_weightedSumSquares
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Equivalence of forms
  - url: https://en.wikipedia.org/wiki/Symmetric_bilinear_form
    locator: Orthogonal basis
  - book: isbn:9780387728285
---

## Statement

Outside characteristic $2$, a change of basis removes every cross term from a quadratic form, so that only a weighted sum of squares is left.
Let $F$ be a field of characteristic not $2$, let $V$ be a vector space over $F$ of finite dimension $n$, and let $Q$ be a [[quadratic form|0HZNE5QZDJ]] on $V$.
Then $V$ has a basis $(e_1, \dots, e_n)$, and there are $a_1, \dots, a_n \in F$, such that for all $x_1, \dots, x_n \in F$
$$Q(x_1 e_1 + \dots + x_n e_n) = a_1 x_1^2 + a_2 x_2^2 + \dots + a_n x_n^2.$$
The basis is [[orthogonal|05Q4JD6XEH]] for the associated symmetric bilinear form, and $a_i = Q(e_i)$.
In matrix form: for each symmetric $n \times n$ matrix $A$ over $F$ there is an invertible matrix $P$ such that $P^{\mathsf{T}} A P$ is diagonal, so every symmetric matrix is [[congruent|NZJDNC6EP6]] to a diagonal matrix.

## Remarks

### Completing squares on an example

Take $Q = x^2 + 4xy + y^2$ on $\mathbb{R}^2$.
Collect the terms with $x$ into one square:
$$x^2 + 4xy + y^2 = (x + 2y)^2 - 4y^2 + y^2 = (x + 2y)^2 - 3y^2.$$
With $u = x + 2y$ and $v = y$ the form is $u^2 - 3v^2$.
This is Lagrange's method, and [[the proof by completing squares|BDT6XBCRDJ]] repeats it one variable at a time; [[a form in three variables|Z762YHP338]] shows two rounds of it.

### The same step with matrices

The matrix of $Q$ is $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$.
Subtract $2$ times row $1$ from row $2$, and then $2$ times column $1$ from column $2$; this is a symmetric row and column reduction.
The two operations together replace $A$ by $P^{\mathsf{T}} A P$ with $P = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}$:
$$P^{\mathsf{T}} A P = \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 2 & -3 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -3 \end{pmatrix}.$$
Check: the columns of $P$ are the new basis vectors $(1, 0)$ and $(-2, 1)$, and $Q(-2, 1) = 4 - 8 + 1 = -3$.
The diagonal $(1, -3)$ agrees with $u^2 - 3v^2$.

### Why each hypothesis is needed

The characteristic must not be $2$.
Over $\mathbb{F}_2$ every form $ax^2 + by^2$ is additive, since $(x + x')^2 = x^2 + x'^2$ there, and $xy$ is not additive; so $xy$ is equivalent to no diagonal form, as [[the forms over F₂|ZEGSCCVGZF]] show.
For bilinear forms the failure is the same: the symmetric form $B(u, v) = u_1 v_2 + u_2 v_1$ on $\mathbb{F}_2^2$ has $B(v, v) = 2 v_1 v_2 = 0$ for every $v$, so an orthogonal basis would make $B$ zero, and $B$ is not zero.

Finite dimension is used because both proofs go by induction on $n$ and the statement names a finite basis.

### What it gives you

The number of nonzero $a_i$ is the [[rank|0EWQEYRVA8]] of $A$, since $P$ is invertible.
Over $\mathbb{R}$, [[Sylvester's law of inertia|0WFED3K3DQ]] says that the numbers of positive, negative and zero $a_i$ do not depend on the basis.
Over $\mathbb{C}$ each nonzero $a_i$ is a square, so the form becomes [[a sum of squares|0CEX9BRXRZ]].
Over a finite field of odd characteristic the theorem is the first step of [[the classification by dimension and discriminant|2HBR7137AD]].
Conversely, if $Q$ is diagonal in a basis, then that basis is orthogonal, so the theorem is the same as the existence of an orthogonal basis.

### What is not unique

The coefficients $a_i$ are not determined by $Q$.
Each $a_i$ can be multiplied by a nonzero square, by scaling $e_i$, and other changes occur too: over $\mathbb{Q}$ the substitution $(x + y, x - y)$ gives
$$(x + y)^2 + (x - y)^2 = 2x^2 + 2y^2,$$
so $x^2 + y^2$ is equivalent to $2x^2 + 2y^2$ although $2$ is not a square in $\mathbb{Q}$.
Over $\mathbb{R}$, [[the principal axis theorem|0PR5P9Z4KM]] picks an orthonormal basis, and then the $a_i$ are the eigenvalues of $A$.

### Watch out

The coefficients that completing squares gives are not the eigenvalues of $A$.
For $x^2 + 4xy + y^2$ the method gives $1$ and $-3$, but the eigenvalues of $A$ are $3$ and $-1$, the roots of $(1 - \lambda)^2 - 4 = 0$.
Only the signs agree, by Sylvester's law, because a general congruence $P^{\mathsf{T}} A P$ is not a similarity $P^{-1} A P$.

## Explanations

### L1 human

Every quadratic form becomes a sum of squares with coefficients after a good change of variables.
For example, $x^2 + 2xy = (x + y)^2 - y^2$.
With $u = x + y$ and $v = y$, the form becomes $u^2 - v^2$, and the cross term is gone.

### L2 human

Here is a typical use: find the signs of $Q = x^2 + 4xy + 2xz + 5y^2 + 8yz + 2z^2$ without computing eigenvalues, as in [[the full example|Z762YHP338]].
First collect the terms with $x$:
$$x^2 + 4xy + 2xz = (x + 2y + z)^2 - 4y^2 - 4yz - z^2, \qquad Q = (x + 2y + z)^2 + y^2 + 4yz + z^2.$$
Then collect the terms with $y$, using $y^2 + 4yz = (y + 2z)^2 - 4z^2$:
$$Q = (x + 2y + z)^2 + (y + 2z)^2 - 3z^2.$$
The new variables $u = x + 2y + z$, $v = y + 2z$ and $w = z$ give $u^2 + v^2 - 3w^2$, so $Q$ takes both signs.
Watch out: the change of variables must be invertible; here it is triangular with $1$ on the diagonal, so it is.

### L3 human

The theorem says that every quadratic space outside characteristic $2$ is an orthogonal sum of lines, written $\langle a_1, \dots, a_n \rangle$.
So the classes $\langle a \rangle$ for $a \in F^{\times}$ generate the [[Witt group|KFVY0RPGF2]].
What is left is to decide when two diagonal forms are equivalent.
Over $\mathbb{R}$ the answer is [[the law of inertia|0WFED3K3DQ]], over finite fields it is the discriminant, and over $\mathbb{Q}$ it is [[the Hasse-Minkowski theorem|R8HCWA981S]].
The topic on [[bilinear and sesquilinear forms|DYAK7YMK7B]] treats the same theorem as the existence of orthogonal bases for symmetric bilinear forms.
