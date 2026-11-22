---
tag: 0DBTE6HVBD
kind: statement
role: proposition
name: Matrix of the adjoint
aliases: [matrix-of-the-adjoint-is-the-conjugate-transpose]
msc: ["15A04", "47A05"]
topics: [3YM9EK6VMB]
audience: ug1
about: [0R9NMSM1ZP, 0DXKE10PHF]
uses: [0ST8QF9T3T, 0EX045E2BP, 0YYMY95FWS, 0FWJ0VW561, 00SPJSDT3Z]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_transpose
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Hermitian_adjoint
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780134860244
    locator: Section 6.3
---

## Statement

In orthonormal bases the matrix of the adjoint is the conjugate transpose of the matrix of the map, and in other bases a correction by the Gram matrix is needed.
Let $V$ and $W$ be finite-dimensional inner product spaces over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $T \colon V \to W$ be a linear map with [[adjoint|0ST8QF9T3T]] $T^*$.
Write $[S]_{C,B}$ for the [[matrix of a linear map|0YYMY95FWS]] $S$ from the basis $B$ to the basis $C$, and $M^*$ for the [[conjugate transpose|0EX045E2BP]] of a matrix $M$.

1. If $B$ is an [[orthonormal basis|0FWJ0VW561]] of $V$ and $C$ is an orthonormal basis of $W$, then
$$[T^*]_{B,C} = \left([T]_{C,B}\right)^*.$$
Over $\mathbb{R}$, this is the transpose of $[T]_{C,B}$.
2. Let $V = W$, and let $B = (b_1, \dots, b_n)$ be any basis of $V$. Let $H$ be the $n \times n$ matrix with the entries $H_{ij} = \ip{b_j}{b_i}$, the transpose of the [[Gram matrix|00SPJSDT3Z]] $G_{ij} = \ip{b_i}{b_j}$ of $B$. Then $H$ is invertible, and
$$[T^*]_B = H^{-1} \left([T]_B\right)^* H.$$

## Remarks

### A complex check

Let $A = \begin{pmatrix} 1 & i \\ 2 & 3 - i \end{pmatrix}$ act on $\mathbb{C}^2$ with the standard inner product $\ip{x}{y} = y^* x$.
The standard basis is orthonormal, so part 1 says that the adjoint has the matrix $A^* = \begin{pmatrix} 1 & 2 \\ -i & 3 + i \end{pmatrix}$.
Test it with $x = (0, 1)$ and $y = (1, 0)$, where $Ax = (i, 3 - i)$ and $A^* y = (1, -i)$:
$$\ip{Ax}{y} = i \cdot \overline{1} = i, \qquad \ip{x}{A^* y} = 0 \cdot \overline{1} + 1 \cdot \overline{(-i)} = i.$$
The two sides agree.

### Why each hypothesis is needed

Part 1 needs orthonormal bases.
In the [[example with the basis (1, 0), (1, 1)|2YX64QQ94Y]], the map $T(x_1, x_2) = (x_2, 0)$ has $[T]_B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ but $[T^*]_B = \begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix}$, which is not the transpose.
The bases must be orthonormal for the inner products that define $T^*$.
For the [[weighted inner product|CPQB5HABC6]] $2x_1 y_1 + x_2 y_2$ on $\mathbb{R}^2$, the standard basis is not orthonormal, and the transpose is not the adjoint.
Over $\mathbb{C}$ the conjugation is needed: for $T = iI$ on $\mathbb{C}$ the matrix is $(i)$ and its transpose is $(i)$, but $T^* = -iI$ has the matrix $(-i)$.

### What it gives you

For a matrix $A$ and the standard inner products on $\mathbb{K}^n$ and $\mathbb{K}^m$, the adjoint of $x \mapsto Ax$ is $y \mapsto A^* y$, so the matrix symbol $A^*$ and the operator symbol agree.
An operator is [[self-adjoint|0MB8HQW495]] exactly when its matrix in one orthonormal basis is [[Hermitian|0EKZCX4K3P]], which over $\mathbb{R}$ means [[symmetric|0N28QN4CYA]].
In the same way, an operator is [[normal|0ENZN5G4CV]] exactly when its matrix in one orthonormal basis is a [[normal matrix|0XYKE8BE7X]].
The rules for adjoints, such as $(ST)^* = T^* S^*$, become the rules for conjugate transposes of matrices.

### The converse

When does the transpose rule hold in a basis $B$ for every operator?
Suppose $[T^*]_B = ([T]_B)^*$ for every operator $T$ on $V$.
Part 2 then gives $H^{-1} M H = M$ for every $n \times n$ matrix $M$, so $H$ commutes with every matrix.
The matrix units $E_{ij}$ then force $H = cI$ with $c = \ip{b_1}{b_1} > 0$.
So the basis is orthogonal and all its vectors have the same length $\sqrt{c}$, and these are exactly the bases for which the rule holds.

### Generalizations

In part 2 the correction by $H$ is the inner product written in coordinates: $\ip{v}{w} = y^* H x$, where $x$ and $y$ are the coordinate columns of $v$ and $w$.
For bounded operators on a Hilbert space with an orthonormal basis, the matrix of $T^*$ is the conjugate transpose of the infinite matrix of $T$.

## Explanations

### L1 human

When we write a map as a table of numbers in perpendicular unit coordinates, the adjoint has a simple table.
We flip the table along its diagonal, and over the complex numbers we also replace each entry by its conjugate.
For the real table with rows $(1, 2)$ and $(3, 4)$, the adjoint has the rows $(1, 3)$ and $(2, 4)$.
In coordinates that are not perpendicular, this simple rule fails.

### L2 human

Here is a typical use: find the adjoint of the operator $T(p) = p(1)$ on the polynomials $a + bx$ with $\ip{p}{q} = \int_{-1}^{1} p q \, dx$, where $p(1)$ is read as a constant polynomial.
An orthonormal basis is $e_0 = \tfrac{1}{\sqrt2}$ and $e_1 = \sqrt{\tfrac32}\, x$.
Then $T e_0 = e_0$ and $T e_1 = \sqrt{\tfrac32} = \sqrt3\, e_0$, so the matrix of $T$ and its transpose are
$$\begin{pmatrix} 1 & \sqrt3 \\ 0 & 0 \end{pmatrix}, \qquad \begin{pmatrix} 1 & 0 \\ \sqrt3 & 0 \end{pmatrix}.$$
So $T^* e_0 = e_0 + \sqrt3\, e_1$ and $T^* e_1 = 0$, which gives $T^*(1) = \sqrt2\,(e_0 + \sqrt3\, e_1) = 1 + 3x$ and $T^*(x) = 0$.
Check with $p = x$ and $q = 1$:
$$\ip{Tp}{q} = \int_{-1}^{1} 1 \, dx = 2, \qquad \ip{p}{T^* q} = \int_{-1}^{1} x (1 + 3x) \, dx = 0 + 2 = 2.$$
So we first choose an orthonormal basis, and then the adjoint is a transpose.
Watch out: in a basis that is not orthonormal, the transpose gives a wrong answer, and part 2 gives the right one.

### L3 human

Part 1 says that the isomorphism between operators and matrices given by orthonormal bases respects the involutions: it sends $T^*$ to the conjugate transpose.
Part 2 shows the general picture: a basis identifies $V$ with $\mathbb{K}^n$ carrying the inner product $y^* H x$ of a positive definite Hermitian matrix $H$, and the adjoint for this inner product is $M \mapsto H^{-1} M^* H$.
The same formula with an indefinite $H$ defines adjoints for indefinite forms, as in the study of the Lorentz group.
