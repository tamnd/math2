---
tag: 306FBDECMB
kind: example
name: Diagonalizing a 2 × 2 matrix
msc: ["15A20", "15A18"]
topics: [Z6S6PWMJPH]
audience: ug1
instance_of: [07SQCNV233, D0AP2R7272, 08VRX3Q4PB, 0TNR9BQ871]
illustrates: [056SW1E0AC, 0Y95Z7MT02]
uses: [0Y17PEKF24, 039HF58KQ5, 0B5H4208Z9, 0TWTS88TWN]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Examples
  - book: isbn:9780321982384
    locator: Section 5.3
---

## Example

Let $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$ over $\R$.

1. The [[characteristic polynomial|0VSSPAFM2C]] is $(t - 4)(t - 3) - 2 = t^2 - 7t + 10 = (t - 5)(t - 2)$. So the [[eigenvalues|0BQAA2BK3Q]] are $5$ and $2$.
2. For $\lambda = 5$: $A - 5I = \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix}$, so $-x + y = 0$, and $v_1 = (1, 1)$. Check: $A v_1 = (5, 5) = 5 v_1$.
3. For $\lambda = 2$: $A - 2I = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}$, so $2x + y = 0$, and $v_2 = (1, -2)$. Check: $A v_2 = (2, -4) = 2 v_2$.
4. Let $P = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}$ and $D = \operatorname{diag}(5, 2)$. Then $\det P = -3 \ne 0$, so $P$ is invertible, and $P^{-1} = \frac{1}{3} \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}$.
5. Multiply back: $P D = \begin{pmatrix} 5 & 2 \\ 5 & -4 \end{pmatrix}$, and $P D P^{-1} = \frac{1}{3} \begin{pmatrix} 10 + 2 & 5 - 2 \\ 10 - 4 & 5 + 4 \end{pmatrix} = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix} = A$.
6. So $A$ is [[diagonalizable|07SQCNV233]] over $\R$, with $A = P D P^{-1}$.
7. The rank-one form: let $w_1 = (\tfrac{2}{3}, \tfrac{1}{3})$ and $w_2 = (\tfrac{1}{3}, -\tfrac{1}{3})$ be the rows of $P^{-1}$, and $E_i = v_i w_i$. Then $E_1 = \frac{1}{3} \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}$ and $E_2 = \frac{1}{3} \begin{pmatrix} 1 & -1 \\ -2 & 2 \end{pmatrix}$.
8. We have $E_1 + E_2 = I$ and $5 E_1 + 2 E_2 = \frac{1}{3} \begin{pmatrix} 12 & 3 \\ 6 & 9 \end{pmatrix} = A$. This is the spectral sum of the [[eigendecomposition|D0AP2R7272]].

## Remarks

The example shows the algorithm for a matrix with distinct eigenvalues, where [[distinct eigenvalues imply diagonalizable|0Y95Z7MT02]].
The matrices $E_1$ and $E_2$ are the projections onto the eigenlines along each other, since $w_i v_j$ is $1$ for $i = j$ and $0$ otherwise.
With the order of the eigenvalues reversed, $P$ has the columns $(1, -2)$ and $(1, 1)$, and $D = \operatorname{diag}(2, 5)$.
If the entry $2$ of $A$ is replaced by $-\tfrac{1}{4}$, the characteristic polynomial becomes $(t - \tfrac{7}{2})^2$, with the eigenspace spanned by $(2, -1)$ alone, and the matrix is no longer diagonalizable.
A diagonalizable map is also [[semisimple|08VRX3Q4PB]].

## Explanations

### L1 human

The matrix stretches the direction of the arrow $(1, 1)$ by $5$.
It stretches the direction of the arrow $(1, -2)$ by $2$.
If we use these two arrows as axes, the matrix is just "multiply the first coordinate by $5$ and the second by $2$".
We can check the claim by multiplying three matrices back together.

### L2 human

We use the result to compute $A^3$.

1. $D^3 = \operatorname{diag}(125, 8)$.
2. $A^3 = P D^3 P^{-1} = 125 E_1 + 8 E_2$.
3. $125 E_1 + 8 E_2 = \frac{1}{3} \begin{pmatrix} 250 + 8 & 125 - 8 \\ 250 - 16 & 125 + 16 \end{pmatrix} = \begin{pmatrix} 86 & 39 \\ 78 & 47 \end{pmatrix}$.
4. Check with the first row: $A^2 = \begin{pmatrix} 18 & 7 \\ 14 & 11 \end{pmatrix}$, and the first row of $A^2 A$ is $(72 + 14, 18 + 21) = (86, 39)$.

The trap is to write $P^{-1} D P$ instead of $P D P^{-1}$: the eigenvectors are the columns of the matrix on the left.
