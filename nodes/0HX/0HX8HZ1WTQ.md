---
tag: 0HX8HZ1WTQ
kind: definition
name: Gram matrix
msc: ["15A63", "15B57"]
topics: [1D4JTZ9VS3]
audience: ug1
defines: 00SPJSDT3Z
uses: [0VGSYBWHV2, 01EK923SKP, 0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Definition

Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$.
Let $k \geq 1$, and let $v_1, \dots, v_k \in V$.
The Gram matrix of $v_1, \dots, v_k$ is the $k \times k$ [[matrix|0JXZKX526R]] $G = G(v_1, \dots, v_k)$ with the entries
$$G_{ij} = \ip{v_i}{v_j} \qquad (1 \leq i, j \leq k).$$
The Gram determinant of $v_1, \dots, v_k$ is $\det G(v_1, \dots, v_k)$.

## Notation

- Our inner product is linear in the first slot. If it is linear in the second slot, as in Mathlib and in physics, the same formula gives the transpose of our matrix.
- For column vectors in $\mathbb{R}^n$ with the dot product, $G = A^T A$, where $A$ has the columns $v_1, \dots, v_k$.
- For column vectors in $\mathbb{C}^n$ with the standard inner product, $G = A^T \overline{A}$.

## Remarks

- The Gram matrix is Hermitian and [[positive semidefinite|01MMVW8CKC]]. The [[concept page|00SPJSDT3Z]] proves both.
- It is invertible if and only if $v_1, \dots, v_k$ are [[linearly independent|~271d272f]].
- Its determinant is the square of the $k$-dimensional [[volume of the parallelepiped|~6efb00d4]] spanned by the $v_i$.

## Explanations

### L1 human

The Gram matrix records all inner products of a list of vectors.
It contains all lengths and all angles between them.
Two lists with the same Gram matrix have the same shape, up to an isometry.

### L2 human

For $v_1 = (1, 0)$ and $v_2 = (3, 4)$ in $\mathbb{R}^2$, the entries are $\ip{v_1}{v_1} = 1$, $\ip{v_1}{v_2} = 3$ and $\ip{v_2}{v_2} = 25$.
So $G = \begin{pmatrix} 1 & 3 \\ 3 & 25 \end{pmatrix}$, and $\det G = 16$.
This is $4^2$, and $4$ is the area of the parallelogram with sides $v_1$ and $v_2$, since its height over $v_1$ is $4$.
A trap: over $\mathbb{C}$, the entry $G_{ji}$ is the conjugate of $G_{ij}$, not equal to it.
