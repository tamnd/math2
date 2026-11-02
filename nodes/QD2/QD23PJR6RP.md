---
tag: QD23PJR6RP
kind: statement
role: theorem
name: Lidskii's theorem
msc: [47B10, 47A10]
uses: [HM2HHE3J51, Z2CP530WDE, M2NEP1K5AE, 0BQAA2BK3Q, 0XC1RDBY7A]
about: [Z2CP530WDE]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_class
---

## Statement

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]], and let $T$ be a [[trace class operator|Z2CP530WDE]] on $H$ with trace $\operatorname{tr} T$ and trace norm $\norm{T}_1$.
Let $(\lambda_n)$ be the nonzero [[eigenvalues|0BQAA2BK3Q]] of $T$, each repeated according to its algebraic multiplicity $\dim \bigcup_{k \ge 1} \ker (T - \lambda_n I)^k$.
Then $\sum_n \abs{\lambda_n} \le \norm{T}_1$, and
$$\operatorname{tr} T = \sum_n \lambda_n.$$

## Remarks

A trace class operator is [[compact|M2NEP1K5AE]], so its nonzero eigenvalues form a finite or null sequence, and each has finite algebraic multiplicity.
The inequality $\sum \abs{\lambda_n} \le \norm{T}_1$ is a consequence of Weyl's inequality between eigenvalues and singular values.
For the identity, one writes $T$ in upper triangular form with respect to a Schur basis of the span of its generalized eigenvectors.
This reduces the theorem to the case of a quasinilpotent trace class operator, whose trace must be shown to be $0$.
This last step is the hard part; one proof uses the Fredholm determinant $\det(I + zT)$, an entire function of $z$ whose zeros are the numbers $-1/\lambda_n$.
For a matrix, the theorem is the fact that the [[trace|0XC1RDBY7A]] is the sum of the eigenvalues.
Example: a trace class operator may have no nonzero eigenvalue at all; then the theorem says its trace is $0$.
The hypothesis matters: for a merely compact operator, the sum $\sum_i \ip{T e_i}{e_i}$ can diverge or depend on the basis.

## Explanations

### L1 human

For a square matrix, adding the diagonal entries gives the same number as adding the eigenvalues.
Lidskii's theorem says that this remains true for trace class operators on infinite-dimensional spaces.
This is surprising, since such an operator may have very few eigenvalues, or none.

### L2 human

The theorem links two different definitions of the trace: a basis-dependent sum of diagonal entries and a spectral sum.
It was proved by Lidskii in 1959; the case of self-adjoint or normal operators is much easier and follows from the spectral theorem.
It is used in the theory of Fredholm determinants, in random matrix theory, and in the study of trace formulas.
