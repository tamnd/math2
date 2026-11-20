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

Let $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
Subtracting $\frac{1}{2}$ of row 1 from row 2 gives the triangular matrix $U = \begin{pmatrix} 2 & 1 \\ 0 & 3/2 \end{pmatrix}$.

1. The diagonal of $U$ suggests the values $2$ and $3/2$.
2. But $p_A(t) = t^2 - 4t + 3 = (t - 1)(t - 3)$, from $\tr A = 4$ and $\det A = 3$. Second method: $(t - 2)^2 - 1 = t^2 - 4t + 3$.
3. Since the [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]], the eigenvalues of $A$ are $1$ and $3$.
4. Check that $2$ is not an [[eigenvalue|0ZND7NQ970]]: $\det(A - 2I) = \det\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = -1 \ne 0$.
5. Check that $3/2$ is not an eigenvalue: $p_A(3/2) = 9/4 - 6 + 3 = -3/4 \ne 0$.

## Remarks

- Row operations replace $A$ by $EA$ for an invertible $E$. In general $EA$ is not similar to $A$, so its eigenvalues differ.
- Row reduction keeps the determinant up to a known factor: here $\det U = 3 = 1 \cdot 3$. It does not keep the individual eigenvalues.
- Row reduction is the right tool in the second step of the method, to find the kernel of $A - \lambda I$.

## Explanations

### L1 human

Row reduction is useful for solving equations.
But it changes the matrix, and with it the eigenvalues.
Here the reduced matrix has diagonal $2, 3/2$, while the eigenvalues are $1$ and $3$.

### L2 human

The typical lesson is to compute $\det(tI - A)$ first, and to row reduce only $A - \lambda I$.
A trap is to row reduce $A$ itself and read the diagonal.
