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

Let $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$, with the SVD of [[the $2 \times 2$ example|B546BDVFQZ]]: $\sigma_1 = 3\sqrt5$, $\sigma_2 = \sqrt5$, $u_1 = \tfrac{1}{\sqrt{10}}(1, 3)$, $v_1 = \tfrac{1}{\sqrt2}(1, 1)$, $u_2 = \tfrac{1}{\sqrt{10}}(-3, 1)$, $v_2 = \tfrac{1}{\sqrt2}(-1, 1)$.

1. The truncated SVD is $A_1 = \sigma_1 u_1 v_1^T = \frac{3\sqrt5}{\sqrt{20}} \begin{pmatrix} 1 & 1 \\ 3 & 3 \end{pmatrix} = \frac32 \begin{pmatrix} 1 & 1 \\ 3 & 3 \end{pmatrix} = \begin{pmatrix} 1.5 & 1.5 \\ 4.5 & 4.5 \end{pmatrix}$.
2. Its rank is $1$, since the second column equals the first.
3. $A - A_1 = \begin{pmatrix} 1.5 & -1.5 \\ -0.5 & 0.5 \end{pmatrix}$. This equals $\sigma_2 u_2 v_2^T = \frac{\sqrt5}{\sqrt{20}} \begin{pmatrix} 3 & -3 \\ -1 & 1 \end{pmatrix}$, as the SVD says.
4. Frobenius error: $\norm{A - A_1}_F^2 = 2.25 + 2.25 + 0.25 + 0.25 = 5$, so $\norm{A - A_1}_F = \sqrt5 = \sigma_2$.
5. Operator norm error: $A - A_1 = \tfrac12 (-3, 1)^T (-1, 1)$ has rank one. For $x$ with $\norm{x} = 1$, $\norm{(A - A_1)x} = \tfrac12 \norm{(-3, 1)} \abs{x_2 - x_1} \le \tfrac12 \sqrt{10} \sqrt2 = \sqrt5$, with equality at $x = v_2$. So $\norm{A - A_1}_2 = \sqrt5 = \sigma_2$.
6. Compare with other rank-one matrices. Keeping the first column, $B = \begin{pmatrix} 3 & 0 \\ 4 & 0 \end{pmatrix}$, gives $A - B = \begin{pmatrix} 0 & 0 \\ 0 & 5 \end{pmatrix}$, with error $5$ in both norms.
7. Keeping the second row, $B = \begin{pmatrix} 0 & 0 \\ 4 & 5 \end{pmatrix}$, gives $A - B = \begin{pmatrix} 3 & 0 \\ 0 & 0 \end{pmatrix}$, with error $3$ in both norms.
8. Both errors are larger than $\sqrt5 \approx 2.24$, as the theorem says.

## Remarks

- Here $\sigma_2$ is the only dropped singular value, so the operator norm error and the Frobenius error are equal. For larger matrices, the Frobenius error $\left(\sum_{i > k} \sigma_i^2\right)^{1/2}$ is larger than $\sigma_{k+1}$ when two or more singular values are dropped.
- The approximation $A_1$ changes every entry of $A$, also the zero entry.
- Since $\sigma_2 = \sqrt5$, every singular matrix $S$ has $\norm{A - S}_2 \ge \sqrt5$, and $A_1$ is a closest singular matrix.

## Explanations

### L1 human

We replace $A$ by the closest matrix whose columns are multiples of one vector.
The SVD gives it at once: keep the largest piece $\sigma_1 u_1 v_1^T$.
The error has size $\sqrt5$, and simpler choices, such as keeping one column, do worse.

### L2 human

The recipe is: compute the SVD, keep the first $k$ terms, and read the error from the dropped singular values.
Steps 4 and 5 check both norms by direct computation.
A trap: rounding or deleting entries of $A$ is not a good low-rank approximation; steps 6 and 7 show errors $5$ and $3$.
