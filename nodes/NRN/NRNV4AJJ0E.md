---
tag: NRNV4AJJ0E
kind: example
name: A strictly upper triangular 3 × 3 matrix whose cube is zero
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [0N4XY7Z3NN, 07BSPZPSMF]
illustrates: [AW5RBMW7RK]
uses: [0MKABWDRNC, 076JGP6R3T, 0419GJC84P]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Examples
---

## Example

Let
$$N = \begin{pmatrix} 0 & 1 & 2 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{pmatrix}$$
over $\mathbb{R}$.
Its entries on and below the main diagonal are $0$, so $N$ is strictly [[upper triangular|0MKABWDRNC]].
We compute its powers by the [[product rule|076JGP6R3T]], one row at a time.

1. Row $i$ of $N^2 = N \cdot N$ is the combination of the rows of $N$ with the entries of row $i$ of $N$ as weights, and for row 1 the weights are $0, 1, 2$:
$$0 \cdot (0, 1, 2) + 1 \cdot (0, 0, 3) + 2 \cdot (0, 0, 0) = (0, 0, 3).$$
2. Row 2 of $N$ has weights $0, 0, 3$, so row 2 of $N^2$ is $3 \cdot (0, 0, 0) = (0, 0, 0)$, and row 3 of $N$ is zero, so row 3 of $N^2$ is zero.
3. So
$$N^2 = \begin{pmatrix} 0 & 0 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \neq 0.$$
4. For $N^3 = N^2 N$, the only nonzero weight is the $3$ in row 1, position 3, and it multiplies row 3 of $N$, which is zero, so $N^3 = 0$.
5. Since $N^3 = 0$ and $N^2 \neq 0$, the matrix $N$ is [[nilpotent|0419GJC84P]] of index exactly $3$, the largest index that the [[nilpotency theorem|AW5RBMW7RK]] allows for order $3$.

## Remarks

Each power moves the nonzero entries one diagonal further up.
The entries of $N$ lie on the first and second diagonals above the main one, the entries of $N^2$ only on the second, and $N^3$ has none left.

The entry $3$ of $N^2$ comes from the single chain of indices $1 \to 2 \to 3$, with weight $n_{12} n_{23} = 1 \cdot 3$.
If we change $n_{23}$ from $3$ to $0$, then $N^2 = 0$ and the index drops to $2$, so the index depends on more than the shape.

The nilpotency gives an inverse for free.
By the [[geometric series for a nilpotent matrix|N40XPYS89W]], $(I - N)^{-1} = I + N + N^2$:
$$I + N + N^2 = \begin{pmatrix} 1 & 1 & 5 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{pmatrix}.$$
Check: the entry $(1, 3)$ of $(I - N)(I + N + N^2)$ is $1 \cdot 5 + (-1) \cdot 3 + (-2) \cdot 1 = 0$.

## Explanations

### L1 human

This matrix has zeros on the diagonal and below it.
Its square has only one nonzero entry, the $3$ in the top right corner.
Its cube is all zeros, so multiplying it by itself three times wipes it out.

### L2 human

The typical use is to see the nilpotency theorem at work with real numbers.
Write $(N^2)_{13} = \sum_k n_{1k} n_{k3}$, and note that a nonzero term needs $1 < k < 3$, so $k = 2$ and the sum is $n_{12} n_{23} = 3$.
For $N^3$ a nonzero term would need indices $1 < k < l < 3$, and no two integers fit between $1$ and $3$.
Watch out: a strictly upper triangular matrix of order $3$ can have index $1$, $2$ or $3$; the theorem only gives the upper bound.
