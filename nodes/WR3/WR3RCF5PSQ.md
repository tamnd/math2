---
tag: WR3RCF5PSQ
kind: statement
role: theorem
name: Block multiplication rule
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
about: [0ASDFEQS6P]
uses: [01AXG9KZQF, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Block_matrix
    locator: Block matrix operations
  - book: isbn:9780321982384
    locator: Section 2.4
---

## Statement

Let $R$ be a ring.
Let $A$ be an $m \times n$ [[block matrix|01AXG9KZQF]] with row partition $(m_1, \dots, m_p)$ and column partition $(n_1, \dots, n_q)$.
Let $B$ be an $n \times r$ block matrix with row partition $(n_1, \dots, n_q)$ and column partition $(r_1, \dots, r_s)$.
Then $AB$ is the block matrix with row partition $(m_i)$, column partition $(r_k)$ and blocks
$$(AB)_{ik} = \sum_{j=1}^{q} A_{ij} B_{jk}, \qquad 1 \le i \le p, \ 1 \le k \le s.$$

## Remarks

### Why each hypothesis is needed

- The column partition of $A$ must equal the row partition of $B$. Otherwise the products $A_{ij} B_{jk}$ are not defined.
- For example, cut the columns of a $3 \times 3$ matrix $A$ as $2 + 1$ and the rows of $B$ as $1 + 2$. Then $A_{11}$ has $2$ columns and $B_{11}$ has $1$ row.
- The order $A_{ij} B_{jk}$ matters, because the blocks are matrices and need not commute.

### Consequences

- With $q = 1$ and $B$ cut into columns, $AB = (A b_1 \mid \cdots \mid A b_r)$: the columns of $AB$ are $A$ times the columns of $B$.
- With $A$ cut into columns and $B$ into rows, $AB = \sum_j a_j b_j^{\mathsf{T}}$, a sum of rank-one matrices (column-row expansion).
- $\begin{pmatrix} A_1 & 0 \\ 0 & A_2 \end{pmatrix} \begin{pmatrix} B_1 & 0 \\ 0 & B_2 \end{pmatrix} = \begin{pmatrix} A_1 B_1 & 0 \\ 0 & A_2 B_2 \end{pmatrix}$, so [[block diagonal matrices|001T5FJDC1]] multiply blockwise.
- The block upper triangular matrices with a fixed partition are closed under products.

### Generalizations

- The rule holds for maps between direct sums of modules, and in any additive category.

## Explanations

### L1 human

We can multiply block matrices as if the blocks were numbers.
We must keep the order of the factors in each product.
The cuts between the columns of the first matrix must match the cuts between the rows of the second.

### L2 human

The entry formula $\sum_l a_{il} b_{lk}$ sums over the inner index $l$.
The block rule groups the values of $l$ by the column blocks of $A$, and each group gives one block product.
