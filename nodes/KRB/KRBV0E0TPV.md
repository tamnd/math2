---
tag: KRBV0E0TPV
kind: example
name: The cube of the Jordan block J₃(2)
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
instance_of: [07PH4RX0X5]
illustrates: [B9CHNGJV5K]
uses: [0PBFS92AJP, DS9TS6AFMW]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_matrix
    locator: Functions of matrices
---

## Example

Let $J = J_3(2)$ be the [[Jordan block|0PBFS92AJP]] of size $3$ with eigenvalue $2$ over $\mathbb{Q}$.
We compute $J^3$ by splitting $J$ into a scalar part and a shift:
$$J = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix} = 2I + N, \qquad N = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}.$$

1. The powers of $N$ move the ones up one diagonal at a time, and the third power is zero:
$$N^2 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \qquad N^3 = 0.$$
2. The scalar matrix $2I$ commutes with $N$, so the [[binomial theorem for commuting matrices|DS9TS6AFMW]] applies:
$$J^3 = (2I)^3 + 3 (2I)^2 N + 3 (2I) N^2 + N^3 = 8I + 12 N + 6 N^2.$$
3. Reading off the three diagonals gives
$$J^3 = \begin{pmatrix} 8 & 12 & 6 \\ 0 & 8 & 12 \\ 0 & 0 & 8 \end{pmatrix}.$$
4. Check with direct products. The square is
$$J^2 = \begin{pmatrix} 4 & 4 & 1 \\ 0 & 4 & 4 \\ 0 & 0 & 4 \end{pmatrix},$$
and the first row of $J^2 J$ is $(4 \cdot 2,\ 4 \cdot 1 + 4 \cdot 2,\ 4 \cdot 1 + 1 \cdot 2) = (8, 12, 6)$, while the second row is $(0, 8, 4 + 8) = (0, 8, 12)$.
5. The minimal polynomial of $J$ is $(x - 2)^3$: the matrix $(J - 2I)^3 = N^3$ is zero, while $(J - 2I)^2 = N^2$ is not.

## Remarks

The entry on the $j$-th diagonal above the main one is $\binom{3}{j} 2^{3-j}$, which gives $8$, $12$ and $6$ for $j = 0, 1, 2$.
The coefficients $1, 3, 3, 1$ of $(a + b)^3$ are all there, but the last one meets $N^3 = 0$ and drops out.
If the block had size $4$, the term $N^3$ would survive and put a $1$ in the top right corner of $J_4(2)^3$.

Watch out for the guess "cube the diagonal and keep the ones": the matrix $8I + N$ is not $J^3$.
The cube of the scalar matrix $2I$ is $8I$, but $J$ also carries the shift, and the cross terms $12N$ and $6N^2$ come from it.
The general rule is the [[lemma on powers of a Jordan block|B9CHNGJV5K]].

## Explanations

### L1 human

To cube this matrix, write it as "two times the identity" plus a shift that moves each basis vector one step.
The shift applied three times gives zero, so the usual pattern $1, 3, 3, 1$ for cubing a sum stops early.
The answer has $8$ on the diagonal, $12$ just above it, and $6$ in the corner.

### L2 human

Here is the same idea used to predict a power without multiplying.
For $J_3(2)^m$ the binomial formula gives $2^m$ on the diagonal, $m\, 2^{m-1}$ on the next diagonal and $\binom{m}{2} 2^{m-2}$ in the corner.
For $m = 3$ these are $8$, $3 \cdot 4 = 12$ and $3 \cdot 2 = 6$, as above.
For $m = 10$ they are $1024$, $10 \cdot 512 = 5120$ and $45 \cdot 256 = 11520$.
This is the typical use: a power of a Jordan block costs a few binomial coefficients, not $m - 1$ matrix products.
