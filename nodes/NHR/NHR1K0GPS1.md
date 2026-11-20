---
tag: NHR1K0GPS1
kind: example
name: A triangular matrix
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [0BQAA2BK3Q, 7JJE96MZQY, 0FY42N02DV]
illustrates: [053QVHF6N7, FWY8A9M5HK, 0NMXDCNNKR, 0C2F40MEBC]
uses: [039HF58KQ5, 0K1KKMFHYH, 0ZND7NQ970, 0S7A0EMPF4, 06YSJVR356, 0FRYPZ6D0X, 0W4FSW1TVB]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Triangular matrix example
  - book: isbn:9780321982384
---

## Example

Let $A = \begin{pmatrix} 2 & 5 & 7 \\ 0 & -1 & 3 \\ 0 & 0 & 2 \end{pmatrix}$ over $\R$.

1. $tI - A$ is upper triangular. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $p_A(t) = (t - 2)(t + 1)(t - 2) = (t - 2)^2(t + 1)$.
2. Expanded, $p_A(t) = t^3 - 3t^2 + 4$.
3. Second method, by the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]]: $\tr A = 3$. The principal $2 \times 2$ minors are $-2$, $4$ and $-2$, with sum $0$. $\det A = -4$. This gives $t^3 - 3t^2 + 0t + 4$.
4. So the [[eigenvalues|0ZND7NQ970]] are the diagonal entries $2$ and $-1$. The [[algebraic multiplicity|0S7A0EMPF4]] of $2$ is $2$.
5. Eigenvalue $2$: $A(1, 0, 0) = (2, 0, 0) = 2(1, 0, 0)$.
6. Eigenvalue $-1$: $A(5, -3, 0) = (10 - 15,\ 3,\ 0) = (-5, 3, 0) = -(5, -3, 0)$.
7. $A - 2I = \begin{pmatrix} 0 & 5 & 7 \\ 0 & -3 & 3 \\ 0 & 0 & 0 \end{pmatrix}$ has rank $2$. By the [[rank-nullity theorem|0W4FSW1TVB]], the [[geometric multiplicity|06YSJVR356]] of $2$ is $1$.

## Remarks

- For a triangular matrix, the eigenvalues are the diagonal entries, each counted as often as it appears.
- The diagonal does not give the geometric multiplicity. Here $2$ appears twice, but $E_2$ is a line.
- The sum of the eigenvalues is $2 + 2 - 1 = 3 = \tr A$, and their product is $-4 = \det A$.

## Explanations

### L1 human

For a triangular matrix, the eigenvalues can be read from the diagonal.
Here they are $2$, $-1$ and $2$.
The eigenvectors still have to be found by solving equations.

### L2 human

The typical use is to read the spectrum of a triangular matrix at once.
A trap is to use this shortcut on a matrix that is not triangular, or after row reduction.
