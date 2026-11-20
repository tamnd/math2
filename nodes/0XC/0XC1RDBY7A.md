---
tag: 0XC1RDBY7A
kind: concept
name: Trace of a matrix
msc: ["15A15"]
topics: [Y1ESNQ2V52]
audience: ug1
uses: [0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Basic properties
  - url: https://en.wikipedia.org/wiki/Frobenius_inner_product
    locator: lead section
same_as:
  wikidata: Q321102
  wikipedia: Trace (linear algebra)
---

## Summary

The trace of a [[square matrix|0JXZKX526R]] is the sum of the entries on its main diagonal, $\operatorname{tr} A = a_{11} + \cdots + a_{nn}$.
The [[formal definition|07PTPSZPME]] states it over a commutative ring.
The trace is [[linear|0GJWQZCPZM]], does not change under the [[transpose|09E1RCZ7YT]], and satisfies the [[cyclic property|0Y4NF1DRKD]] $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.
It is not multiplicative: $\operatorname{tr}(AB) \neq \operatorname{tr} A \operatorname{tr} B$ in general.

## Motivation

The trace is the simplest number attached to a square matrix that does not depend on the basis.
By the cyclic property, $\operatorname{tr}(P^{-1} A P) = \operatorname{tr} A$, so [[similar matrices|0E89HQATM8]] have the same trace.
So the [[trace of a linear map|0KZDNGA561]] is well defined.
Over $\mathbb{C}$ it is the [[sum of the eigenvalues|0NMXDCNNKR]], and it is a coefficient of the [[characteristic polynomial|0FRYPZ6D0X]].
The formula $\operatorname{tr}(A^{\mathsf{T}} B) = \sum_{i,j} a_{ij} b_{ij}$ makes it the source of the standard inner product on matrices.

## Notation

- Books write $\operatorname{tr} A$, $\operatorname{Tr} A$, $\operatorname{trace} A$ or $\operatorname{Sp} A$ (from the German *Spur*).
- In Mathlib, `Matrix.trace A` is the trace. It is defined for square matrices indexed by any finite type `n`, and the order of the indices plays no part.

## Remarks

### Examples

- [[The trace of AᵀA is the sum of the squares of the entries|~eb388508]].
- [[The Frobenius inner product of two matrices|~cde503c5]].
- $\operatorname{tr} I_n = n$ and $\operatorname{tr} 0 = 0$.

### Non-examples

- [[The trace is not a ring homomorphism|~c5ad9f38]].
- A $2 \times 3$ matrix has no trace, because it is not square.

### Basic properties

For $n \times n$ matrices $A$ and $B$ over a commutative ring $R$ and $c \in R$:

- $\operatorname{tr}(A + B) = \operatorname{tr} A + \operatorname{tr} B$ and $\operatorname{tr}(cA) = c \operatorname{tr} A$, by [[linearity|0GJWQZCPZM]].
- $\operatorname{tr}(A^{\mathsf{T}}) = \operatorname{tr} A$, by [[this statement|09E1RCZ7YT]].
- $\operatorname{tr}(AB) = \operatorname{tr}(BA)$, also for an $m \times n$ matrix $A$ and an $n \times m$ matrix $B$, by the [[cyclic property|0Y4NF1DRKD]].
- $\operatorname{tr}(ABC) = \operatorname{tr}(BCA) = \operatorname{tr}(CAB)$, but $\operatorname{tr}(ABC)$ can differ from $\operatorname{tr}(BAC)$; see [[this counterexample|~59a53e89]].
- $\operatorname{tr}(AB - BA) = 0$. So [[AB − BA = I has no solution|~94d188c9]] over a field of characteristic $0$.
- For real matrices, $\operatorname{tr}(A^{\mathsf{T}} A) = \sum_{i,j} a_{ij}^2 \ge 0$, with equality only for $A = 0$.
- The trace of a [[nilpotent matrix|07BSPZPSMF]] over a field is $0$, and the trace of an [[idempotent matrix|0KCE8CG86P]] over a field is its rank; both use later theory.

### Common errors

- Taking $\operatorname{tr}(AB) = \operatorname{tr} A \operatorname{tr} B$.
- Using the cyclic property for all permutations of three or more factors.
- Reading $\operatorname{tr} A^{-1}$ as $1/\operatorname{tr} A$.

## Explanations

### L1 human

The trace adds up the numbers on the main diagonal of a square matrix.
For the identity matrix of order $n$, the trace is $n$.

### L2 human

The trace is a linear map from $M_n(R)$ to $R$.
It forgets most of the matrix, but it keeps the information that survives a change of basis.
The rule $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ is the key property, and it explains this invariance.

### L3 human

Up to a scalar, the trace is the only linear form $\varphi$ on $M_n(F)$ with $\varphi(AB) = \varphi(BA)$ for all $A$ and $B$.
The reason is that such a $\varphi$ vanishes on all commutators, and the commutators span the matrices of trace $0$.
The bilinear form $(A, B) \mapsto \operatorname{tr}(AB)$ is nondegenerate on $M_n(F)$, and it identifies $M_n(F)$ with its dual space.
