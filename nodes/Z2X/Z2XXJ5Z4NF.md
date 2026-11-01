---
tag: Z2XXJ5Z4NF
kind: definition
name: Hadamard product
msc: [15A99, 15B48]
defines: SQT6QCEXZ8
uses: [0VD9ZSWWJG, 0GYGHKX834]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard_product_(matrices)
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $m, n \ge 1$.
Let $A = (a_{ij})$ and $B = (b_{ij})$ be $m \times n$ [[matrices|0VD9ZSWWJG]] over $R$.
The *Hadamard product* of $A$ and $B$ is the $m \times n$ matrix $A \circ B$ with entries
$$(A \circ B)_{ij} = a_{ij} b_{ij}$$
for $1 \le i \le m$ and $1 \le j \le n$.

## Remarks

Example: for $A = \begin{pmatrix} 1 & 0 & 2 \end{pmatrix}$ and $B = \begin{pmatrix} 3 & 5 & -1 \end{pmatrix}$, the entries of $A \circ B$ are $1 \cdot 3$, $0 \cdot 5$ and $2 \cdot (-1)$, so $A \circ B = \begin{pmatrix} 3 & 0 & -2 \end{pmatrix}$.
Non-example: a $2 \times 2$ matrix and a $2 \times 3$ matrix have no Hadamard product, because the two matrices must have the same size.
The Hadamard product is commutative, associative and distributive over addition.
Its identity element is the $m \times n$ matrix $J$ with all entries $1$, not the identity matrix.
Other notations are $A \odot B$ and $A * B$.
