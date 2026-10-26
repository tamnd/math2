---
tag: ~e4f8becb
kind: definition
name: Matrix–vector product
msc: [15A99]
defines: ~5bc8da49
uses: [~a2759ca2]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: lead section
---

## Definition

Let $R$ be a ring, let $A = (a_{ij})$ be an $m \times n$ [[matrix|~52f4e417]] over $R$, and let $x = (x_1, \dots, x_n)^T \in R^n$ be a column vector.
The *matrix–vector product* $Ax$ is the column vector in $R^m$ with entries
$$(Ax)_i = \sum_{j=1}^{n} a_{ij} x_j$$
for $1 \le i \le m$.

## Remarks

If $A_1, \dots, A_n$ are the columns of $A$, then $Ax = x_1 A_1 + \cdots + x_n A_n$, a [[linear combination|~2c120615]] of the columns.
A [[system of linear equations|~12095b88]] is the equation $Ax = b$.
The map $x \mapsto Ax$ is linear, see [[multiplication by a matrix as a linear map|~fef0ead1]].
For example, $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 7 \end{pmatrix}$.

## Explanations

### L1 human

To multiply a matrix by a vector, take each row of the matrix in turn.
Multiply its entries by the entries of the vector, position by position, and add the results.
Each row gives one entry of the answer.
