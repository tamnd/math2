---
tag: DXX58EAKG3
kind: example
name: A nonzero matrix with square zero
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [07BSPZPSMF]
not_instance_of:
  - target: 0ZTKJJDGR7
    note: the entry in row 1 and column 2 is 1, so the matrix is not the zero matrix, although its square is the zero matrix
uses: [4KY5AWGMW5, 076JGP6R3T, 0419GJC84P]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Examples
---

## Example

Let
$$N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$$
over the real numbers.
We show that $N$ is not the zero matrix but $N^2$ is.

1. The entry $n_{12}$ is $1$, so $N$ is not the [[zero matrix|4KY5AWGMW5]].
2. The entry $(i, j)$ of $N^2$ is $n_{i1} n_{1j} + n_{i2} n_{2j}$, by the row-times-column rule of [[matrix multiplication|076JGP6R3T]].
3. The first column of $N$ is zero, so $n_{i1} = 0$, and the second row of $N$ is zero, so $n_{2j} = 0$. Both terms vanish for every $i$ and $j$.
4. So
$$N^2 = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 0 \\ 0 \cdot 0 + 0 \cdot 0 & 0 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}.$$
5. Since $N \ne 0$ and $N^2 = 0$, the matrix $N$ is [[nilpotent|0419GJC84P]] of index $2$.

## Remarks

For real numbers, $x^2 = 0$ forces $x = 0$.
The example shows that the matrix equation $X^2 = 0$ has nonzero solutions, so we cannot take square roots of zero the way we do with numbers.

As a map of the plane, $N$ sends $e_2 = (0, 1)$ to $e_1 = (1, 0)$ and sends $e_1$ to $0$.
Applying it twice sends both basis vectors to $0$, which is the same computation in geometric form.

The example is one of a whole family.
A direct computation gives
$$\begin{pmatrix} a & b \\ c & -a \end{pmatrix}^2 = \begin{pmatrix} a^2 + bc & 0 \\ 0 & a^2 + bc \end{pmatrix},$$
so every such matrix with $a^2 + bc = 0$ has square zero; our $N$ is the case $a = 0$, $b = 1$, $c = 0$.
If we change the corner entry of $N$ to any nonzero number $t$, the square is still zero, but if we put a nonzero entry on the diagonal, the square is no longer zero.

## Explanations

### L1 human

This matrix is not the zero matrix, because it has a $1$ in the top right corner.
When we multiply it by itself, that $1$ is only ever multiplied by zeros.
So every entry of the product is $0$, and the square is the zero matrix.

### L2 human

The fast way to see $N^2 = 0$ is to follow the basis vectors: $N$ moves $e_2$ to $e_1$ and $e_1$ to $0$, so two steps of $N$ send every vector to $0$.
Check with a vector: $N(3, 5) = (5, 0)$ and $N(5, 0) = (0, 0)$.
Watch out: the same picture shows why $N$ is not invertible, since it sends $e_1 \ne 0$ to $0$.
