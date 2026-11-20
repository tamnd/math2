---
tag: 0S4WTRE9GG
kind: statement
role: proposition
name: Inverse of a product
msc: [15A09]
topics: [P8J6QR66TJ]
audience: ug1
about: [0EB9N0S33C]
uses: [0TWTS88TWN, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Properties
  - book: isbn:9780321982384
    locator: Section 2.2
  - book: isbn:9780135367971
    locator: Section 1.6
---

## Statement

1. Let $R$ be a commutative ring and let $A$ and $B$ be [[invertible|0TWTS88TWN]] $n \times n$ matrices over $R$. Then the [[product|076JGP6R3T]] $AB$ is invertible, and $$(AB)^{-1} = B^{-1} A^{-1}.$$
2. More generally, if $A_1, \dots, A_k$ are invertible $n \times n$ matrices over $R$, then $A_1 A_2 \cdots A_k$ is invertible, and $(A_1 A_2 \cdots A_k)^{-1} = A_k^{-1} \cdots A_2^{-1} A_1^{-1}$.
3. Let $F$ be a field and let $A_1, \dots, A_k$ be $n \times n$ matrices over $F$. Then the product $A_1 A_2 \cdots A_k$ is invertible if and only if each factor $A_i$ is invertible.

## Remarks

### Why each hypothesis is needed

In part 3 the factors must be square.
For the $2 \times 3$ matrix $A$ and the $3 \times 2$ matrix $B$ of the [[right inverse example|~710ae60f]], the product $AB = I_2$ is invertible, but neither factor is invertible.
The order of the factors in part 1 matters: $(AB)^{-1} = A^{-1} B^{-1}$ is false in general.
For $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, the matrix $A^{-1} B^{-1}$ is not the inverse of $AB$, as the L2 explanation shows.

### Consequences

- The invertible $n \times n$ matrices over $R$ form a group under multiplication, the [[general linear group|0FCHE902D7]].
- A product of [[elementary matrices|01REXW3WWE]] is invertible, and its inverse is the product of the inverse elementary matrices in the reverse order.
- By part 3, if $AB$ is singular, then $A$ or $B$ is singular.

### Converse

Part 3 is the converse of part 2 over a field.
Its proof uses the theorem that a [[one-sided inverse of a square matrix is two-sided|0753Y2X5K6]].
Part 3 also holds over each commutative ring, by the [[determinant criterion|03Q7RE2HXR]]: $\det(A_1 \cdots A_k)$ is a unit if and only if each $\det A_i$ is a unit.

### Generalizations

Parts 1 and 2 hold in each monoid.
The units of a monoid form a group, and the inverse of a product is the product of the inverses in the reverse order.

## Explanations

### L1 human

To undo two steps, we undo the last step first.
If we first apply $B$ and then $A$, then we must first undo $A$ and then undo $B$.
So the inverse of $AB$ is $B^{-1} A^{-1}$, with the order reversed.
Think of socks and shoes: we put on socks first, but we take off shoes first.

### L2 human

Worked example: let $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.

1. $AB = \begin{pmatrix} 1 + 1 & 0 + 1 \\ 0 + 1 & 0 + 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$.
2. $A^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$ and $B^{-1} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}$; each product with the original matrix is $I_2$.
3. $B^{-1} A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 1 + 1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.
4. Check: $(AB)(B^{-1}A^{-1}) = \begin{pmatrix} 2 - 1 & -2 + 2 \\ 1 - 1 & -1 + 2 \end{pmatrix} = I_2$.
5. The wrong order gives $A^{-1} B^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$, and $(AB)(A^{-1}B^{-1}) = \begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix} \ne I_2$.

The typical use of part 3 is to show that a matrix is singular, or to split an invertible matrix into simpler invertible factors.

### L3 human

Parts 1 and 2 hold in every monoid, so the invertible $n \times n$ matrices form the group of units $\mathrm{GL}_n(R)$ of the matrix ring.
Part 3 uses that the factors are square matrices: it rests on the fact that a one-sided inverse of a square matrix is two-sided.
In an arbitrary monoid part 3 fails, as the shift operators on sequences show: $ST = 1$ while neither $S$ nor $T$ is invertible.
