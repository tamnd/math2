---
tag: 0ETGP0XVCJ
kind: statement
role: theorem
name: Gershgorin circle theorem
msc: [15A42, 15A18]
uses: [0ZND7NQ970]
sources:
  - url: https://en.wikipedia.org/wiki/Gershgorin_circle_theorem
    locator: Statement and proof
same_as:
  wikidata: Q978688
  wikipedia: Gershgorin circle theorem
---

## Statement

Let $A = (a_{ij})$ be an $n \times n$ matrix over $\C$.
For $1 \le i \le n$, let $R_i = \sum_{j \ne i} \abs{a_{ij}}$, and let $D_i = \{z \in \C : \abs{z - a_{ii}} \le R_i\}$ be the closed disc with centre $a_{ii}$ and radius $R_i$.
Then each [[eigenvalue|0BQAA2BK3Q]] of $A$ lies in at least one of the discs $D_1, \dots, D_n$.

## Remarks

The discs are called *Gershgorin discs*.
The proof takes an eigenvector $x$ and an index $i$ with $\abs{x_i}$ maximal, and estimates row $i$ of $Ax = \lambda x$.
Since $A$ and $A^T$ have the same eigenvalues, the same holds with column sums.
A strictly diagonally dominant matrix, with $\abs{a_{ii}} > R_i$ for all $i$, has no eigenvalue $0$, so it is invertible.

## Explanations

### L1 human

The eigenvalues of a matrix lie near its diagonal entries, when the other entries are small.
Each row gives a disc around its diagonal entry, with the radius equal to the sum of the other absolute values of the row.
Every eigenvalue lies in one of these discs.
