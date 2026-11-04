---
tag: 3JJPXYGSB4
kind: proof
name: Proof of the Laplace expansion along a column by transposition
msc: [15A15]
proves: 06AMCJMMVM
uses: [0C08BQ3M05, 0ZZQ2E1MTE, 0W809K6AW0, 0W2QAVJQ1W, 0SD528P0EK]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_expansion
    locator: lead section
---

## Proof

We apply the expansion along a row to the transpose of $A$.

1. Let $A = (a_{kl})$ be an $n \times n$ matrix over $K$ with $n \ge 2$, and fix a column $j$.
2. Let $B = A^T$ be the [[transpose|0W809K6AW0]] of $A$. So $B$ has entries $b_{kl} = a_{lk}$.
3. For indices $r, s$, let $N_{rs}$ be the [[minor|0SD528P0EK]] of $B$ that results when row $r$ and column $s$ of $B$ are deleted.
4. Fix $i$, and let $A_{ij}$ be $A$ with row $i$ and column $j$ deleted. Deleting row $j$ and column $i$ of $B$ gives the transpose $(A_{ij})^T$.
5. Indeed, both matrices keep the entries $a_{kl}$ with $k \ne i$ and $l \ne j$, in the same order. Each puts $a_{kl}$ in the row for $l$ and the column for $k$.
6. By the rule for the [[determinant of a transpose|0ZZQ2E1MTE]], $N_{ji} = \det (A_{ij})^T = \det A_{ij} = M_{ij}$, for each $i$.
7. By the [[Laplace expansion along row $j$|0C08BQ3M05]] of $B$, $\det B = \sum_{i=1}^{n} (-1)^{j+i} b_{ji} N_{ji}$.
8. By steps 2 and 6, the right side is $\sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij}$.
9. By the rule for the determinant of a transpose, $\det B = \det A$.
10. With the [[cofactors|0W2QAVJQ1W]] $C_{ij} = (-1)^{i+j} M_{ij}$, steps 7 to 9 give $\det A = \sum_{i=1}^{n} a_{ij} C_{ij} = \sum_{i=1}^{n} (-1)^{i+j} a_{ij} M_{ij}$.

## Idea

Transposing turns columns into rows and does not change any determinant. So the expansion along column $j$ of $A$ is the expansion along row $j$ of $A^T$, with the same minors.
