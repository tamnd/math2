---
tag: Q3FKC0FMXR
kind: example
name: The set of all matrices of all sizes is not a ring
msc: ["16S50", "15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
not_instance_of:
  - target: AB2MD5CD13
    note: the sum of a 1 by 1 matrix and a 2 by 2 matrix is not defined, so addition is not a binary operation on the set of all matrices
uses: [0BVXADM10P, 076JGP6R3T, 0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_ring
    locator: lead section
---

## Example

Let $\mathcal{M}$ be the set of all real matrices of all sizes $m \times n$ with $m, n \ge 1$.

1. A [[ring|0894J980RK]] needs an addition defined for every pair of its elements.
2. The [[sum|0BVXADM10P]] of $\begin{pmatrix} 1 \end{pmatrix}$ and $I_2$ is not defined, because the sizes differ.
3. So addition is not a binary operation on $\mathcal{M}$, and $\mathcal{M}$ is not a ring.
4. The [[product|076JGP6R3T]] also fails for many pairs, such as two $2 \times 3$ matrices.
5. Even the set $M_2(\mathbb{R}) \cup M_3(\mathbb{R})$ is not a ring, by the same argument.

## Remarks

For each fixed $n$, the set $M_n(\mathbb{R})$ is a ring.
The direct product $M_2(\mathbb{R}) \times M_3(\mathbb{R})$ is a ring, and it is isomorphic to the ring of [[block diagonal matrices|001T5FJDC1]] $\operatorname{diag}(A, B)$ of order 5.
All matrices of all sizes form a category, where the product is a partial operation.

## Explanations

### L1 human

A ring needs a sum for any two of its elements.
Matrices of different sizes have no sum, so we must fix one size.

### L2 human

The fix in the remarks puts matrices of different sizes into one bigger matrix.
Then the sizes agree, and the rules of the matrix ring apply.
