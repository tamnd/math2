---
tag: 97HQ4MPNBS
kind: proof
name: Proof of the Laplace expansion by multilinearity
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: 0C08BQ3M05
methods: [DX2H7AD66G]
uses: [0PPG793642, 09YB3WQG38, 0ZZQ2E1MTE, 1C8RRWHD45, 0W2QAVJQ1W, 0SD528P0EK]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_expansion
    locator: Proof
---

## Proof

Fix row $i$, and let $e_1, \dots, e_n$ be the standard rows.

1. Row $i$ of $A$ is $\sum_j a_{ij} e_j$. By [[multilinearity|0PPG793642]] in row $i$, $\det A = \sum_j a_{ij} \det A^{(j)}$, where $A^{(j)}$ is $A$ with row $i$ replaced by $e_j$.
2. Fix $j$. It is enough to show $\det A^{(j)} = (-1)^{i+j} M_{ij}$, by the definition of the [[cofactor|0W2QAVJQ1W]].
3. For each $k \neq i$, subtract $a_{kj}$ times row $i$ from row $k$ of $A^{(j)}$. Since row $i$ is $e_j$, this only sets the entry $(k, j)$ to $0$.
4. By the [[effect of row operations|09YB3WQG38]], these steps do not change $\det$. Call the result $B$. Column $j$ of $B$ is $e_i$, and row $i$ of $B$ is $e_j$.
5. Deleting row $i$ and column $j$ of $B$ gives the same matrix $A_{ij}$ as for $A$, whose determinant is the [[minor|0SD528P0EK]] $M_{ij}$.
6. Move row $i$ of $B$ to the top by $i - 1$ swaps of neighbouring rows. By the effect of row operations, $\det$ changes by $(-1)^{i-1}$.
7. Move column $j$ to the front by $j - 1$ swaps of neighbouring columns. By the [[transpose rule|0ZZQ2E1MTE]], column swaps also change the sign, so $\det$ changes by $(-1)^{j-1}$.
8. The result is $\begin{pmatrix} 1 & 0 \\ 0 & A_{ij} \end{pmatrix}$, with the rows and columns of $A_{ij}$ in their original order. So $\det A^{(j)} = (-1)^{i+j} \det \begin{pmatrix} 1 & 0 \\ 0 & A_{ij} \end{pmatrix}$.
9. For $(n-1) \times (n-1)$ matrices $X$, let $D(X) = \det \begin{pmatrix} 1 & 0 \\ 0 & X \end{pmatrix}$. By multilinearity of $\det$, $D$ is multilinear in the rows of $X$.
10. If $X$ has two equal rows, then so does the bordered matrix, and $D(X) = 0$. So $D$ is alternating, and $D(I_{n-1}) = \det I_n = 1$.
11. By the [[existence and uniqueness theorem|1C8RRWHD45]], $D(X) = \det X$. So $\det A^{(j)} = (-1)^{i+j} M_{ij}$.
12. With step 1, $\det A = \sum_j a_{ij} (-1)^{i+j} M_{ij} = \sum_j a_{ij} C_{ij}$.

## Idea

Linearity in row $i$ splits $\det A$ into $n$ pieces, one for each entry of the row.
In each piece row $i$ is a standard row, and row operations clear its column.
Moving that row and column to the corner costs the sign $(-1)^{i+j}$ and leaves the minor.

## Variants

The [[proof by the Leibniz formula|AF3XSRXE6T]] groups the Leibniz terms instead, and computes the same sign by counting transpositions.
This proof avoids that sign count, at the price of the uniqueness theorem in step 11.
