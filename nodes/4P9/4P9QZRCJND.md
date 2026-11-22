---
tag: 4P9QZRCJND
kind: example
name: Jordan-Chevalley decomposition of a 3 × 3 matrix
msc: ["15A21"]
topics: [Z6S6PWMJPH]
audience: grad
not_instance_of:
  - target: 07SQCNV233
    note: the nilpotent part N of A is not 0, so A itself is not diagonalizable
illustrates: [011K11VPJN, ACBNK1VFVG]
uses: [0QS8P74F2Z, 0M8MHYERTY, 0Y17PEKF24, 0VY3WPP9Y3]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan%E2%80%93Chevalley_decomposition
    locator: Decomposition of a linear operator
---

## Example

Let
$$A = \begin{pmatrix} 1 & 1 & 1 \\ -1 & 3 & 1 \\ 0 & 0 & 1 \end{pmatrix}$$
over $\R$.
We compute its [[Jordan-Chevalley decomposition|011K11VPJN]] $A = S + N$, with $S$ diagonalizable, $N$ nilpotent and $S N = N S$, as in the [[generalized eigenspace example|18WSA33PKA]].

1. The matrix is block upper triangular, with the block $\begin{pmatrix} 1 & 1 \\ -1 & 3 \end{pmatrix}$ of trace $4$ and determinant $4$, and the block $(1)$.
   So $p_A = (t^2 - 4t + 4)(t - 1) = (t - 1)(t - 2)^2$.
2. The factors $t - 1$ and $(t - 2)^2$ are coprime, and [[Bézout's identity|0VY3WPP9Y3]] for them is
$$(t - 2)^2 - (t - 1)(t - 3) = (t^2 - 4t + 4) - (t^2 - 4t + 3) = 1.$$
3. By the [[kernels lemma|ACBNK1VFVG]], the projection onto $V_1 = \ker (A - I)$ along $V_2 = \ker (A - 2I)^2$ is $\pi_1 = (A - 2I)^2$, and the other projection is $\pi_2 = I - \pi_1$.
4. With $M = A - 2I = \begin{pmatrix} -1 & 1 & 1 \\ -1 & 1 & 1 \\ 0 & 0 & -1 \end{pmatrix}$ we get
$$\pi_1 = M^2 = \begin{pmatrix} 0 & 0 & -1 \\ 0 & 0 & -1 \\ 0 & 0 & 1 \end{pmatrix}, \qquad \pi_2 = I - M^2 = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}.$$
5. The semisimple part is $1$ on $V_1$ and $2$ on $V_2$:
$$S = 1 \cdot \pi_1 + 2 \pi_2 = 2I - M^2 = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 2 & 1 \\ 0 & 0 & 1 \end{pmatrix}.$$
   Since $M^2 = A^2 - 4A + 4I$, this is the polynomial $S = -A^2 + 4A - 2I$ in $A$.
6. The nilpotent part is
$$N = A - S = A^2 - 3A + 2I = (A - I)(A - 2I) = \begin{pmatrix} -1 & 1 & 0 \\ -1 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$
7. Square it: the first two rows of $N$ are $(-1, 1, 0)$, and the first two columns are $(-1, -1, 0)$ and $(1, 1, 0)$, so every entry of $N^2$ is $1 - 1 = 0$ or $-1 + 1 = 0$ or $0$.
   So $N^2 = 0$, and $N$ is [[nilpotent|063D5Z2C70]].
8. Let $Q = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & -1 \end{pmatrix}$, whose columns are $e_1$, $e_2$ and $(1, 1, -1)$.
   A direct product shows $Q^2 = I$, so $Q^{-1} = Q$.
   Multiply back with $D = \operatorname{diag}(2, 2, 1)$:
$$Q D = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 2 & 1 \\ 0 & 0 & -1 \end{pmatrix}, \qquad Q D Q^{-1} = \begin{pmatrix} 2 & 0 & 2 - 1 \\ 0 & 2 & 2 - 1 \\ 0 & 0 & 1 \end{pmatrix} = S.$$
   So $S$ is [[diagonalizable|07SQCNV233]].
9. Finally the two parts commute:
$$S N = \begin{pmatrix} -2 & 2 & 0 \\ -2 & 2 & 0 \\ 0 & 0 & 0 \end{pmatrix} = N S.$$

## Remarks

The example shows the shape of the general proof: Bézout's identity gives the projections, the projections give $S$, and $S$ comes out as a polynomial in $A$.
The polynomial $g(t) = -t^2 + 4t - 2$ satisfies $g(1) = 1$, $g(2) = 2$ and $g'(2) = 0$, so $g \equiv 1 \bmod (t - 1)$ and $g \equiv 2 \bmod (t - 2)^2$, which are the congruences of the Chinese remainder form of the proof.
Since $N = (A - I)(A - 2I)$, the part $N$ is $0$ on $V_1$, and on $V_2$ it equals $A - 2I$.
The matrix $A$ itself is not diagonalizable, because its nilpotent part is not $0$.

Watch out: the diagonal part $\operatorname{diag}(1, 3, 1)$ of $A$ is not $S$.
It is not even a possible $S$, since it does not commute with $R = A - \operatorname{diag}(1, 3, 1)$: the $(1, 2)$ entry of $\operatorname{diag}(1, 3, 1) R$ is $1 \cdot 1 = 1$, while that of $R \operatorname{diag}(1, 3, 1)$ is $1 \cdot 3 = 3$.
If the entry $-1$ of $A$ is changed to $-2$, the block $\begin{pmatrix} 1 & 1 \\ -2 & 3 \end{pmatrix}$ has $p = t^2 - 4t + 5$ with roots $2 \pm i$, the matrix becomes diagonalizable over $\C$, and then $N = 0$ over $\C$.

## Explanations

### L1 human

We split the matrix $A$ into two parts.
The first part $S$ only stretches, by $2$, $2$ and $1$ along three directions.
The second part $N$ gives zero after two steps.
The two parts commute, and both are built from $A$ by sums and products.

### L2 human

As a check, $S$ and $A$ have the same characteristic polynomial.

1. The matrix $S$ is upper triangular with diagonal entries $2, 2, 1$.
2. So $p_S = (t - 2)^2 (t - 1)$, by the determinant of a triangular matrix.
3. This equals $p_A$, as it must, since $N$ is nilpotent and commutes with $S$.

The typical use is to compute powers.
Since $N^2 = 0$ and $S N = N S$, the binomial theorem gives
$$A^k = (S + N)^k = S^k + k S^{k-1} N,$$
and $S^k = Q \operatorname{diag}(2^k, 2^k, 1) Q^{-1}$ is easy.
The trap is to take $S$ as the diagonal of $A$, which gives a split with parts that do not commute.
