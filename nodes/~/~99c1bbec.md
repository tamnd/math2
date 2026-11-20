---
tag: ~99c1bbec
kind: example
name: The cube of the Jordan block J₃(2)
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
instance_of: [07PH4RX0X5]
illustrates: [~d1324a3e]
uses: [0PBFS92AJP, DS9TS6AFMW]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_matrix
    locator: Functions of matrices
---

## Example

Let $J = J_3(2) = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix} = 2I + N$, with $N = J_3(0)$.

1. $N^2 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ and $N^3 = 0$.
2. $2I$ and $N$ commute, so the [[binomial theorem for commuting matrices|DS9TS6AFMW]] gives $J^3 = 8I + 3 \cdot 4 N + 3 \cdot 2 N^2 + N^3 = 8I + 12N + 6N^2$.
3. So $J^3 = \begin{pmatrix} 8 & 12 & 6 \\ 0 & 8 & 12 \\ 0 & 0 & 8 \end{pmatrix}$.
4. Check by direct products: $J^2 = \begin{pmatrix} 4 & 4 & 1 \\ 0 & 4 & 4 \\ 0 & 0 & 4 \end{pmatrix}$, and $J^2 J$ has first row $(8, 4 + 8, 4 + 2) = (8, 12, 6)$ and second row $(0, 8, 8 + 4) = (0, 8, 12)$.
5. The minimal polynomial of $J$ is $(x - 2)^3$, and indeed $(J - 2I)^3 = N^3 = 0$ while $(J - 2I)^2 = N^2 \ne 0$.

## Remarks

The entries on the $j$-th diagonal above the main diagonal are $\binom{3}{j} 2^{3-j}$, that is $8$, $12$, $6$.
The diagonal entry $8 = 2^3$ alone is not enough: the matrix $8I$ is the cube of $2I$, not of $J$.

## Explanations

### L1 human

To cube this matrix, split it into twice the identity plus a shift.
The binomial formula then gives the answer in one line, because the shift cubed is zero.

### L2 human

The coefficients $1, 3, 3, 1$ of $(a + b)^3$ appear as $8 = 1 \cdot 2^3$, $12 = 3 \cdot 2^2$ and $6 = 3 \cdot 2$.
The last term $1 \cdot N^3$ is zero, so the corner entry is $6$ and nothing more.
