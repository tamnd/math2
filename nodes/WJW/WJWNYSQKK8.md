---
tag: WJWNYSQKK8
kind: concept
name: Matrix congruence
aliases: [congruent-matrices]
msc: ["15A63", "15A21"]
topics: [DYAK7YMK7B]
audience: ug1
uses: [0EB9N0S33C, 09DXWYRD43, 0QK6K857HS]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester%27s_law_of_inertia
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Matrix_congruence
  - url: https://en.wikipedia.org/wiki/Matrix_congruence
    locator: Congruence over the reals
  - book: isbn:9780135367971
    locator: Chapter 10
same_as:
  wikidata: Q377286
  wikipedia: Matrix congruence
---

## Summary

Let $F$ be a field.
Two $n \times n$ matrices $A$ and $A'$ over $F$ are congruent when $A' = P^T A P$ for some [[invertible|0EB9N0S33C]] $n \times n$ matrix $P$ over $F$.
The [[formal definition|NZJDNC6EP6]] states the same.
Congruent matrices are the [[matrices|0QK6K857HS]] of one [[bilinear form|0SQZMXB6GP]] in two bases.
Congruence matters because it is the right equivalence for forms, just as [[similarity|0E89HQATM8]] is the right equivalence for linear maps $V \to V$.

## Motivation

A form has a matrix in each basis, and these matrices differ.
We want to know when two matrices describe the same form, so that we can choose the simplest one.
The [[change of basis rule|0SPYAGE7T0]] answers this: the matrices of one form are exactly the matrices $P^T A P$.
So the classification of forms is the classification of matrices up to congruence.

## Notation

- We write $A \cong A'$ or $A \sim_c A'$ when $A$ and $A'$ are congruent. Many books use no symbol.
- Over $\C$ the name $*$-congruence or conjunctivity is used for $A' = P^* A P$ with the [[conjugate transpose|0DXKE10PHF]] $P^*$. It is the relation for [[sesquilinear forms|054YEQ0Y8M]] in the convention $h(x, y) = y^* A x$.

## Remarks

### Examples

- $I_2$ and $\operatorname{diag}(4, 9)$ are congruent over $\Q$, with $P = \operatorname{diag}(2, 3)$, because $P^T I_2 P = P^2$.
- $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $\operatorname{diag}(2, -2)$ are congruent over $\Q$, with $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
- [[$\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ and $\operatorname{diag}(1, -3)$ are congruent|57GZX8S4ES]], but their eigenvalues differ.
- The matrices of a [[change of basis on $\Q^2$|2X09GT6SMD]] are congruent: $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ and $\begin{pmatrix} 6 & -4 \\ 0 & 2 \end{pmatrix}$.
- Every alternating matrix is congruent to a block diagonal matrix of blocks $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and zeros, by the [[classification of alternating forms|V8KKHKXXB3]].

### Non-examples

- $I_2$ and $-I_2$ are not congruent over $\R$: $x^T P^T P x = \norm{Px}^2 \ge 0$, but $x^T(-I_2)x < 0$ for $x \neq 0$.
- [[$I_2$ and $\operatorname{diag}(1, 2)$ are not congruent over $\Q$|R4ZDJG99Q0]]: the ratio $2$ of their determinants is not a square in $\Q$.
- A symmetric matrix and a nonsymmetric matrix are never congruent, because congruence keeps symmetry.
- $\operatorname{diag}(1, 0)$ and $I_2$ are not congruent over any field, because congruence keeps the rank.

### Basic properties

- [[Congruence is an equivalence relation, and it keeps rank and symmetry|D3E2Y85S6H]].
- It also keeps skew-symmetry and the property $x^T A x = 0$ for all $x$.
- It multiplies the determinant by the nonzero square $(\det P)^2$.
- Over $\R$, the congruence class of a symmetric matrix is fixed by its rank and its [[signature|07EZA80NEH]], by [[Sylvester's law of inertia|0WFED3K3DQ]].
- Over $\C$, the congruence class of a symmetric matrix is fixed by its rank alone, by the [[classification of complex quadratic forms|0CEX9BRXRZ]].

### History

Sylvester published the law of inertia, which classifies real symmetric matrices up to congruence, in 1852, according to the Wikipedia article on the law.

### Common errors

- Congruence is not similarity. Congruent matrices can have different eigenvalues, different traces and different determinants.
- When $P$ is orthogonal, $P^T = P^{-1}$, so congruence by $P$ and similarity by $P$ agree. This special case does not hold for a general $P$.
- Over $\Q$, the determinant changes by a square, so $\det A$ and $\det A'$ need not be equal. Only their square classes agree.

## Explanations

### L1 human

A form gives a square of numbers once we choose a basis.
If we choose another basis, we get another square of numbers for the same form.
We call two such squares congruent.
For example, the identity square and the square with $4$ and $9$ on the diagonal are congruent: stretch the first axis by $2$ and the second by $3$.

### L2 human

We show that $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is congruent to $\operatorname{diag}(2, -2)$ over $\Q$.

1. Take $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, with $\det P = -2$, so $P$ is invertible.
2. $AP = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$.
3. $P^T(AP) = \begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix}$.
4. So the form $x_1 y_2 + x_2 y_1$ becomes $2x'_1 y'_1 - 2x'_2 y'_2$ in the new basis $(1, 1), (1, -1)$.

The typical use is to bring the matrix of a form into a simple normal form.
A trap: the eigenvalues of $A$ are $1$ and $-1$, but the diagonal entries of the congruent matrix are $2$ and $-2$.
Congruence does not keep eigenvalues.

### L3 human

Congruence is the orbit relation of the action $(P, A) \mapsto P^T A P$ of $GL_n(F)$ on $M_n(F)$.
The stabilizer of a symmetric $A$ is the [[orthogonal group|0TKYAEJ8N7]] of the form, and the stabilizer of an alternating $A$ is a [[symplectic group|X12FS2JAP0]].
For symmetric matrices the invariants of the orbits depend on the field.
Over $\C$ the rank is enough, and over $\R$ we need the rank and the signature.
Over a finite field of odd characteristic we need the rank and a discriminant.
Over $\Q$ the classification needs the local invariants of the [[Hasse-Minkowski theorem|R8HCWA981S]].
