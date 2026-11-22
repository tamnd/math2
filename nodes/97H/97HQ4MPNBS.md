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

We split row $i$ into its entries times standard rows, and we reduce each piece to a minor by row operations and swaps.
Let $A = (a_{kl})$ be an $n \times n$ matrix over a commutative ring $K$ with $n \ge 2$, fix a row $i$, and let $e_1, \dots, e_n$ be the standard rows.

*Splitting row $i$.*

1. Row $i$ of $A$ is $\sum_j a_{ij} e_j$.
   Let $A^{(j)}$ be $A$ with row $i$ replaced by $e_j$.
   By [[multilinearity|0PPG793642]] in row $i$,
$$\det A = \sum_{j=1}^{n} a_{ij} \det A^{(j)}.$$
2. By the definition of the [[cofactor|0W2QAVJQ1W]], it is enough to show that $\det A^{(j)} = (-1)^{i+j} M_{ij}$ for each $j$.
   From now on we fix $j$.

*Clearing column $j$.*

3. For each $k \neq i$, subtract $a_{kj}$ times row $i$ from row $k$ of $A^{(j)}$.
   Row $i$ is $e_j$, so this step only changes the entry $(k, j)$, and it changes it to $0$.
4. By the [[effect of row operations|09YB3WQG38]], these steps do not change the determinant.
   Call the result $B$, so $\det B = \det A^{(j)}$.
5. Column $j$ of $B$ is the standard column with $1$ in place $i$, and row $i$ of $B$ is $e_j$.
   Deleting row $i$ and column $j$ of $B$ leaves the same matrix $A_{ij}$ as for $A$, whose determinant is the [[minor|0SD528P0EK]] $M_{ij}$.

*Moving the $1$ to the corner.*

6. Move row $i$ of $B$ to the top by $i - 1$ swaps of adjacent rows.
   Each swap changes the sign of the determinant, so the total factor is $(-1)^{i-1}$.
7. Move column $j$ to the front by $j - 1$ swaps of adjacent columns.
   By the [[transpose rule|0ZZQ2E1MTE]], a column swap also changes the sign, so the factor is $(-1)^{j-1}$.
8. The rows and columns of $A_{ij}$ keep their order during these swaps, so the result is a bordered matrix, and
$$\det A^{(j)} = (-1)^{i-1} (-1)^{j-1} \det \begin{pmatrix} 1 & 0 \\ 0 & A_{ij} \end{pmatrix} = (-1)^{i+j} \det \begin{pmatrix} 1 & 0 \\ 0 & A_{ij} \end{pmatrix}.$$

*The bordered determinant.*

9. For $(n-1) \times (n-1)$ matrices $X$, put
$$D(X) = \det \begin{pmatrix} 1 & 0 \\ 0 & X \end{pmatrix}.$$
   A row of $X$ is a row of the bordered matrix with a $0$ in front, so $D$ is multilinear in the rows of $X$ by multilinearity of $\det$.
10. If $X$ has two equal rows, then the bordered matrix has two equal rows, so $D(X) = 0$.
    Also $D(I_{n-1}) = \det I_n = 1$.
11. So $D$ is multilinear, alternating and normalized in the rows.
    By the [[existence and uniqueness theorem|1C8RRWHD45]], $D(X) = \det X$ for every $X$.
12. With $X = A_{ij}$, steps 8 and 11 give $\det A^{(j)} = (-1)^{i+j} M_{ij}$.
13. By step 1, $\det A = \sum_j a_{ij} (-1)^{i+j} M_{ij} = \sum_j a_{ij} C_{ij}$, which is the Laplace expansion along row $i$.

## Idea

Linearity in row $i$ splits $\det A$ into $n$ pieces, one for each entry of the row.
In each piece row $i$ is a standard row $e_j$, and its single $1$ lets us clear the rest of column $j$ without changing the determinant.
Moving that row and that column to the top left corner costs the sign $(-1)^{i+j}$.
What is left is the minor $M_{ij}$ with a $1$ in the corner, and the uniqueness theorem says that the corner changes nothing.

## Variants

The [[proof by the Leibniz formula|AF3XSRXE6T]] groups the Leibniz terms instead, and it finds the same sign by counting transpositions.
The present proof avoids that count, but it needs the uniqueness theorem in step 11.
Step 11 can also be done with the Leibniz formula: a permutation that gives a nonzero term of the bordered matrix must fix the first index, and the remaining terms are those of $\det X$.
