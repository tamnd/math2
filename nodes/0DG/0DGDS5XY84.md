---
tag: 0DGDS5XY84
kind: concept
name: Alternating bilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
specializes: [0SQZMXB6GP, 0K6CH0MT0F]
uses: [0SQZMXB6GP, 0QK6K857HS, 0PBY4E9GQF, 1ZB13N78XW]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Symmetric, skew-symmetric, and alternating forms
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
    locator: Skew-symmetric and alternating forms
  - book: isbn:9780387728285
    locator: Chapter 11
inventory: [JEX1WKZNKA]
---

## Summary

Let $V$ be a vector space over a field $F$.
A [[bilinear form|0SQZMXB6GP]] $B$ on $V$ is alternating when $B(v, v) = 0$ for all $v \in V$.
It is skew-symmetric when $B(u, v) = -B(v, u)$ for all $u, v \in V$.
The [[formal definition|08ZQAKBKHF]] states the alternating condition.
Every alternating form is skew-symmetric, and the two notions agree when the [[characteristic|1ZB13N78XW]] of $F$ is not $2$.
Alternating forms matter because they measure signed areas, and the nondegenerate ones make [[symplectic vector spaces|PQ7JJY0VPH]].

## Motivation

In the plane, the signed area of the parallelogram spanned by $u$ and $v$ is $u_1 v_2 - u_2 v_1$.
This area is bilinear, it changes sign when $u$ and $v$ swap, and it is $0$ when $u = v$.
A form with the last property is the bilinear version of the [[alternating multilinear maps|0K6CH0MT0F]] of determinant theory.
The same forms appear in classical mechanics, where positions and momenta pair by an alternating form.

## Notation

- An alternating form is often written $\omega$ or $\omega(u, v)$, in particular in symplectic geometry.
- The matrix of an alternating form is a [[skew-symmetric matrix|0PBY4E9GQF]] with zero diagonal. Some books call such a matrix an alternating matrix.
- The words "antisymmetric" and "skew-symmetric" mean the same thing for forms: $B(u, v) = -B(v, u)$.

## Remarks

### Examples

- The [[determinant form $x_1 y_2 - x_2 y_1$ on $F^2$|~d5093041]] is alternating, because $x_1 x_2 - x_2 x_1 = 0$.
- On $F^4$ the form $x_1 y_3 + x_2 y_4 - x_3 y_1 - x_4 y_2$ is alternating, because $B(x, x) = x_1 x_3 + x_2 x_4 - x_3 x_1 - x_4 x_2 = 0$.
- The [[Pfaffian example|M0JEPXXWQM]] matrix $\begin{pmatrix} 0 & 1 & 2 & 3 \\ -1 & 0 & 4 & 5 \\ -2 & -4 & 0 & 6 \\ -3 & -5 & -6 & 0 \end{pmatrix}$ defines an alternating form on $\Q^4$; a [[symplectic basis for it|~b44ceee3]] exists.
- The [[form on $\Q^3$ with matrix $\begin{pmatrix} 0 & 1 & 0 \\ -1 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}$|~35320308]] is alternating and degenerate.
- For $a, b \in V^*$, the form $B(u, v) = a(u) b(v) - a(v) b(u)$ is alternating, because $B(u, u) = a(u)b(u) - a(u)b(u) = 0$.

### Non-examples

- The [[identity form $x_1 y_1 + x_2 y_2$ over $\mathbb{F}_2$|~45504b21]] is skew-symmetric but not alternating: $B(e_1, e_1) = 1$.
- The [[dot product|0S52TNNTH9]] on $\R^n$ is not alternating, because $e_1 \cdot e_1 = 1$.
- The [[form with matrix $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$|~08303f03]] is neither symmetric nor skew-symmetric.

### Basic properties

- [[Alternating forms are skew-symmetric, and the converse holds outside characteristic 2|~205a4a20]].
- In the same statement: $B$ is alternating exactly when its matrix $A$ satisfies $A^T = -A$ and $A_{ii} = 0$ for all $i$.
- In characteristic $2$, skew-symmetric means symmetric, since $-1 = 1$.
- The rank of an alternating form is even, and its matrix is [[congruent|WJWNYSQKK8]] to a sum of blocks $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and zeros, by the [[classification of alternating forms|~a52a9f11]].
- Orthogonality for an alternating form is symmetric, since $B(u, v) = 0$ gives $B(v, u) = 0$. So the form is [[reflexive|~b3103bb5]].
- Every vector is orthogonal to itself, so every vector is [[isotropic|~0d389e21]] for an alternating form.
- If $\operatorname{char} F \neq 2$, a [[skew-symmetric matrix of odd size is singular|55RX9C0ZTH]]. So an alternating form on a space of odd dimension is degenerate.
- The determinant of an alternating matrix is the square of its [[Pfaffian|NH5HWBPWS9]].

### Common errors

- "Skew-symmetric" and "alternating" differ in characteristic $2$. Over $\mathbb{F}_2$, the identity matrix is skew-symmetric, but its form is not alternating.
- A skew-symmetric matrix over $\mathbb{F}_2$ need not have zero diagonal. The test for an alternating form needs both $A^T = -A$ and a zero diagonal.
- An alternating form gives $B(v, v) = 0$ for every $v$, but this does not make it the zero form. The determinant form is nonzero.

## Explanations

### L1 human

An alternating form gives zero when both vectors are equal.
Then swapping the two vectors changes the sign of the value.
The signed area of the parallelogram spanned by two plane vectors is an example.
For $(1, 0)$ and $(0, 1)$ the signed area is $1$, and in the other order it is $-1$.
A vector with itself spans no area, so the value is $0$.

### L2 human

We check that $B(x, y) = x^T A y$ with $A = \begin{pmatrix} 0 & 2 & -1 \\ -2 & 0 & 3 \\ 1 & -3 & 0 \end{pmatrix}$ on $\Q^3$ is alternating.

1. $A^T = -A$: for example $A_{12} = 2$ and $A_{21} = -2$.
2. The diagonal of $A$ is zero.
3. By the matrix criterion, $B$ is alternating.
4. A direct check with $x = (1, 1, 1)$: $Ax = (1, 1, -2)$, and $x^T A x = 1 + 1 - 2 = 0$.
5. Since $3$ is odd, $\det A = 0$, so $B$ is degenerate. Here $(3, 1, 2)$ spans the kernel: $A(3, 1, 2)^T = (0, 0, 0)$.

The typical use is in determinants and in symplectic geometry, where alternating forms measure oriented areas.
A trap: over a field of characteristic $2$, checking $A^T = -A$ is not enough.
We must also check that the diagonal is zero.

### L3 human

Alternating bilinear forms on $V$ are the elements of $(\Lambda^2 V)^*$, the second exterior power, and in finite dimension they are the $2$-forms of $\Lambda^2 V^*$.
A differential $2$-form on a manifold is a smooth family of alternating forms on the tangent spaces, and a closed nondegenerate one is a [[symplectic structure|CAN490EPRT]].
The classification of alternating forms is simpler than that of symmetric forms: over every field only the rank matters.
In characteristic $2$ the alternating forms are a proper subclass of the symmetric forms, and they behave better than the skew-symmetric forms.
