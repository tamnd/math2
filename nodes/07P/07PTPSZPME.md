---
tag: 07PTPSZPME
kind: definition
name: Trace of a matrix
msc: [15A15]
defines: 0XC1RDBY7A
uses: [0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Definition
---

## Definition

Let $R$ be a commutative ring and let $A = (a_{ij})$ be an $n \times n$ [[square matrix|0JXZKX526R]] over $R$.
The *trace* of $A$ is
$$\tr A = \sum_{i=1}^{n} a_{ii} = a_{11} + a_{22} + \cdots + a_{nn}.$$

## Remarks

The trace of $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ is $5$.
The trace is [[linear|0GJWQZCPZM]], it is [[invariant under transpose|09E1RCZ7YT]], and [[$\tr(AB) = \tr(BA)$|0Y4NF1DRKD]].
Similar matrices have the same trace, so the [[trace of a linear map|0KZDNGA561]] is well defined.
Over an algebraically closed field, the trace is the [[sum of the eigenvalues|0NMXDCNNKR]], counted with multiplicity.

## Explanations

### L1 human

The trace adds up the numbers on the main diagonal of a square matrix.
It is a single number that does not change when we change the basis.
For the identity matrix of order $n$, the trace is $n$.
