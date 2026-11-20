---
tag: XGRN8RY29P
kind: example
name: A real matrix with complex eigenvalues
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [0VSSPAFM2C, 7JJE96MZQY]
illustrates: [053QVHF6N7, 0NMXDCNNKR, 0C2F40MEBC]
uses: [039HF58KQ5, 0ZND7NQ970, 0B5H4208Z9, 053QVHF6N7, 0FTH2E9TAS]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenvalues and characteristic polynomial
  - book: isbn:9780321982384
---

## Example

Let $A = \begin{pmatrix} 3 & -2 \\ 4 & -1 \end{pmatrix}$, a real matrix viewed over $\C$.

1. By the [[definition of the characteristic polynomial|039HF58KQ5]], $p_A(t) = (t - 3)(t + 1) + 8 = t^2 - 2t + 5$.
2. Second method: $\tr A = 2$ and $\det A = -3 + 8 = 5$. This gives the same polynomial.
3. The discriminant is $4 - 20 = -16$. So the roots are $\lambda = 1 + 2i$ and $\bar\lambda = 1 - 2i$, and $A$ has no real eigenvalue.
4. For $\lambda = 1 + 2i$: the first row of $A - \lambda I$ is $(2 - 2i,\ -2)$. So $v = (1,\ 1 - i)$ solves $(A - \lambda I)v = 0$.
5. Check: $Av = (3 - 2(1 - i),\ 4 - (1 - i)) = (1 + 2i,\ 3 + i)$.
6. And $\lambda v = (1 + 2i,\ (1 + 2i)(1 - i)) = (1 + 2i,\ 1 - i + 2i + 2) = (1 + 2i,\ 3 + i)$. So $Av = \lambda v$.
7. $A$ has real entries. So taking the [[complex conjugate|0FTH2E9TAS]] of $Av = \lambda v$ gives $A\bar v = \bar\lambda \bar v$, with $\bar v = (1,\ 1 + i)$.

## Remarks

- The eigenvalues of a real matrix that are not real come in conjugate pairs, with conjugate eigenvectors.
- $\lambda + \bar\lambda = 2 = \tr A$ and $\lambda\bar\lambda = 1 + 4 = 5 = \det A$.
- With $v = (1, 1) + i(0, -1)$, the real basis $(1, 1), (0, -1)$ puts $A$ in the form $\begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}$, a rotation combined with a scaling by $\sqrt 5$.

## Explanations

### L1 human

This real matrix has no real eigenvalue.
Its eigenvalues are the complex numbers $1 + 2i$ and $1 - 2i$.
Geometrically, it turns the plane and stretches it.

### L2 human

The typical use is to find complex eigenvectors by the same method as real ones.
One eigenvector is enough, because the other one is its conjugate.
A trap is to forget that $i^2 = -1$ when checking $Av = \lambda v$.
