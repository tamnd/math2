---
tag: RFHTECHY4J
kind: example
name: Best rank-one approximation of a 2 × 2 matrix
msc: [15A18, 65F55]
topics: [SS4EVPKT3A]
audience: ug2
illustrates: [JJT6GC055J]
uses: [000NPTMX6J, K33BQX70N0, 0ZTEH055YF]
sources:
  - url: https://en.wikipedia.org/wiki/Low-rank_approximation
    locator: Basic low-rank approximation problem
---

## Example

Let $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$, with the SVD of [[the 2 by 2 example|B546BDVFQZ]]:
$$\sigma_1 = 3\sqrt5, \quad u_1 = \tfrac{1}{\sqrt{10}}(1, 3), \quad v_1 = \tfrac{1}{\sqrt2}(1, 1), \qquad \sigma_2 = \sqrt5, \quad u_2 = \tfrac{1}{\sqrt{10}}(-3, 1), \quad v_2 = \tfrac{1}{\sqrt2}(-1, 1).$$
Check: $A v_1 = \tfrac{1}{\sqrt2}(3, 9)$, which is $3\sqrt5 \cdot \tfrac{1}{\sqrt{10}}(1, 3)$, and $A v_2 = \tfrac{1}{\sqrt2}(-3, 1)$, which is $\sqrt5 \cdot \tfrac{1}{\sqrt{10}}(-3, 1)$.
We find the best rank-one approximation and test the [[Eckart-Young-Mirsky theorem|JJT6GC055J]] against two other choices.

1. The truncated SVD keeps the first term. Since $\sigma_1 / (\sqrt{10} \sqrt2) = 3\sqrt5 / \sqrt{20} = \tfrac32$,
$$A_1 = \sigma_1 u_1 v_1^{\mathsf{T}} = \frac32 \begin{pmatrix} 1 & 1 \\ 3 & 3 \end{pmatrix} = \begin{pmatrix} 1.5 & 1.5 \\ 4.5 & 4.5 \end{pmatrix}.$$
2. The rank of $A_1$ is $1$, because its two columns are equal and nonzero.
3. The error matrix is
$$A - A_1 = \begin{pmatrix} 1.5 & -1.5 \\ -0.5 & 0.5 \end{pmatrix}.$$
It equals the dropped term $\sigma_2 u_2 v_2^{\mathsf{T}} = \frac{\sqrt5}{\sqrt{20}} \begin{pmatrix} 3 & -3 \\ -1 & 1 \end{pmatrix} = \frac12 \begin{pmatrix} 3 & -3 \\ -1 & 1 \end{pmatrix}$, as the SVD says.
4. The [[Frobenius norm|K33BQX70N0]] of the error is the root of the sum of the squared entries: $\norm{A - A_1}_F^2 = 2.25 + 2.25 + 0.25 + 0.25 = 5$, so $\norm{A - A_1}_F = \sqrt5 = \sigma_2$.
5. For the [[operator norm|0ZTEH055YF]], write $A - A_1 = \tfrac12 (-3, 1)^{\mathsf{T}} (-1, 1)$. For a unit vector $x$, we get $(A - A_1) x = \tfrac12 (x_2 - x_1) (-3, 1)$, so
$$\norm{(A - A_1) x} = \tfrac12 \sqrt{10} \, \abs{x_2 - x_1} \le \tfrac12 \sqrt{10} \sqrt{2} = \sqrt5,$$
since $\abs{x_2 - x_1} \le \sqrt2$ by the Cauchy-Schwarz inequality, with equality at $x = v_2$. So $\norm{A - A_1}_2 = \sqrt5 = \sigma_2$.
6. Keeping the first column gives the rank-one matrix $B = \begin{pmatrix} 3 & 0 \\ 4 & 0 \end{pmatrix}$, and $A - B = \begin{pmatrix} 0 & 0 \\ 0 & 5 \end{pmatrix}$ has error $5$ in both norms.
7. Keeping the second row gives $B = \begin{pmatrix} 0 & 0 \\ 4 & 5 \end{pmatrix}$, and $A - B = \begin{pmatrix} 3 & 0 \\ 0 & 0 \end{pmatrix}$ has error $3$ in both norms.
8. Both errors are larger than $\sqrt5 \approx 2.24$, as the theorem predicts.

## Remarks

The example shows that the best rank-one matrix is not built from the rows or columns of $A$.
It changes every entry, even the zero in position $(1, 2)$, which becomes $1.5$.

Here $\sigma_2$ is the only dropped singular value, so the operator norm error and the Frobenius error are equal.
For a larger matrix with two or more dropped values, the Frobenius error $\left(\sum_{i > k} \sigma_i^2\right)^{1/2}$ is larger than the operator norm error $\sigma_{k+1}$.

Since $\sigma_2 = \sqrt5$, every singular $2 \times 2$ matrix $S$ has $\norm{A - S}_2 \ge \sqrt5$, and $A_1$ is a closest singular matrix to $A$.
If we change the entry $5$ to a number $t$, the singular values change, and $A_1$ changes with them; for $t = 0$ the matrix $A$ itself has rank one and the error is $0$.

## Explanations

### L1 human

We replace $A$ by the closest matrix whose columns are all multiples of one vector.
The SVD gives it at once: keep the largest piece $\sigma_1 u_1 v_1^{\mathsf{T}}$ and drop the other.
The error has size $\sqrt5 \approx 2.24$, and simpler choices, such as keeping one column or one row, give errors $5$ and $3$.

### L2 human

The recipe has three steps: compute the SVD, keep the first $k$ terms, and read the error from the singular values that you drop.
Steps 4 and 5 confirm both errors by direct computation, without trusting the theorem.
This is the typical use of the theorem: to compress a matrix and to know in advance how much is lost.
Watch out: deleting or rounding entries of $A$ is not a good low-rank approximation, as steps 6 and 7 show.
