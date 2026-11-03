---
tag: YARP6081MC
kind: definition
name: Structure constants
msc: [17A01, 17B05]
defines: HFXWYNFB9A
uses: [1SENAHZW5A, 0KCQ9Y3QKA]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_constants
---

## Definition

Let $K$ be a field and let $A$ be an [[algebra|1SENAHZW5A]] over $K$ of finite dimension $n$.
Let $e_1, \dots, e_n$ be a [[basis|0KCQ9Y3QKA]] of $A$.
The *structure constants* of $A$ in this basis are the scalars $c_{ij}^k \in K$, for $1 \le i, j, k \le n$, defined by
$$e_i e_j = \sum_{k=1}^{n} c_{ij}^k e_k.$$

## Remarks

By bilinearity, for $x = \sum_i x_i e_i$ and $y = \sum_j y_j e_j$ the product is $xy = \sum_{i,j,k} x_i y_j c_{ij}^k e_k$.
Conversely, any family of $n^3$ scalars $c_{ij}^k$ defines an algebra structure on $K^n$ in this way.
The algebra is commutative if and only if $c_{ij}^k = c_{ji}^k$ for all $i, j, k$.
It is associative if and only if $\sum_l c_{ij}^l c_{lk}^m = \sum_l c_{jk}^l c_{il}^m$ for all $i, j, k, m$.
Example: for $\R^3$ with the cross product and the standard basis, $c_{ij}^k = \varepsilon_{ijk}$, the Levi-Civita symbol; for instance $e_1 \times e_2 = e_3$ gives $c_{12}^3 = 1$.
The structure constants depend on the basis: in another basis of the same algebra they are in general different numbers.
