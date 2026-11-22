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

Why does a matrix ring fix one size $n$?
Let $\mathcal{M}$ be the set of all real matrices of all sizes $m \times n$ with $m, n \ge 1$, and test it against the definition of a [[ring|0894J980RK]].

1. A ring needs a sum $x + y$ for every pair $x, y$ of its elements, and the sum must lie in the ring.
2. The [[sum of two matrices|0BVXADM10P]] is defined only when they have the same size, entry by entry.
3. The matrices $\begin{pmatrix} 1 \end{pmatrix}$ and $I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ both lie in $\mathcal{M}$, but they have different sizes, so they have no sum.
4. So addition is not a binary operation on $\mathcal{M}$, and $\mathcal{M}$ is not a ring.
5. The [[product|076JGP6R3T]] fails as well. Two $2 \times 3$ matrices have no product, because a row of length $3$ cannot be multiplied with a column of length $2$.
6. The same argument applies to the union $M_2(\mathbb{R}) \cup M_3(\mathbb{R})$, since $I_2 + I_3$ is not defined. So it is not a ring either.

## Remarks

### How to repair it

For each fixed $n$, the set $M_n(\mathbb{R})$ is a ring, the [[matrix ring|AB2MD5CD13]].
To combine two sizes, place the matrices along the diagonal of a larger one.
The direct product $M_2(\mathbb{R}) \times M_3(\mathbb{R})$, with operations in each factor, is a ring.
It is isomorphic to the ring of $5 \times 5$ [[block diagonal matrices|001T5FJDC1]] $\operatorname{diag}(A, B)$, because
$$\begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix}\begin{pmatrix} A' & 0 \\ 0 & B' \end{pmatrix} = \begin{pmatrix} AA' & 0 \\ 0 & BB' \end{pmatrix}.$$

### What structure the set does have

The set $\mathcal{M}$ still has a partial product: $AB$ exists exactly when $A$ has as many columns as $B$ has rows.
This product is associative whenever it is defined, and each $I_n$ acts as an identity on the matrices of matching size.
In the language of categories, the real matrices are the arrows of a category whose objects are the positive integers, with an $m \times n$ matrix as an arrow from $n$ to $m$.
A ring is the special case of such a structure with one object, where every product is defined.

## Explanations

### L1 human

A ring needs a sum for any two of its elements.
A $1 \times 1$ matrix and a $2 \times 2$ matrix have no sum, because their entries do not line up.
So to get a ring, we must keep all the matrices the same square size.

### L2 human

The typical use of this example is a habit: before calling a set a ring, check that both operations are defined for every pair of elements.
The repair in the remarks puts matrices of different sizes into one bigger block diagonal matrix.
Then the sizes agree, and the rules of the matrix ring apply.
Watch out: the set of all $n \times n$ matrices for one fixed $n$ is a ring, but the set of all $m \times n$ matrices with $m \ne n$ is only a group under addition.
