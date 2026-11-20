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

Let $F$ be a field, let $n \ge 1$, and let $p(x) = x^n + c_{n-1} x^{n-1} + \cdots + c_1 x + c_0$ be a [[monic polynomial|0C3QBCR46M]] over $F$.
The *companion matrix* of $p$ is the $n \times n$ [[matrix|0CP7YY6NAG]]
$$C(p) = \begin{pmatrix} 0 & 0 & \cdots & 0 & -c_0 \\ 1 & 0 & \cdots & 0 & -c_1 \\ 0 & 1 & \cdots & 0 & -c_2 \\ \vdots & & \ddots & & \vdots \\ 0 & 0 & \cdots & 1 & -c_{n-1} \end{pmatrix}.$$
Its entries are $C(p)_{i+1, i} = 1$ for $1 \le i < n$, $C(p)_{i, n} = -c_{i-1}$ for $1 \le i \le n$, and $0$ in all other positions.
For $n = 1$, $C(x + c_0) = (-c_0)$.

## Notation

This is the column version.
Many books use the row version $C(p)^{\mathsf T}$, with ones above the diagonal and $-c_0, \dots, -c_{n-1}$ in the last row.
Some books put the coefficients in the first row or the first column instead.
State the version in use before you compute with it.

## Remarks

- In terms of the standard basis, $C(p) e_i = e_{i+1}$ for $i < n$ and $C(p) e_n = -\sum_{i=1}^{n} c_{i-1} e_i$.
- The [[characteristic polynomial|039HF58KQ5]] and the [[minimal polynomial|03NDVCSHSB]] of $C(p)$ are both $p$, by the [[theorem on companion matrices|~dd227218]].
- Companion matrices are the blocks of the [[rational canonical form|042JWAR3Q0]].

## Explanations

### L1 human

For each polynomial with leading coefficient $1$, the companion matrix is a matrix with exactly that characteristic polynomial.
It shifts each basis vector to the next one, and the coefficients of the polynomial fix the image of the last one.
For $x$ squared minus $3x$ plus $2$, the matrix has first column $0, 1$ and second column $-2, 3$.

### L2 human

1. Let $p = x^2 - 3x + 2$, so $c_0 = 2$ and $c_1 = -3$.
2. The last column is $(-c_0, -c_1) = (-2, 3)$, and the entry below the diagonal is $1$.
3. So $C(p) = \begin{pmatrix} 0 & -2 \\ 1 & 3 \end{pmatrix}$, with trace $3$ and determinant $2$.
4. Then $\chi_{C(p)} = x^2 - 3x + 2 = p$, since for a $2 \times 2$ matrix $\chi = x^2 - (\operatorname{tr}) x + \det$.

The trap is to forget the minus signs, or to use the row version in one place and the column version in another.
