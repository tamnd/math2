---
tag: D2XKRGZDBK
kind: example
name: Four views of the product of two 2 × 2 matrices
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [032Q9FB8MT]
uses: [076JGP6R3T, 0CCQV3884B]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: Definitions
  - book: isbn:9780321982384
    locator: Section 2.1
---

## Example

Let
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \qquad B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}.$$
We compute the [[product|032Q9FB8MT]] $AB$ in four ways from the [[definition|076JGP6R3T]], and then in the other order.

1. By entries, each entry is a row of $A$ times a column of $B$:
$$AB = \begin{pmatrix} 1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8 \\ 3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8 \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}.$$
2. By columns, column $j$ of $AB$ is the [[matrix-vector product|0CCQV3884B]] of $A$ with column $j$ of $B$, a combination of the columns of $A$:
$$A \begin{pmatrix} 5 \\ 7 \end{pmatrix} = 5 \begin{pmatrix} 1 \\ 3 \end{pmatrix} + 7 \begin{pmatrix} 2 \\ 4 \end{pmatrix} = \begin{pmatrix} 19 \\ 43 \end{pmatrix}, \qquad A \begin{pmatrix} 6 \\ 8 \end{pmatrix} = 6 \begin{pmatrix} 1 \\ 3 \end{pmatrix} + 8 \begin{pmatrix} 2 \\ 4 \end{pmatrix} = \begin{pmatrix} 22 \\ 50 \end{pmatrix}.$$
3. By rows, row $i$ of $AB$ is a combination of the rows of $B$ with the entries of row $i$ of $A$ as weights:
$$1 \cdot (5, 6) + 2 \cdot (7, 8) = (19, 22), \qquad 3 \cdot (5, 6) + 4 \cdot (7, 8) = (43, 50).$$
4. By outer products, $AB$ is column 1 of $A$ times row 1 of $B$, plus column 2 of $A$ times row 2 of $B$:
$$\begin{pmatrix} 1 \\ 3 \end{pmatrix} \begin{pmatrix} 5 & 6 \end{pmatrix} + \begin{pmatrix} 2 \\ 4 \end{pmatrix} \begin{pmatrix} 7 & 8 \end{pmatrix} = \begin{pmatrix} 5 & 6 \\ 15 & 18 \end{pmatrix} + \begin{pmatrix} 14 & 16 \\ 28 & 32 \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}.$$
5. In the other order, the entries of $BA$ are
$$BA = \begin{pmatrix} 5 \cdot 1 + 6 \cdot 3 & 5 \cdot 2 + 6 \cdot 4 \\ 7 \cdot 1 + 8 \cdot 3 & 7 \cdot 2 + 8 \cdot 4 \end{pmatrix} = \begin{pmatrix} 23 & 34 \\ 31 & 46 \end{pmatrix},$$
which is not $AB$.

## Remarks

All four views add the same eight products $a_{ik} b_{kj}$, and they only group them in different ways.
The column view shows that every column of $AB$ lies in the span of the columns of $A$.
The row view shows that every row of $AB$ lies in the span of the rows of $B$.
The outer product view writes $AB$ as a sum of matrices of rank at most one, which is the basis of the [[block multiplication rule|WR3RCF5PSQ]].

Step 5 shows that the order matters even for these small matrices.
Check: both products have the same trace, $19 + 50 = 69 = 23 + 46$, as the [[cyclic property of the trace|0Y4NF1DRKD]] predicts.
If you change $B$ to the identity matrix, all four views return $A$ itself, and then $AB = BA$.

## Explanations

### L1 human

The usual rule is "row times column" for each entry.
You can also build the product one column at a time or one row at a time, or add up simple pieces.
For example, the first column of the product is $5$ times the first column of $A$ plus $7$ times the second, which is $(19, 43)$.
All the ways give the same table of numbers.

### L2 human

Which view should you use?
To find one entry, use row times column.
To see which vectors $AB$ can produce, use the column view, since each column of $AB$ is a combination of the columns of $A$.
To see the rank or to split a large product into pieces, use the outer products.
Watch out: the row view uses the rows of $B$, not the rows of $A$, and mixing them up gives a wrong product.
