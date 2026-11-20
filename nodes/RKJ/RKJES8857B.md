---
tag: RKJES8857B
kind: example
name: The trace of transposition on 2 x 2 matrices
msc: ["15A04", "15A15"]
topics: [S6559D61BP]
audience: ug1
instance_of: [0KZDNGA561]
illustrates: [0WCPH5Z7FA]
uses: [0RPDTWY2JS, 0YQSGNYE3K, 07PTPSZPME, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a linear operator
---

## Example

Let $V = M_2(\R)$, of dimension $4$, and let $T \colon V \to V$ be $T(X) = X^\top$, the [[transpose|0W809K6AW0]].
Write $E_{ij}$ for the matrix with $1$ in position $(i, j)$ and $0$ elsewhere.

1. Standard basis $B = (E_{11}, E_{12}, E_{21}, E_{22})$. $T(E_{11}) = E_{11}$, $T(E_{12}) = E_{21}$, $T(E_{21}) = E_{12}$ and $T(E_{22}) = E_{22}$.
2. So the [[matrix|0YQSGNYE3K]] of $T$ is
$$[T]_B = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.$$
3. Its [[trace|07PTPSZPME]] is $1 + 0 + 0 + 1 = 2$.
4. Second basis $B' = (E_{11}, E_{22}, E_{12} + E_{21}, E_{12} - E_{21})$. The first three are symmetric, and the last is antisymmetric.
5. $T(E_{11}) = E_{11}$, $T(E_{22}) = E_{22}$ and $T(E_{12} + E_{21}) = E_{21} + E_{12}$.
6. $T(E_{12} - E_{21}) = E_{21} - E_{12} = -(E_{12} - E_{21})$.
7. So $[T]_{B'} = \operatorname{diag}(1, 1, 1, -1)$, with trace $1 + 1 + 1 - 1 = 2$.
8. Both bases give $\tr T = 2$.

## Remarks

- The value $2$ is $\dim(\text{symmetric}) - \dim(\text{antisymmetric}) = 3 - 1$.
- On $M_n(\R)$, transposition has trace $\tfrac{n(n+1)}{2} - \tfrac{n(n-1)}{2} = n$.
- The map $\tfrac{1}{2}(\id + T)$ is the projection onto the symmetric matrices. Its trace is $\tfrac{1}{2}(4 + 2) = 3$, its rank.

## Explanations

### L1 human

Transposition keeps the diagonal entries and exchanges the two other entries.
In the standard basis, only the two diagonal positions contribute $1$ each to the trace.

### L2 human

In a basis of symmetric and antisymmetric matrices, $T$ is diagonal with entries $1$ and $-1$.
The trace is the number of entries $1$ minus the number of entries $-1$, so $3 - 1 = 2$, the same as in the standard basis.
