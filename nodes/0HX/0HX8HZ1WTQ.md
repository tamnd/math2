---
tag: 0HX8HZ1WTQ
kind: definition
name: Gram matrix
msc: [15A63, 15B57]
defines: 00SPJSDT3Z
uses: [0VGSYBWHV2]
sources:
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: lead section
---

## Definition

Let $V$ be an inner product space over $\R$ or $\C$, and let $v_1, \dots, v_k \in V$.
The *Gram matrix* of $v_1, \dots, v_k$ is the $k \times k$ matrix $G$ with entries
$$G_{ij} = \langle v_i, v_j \rangle \qquad (1 \le i, j \le k),$$
where $\langle \cdot, \cdot \rangle$ is the [[inner product|0NB0AWGJBW]].

## Remarks

The Gram matrix is Hermitian and [[positive semidefinite|01MMVW8CKC]].
It is invertible if and only if $v_1, \dots, v_k$ are linearly independent.
For real column vectors $v_i \in \R^n$ with the dot product, $G = A^T A$, where $A$ has the columns $v_1, \dots, v_k$.
Its determinant is the square of the $k$-dimensional volume of the parallelepiped spanned by the $v_i$.

## Explanations

### L1 human

The Gram matrix records all inner products of a list of vectors.
It contains all lengths and all angles between them.
Two lists with the same Gram matrix have the same shape, up to an isometry.
