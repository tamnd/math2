---
tag: JW8JBGJKE3
kind: example
name: Matrix multiplication is a binary operation on the square matrices of one size
msc: [08A02]
topics: [BAZT8JJ70S]
audience: school
instance_of: [0M418FE7BB]
uses: [0JXZKX526R, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: Definition
---

## Example

Let $n$ be a positive integer, and let $M_n(\mathbb{R})$ be the set of all $n \times n$ [[square matrices|0JXZKX526R]] with real entries.
For $A, B \in M_n(\mathbb{R})$, the [[matrix product|032Q9FB8MT]] $AB$ is the matrix with the entries
$$(AB)_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}, \qquad 1 \le i, j \le n.$$
We check that matrix multiplication is a [[binary operation|0M418FE7BB]] on $M_n(\mathbb{R})$.

1. The rule gives a value for each pair. The product $AB$ is defined when the number of columns of $A$ equals the number of rows of $B$. Both numbers are $n$.
2. The value is in $M_n(\mathbb{R})$. The product $AB$ has $n$ rows, as $A$ has, and $n$ columns, as $B$ has. Each entry is a sum of products of real numbers, so it is a real number.

Thus matrix multiplication is a binary operation on $M_n(\mathbb{R})$.

For $n = 2$, take
$$A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.$$
Then
$$AB = \begin{pmatrix} 1 \cdot 0 + 2 \cdot 1 & 1 \cdot 1 + 2 \cdot 0 \\ 0 \cdot 0 + 1 \cdot 1 & 0 \cdot 1 + 1 \cdot 0 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 0 \end{pmatrix}, \qquad BA = \begin{pmatrix} 0 & 1 \\ 1 & 2 \end{pmatrix}.$$
Both products are again $2 \times 2$ real matrices.

## Remarks

The example shows a binary operation that is not [[commutative|099E72KTF8]], because $AB \neq BA$ for the matrices above.
Matrix multiplication is [[associative|0K8F7PVDMX]], and the identity matrix $I_n$ is an [[identity element|07WYQPB8E3]].
When we change the set to all real matrices of all sizes, the rule is no longer a binary operation: the product of a $2 \times 3$ matrix and a $2 \times 3$ matrix is not defined.
When we change the set to the [[invertible matrices|0EB9N0S33C]] of size $n$, the rule is still a binary operation, because $AB$ is invertible with inverse $B^{-1}A^{-1}$.
With this change we get the [[general linear group|0FCHE902D7]] $\mathrm{GL}_n(\mathbb{R})$.

## Explanations

### L1 human

A $2 \times 2$ matrix is a square of four numbers.
There is a fixed rule that combines two such squares into a third square of four numbers.
Since the result is again a square of the same size, this rule is a binary operation on these squares.
The order of the two squares can change the result.
For example, the two squares of the example give two different products in the two orders.

### L2 human

We compute one product in full and use it to show that the order matters.
Take $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $C = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ in $M_2(\mathbb{R})$.

1. The entry in row $1$ and column $1$ of $AC$ is $1 \cdot 1 + 1 \cdot 1 = 2$.
2. The entry in row $1$ and column $2$ of $AC$ is $1 \cdot 0 + 1 \cdot 1 = 1$.
3. The entry in row $2$ and column $1$ of $AC$ is $0 \cdot 1 + 1 \cdot 1 = 1$.
4. The entry in row $2$ and column $2$ of $AC$ is $0 \cdot 0 + 1 \cdot 1 = 1$.
5. The same rule gives $CA = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.

So $AC = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \neq CA$.
The typical use of this binary operation is in linear algebra: the product $AB$ is the matrix of the composition of the linear maps of $A$ and $B$.
A trap is to multiply the matrices entry by entry; that rule is a different binary operation, the [[Hadamard product|SQT6QCEXZ8]].
