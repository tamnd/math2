---
tag: 14AEYBTCAV
kind: proof
name: Proof of the block multiplication rule
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
proves: WR3RCF5PSQ
methods: [0NTF6DMVAP]
uses: [01AXG9KZQF, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Block matrix operations
---

## Proof

We write one entry of $AB$ with the entry rule, split the sum over the inner index into the column blocks of $A$, and recognize each piece as an entry of a block product.

Let $N_j = n_1 + \dots + n_j$ with $N_0 = 0$, and let $J_j = \{N_{j-1} + 1, \dots, N_j\}$ be the set of column indices of the $j$-th column block of $A$.
In the same way let $M_i = m_1 + \dots + m_i$, $R_k = r_1 + \dots + r_k$, $I_i = \{M_{i-1} + 1, \dots, M_i\}$ and $K_k = \{R_{k-1} + 1, \dots, R_k\}$.

1. The sets $J_1, \dots, J_q$ are disjoint, and their union is $\{1, \dots, n\}$, because $N_q = n_1 + \dots + n_q = n$.
2. Fix $i$ and $k$, a row index $a \in I_i$ and a column index $c \in K_k$. By the [[entry rule of the product|076JGP6R3T]],
$$(AB)_{ac} = \sum_{l=1}^{n} A_{al} B_{lc}.$$
3. By step 1 we may split the sum into groups, one for each $j$:
$$(AB)_{ac} = \sum_{j=1}^{q} \sum_{l \in J_j} A_{al} B_{lc}.$$
4. By the [[definition of a block matrix|01AXG9KZQF]], for $l \in J_j$ the entry $A_{al}$ lies in the block $A_{ij}$, in its row $a - M_{i-1}$ and its column $l - N_{j-1}$.
5. The row partition of $B$ is $(n_1, \dots, n_q)$ by hypothesis, so for $l \in J_j$ the entry $B_{lc}$ lies in the block $B_{jk}$, in its row $l - N_{j-1}$ and its column $c - R_{k-1}$.
6. As $l$ runs through $J_j$, the index $t = l - N_{j-1}$ runs through $1, \dots, n_j$. So by steps 4 and 5 the inner sum is
$$\sum_{t=1}^{n_j} (A_{ij})_{a - M_{i-1},\, t}\, (B_{jk})_{t,\, c - R_{k-1}},$$
which is the entry at position $(a - M_{i-1}, c - R_{k-1})$ of the $m_i \times r_k$ product $A_{ij} B_{jk}$, by the entry rule.
7. Put steps 3 and 6 together: $(AB)_{ac}$ is the entry at position $(a - M_{i-1}, c - R_{k-1})$ of $\sum_{j=1}^{q} A_{ij} B_{jk}$.
8. As $a$ runs through $I_i$ and $c$ runs through $K_k$, these positions run through the whole $m_i \times r_k$ block. So the block of $AB$ in rows $I_i$ and columns $K_k$ is $\sum_j A_{ij} B_{jk}$.

This holds for every $i$ and $k$, so $AB$ has the stated blocks.

## Idea

Each entry of $AB$ is a sum over the inner index.
Cut that index into the column blocks of $A$, and the sum falls into pieces, one for each $j$.
Because the rows of $B$ are cut in the same places, each piece only involves the blocks $A_{ij}$ and $B_{jk}$, and it is exactly one entry of their product.
The rest of the proof is bookkeeping of the offsets $M_{i-1}$, $N_{j-1}$ and $R_{k-1}$.

## Variants

A proof by linear maps avoids the indices.
Write $F^n = F^{n_1} \oplus \dots \oplus F^{n_q}$ and similarly for $F^m$ and $F^r$, and read $A_{ij}$ as the component of $x \mapsto Ax$ from the $j$-th summand to the $i$-th.
Then the composite $x \mapsto A(Bx)$ has the component $\sum_j A_{ij} B_{jk}$ from the $k$-th summand to the $i$-th, since a vector in the $k$-th summand is sent by $B$ to the sum of its components, and $A$ acts on each one.
Matrix multiplication matches composition, so this is the block rule.
