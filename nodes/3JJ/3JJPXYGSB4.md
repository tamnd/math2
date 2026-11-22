---
tag: 3JJPXYGSB4
kind: proof
name: Proof of the Laplace expansion along a column by transposition
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: 06AMCJMMVM
methods: [0NTF6DMVAP]
uses: [0C08BQ3M05, 0ZZQ2E1MTE, 0W809K6AW0, 0W2QAVJQ1W, 0SD528P0EK]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_expansion
    locator: lead section
---

## Proof

We apply the expansion along a row to the transpose of $A$, and we check that its minors are the minors of $A$.

1. Let $A = (a_{kl})$ be an $n \times n$ matrix over a commutative ring $K$ with $n \ge 2$, and fix a column $j$.
2. Let $B = A^{\mathsf{T}}$ be the [[transpose|0W809K6AW0]] of $A$, so $B$ has the entries $b_{kl} = a_{lk}$.
3. For indices $r, s$, let $N_{rs}$ be the [[minor|0SD528P0EK]] of $B$ that we get by deleting row $r$ and column $s$ of $B$.
4. Fix $i$, and let $A_{ij}$ be $A$ with row $i$ and column $j$ deleted.
   Deleting row $j$ and column $i$ of $B$ gives the transpose $(A_{ij})^{\mathsf{T}}$.
   Indeed, both matrices keep the entries $a_{kl}$ with $k \ne i$ and $l \ne j$, in the same order, and each puts $a_{kl}$ in the row for $l$ and the column for $k$.
5. By the rule for the [[determinant of a transpose|0ZZQ2E1MTE]], $N_{ji} = \det (A_{ij})^{\mathsf{T}} = \det A_{ij} = M_{ij}$ for each $i$.
6. By the [[Laplace expansion along row $j$|0C08BQ3M05]] of $B$,
$$\det B = \sum_{i=1}^{n} (-1)^{j+i} b_{ji} N_{ji}.$$
7. By steps 2 and 5, the right side equals $\sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij}$.
8. By the rule for the determinant of a transpose, $\det B = \det A$.
9. With the [[cofactors|0W2QAVJQ1W]] $C_{ij} = (-1)^{i+j} M_{ij}$, steps 6 to 8 give
$$\det A = \sum_{i=1}^{n} a_{ij} C_{ij} = \sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij}.$$

## Idea

Transposing turns columns into rows and does not change any determinant.
So the expansion down column $j$ of $A$ is the expansion along row $j$ of $A^{\mathsf{T}}$.
The only thing to check is that the small determinants match, and they do, because the minor of $A^{\mathsf{T}}$ at $(j, i)$ is the transpose of the minor of $A$ at $(i, j)$.

## Variants

The [[proof by multilinearity|97HQ4MPNBS]] can be run with columns in place of rows.
It then uses the linearity of $\det$ in the columns and the effect of column operations.
