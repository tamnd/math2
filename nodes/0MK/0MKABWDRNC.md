---
tag: 0MKABWDRNC
kind: definition
name: Upper triangular matrix
msc: [15A99]
defines: 0N4XY7Z3NN
uses: [0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: lead section
inventory: [1W8C1QV0S3]
---

## Definition

Let $R$ be a ring and let $n \ge 0$ be an integer.
A [[square matrix|0JXZKX526R]] $U = (u_{ij})$ of order $n$ over $R$ is *upper triangular* when $u_{ij} = 0$ for all $i > j$.
It is *strictly upper triangular* when $u_{ij} = 0$ for all $i \ge j$.

## Remarks

Sums and products of upper triangular matrices of the same order are upper triangular.
The [[determinant of a triangular matrix|0K1KKMFHYH]] is the product of its diagonal entries.
The diagonal entries of an upper triangular matrix over a field are its [[eigenvalues|0BQAA2BK3Q]].
A system $Ux = b$ with $U$ upper triangular and invertible is solved by [[back substitution|0ATFVE08MW]].

## Explanations

### L1 human

An upper triangular matrix has zeros everywhere below its diagonal.
Its nonzero entries fill a triangle at the top right.
For example, $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ is upper triangular.
