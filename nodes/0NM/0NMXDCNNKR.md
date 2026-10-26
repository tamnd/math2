---
tag: 0NMXDCNNKR
kind: statement
role: theorem
name: Trace is the sum of the eigenvalues
msc: [15A15, 15A18]
uses: [0FRYPZ6D0X, 0ZND7NQ970, 0S7A0EMPF4]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace as the sum of eigenvalues
---

## Statement

Let $F$ be a field and let $A$ be an $n \times n$ matrix over $F$.
Assume that the characteristic polynomial of $A$ splits over $F$ as $p_A(t) = (t - \lambda_1) \cdots (t - \lambda_n)$.
Then
$$\tr A = \lambda_1 + \lambda_2 + \cdots + \lambda_n.$$

## Remarks

The $\lambda_i$ are the [[eigenvalues|0BQAA2BK3Q]] of $A$, each repeated according to its [[algebraic multiplicity|0FY42N02DV]].
The hypothesis always holds over $\C$.
The statement follows by comparing the coefficients of $t^{n-1}$, see [[the trace as a coefficient|0FRYPZ6D0X]].
For example, $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ has eigenvalues $1$ and $3$, and trace $4$.

## Explanations

### L1 human

The trace of a matrix is the sum of its eigenvalues, counted with multiplicity.
For a diagonal matrix this is clear, because the eigenvalues are the diagonal entries.
The statement says that it stays true for every complex matrix.
