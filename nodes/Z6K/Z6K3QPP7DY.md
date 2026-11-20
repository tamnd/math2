---
tag: Z6K3QPP7DY
kind: example
name: The symmetric matrix with rows (2, 1) and (1, 2)
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [0BQAA2BK3Q, 0N6960W0BV, 0XPX5NC67E, 7JJE96MZQY]
illustrates: [053QVHF6N7, 0NMXDCNNKR, 0C2F40MEBC]
uses: [0ZND7NQ970, 0B5H4208Z9, 039HF58KQ5, 04EHB7YDQS, 053QVHF6N7]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Two-dimensional matrix example
  - book: isbn:9780134860244
---

## Example

Let $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ over $\R$.
We find its [[eigenvalues|0ZND7NQ970]] and [[eigenvectors|0B5H4208Z9]] by the method for [[computing eigenvalues by hand|7JJE96MZQY]].

1. The [[characteristic polynomial|039HF58KQ5]] is $p_A(t) = \det(tI - A) = (t - 2)^2 - 1 = t^2 - 4t + 3$.
2. Second method: for a $2 \times 2$ matrix, $p_A(t) = t^2 - (\tr A)t + \det A$. Here $\tr A = 4$ and $\det A = 4 - 1 = 3$. This gives the same polynomial.
3. $t^2 - 4t + 3 = (t - 1)(t - 3)$. Since the [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]], the eigenvalues are $1$ and $3$.
4. For $\lambda = 1$: $A - I = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, with kernel spanned by $v_1 = (1, -1)$.
5. Check: $A v_1 = (2 - 1,\ 1 - 2) = (1, -1) = 1 \cdot v_1$.
6. For $\lambda = 3$: $A - 3I = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}$, with kernel spanned by $v_2 = (1, 1)$.
7. Check: $A v_2 = (2 + 1,\ 1 + 2) = (3, 3) = 3 \cdot v_2$.
8. So the [[spectrum|04EHB7YDQS]] of $A$ is $\{1, 3\}$.

## Remarks

- The sum of the eigenvalues is $1 + 3 = 4 = \tr A$, and their product is $1 \cdot 3 = 3 = \det A$.
- The eigenvectors $(1, -1)$ and $(1, 1)$ are orthogonal, as for every real symmetric matrix with distinct eigenvalues.
- With $S = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$, $S^{-1} A S = \operatorname{diag}(1, 3)$.
- The [[minimal polynomial|03NDVCSHSB]] is $p_A$, because $p_A$ has two distinct roots.

## Explanations

### L1 human

The matrix stretches the line through $(1, 1)$ by $3$.
It keeps each vector on the line through $(1, -1)$ fixed.
These two lines are the eigenvector directions.

### L2 human

The two-step method is typical: factor $p_A$, then solve $(A - \lambda I)v = 0$ for each root.
Always check $Av = \lambda v$ at the end.
A trap is to read the eigenvalues from the diagonal entries $2, 2$, which is wrong for a matrix that is not triangular.
