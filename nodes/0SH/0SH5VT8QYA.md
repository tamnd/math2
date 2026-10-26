---
tag: 0SH5VT8QYA
kind: statement
role: theorem
name: Basis of a tensor product
msc: [15A69]
uses: [0G31VJ5YS5, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Tensor_product
    locator: From bases
---

## Statement

Let $F$ be a field, and let $V$ and $W$ be vector spaces over $F$.
Let $(e_i)_{i \in I}$ be a [[basis|0KCQ9Y3QKA]] of $V$ and let $(f_j)_{j \in J}$ be a basis of $W$.
Then the family $(e_i \otimes f_j)_{(i, j) \in I \times J}$ is a basis of the [[tensor product|0BF2DE2SYK]] $V \otimes W$.

## Remarks

So each vector of $V \otimes W$ is uniquely $\sum_{i,j} c_{ij}\, e_i \otimes f_j$ with only finitely many nonzero $c_{ij} \in F$.
For $v = \sum_i a_i e_i$ and $w = \sum_j b_j f_j$, $v \otimes w = \sum_{i,j} a_i b_j\, e_i \otimes f_j$.
Thus the coefficients of a vector $v \otimes w$ form a matrix of rank at most $1$.

## Explanations

### L1 human

From a basis of each factor, we get a basis of the tensor product.
Its vectors are all the products of a basis vector of $V$ and a basis vector of $W$.
A vector of $V \otimes W$ is like a matrix of coefficients.
