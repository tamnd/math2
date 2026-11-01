---
tag: 71K5G4GNNZ
kind: definition
name: Sparse matrix
msc: [65F50, 15B99]
defines: JGACZYEEY7
uses: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Sparse_matrix
---

## Definition

Let $A$ be an $m \times n$ [[matrix|0VD9ZSWWJG]], and let $\operatorname{nnz}(A)$ be the number of its nonzero entries.
The matrix $A$ is *sparse* when $\operatorname{nnz}(A)$ is small compared with $mn$, so that it pays to store and process only the nonzero entries.
For a family of $n \times n$ matrices with $n$ growing, a common precise form of this condition is $\operatorname{nnz}(A) = O(n)$.

## Remarks

The notion has no fixed threshold; it depends on the size of the matrix and on the algorithms in use.
The *density* of $A$ is $\operatorname{nnz}(A) / (mn)$, and a matrix that is not sparse is called *dense*.
Example: the $n \times n$ [[tridiagonal matrix|DARX1KZRHZ]] with $2$ on the diagonal and $-1$ beside it has $3n - 2$ nonzero entries, which is $O(n)$, so the family is sparse.
Non-example: the $n \times n$ matrix with all entries $1$ has $n^2$ nonzero entries, so it is dense.
Common storage formats are the coordinate list and the compressed sparse row format.
