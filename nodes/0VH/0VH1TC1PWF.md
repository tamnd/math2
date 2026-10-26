---
tag: 0VH1TC1PWF
kind: definition
name: Companion matrix
msc: [15A21]
defines: 0ZCWPNZTQ3
uses: [0CP7YY6NAG, 039HF58KQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Companion_matrix
    locator: lead section
---

## Definition

Let $F$ be a field, let $n \ge 1$, and let $p(t) = t^n + c_{n-1} t^{n-1} + \cdots + c_1 t + c_0$ be a monic polynomial over $F$.
The *companion matrix* of $p$ is the $n \times n$ matrix
$$C(p) = \begin{pmatrix} 0 & 0 & \cdots & 0 & -c_0 \\ 1 & 0 & \cdots & 0 & -c_1 \\ 0 & 1 & \cdots & 0 & -c_2 \\ \vdots & & \ddots & & \vdots \\ 0 & 0 & \cdots & 1 & -c_{n-1} \end{pmatrix}.$$

## Remarks

The [[characteristic polynomial|0VSSPAFM2C]] and the [[minimal polynomial|03NDVCSHSB]] of $C(p)$ both equal $p$.
In the basis $e_1, \dots, e_n$, the map of $C(p)$ sends $e_i$ to $e_{i+1}$ for $i < n$.
Some authors use the transpose of this matrix as the companion matrix.
Companion matrices are the blocks of the [[rational canonical form|042JWAR3Q0]].

## Explanations

### L1 human

For each monic polynomial, the companion matrix is a matrix with exactly that characteristic polynomial.
It shifts each basis vector to the next one, and the polynomial fixes the image of the last one.
So questions about roots of polynomials become questions about eigenvalues of matrices.
