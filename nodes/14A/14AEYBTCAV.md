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

Let $N_j = n_1 + \cdots + n_j$ with $N_0 = 0$, and let $J_j = \{N_{j-1} + 1, \dots, N_j\}$ be the indices of the $j$-th column block of $A$.
Define $I_i$ for the $m_i$ and $K_k$ for the $r_k$ in the same way.

1. The sets $J_1, \dots, J_q$ are disjoint and their union is $\{1, \dots, n\}$, because $n = n_1 + \cdots + n_q$.
2. Fix $i$ and $k$, and fix a row index $a \in I_i$ and a column index $c \in K_k$ of $AB$. By the [[product rule|076JGP6R3T]], $(AB)_{ac} = \sum_{l=1}^{n} A_{al} B_{lc}$.
3. By step 1 we can split this sum into groups: $(AB)_{ac} = \sum_{j=1}^{q} \sum_{l \in J_j} A_{al} B_{lc}$.
4. By the [[definition of a block matrix|01AXG9KZQF]], for $l \in J_j$ the entry $A_{al}$ is an entry of the block $A_{ij}$. It sits in row $a - M_{i-1}$ and column $l - N_{j-1}$ of the block, where $M_{i-1} = m_1 + \cdots + m_{i-1}$.
5. Since $B$ has row partition $(n_j)$, for $l \in J_j$ the entry $B_{lc}$ is an entry of the block $B_{jk}$, in row $l - N_{j-1}$ and column $c - R_{k-1}$, where $R_{k-1} = r_1 + \cdots + r_{k-1}$.
6. So the inner sum $\sum_{l \in J_j} A_{al} B_{lc}$ is the product rule for one entry of the $m_i \times r_k$ matrix $A_{ij} B_{jk}$. It is the entry at $(a - M_{i-1}, c - R_{k-1})$.
7. By steps 3 and 6, $(AB)_{ac}$ is the entry at $(a - M_{i-1}, c - R_{k-1})$ of $\sum_{j} A_{ij} B_{jk}$.
8. This holds for all $a \in I_i$ and $c \in K_k$. So the $(i, k)$ block of $AB$ is $\sum_j A_{ij} B_{jk}$.

## Idea

Each entry of $AB$ is a sum over the inner index.
Cutting the inner index into the column blocks of $A$ splits the sum into pieces.
Each piece is an entry of a block product $A_{ij} B_{jk}$, because the row blocks of $B$ use the same cuts.

## Variants

- By linear maps: $A$ and $B$ are maps between direct sums, and the block $A_{ij}$ is the map from the $j$-th summand to the $i$-th. Composition then gives $(AB)_{ik} = \sum_j A_{ij} B_{jk}$.
