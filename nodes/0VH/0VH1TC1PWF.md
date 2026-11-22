---
tag: 0VH1TC1PWF
kind: definition
name: Companion matrix
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
defines: 0ZCWPNZTQ3
uses: [0CP7YY6NAG, 0C3QBCR46M]
sources:
  - url: https://en.wikipedia.org/wiki/Companion_matrix
    locator: lead section
inventory: [EGQ8TF53DJ]
---

## Definition

The companion matrix of a monic polynomial is a square matrix built from its coefficients, with ones just below the diagonal and the negated coefficients in the last column.
Let $F$ be a field, let $n \ge 1$, and let $p(x) = x^n + c_{n-1} x^{n-1} + \cdots + c_1 x + c_0$ be a [[monic polynomial|0C3QBCR46M]] over $F$.
The *companion matrix* of $p$ is the $n \times n$ [[matrix|0CP7YY6NAG]]
$$C(p) = \begin{pmatrix} 0 & 0 & \cdots & 0 & -c_0 \\ 1 & 0 & \cdots & 0 & -c_1 \\ 0 & 1 & \cdots & 0 & -c_2 \\ \vdots & & \ddots & & \vdots \\ 0 & 0 & \cdots & 1 & -c_{n-1} \end{pmatrix}.$$
Its entries are $C(p)_{i+1, i} = 1$ for $1 \le i < n$, $C(p)_{i, n} = -c_{i-1}$ for $1 \le i \le n$, and $0$ in all other positions.
For $n = 1$ this gives $C(x + c_0) = (-c_0)$.

## Notation

This is the column version.
Many books use the row version $C(p)^{\mathsf T}$, with ones above the diagonal and $-c_0, \dots, -c_{n-1}$ in the last row.
Some books put the coefficients in the first row or in the first column instead.
State the version you use before you compute with it.

## Remarks

Each part of the definition has a job.
The ones below the diagonal say that $C(p) e_i = e_{i+1}$ for $i < n$, so $e_1$ runs through the whole standard basis.
The last column says that $C(p) e_n = -c_0 e_1 - c_1 e_2 - \cdots - c_{n-1} e_n$, and this is exactly what makes $p(C(p)) e_1 = 0$.
The polynomial must be monic so that the leading coefficient $1$ does not appear in the matrix; for $2x^2 + 4$, first divide by $2$ and use $x^2 + 2$.

For $p = x^2 - 3x + 2$ we have $c_0 = 2$ and $c_1 = -3$, so the last column is $(-2, 3)$ and
$$C(p) = \begin{pmatrix} 0 & -2 \\ 1 & 3 \end{pmatrix}.$$
Its trace is $3$ and its determinant is $2$, so its characteristic polynomial is $x^2 - 3x + 2 = p$.
The [[theorem on companion matrices|XYR7GPH20K]] proves in general that the [[characteristic polynomial|039HF58KQ5]] and the [[minimal polynomial|03NDVCSHSB]] of $C(p)$ are both $p$.
The matrix $\begin{pmatrix} 2 & 0 \\ 1 & 1 \end{pmatrix}$ is not a companion matrix in this version, because its first column is not $e_2$.
The [[concept page on companion matrices|0ZCWPNZTQ3]] shows how they arise from cyclic maps and how they build the [[rational canonical form|042JWAR3Q0]].

## Explanations

### L1 human

For each polynomial with leading coefficient $1$, the companion matrix is a matrix with exactly that characteristic polynomial.
It shifts each basis vector to the next one, and the coefficients of the polynomial fix the image of the last one.
For $x^2 - 3x + 2$, the matrix has first column $(0, 1)$ and second column $(-2, 3)$.

### L2 human

Here is the construction for a cubic.
Let $p = x^3 + 5x - 7$, so $c_0 = -7$, $c_1 = 5$ and $c_2 = 0$.
The last column is $(-c_0, -c_1, -c_2) = (7, -5, 0)$, and the ones go just below the diagonal:
$$C(p) = \begin{pmatrix} 0 & 0 & 7 \\ 1 & 0 & -5 \\ 0 & 1 & 0 \end{pmatrix}.$$
Check: $C(p) e_3 = (7, -5, 0) = -c_0 e_1 - c_1 e_2 - c_2 e_3$, and $\det C(p) = (-1)^3 c_0 = 7$.
The trap is to forget the minus signs, or to use the row version in one place and the column version in another.
