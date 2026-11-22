---
tag: TVNYJ89WDJ
kind: example
name: A 2 × 3 matrix is not square and has no square
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
not_instance_of:
  - target: 0JXZKX526R
    note: the matrix has 2 rows and 3 columns, so the product AA is not defined, although AA^T and A^TA are defined
uses: [0CP7YY6NAG, 076JGP6R3T, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: Definition
---

## Example

A rectangular matrix that is not square cannot be multiplied by itself, but it has two square relatives.
Let
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}.$$

1. The matrix $A$ has 2 rows and 3 columns, and $2 \neq 3$, so $A$ is not a [[square matrix|0CP7YY6NAG]].
2. The [[product|076JGP6R3T]] $AB$ is defined only when $B$ has as many rows as $A$ has columns. For $B = A$ this asks for $2$ rows to equal $3$ columns, so $A^2$ is not defined.
3. The [[transpose|0W809K6AW0]] $A^{\mathsf{T}}$ is $3 \times 2$, so $AA^{\mathsf{T}}$ is defined and is $2 \times 2$. Its entries are the dot products of the rows $(1, 2, 3)$ and $(4, 5, 6)$ of $A$:
$$AA^{\mathsf{T}} = \begin{pmatrix} 1 + 4 + 9 & 4 + 10 + 18 \\ 4 + 10 + 18 & 16 + 25 + 36 \end{pmatrix} = \begin{pmatrix} 14 & 32 \\ 32 & 77 \end{pmatrix}.$$
4. The product $A^{\mathsf{T}}A$ is also defined, and it is $3 \times 3$. Its entries are the dot products of the columns $(1, 4)$, $(2, 5)$ and $(3, 6)$ of $A$:
$$A^{\mathsf{T}}A = \begin{pmatrix} 1 + 16 & 2 + 20 & 3 + 24 \\ 2 + 20 & 4 + 25 & 6 + 30 \\ 3 + 24 & 6 + 30 & 9 + 36 \end{pmatrix} = \begin{pmatrix} 17 & 22 & 27 \\ 22 & 29 & 36 \\ 27 & 36 & 45 \end{pmatrix}.$$
5. The products in steps 3 and 4 are square, but one has order 2 and the other has order 3. So neither of them can be called the square of $A$.

## Remarks

The example shows that the size rule of matrix multiplication, and not the entries, decides whether a power exists.
Any $m \times n$ matrix with $m \neq n$ fails in the same way, while any $n \times n$ matrix has all its powers.

The two products $AA^{\mathsf{T}}$ and $A^{\mathsf{T}}A$ are the nearest replacements for a square.
Their diagonal entries are squared lengths: $14 = 1^2 + 2^2 + 3^2$ for the first row of $A$, and $17 = 1^2 + 4^2$ for the first column.
Both are [[symmetric|0VR671PHE5]], since the entry $(i, j)$ and the entry $(j, i)$ are the same dot product.

Watch out for software that squares entry by entry.
It returns $\begin{pmatrix} 1 & 4 & 9 \\ 16 & 25 & 36 \end{pmatrix}$ without complaint, but this array is not a matrix product, and it hides the fact that $A^2$ does not exist.

## Explanations

### L1 human

To multiply a matrix by itself, each row must be as long as each column.
Here every row has 3 numbers and every column has 2 numbers.
Row times column then has nothing to pair the third number of the row with, so the product does not exist.

### L2 human

The test for a product $AB$ is to write the sizes side by side, $(2 \times 3)(2 \times 3)$, and compare the two inner numbers.
They are $3$ and $2$, which differ, so $AA$ is not defined.
For $AA^{\mathsf{T}}$ the sizes are $(2 \times 3)(3 \times 2)$, the inner numbers agree, and the outer numbers give the size $2 \times 2$ of the result.
The typical use of $A^{\mathsf{T}}A$ is in least squares, where the normal equations $A^{\mathsf{T}}A x = A^{\mathsf{T}} b$ replace a system $Ax = b$ that has no exact solution.
The trap is to assume that $AA^{\mathsf{T}}$ and $A^{\mathsf{T}}A$ are equal, when here they do not even have the same size.
