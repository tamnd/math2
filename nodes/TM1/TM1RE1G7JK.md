---
tag: TM1RE1G7JK
kind: statement
role: theorem
name: Schur product theorem
msc: [15B48, 15A45]
uses: [SQT6QCEXZ8, 01MMVW8CKC, 0KX66CZMBB, 0DGZBQWZWN]
about: [SQT6QCEXZ8, 01MMVW8CKC]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_product_theorem
same_as:
  wikidata: Q17103152
  wikipedia: Schur product theorem
---

## Statement

Let $n \ge 1$ and let $A$ and $B$ be $n \times n$ complex [[positive semidefinite matrices|01MMVW8CKC]].
Then their [[Hadamard product|SQT6QCEXZ8]] $A \circ B$, the matrix with entries $(A \circ B)_{ij} = a_{ij} b_{ij}$, is positive semidefinite.

## Remarks

By the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]], $B = \sum_k v_k v_k^*$ for some vectors $v_k \in \C^n$.
For one vector $v$, $A \circ (v v^*) = D A D^*$ with $D = \operatorname{diag}(v_1, \ldots, v_n)$, which is positive semidefinite.
So $A \circ B = \sum_k D_k A D_k^*$ is a sum of positive semidefinite matrices.
Example: $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$ are positive definite, and $A \circ B = \begin{pmatrix} 2 & -1 \\ -1 & 4 \end{pmatrix}$ has trace $6$ and determinant $7$, so it is positive definite.
If $A$ and $B$ are both [[positive definite|0KX66CZMBB]], then so is $A \circ B$.
The hypothesis on $B$ is needed: with $A = I_2$ and $B = \operatorname{diag}(1, -1)$, $A \circ B = B$ is not positive semidefinite.

## Explanations

### L1 human

Multiply two matrices entry by entry, not by the usual row-times-column rule.
If both matrices are positive semidefinite, the result is again positive semidefinite.
For the usual product this would fail, since $AB$ need not even be Hermitian.

### L2 human

Positive semidefinite matrices are [[Gram matrices|00SPJSDT3Z]] $a_{ij} = \ip{x_i}{x_j}$, and the entrywise product of two Gram matrices is the Gram matrix of the tensor products $x_i \otimes y_i$; this gives a second proof.
The theorem shows that the entrywise power $(a_{ij}^k)$ and the entrywise exponential $(e^{a_{ij}})$ of a positive semidefinite matrix are positive semidefinite.
This is why sums, products and exponentials of positive definite kernels are again positive definite kernels in machine learning.
