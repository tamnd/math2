---
tag: 8JW8F4VVED
kind: statement
role: theorem
name: Robinson–Schensted–Knuth correspondence
msc: ["05E05", "05E10", 05A19]
uses: [Q6TH9PH2R7, 1SCF8X47G1, 43VFMJCDYJ, 0VD9ZSWWJG]
about: [Q6TH9PH2R7]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson%E2%80%93Schensted%E2%80%93Knuth_correspondence
same_as:
  wikidata: Q2997914
  wikipedia: Robinson–Schensted–Knuth correspondence
---

## Statement

Let $m, n \ge 1$.
Let $A = (a_{ij})$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] with nonnegative integer entries.
List the pairs $(i, j)$ in lexicographic order, each pair repeated $a_{ij}$ times.
Insert the second coordinates $j$ in this order into the empty tableau by row insertion, and let $P(A)$ be the result.
Let $Q(A)$ be the tableau that has entry $i$ in the cell created when the pair $(i, j)$ is inserted.

1. $P(A)$ and $Q(A)$ are semistandard [[Young tableaux|Q6TH9PH2R7]] of the same shape.
2. The entry $j$ appears in $P(A)$ exactly $\sum_i a_{ij}$ times, and the entry $i$ appears in $Q(A)$ exactly $\sum_j a_{ij}$ times.
3. The map $A \mapsto (P(A), Q(A))$ is a bijection onto the set of pairs $(P, Q)$ of semistandard tableaux of the same shape. Here $P$ has entries in $\set{1, \dots, n}$ and $Q$ has entries in $\set{1, \dots, m}$.
4. $P(A^T) = Q(A)$ and $Q(A^T) = P(A)$.

## Remarks

The insertion rule is the one of the [[Robinson–Schensted correspondence|1SCF8X47G1]]: an inserted entry $x$ bumps the leftmost entry of the row that is strictly larger than $x$.
Equal first coordinates are listed with increasing second coordinates, so the recording tableau stays semistandard.
For a permutation matrix the construction gives back the Robinson–Schensted correspondence.

Example: for $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ the pairs are $(1,1), (1,2), (2,2)$.
Inserting $1, 2, 2$ gives $P = \begin{smallmatrix} 1 & 2 & 2 \end{smallmatrix}$, and $Q = \begin{smallmatrix} 1 & 1 & 2 \end{smallmatrix}$.
The column sums $1, 2$ of $A$ match the content of $P$, and the row sums $2, 1$ match the content of $Q$.

## Explanations

### L1 human

The correspondence turns a table of counts into a pair of semistandard tableaux of the same shape, and back.
The column totals of the table become the numbers of $1$s, $2$s, and so on in one tableau.
The row totals become the same numbers for the other tableau.

### L2 human

Summing over all matrices with weight $\prod_{i,j} (x_i y_j)^{a_{ij}}$ gives the Cauchy identity
$$\prod_{i=1}^{m} \prod_{j=1}^{n} \frac{1}{1 - x_i y_j} = \sum_{\lambda} s_\lambda(x_1, \dots, x_m) \, s_\lambda(y_1, \dots, y_n),$$
where $s_\lambda$ is the [[Schur polynomial|43VFMJCDYJ]].
Part 4 applied to symmetric matrices gives similar identities for $\sum_\lambda s_\lambda$.
The correspondence is due to Knuth, and it is the main bijective tool in the theory of symmetric functions.
