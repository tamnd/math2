---
tag: 07PTPSZPME
kind: definition
name: Trace of a matrix
msc: ["15A15"]
topics: [Y1ESNQ2V52]
audience: ug1
defines: 0XC1RDBY7A
uses: [0CP7YY6NAG]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.trace
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Definition
---

## Definition

The trace of a square matrix is the sum of its diagonal entries.
Let $R$ be a commutative ring and let $A = (a_{ij})$ be an $n \times n$ [[square matrix|0CP7YY6NAG]] over $R$.
The *trace* of $A$ is
$$\operatorname{tr} A = \sum_{i=1}^{n} a_{ii} = a_{11} + a_{22} + \cdots + a_{nn}.$$

## Notation

Other notations are $\operatorname{Tr} A$ and $\operatorname{Sp} A$.
In Mathlib, `Matrix.trace A` is the sum of the diagonal entries over a finite index type, and it needs only an additive commutative monoid of entries.

## Remarks

For example,
$$\operatorname{tr} \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = 1 + 4 = 5, \qquad \operatorname{tr} I_n = n, \qquad \operatorname{tr} 0 = 0.$$
The entries off the diagonal play no part, so $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 \\ 0 & 4 \end{pmatrix}$ have the same trace.
Only square matrices have a trace.

The trace is [[linear|0GJWQZCPZM]], it is [[invariant under transpose|09E1RCZ7YT]], and $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ by the [[cyclic property|0Y4NF1DRKD]].
So similar matrices have the same trace, and the [[trace of a linear map|0KZDNGA561]] is well defined.
Over an algebraically closed field, the trace is the [[sum of the eigenvalues|0NMXDCNNKR]], counted with multiplicity.
The [[concept page|0XC1RDBY7A]] gives these rules with examples, including the inner product $\operatorname{tr}(A^{\mathsf{T}} B)$.

## Explanations

### L1 human

The trace adds up the numbers on the main diagonal of a square matrix.
For the identity matrix of order $n$ the trace is $n$.

### L2 human

Only the $n$ diagonal entries enter the trace, and each enters with coefficient $1$.
So the trace is the linear form on $M_n(R)$ that sends the matrix unit $E_{ii}$ to $1$ and $E_{ij}$ to $0$ for $i \neq j$.
Since every matrix is $\sum_{i,j} a_{ij} E_{ij}$, these values determine it: $\operatorname{tr} A = \sum_i a_{ii}$.
