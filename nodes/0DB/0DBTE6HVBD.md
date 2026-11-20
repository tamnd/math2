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

Let $V$ and $W$ be finite-dimensional inner product spaces over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $T \colon V \to W$ be a linear map with [[adjoint|0ST8QF9T3T]] $T^*$.
Write $[S]_{C,B}$ for the [[matrix of a linear map|0YYMY95FWS]] $S$ from the basis $B$ to the basis $C$, and $M^*$ for the [[conjugate transpose|0EX045E2BP]] of a matrix $M$.

1. If $B$ is an [[orthonormal basis|0FWJ0VW561]] of $V$ and $C$ is an orthonormal basis of $W$, then
$$[T^*]_{B,C} = \left([T]_{C,B}\right)^*.$$
Over $\mathbb{R}$, this is the transpose of $[T]_{C,B}$.
2. Let $V = W$, and let $B = (b_1, \dots, b_n)$ be any basis of $V$. Let $H$ be the $n \times n$ matrix with the entries $H_{ij} = \ip{b_j}{b_i}$, the transpose of the [[Gram matrix|00SPJSDT3Z]] of $B$. Then $H$ is invertible, and
$$[T^*]_B = H^{-1} \left([T]_B\right)^* H.$$

## Remarks

### Why each hypothesis is needed

- Part 1 needs orthonormal bases. [[The example with the basis $(1, 0)$, $(1, 1)$|2YX64QQ94Y]] has $[T]_B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ but $[T^*]_B = \begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix}$, which is not the transpose.
- Part 1 needs the inner products on $V$ and $W$ that define $T^*$. For [[a weighted inner product|CPQB5HABC6]] on $\mathbb{R}^2$, the standard basis is not orthonormal, and the transpose is not the adjoint.
- Over $\mathbb{C}$, the conjugation is needed. For $T = iI$ on $\mathbb{C}$, the matrix is $(i)$, its transpose is $(i)$, but $T^* = -iI$ has the matrix $(-i)$.

### Consequences

- For a matrix $A$ and the standard inner products on $\mathbb{K}^n$ and $\mathbb{K}^m$, the adjoint of $x \mapsto Ax$ is $y \mapsto A^* y$. So the matrix notation $A^*$ and the operator notation agree.
- An operator $T$ is [[self-adjoint|0MB8HQW495]] if and only if its matrix in one orthonormal basis is [[Hermitian|0EKZCX4K3P]] (over $\mathbb{C}$) or [[symmetric|0N28QN4CYA]] (over $\mathbb{R}$).
- An operator $T$ is [[normal|0ENZN5G4CV]] if and only if its matrix in one orthonormal basis is a [[normal matrix|0XYKE8BE7X]].
- The rules for adjoints, such as $(ST)^* = T^* S^*$, match the rules for conjugate transposes of matrices.

### Converse

Part 1 has a converse for one basis $B$ of $V$.
If $[T^*]_B = ([T]_B)^*$ for every operator $T$ on $V$, then part 2 gives $H^{-1} M H = M$ for every $n \times n$ matrix $M$.
So $H$ commutes with every matrix, and the matrix units $E_{ij}$ force $H = cI$ with $c = \ip{b_1}{b_1} > 0$.
Hence the basis $B$ is orthogonal, and all its vectors have the same length $\sqrt{c}$.

### Generalizations

- In part 2, the correction by $H$ is a change of inner product: in the coordinates of $B$, the inner product is $\ip{v}{w} = y^* H x$, where $x$ and $y$ are the coordinate vectors of $v$ and $w$.
- For bounded operators on a Hilbert space with an orthonormal basis, the matrix of $T^*$ is the conjugate transpose of the infinite matrix of $T$.

## Explanations

### L1 human

When we write a map as a table of numbers in perpendicular unit coordinates, the adjoint has a simple table.
We flip the table along its diagonal, and over the complex numbers we also replace each entry by its conjugate.
For the real table $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, the adjoint has the table $\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$.
In coordinates that are not perpendicular, this simple rule fails.

### L2 human

Worked example: a complex matrix.

1. Let $A = \begin{pmatrix} 1 & i \\ 2 & 3 - i \end{pmatrix}$ act on $\mathbb{C}^2$ with the standard inner product.
2. The standard basis is orthonormal, so the adjoint has the matrix $A^* = \begin{pmatrix} 1 & 2 \\ -i & 3 + i \end{pmatrix}$.
3. Check with $x = (0, 1)$ and $y = (1, 0)$. Then $Ax = (i, 3 - i)$, and $\ip{Ax}{y} = i \cdot \overline{1} = i$.
4. Also $A^* y = (1, -i)$, and $\ip{x}{A^* y} = 0 \cdot 1 + 1 \cdot \overline{-i} = i$. The two sides agree.

The typical use: compute adjoints of concrete operators by choosing an orthonormal basis first.
A trap: in a basis that is not orthonormal, the transpose gives a wrong answer, and part 2 gives the right one.

### L3 human

Part 1 says that the isomorphism between operators and matrices, given by orthonormal bases, is an isomorphism of algebras with involution.
Part 2 shows what happens in general: a basis identifies $V$ with $\mathbb{K}^n$ with the inner product given by the positive definite Hermitian matrix $H$.
The adjoint for this inner product is $M \mapsto H^{-1} M^* H$.
The same formula, with an indefinite $H$, defines adjoints for indefinite forms, as in the Lorentz group.
