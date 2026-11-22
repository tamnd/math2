---
tag: WYQGZK8GFT
kind: statement
role: theorem
name: The discriminant of a quadratic form is an invariant of equivalence
msc: ["11E04", 15A63]
topics: [6TSCEW8QMK]
audience: ug2
about: [MZFRXECCMC]
uses: [0HZNE5QZDJ, VN9AG8JKYT, 0SPYAGE7T0, D3E2Y85S6H, 00KDZRW4C0, 9160DW40TE]
proofs: [DQH11Y1KMD]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Equivalence of forms
---

## Statement

A change of basis multiplies the determinant of the matrix of a quadratic form by a nonzero square, so the determinant modulo squares is a property of the form itself.

Let $F$ be a field of characteristic not $2$, and let $A$ be a symmetric $n \times n$ matrix over $F$.

1. For every invertible $n \times n$ matrix $P$ over $F$, we have $\det(P^{\mathsf{T}} A P) = \det(P)^2 \det A$, as in [[the congruence statement|D3E2Y85S6H]].
2. Let $Q$ be a [[quadratic form|0HZNE5QZDJ]] on a vector space $V$ of finite dimension $n$ over $F$. The matrices of $Q$ in two bases of $V$ have determinants that are either both $0$ or both nonzero and in the same [[square class|9160DW40TE]]. So the [[discriminant|MZFRXECCMC]] of $Q$ does not depend on the basis.
3. If two quadratic forms on $V$ are equivalent, then they have the same discriminant.

## Remarks

### A first check

Take $Q = x^2 + y^2$ on $\mathbb{Q}^2$, with matrix $I$, and the new variables $x = u + v$, $y = u - v$.
Then $Q = (u + v)^2 + (u - v)^2 = 2u^2 + 2v^2$, and the change of basis matrix is
$$P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \qquad P^{\mathsf{T}} I P = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}.$$
The determinant went from $1$ to $4$.
Check: $\det P = -2$, and $\det(P)^2 \cdot 1 = 4$, as part 1 says.
So the number changed, but its square class did not.

### Why each hypothesis is needed

The matrix $P$ must be invertible.
For $P = 0$ we get $\det(P^{\mathsf{T}} A P) = 0$ for every $A$, and the information is lost.
An invertible $P$ has $\det P \ne 0$, so the factor $\det(P)^2$ is a nonzero square and keeps the class.

The characteristic must not be $2$ for parts 2 and 3.
Part 1 is a rule about determinants and holds over every field.
But in characteristic $2$ each cross term of $x^{\mathsf{T}} A x$ appears twice and vanishes, so $x^{\mathsf{T}} A x = \sum_i a_{ii} x_i^2$ for symmetric $A$.
So a form such as $xy$ has no symmetric matrix at all; see [[the forms over F₂|ZEGSCCVGZF]].

The dimension must be finite, so that $A$ is a square matrix with a determinant.

### What it gives you

The main use is a proof of non-equivalence.
If two forms have different discriminants, then they are not equivalent.
For example, $x^2 + y^2$ and $x^2 + 2y^2$ are [[not equivalent over Q|C18PABZVSN]], because $2$ is not a rational square.

Over $\mathbb{R}$ the square classes are the two signs, so the sign of $\det A$ is an invariant.
For a nondegenerate form with $p$ positive and $q$ negative squares, it equals $(-1)^q$, in line with [[Sylvester's law of inertia|0WFED3K3DQ]].
Part 2 also shows that nondegeneracy, the condition $\det A \ne 0$, does not depend on the basis.

### The converse

The converse is false in general.
Over $\mathbb{Q}$, the forms $x^2 + y^2$ and $-x^2 - y^2$ both have discriminant $1$, but the first takes only positive values at nonzero vectors and the second only negative ones.
Over $\mathbb{R}$ the same pair shows that the converse fails there too.
Over a finite field of odd order, the converse holds for nondegenerate forms of the same dimension, by [[the finite field theorem|2HBR7137AD]].

### Generalizations

The rule $\det(P^{\mathsf{T}} A P) = \det(P)^2 \det A$ holds in every characteristic, so the discriminant of a symmetric bilinear form is defined over every field.
For a Hermitian matrix $A$ and an invertible complex matrix $P$, the same argument gives
$$\det(P^* A P) = \overline{\det P} \, \det A \, \det P = |\det P|^2 \det A,$$
so the real number $\det A$ is an invariant up to positive real factors, which is its sign.

### Watch out

The test depends on the field.
The quotient $2$ of the determinants of $x^2 + 2y^2$ and $x^2 + y^2$ is a square in $\mathbb{R}$ and in $\mathbb{F}_7$, where $2 = 3^2$, but not in $\mathbb{Q}$ or $\mathbb{F}_3$.
So the same two forms are equivalent over $\mathbb{R}$ and $\mathbb{F}_7$ and not equivalent over $\mathbb{Q}$ and $\mathbb{F}_3$.

### Try it

Show that $3x^2 + y^2$ and $x^2 + y^2$ are not equivalent over $\mathbb{Q}$.
The determinants are $3$ and $1$, and $3$ is not the square of a rational number, so the discriminants differ.

## History

The rule of part 1 follows from the product rule for determinants, which Cauchy and Binet each proved in 1812.

## Explanations

### L1 human

Changing the variables of a quadratic form multiplies the determinant of its matrix by a square number.
So the determinant up to squares is the same in every choice of variables.
For example, $x^2 + y^2$ becomes $2u^2 + 2v^2$ when $x = u + v$ and $y = u - v$.
The determinant changes from $1$ to $4$, and $4 = 2^2$ is a square.

### L2 human

Here is the typical use: prove that $Q_1 = x^2 - 2y^2$ and $Q_2 = x^2 - y^2$ are not equivalent over $\mathbb{Q}$.
Compute the two determinants and their quotient:
$$\det \operatorname{diag}(1, -2) = -2, \qquad \det \operatorname{diag}(1, -1) = -1, \qquad \frac{-2}{-1} = 2.$$
The quotient $2$ is not a rational square, so the discriminants differ and the forms are not equivalent.
Both forms are indefinite with one positive and one negative square, so over $\mathbb{R}$ they are equivalent.
Watch out: the discriminant only proves non-equivalence; equal discriminants never prove equivalence by themselves over $\mathbb{Q}$.

### L3 human

In coordinate-free terms, $Q$ induces a symmetric form on the line $\Lambda^n V$, and a change of basis acts on that line by $\det P$, which multiplies the form by $\det(P)^2$.
So the discriminant is an invariant of the isometry class of the quadratic space, and it is multiplicative on orthogonal sums.
It is the first of the classical invariants over $\mathbb{Q}$ and the $p$-adic fields, together with the signature and the Hasse invariants; see [[quadratic forms over local and global fields|NQC5CJZY4J]].
