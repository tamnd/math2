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

Two block matrices whose cuts match in the middle can be multiplied as if their blocks were entries.
Let $R$ be a ring.
Let $A$ be an $m \times n$ [[block matrix|01AXG9KZQF]] over $R$ with row partition $(m_1, \dots, m_p)$ and column partition $(n_1, \dots, n_q)$.
Let $B$ be an $n \times r$ block matrix over $R$ with row partition $(n_1, \dots, n_q)$ and column partition $(r_1, \dots, r_s)$.
Then $AB$ is the block matrix with row partition $(m_1, \dots, m_p)$, column partition $(r_1, \dots, r_s)$ and blocks
$$(AB)_{ik} = \sum_{j=1}^{q} A_{ij} B_{jk}, \qquad 1 \le i \le p, \ 1 \le k \le s.$$

## Remarks

### Why each hypothesis is needed

The column partition of $A$ must equal the row partition of $B$, since otherwise the block products are not defined.
For example, cut the columns of a $3 \times 3$ matrix $A$ as $2 + 1$ and the rows of a $3 \times 3$ matrix $B$ as $1 + 2$.
Then $A_{11}$ has $2$ columns and $B_{11}$ has $1$ row, so $A_{11} B_{11}$ does not exist.
The order $A_{ij} B_{jk}$ in each term must also be kept, because the blocks are matrices and need not commute.
The ring $R$ need not be commutative, since the proof only regroups the sum in the entry rule.

### A worked case

For two $3 \times 3$ matrices cut as $2 + 1$, [[the worked product|7C93RPT1MB]] computes the four blocks of $AB$ and checks two entries.
The bottom left block there is
$$A_{21} B_{11} + A_{22} B_{21} = \begin{pmatrix} 3 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 4 \end{pmatrix} = \begin{pmatrix} 3 & 4 \end{pmatrix}.$$

### What it gives you

The rule contains the standard views of the [[matrix product|076JGP6R3T]] as special cases.
Cut $B$ into its columns and do not cut $A$: then $AB = (A b_1 \mid \dots \mid A b_r)$, so each column of $AB$ is $A$ times a column of $B$.
Cut $A$ into its columns $a_j$ and $B$ into its rows $b_j^{\mathsf{T}}$: then $AB = \sum_j a_j b_j^{\mathsf{T}}$, a sum of matrices of rank at most one.
With zero blocks off the diagonal, $\operatorname{diag}(A_1, A_2) \operatorname{diag}(B_1, B_2) = \operatorname{diag}(A_1 B_1, A_2 B_2)$, so [[block diagonal matrices|001T5FJDC1]] multiply blockwise.
Block upper triangular matrices with one fixed partition are closed under products, because the block below the diagonal of a product is a sum of products that each contain a zero block.

### Generalizations

The rule holds for matrices of maps between direct sums of modules, and in any additive category, where it is the composition of maps between direct sums.
## Explanations

### L1 human

We can multiply block matrices as if the blocks were numbers.
Two things must be watched: the order of the factors in each product stays the same, and the cuts between the columns of the first matrix must match the cuts between the rows of the second.
Then every block product has sizes that fit.

### L2 human

The entry formula $(AB)_{ac} = \sum_l a_{al} b_{lc}$ sums over the inner index $l$.
The block rule sorts the values of $l$ into the column blocks of $A$, and each group of terms is one entry of a block product.
Here is a typical use: square $M = \begin{pmatrix} I & B \\ 0 & I \end{pmatrix}$ with square blocks.
The rule gives
$$M^2 = \begin{pmatrix} I \cdot I + B \cdot 0 & I B + B I \\ 0 \cdot I + I \cdot 0 & 0 \cdot B + I \cdot I \end{pmatrix} = \begin{pmatrix} I & 2B \\ 0 & I \end{pmatrix},$$
and in the same way $M^k$ has $kB$ in the top right block.
Watch out: the top right block is the sum $IB + BI$ of two block products, and dropping one of them gives the wrong answer $B$.

### L3 human

A block matrix is the matrix of a map $\bigoplus_j V_j \to \bigoplus_i W_i$, with $A_{ij}$ the component from $V_j$ to $W_i$.
The rule then says that the components of a composite are $(g \circ f)_{ik} = \sum_j g_{ij} \circ f_{jk}$, which is the definition of composition in the additive category of direct sums.
Fast multiplication algorithms, such as Strassen's, apply a cleverer block rule recursively to $2 \times 2$ block matrices.
