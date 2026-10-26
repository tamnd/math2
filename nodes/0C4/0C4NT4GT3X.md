---
tag: 0C4NT4GT3X
kind: statement
role: theorem
name: Eigenvalues of a self-adjoint operator are real
msc: [47B15, 15A18]
uses: [0MB8HQW495, 0ZND7NQ970]
sources:
  - url: https://en.wikipedia.org/wiki/Self-adjoint_operator
    locator: Properties
---

## Statement

Let $V$ be a finite-dimensional inner product space over $\R$ or $\C$, and let $T \colon V \to V$ be a [[self-adjoint|0NEGN5CRSC]] linear map.
Then each [[eigenvalue|0BQAA2BK3Q]] of $T$ is a real number.

## Remarks

If $T(v) = \lambda v$ with $v \ne 0$, then $\lambda \langle v, v \rangle = \langle T(v), v \rangle = \langle v, T(v) \rangle = \bar\lambda \langle v, v \rangle$, so $\lambda = \bar\lambda$.
In particular, a [[Hermitian matrix|0P17NGQQMQ]] has only real eigenvalues.
So a real [[symmetric matrix|0VR671PHE5]] has only real eigenvalues, also when we view it as a complex matrix.

## Explanations

### L1 human

Self-adjoint maps never have complex eigenvalues that are not real.
For example, the symmetric matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has the eigenvalues $1$ and $-1$.
By contrast, the rotation matrix $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ is not symmetric, and its eigenvalues are $\pm i$.
