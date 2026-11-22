---
tag: M1XGWNT48M
kind: example
name: Row reduction changes the eigenvalues
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
not_instance_of:
  - target: 7JJE96MZQY
    note: Row reducing A and reading the diagonal is not a valid way to compute eigenvalues
  - target: 0BQAA2BK3Q
    note: The diagonal entries 2 and 3/2 of the row-reduced matrix are not eigenvalues of A
uses: [0ZND7NQ970, 039HF58KQ5, 053QVHF6N7]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Classical method
  - book: isbn:9780321982384
---

## Example

Let $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ over $\mathbb{R}$.
Subtract $\tfrac{1}{2}$ of row $1$ from row $2$, which gives the upper triangular matrix
$$U = \begin{pmatrix} 2 & 1 \\ 0 & 3/2 \end{pmatrix}.$$
The diagonal of $U$ suggests the values $2$ and $3/2$, and we show that neither one is an eigenvalue of $A$.

1. The characteristic polynomial of $A$ is
$$p_A(t) = (t - 2)^2 - 1 = t^2 - 4t + 3 = (t - 1)(t - 3).$$
   Check: $\tr A = 4$ and $\det A = 4 - 1 = 3$ give the same polynomial.
2. Since the [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]], the [[eigenvalues|0ZND7NQ970]] of $A$ are $1$ and $3$.
3. The value $2$ is not an eigenvalue, because
$$\det(A - 2I) = \det \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = -1 \ne 0.$$
4. The value $3/2$ is not an eigenvalue, because
$$p_A(3/2) = \tfrac{9}{4} - 6 + 3 = -\tfrac{3}{4} \ne 0.$$

## Remarks

A row operation replaces $A$ by $EA$ for an invertible elementary matrix $E$.
Eigenvalues are kept by similarity, $A \mapsto S^{-1} A S$, and $EA$ is in general not similar to $A$.
Here the eigenvalues of $U$ are $2$ and $3/2$, while those of $A$ are $1$ and $3$.

Row reduction does keep the determinant, up to a known factor, and adding a multiple of one row to another keeps it exactly.
Indeed $\det U = 2 \cdot \tfrac{3}{2} = 3 = \det A$, which is the product $1 \cdot 3$ of the eigenvalues.
So the product survives, but the individual eigenvalues do not, and neither does the trace: $\tr U = 7/2 \ne 4$.

Row reduction is still the right tool in the second stage of the method.
Once $\lambda$ is known, we row reduce $A - \lambda I$ to find its kernel, the eigenspace.

## Explanations

### L1 human

Row reduction is a good tool for solving equations.
But each row operation changes the matrix, and the eigenvalues change with it.
Here the reduced matrix has $2$ and $3/2$ on its diagonal, while the eigenvalues of the original matrix are $1$ and $3$.

### L2 human

The correct order is to compute $\det(tI - A)$ first, find its roots, and row reduce only the matrices $A - \lambda I$.
Watch out: row reducing $A$ itself and reading the diagonal gives wrong values, as steps 3 and 4 show.
