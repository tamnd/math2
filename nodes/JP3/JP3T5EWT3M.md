---
tag: JP3T5EWT3M
kind: example
name: The swap matrix is not diagonal although its square is the identity
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
not_instance_of:
  - target: 044JNC7ZAA
    note: the swap matrix (0, 1; 1, 0) has the nonzero entries 1 at the positions (1, 2) and (2, 1), off the main diagonal
uses: [0Q9PGXD9E4, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_matrix
    locator: lead section
---

## Example

Let
$$P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$
over $\mathbb{R}$.
We show that $P$ is not diagonal, and that the rule for powers of diagonal matrices fails for it.

1. The entries $p_{12}$ and $p_{21}$ are off the diagonal, and both equal $1 \ne 0$. So $P$ is not [[diagonal|0Q9PGXD9E4]].
2. The diagonal of $P$ is $(0, 0)$. The only diagonal matrix with this diagonal is the zero matrix, and $P \ne 0$.
3. By the [[product rule|076JGP6R3T]], multiply rows of $P$ by columns of $P$:
$$P^2 = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 1 & 0 \cdot 1 + 1 \cdot 0 \\ 1 \cdot 0 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I.$$
4. The diagonal of $P^2$ is $(1, 1)$, while the squares of the diagonal entries of $P$ are $(0, 0)$. So "square each diagonal entry" gives the wrong answer here.

## Remarks

The example shows that the diagonal of a product depends on the entries off the diagonal too, unless the factors are diagonal.
The entry $(1, 1)$ of $P^2$ is $p_{11}^2 + p_{12} p_{21}$, and the term $p_{12} p_{21} = 1$ comes from outside the diagonal.

The matrix $P$ swaps the two coordinates of a vector, so doing it twice changes nothing, and $P$ is an [[involutory matrix|NH2QE3671N]].
It is [[diagonalizable|07SQCNV233]] all the same.
We have $P(1, 1) = (1, 1)$ and $P(1, -1) = (-1, 1) = -(1, -1)$, so in the basis $(1, 1)$, $(1, -1)$ the map of $P$ has the matrix $\operatorname{diag}(1, -1)$.
So a matrix can fail to be diagonal in one basis and be diagonal in another.

## Explanations

### L1 human

This matrix has its ones off the diagonal, so it is not diagonal.
It exchanges the two coordinates of a vector: $(3, 5)$ becomes $(5, 3)$.
Exchanging twice gives back the start, so its square is the identity.

### L2 human

Being diagonal is a property of the matrix in one basis, and being diagonalizable is a property of the linear map.
The matrix $P$ is diagonalizable but not diagonal, and the basis $(1, 1)$, $(1, -1)$ shows it.
Watch out: a zero diagonal does not make a matrix small or nilpotent; here the square of $P$ is $I$.
