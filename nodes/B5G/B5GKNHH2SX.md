---
tag: B5GKNHH2SX
kind: statement
role: proposition
name: Peirce decomposition
msc: [16U40, 16S50]
uses: [0894J980RK, 0X4JKZXJ86, SS8T32TMEX]
about: [SS8T32TMEX, 0N5NJZKKN3]
sources:
  - url: https://en.wikipedia.org/wiki/Peirce_decomposition
same_as:
  wikidata: Q7160950
  wikipedia: Peirce decomposition
---

## Statement

Let $R$ be a [[ring|0894J980RK]] and let $e_1, \dots, e_n$ be a [[complete set of orthogonal idempotents|SS8T32TMEX]] of $R$.
For $1 \le i, j \le n$ put $R_{ij} = e_i R e_j = \set{e_i r e_j : r \in R}$.
Then:

1. $R = \bigoplus_{i,j=1}^{n} R_{ij}$ as an abelian group, and the component of $r \in R$ in $R_{ij}$ is $e_i r e_j$.
2. $R_{ij} R_{kl} \subseteq R_{il}$ if $j = k$, and $R_{ij} R_{kl} = 0$ if $j \ne k$.
3. Each $R_{ii}$ is a ring with unit element $e_i$, under the addition and multiplication of $R$.

## Remarks

The proof writes $r = 1 \cdot r \cdot 1 = \sum_{i,j} e_i r e_j$, which gives the sum.
The sum is direct: if $\sum_{i,j} e_i r_{ij} e_j = 0$, then multiplying by $e_k$ on the left and $e_l$ on the right leaves $e_k r_{kl} e_l = 0$, by the [[idempotent|0X4JKZXJ86]] and orthogonality relations.
Part 2 follows from $e_j e_k = 0$ for $j \ne k$.
For a single idempotent $e$ and $f = 1 - e$ this reads $R = eRe \oplus eRf \oplus fRe \oplus fRf$.
Example: in $M_2(K)$ with $e = E_{11}$, the four pieces are the matrices supported on one of the four entries, and the decomposition is the splitting of a matrix into its entries.
In general $R$ is isomorphic to the ring of $n \times n$ matrices $(a_{ij})$ with $a_{ij} \in R_{ij}$, with the usual matrix operations.

## Explanations

### L1 human

Idempotents act like projections, and a complete set of them splits the unit element into pieces.
Cutting every element of the ring on both sides by these pieces writes the ring as a "matrix" of smaller parts.
For a matrix ring with the diagonal matrix units, this is just splitting a matrix into its entries.

### L2 human

The Peirce decomposition is the basic tool for reducing questions about a ring to the corner rings $e R e$.
It shows that a ring with a complete set of orthogonal idempotents looks like a generalized matrix ring.
If the idempotents are central, the off-diagonal pieces vanish and $R$ is the direct product $R_{11} \times \cdots \times R_{nn}$.
It is used in the structure theory of Artinian rings and when idempotents are lifted modulo an ideal.
