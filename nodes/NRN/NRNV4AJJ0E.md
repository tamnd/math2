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
$$N = \begin{pmatrix} 0 & 1 & 2 \\ 0 & 0 & 3 \\ 0 & 0 & 0 \end{pmatrix},$$
which is strictly [[upper triangular|0MKABWDRNC]].

1. Row 1 of $N^2$ is $0 \cdot (0, 1, 2) + 1 \cdot (0, 0, 3) + 2 \cdot (0, 0, 0) = (0, 0, 3)$.
2. Row 2 of $N^2$ is $3 \cdot (0, 0, 0) = (0, 0, 0)$, and row 3 is $0$.
3. So $N^2 = \begin{pmatrix} 0 & 0 & 3 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = 3E_{13} \neq 0$.
4. Row 1 of $N^3 = N^2 N$ is $3 \cdot (\text{row 3 of } N) = (0, 0, 0)$, and the other rows are $0$. So $N^3 = 0$.
5. Thus $N$ is [[nilpotent|0419GJC84P]] of index exactly $3 = n$, as allowed by the [[nilpotency theorem|AW5RBMW7RK]].

## Remarks

Each power moves the nonzero entries one diagonal up: $N$ lives on diagonals 1 and 2, $N^2$ on diagonal 2, and $N^3$ on none.
By the [[geometric series|N40XPYS89W]], $(I - N)^{-1} = I + N + N^2 = \begin{pmatrix} 1 & 1 & 5 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{pmatrix}$.

## Explanations

### L1 human

This matrix has zeros on and below the diagonal.
Its square has only one nonzero entry, in the top right corner, and its cube is zero.

### L2 human

The entry $3$ of $N^2$ comes from the path $1 \to 2 \to 3$ with weights $n_{12} n_{23} = 1 \cdot 3$.
A path of length 3 in three indices that always goes up does not exist, so $N^3 = 0$.
