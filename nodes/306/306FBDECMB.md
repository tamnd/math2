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
We find $P$ and $D$ with $A = P D P^{-1}$, and then write $A$ as a sum of two projections.

1. The [[characteristic polynomial|0VSSPAFM2C]] is
$$\det(t I - A) = (t - 4)(t - 3) - 2 = t^2 - 7t + 10 = (t - 5)(t - 2),$$
so the [[eigenvalues|0BQAA2BK3Q]] are $5$ and $2$.
2. For $\lambda = 5$, the matrix $A - 5I = \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix}$ gives the equation $-x + y = 0$, so $v_1 = (1, 1)$.
   Check: $A v_1 = (5, 5) = 5 v_1$.
3. For $\lambda = 2$, the matrix $A - 2I = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}$ gives the equation $2x + y = 0$, so $v_2 = (1, -2)$.
   Check: $A v_2 = (2, -4) = 2 v_2$.
4. Put $v_1$ and $v_2$ as the columns of $P$, and the eigenvalues in the same order in $D$:
$$P = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}, \qquad D = \begin{pmatrix} 5 & 0 \\ 0 & 2 \end{pmatrix}.$$
   Since $\det P = -2 - 1 = -3 \ne 0$, the matrix $P$ is invertible, and the formula for a $2 \times 2$ inverse gives
$$P^{-1} = \frac{1}{-3} \begin{pmatrix} -2 & -1 \\ -1 & 1 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix}.$$
5. Multiply back:
$$P D P^{-1} = \begin{pmatrix} 5 & 2 \\ 5 & -4 \end{pmatrix} \cdot \frac{1}{3} \begin{pmatrix} 2 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 10 + 2 & 5 - 2 \\ 10 - 4 & 5 + 4 \end{pmatrix} = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}.$$
   So $A$ is [[diagonalizable|07SQCNV233]] over $\R$.
6. For the rank-one form, let $w_1 = (\tfrac{2}{3}, \tfrac{1}{3})$ and $w_2 = (\tfrac{1}{3}, -\tfrac{1}{3})$ be the rows of $P^{-1}$, and let $E_i = v_i w_i$, a column times a row:
$$E_1 = \frac{1}{3} \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}, \qquad E_2 = \frac{1}{3} \begin{pmatrix} 1 & -1 \\ -2 & 2 \end{pmatrix}.$$
7. Add them with and without the eigenvalues as weights:
$$E_1 + E_2 = \frac{1}{3} \begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix} = I, \qquad 5 E_1 + 2 E_2 = \frac{1}{3} \begin{pmatrix} 12 & 3 \\ 6 & 9 \end{pmatrix} = A.$$
   This is the spectral sum of the [[eigendecomposition|D0AP2R7272]].

## Remarks

The matrix has two distinct eigenvalues, so the result was known in advance from the rule that [[n distinct eigenvalues imply diagonalizable|0Y95Z7MT02]].
The computation still matters, because it finds the matrices $P$ and $D$, and the check in step 5 confirms them.
The matrices $E_1$ and $E_2$ are the projections onto each eigenline along the other one, because $w_i v_j$ is $1$ for $i = j$ and $0$ for $i \ne j$.
Every diagonalizable map is also [[semisimple|08VRX3Q4PB]], so the example is one of those as well.

The answer depends on choices.
If we list the eigenvalues in the other order, then $P$ has the columns $(1, -2)$ and $(1, 1)$, and $D = \operatorname{diag}(2, 5)$.
Each column of $P$ can also be scaled by a nonzero number without changing $D$.

A small change of one entry can destroy the result.
If the entry $2$ of $A$ becomes $-\tfrac{1}{4}$, then the trace is still $7$ and the determinant is $12 + \tfrac{1}{4} = \tfrac{49}{4}$, so the characteristic polynomial is $t^2 - 7t + \tfrac{49}{4} = (t - \tfrac{7}{2})^2$.
The new matrix minus $\tfrac{7}{2} I$ is $\begin{pmatrix} 1/2 & 1 \\ -1/4 & -1/2 \end{pmatrix}$, whose kernel is the line spanned by $(2, -1)$, so the new matrix is not diagonalizable.

## Explanations

### L1 human

The matrix stretches the direction of the arrow $(1, 1)$ by $5$.
It stretches the direction of the arrow $(1, -2)$ by $2$.
If we use these two arrows as axes, the matrix is just the rule "multiply the first coordinate by $5$ and the second by $2$".
Multiplying the three matrices $P$, $D$ and $P^{-1}$ back together confirms that this rule describes $A$.

### L2 human

The typical use of a diagonalization is a power of the matrix, so let us compute $A^3$.
The power of $D$ is $D^3 = \operatorname{diag}(125, 8)$, and the spectral sum gives
$$A^3 = P D^3 P^{-1} = 125 E_1 + 8 E_2 = \frac{1}{3} \begin{pmatrix} 250 + 8 & 125 - 8 \\ 250 - 16 & 125 + 16 \end{pmatrix} = \begin{pmatrix} 86 & 39 \\ 78 & 47 \end{pmatrix}.$$
Check it by direct multiplication.
First $A^2 = \begin{pmatrix} 18 & 7 \\ 14 & 11 \end{pmatrix}$, and then
$$A^2 A = \begin{pmatrix} 72 + 14 & 18 + 21 \\ 56 + 22 & 14 + 33 \end{pmatrix} = \begin{pmatrix} 86 & 39 \\ 78 & 47 \end{pmatrix}.$$
Watch out: the formula is $P D^3 P^{-1}$, with the eigenvectors in the matrix on the left, and $P^{-1} D^3 P$ gives a different and wrong matrix.
