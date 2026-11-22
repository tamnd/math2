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

The trace is the cheapest number you can attach to a square matrix, and it still carries information that survives a change of basis.
For a [[square matrix|0JXZKX526R]] $A = (a_{ij})$ of order $n$ it is the sum of the diagonal entries,
$$\operatorname{tr} A = a_{11} + a_{22} + \cdots + a_{nn},$$
as in the [[formal definition|07PTPSZPME]].
The trace is [[linear|0GJWQZCPZM]], it does not change under the [[transpose|09E1RCZ7YT]], and it satisfies the [[cyclic property|0Y4NF1DRKD]] $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.
The number $\operatorname{tr}(A^{\mathsf{T}} B)$ is the sum of the products of matching entries, which gives an inner product on matrices.

## Motivation

Most of a matrix depends on the basis you choose, and the trace is one of the few things that does not.
By the cyclic property, $\operatorname{tr}(P^{-1} A P) = \operatorname{tr}(A P P^{-1}) = \operatorname{tr} A$, so [[similar matrices|0E89HQATM8]] have the same trace, and the [[trace of a linear map|0KZDNGA561]] is well defined.
Over $\mathbb{C}$ it is the [[sum of the eigenvalues|0NMXDCNNKR]] counted with multiplicity, and up to sign it is the coefficient of $x^{n-1}$ in the [[characteristic polynomial|0FRYPZ6D0X]].
For a $2 \times 2$ matrix that polynomial is $x^2 - (\operatorname{tr} A) x + \det A$.
The trace also turns the matrix product into the standard inner product on matrices, and it is the tool that rules out $AB - BA = I$.

## Notation

Books write $\operatorname{tr} A$, $\operatorname{Tr} A$, $\operatorname{trace} A$ or $\operatorname{Sp} A$, the last from the German word *Spur*.
In Mathlib, `Matrix.trace A` is the trace.
It is defined for square matrices indexed by any finite type, and the order of the indices plays no part.

## Remarks

### A first computation

The matrix with rows $(1, 2, 3)$, $(4, 5, 6)$ and $(7, 8, 9)$ has trace $1 + 5 + 9 = 15$.
For $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ the two products differ,
$$AB = \begin{pmatrix} 2 & 1 \\ 4 & 3 \end{pmatrix}, \qquad BA = \begin{pmatrix} 3 & 4 \\ 1 & 2 \end{pmatrix},$$
but both have trace $5$, as the cyclic property predicts.

### What it is not

A $2 \times 3$ matrix has no trace, because the trace is defined only for square matrices.
The trace is not multiplicative: [[the trace is not a ring homomorphism|5F9NN7QTXA]], and already $\operatorname{tr}(I_2 I_2) = 2$ while $\operatorname{tr} I_2 \operatorname{tr} I_2 = 4$.
It does not determine the matrix either, since $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 2 & 5 \\ 0 & 0 \end{pmatrix}$ both have trace $2$.

### The rules you can use

For $n \times n$ matrices $A$ and $B$ over a commutative ring $R$ and $c \in R$:

- $\operatorname{tr}(A + B) = \operatorname{tr} A + \operatorname{tr} B$ and $\operatorname{tr}(cA) = c \operatorname{tr} A$, by [[linearity|0GJWQZCPZM]].
- $\operatorname{tr}(A^{\mathsf{T}}) = \operatorname{tr} A$, since the transpose keeps the diagonal; see [[this statement|09E1RCZ7YT]].
- $\operatorname{tr}(AB) = \operatorname{tr}(BA)$, even for an $m \times n$ matrix $A$ and an $n \times m$ matrix $B$, by the [[cyclic property|0Y4NF1DRKD]].
- $\operatorname{tr}(ABC) = \operatorname{tr}(BCA) = \operatorname{tr}(CAB)$, the cyclic shifts.
- $\operatorname{tr}(AB - BA) = 0$, so [[AB − BA = I has no solution|E2P5TNE0G9]] over a field of characteristic $0$.

Later theory adds that a [[nilpotent matrix|07BSPZPSMF]] over a field has trace $0$, and that an [[idempotent matrix|0KCE8CG86P]] over $\mathbb{R}$ or $\mathbb{C}$ has trace equal to its rank.

### The trace as an inner product

The diagonal entry $(A^{\mathsf{T}} B)_{jj}$ is $\sum_i a_{ij} b_{ij}$, so
$$\operatorname{tr}(A^{\mathsf{T}} B) = \sum_{i,j} a_{ij} b_{ij},$$
the dot product of $A$ and $B$ read as vectors with $n^2$ entries.
[[The Frobenius inner product|Z88VRHAS1X]] computes this for two $2 \times 2$ matrices.
With $B = A$ it gives the sum of the squares of the entries, as in [[the trace of AᵀA|6VBAP0MZQN]], so for real $A$ the number $\operatorname{tr}(A^{\mathsf{T}} A)$ is $0$ only when $A = 0$.

### Watch out

The cyclic property allows cyclic shifts, not all orders.
[[This counterexample|GMT2VT9841]] gives $\operatorname{tr}(ABC) = 1$ and $\operatorname{tr}(BAC) = 0$.
Also $\operatorname{tr}(A^{-1})$ is not $1 / \operatorname{tr} A$: for $A = \operatorname{diag}(1, 2)$ you get $\operatorname{tr}(A^{-1}) = 1 + \tfrac12 = \tfrac32$, while $1 / \operatorname{tr} A = \tfrac13$.

### Try it

First, find the trace of the matrix with rows $(2, 0, 1)$, $(3, -1, 4)$ and $(5, 6, 7)$.
It is $2 - 1 + 7 = 8$.

Second, compute $\operatorname{tr}(A^{\mathsf{T}} A)$ for $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ without multiplying.
It is the sum of the squares of the entries, $1 + 1 + 0 + 1 = 3$.

## Explanations

### L1 human

The trace adds up the numbers on the main diagonal of a square matrix.
For the identity matrix of order $n$ you add $n$ ones, so the trace is $n$.
The numbers off the diagonal do not count at all.

### L2 human

The trace is a linear map from $M_n(R)$ to $R$, and the rule $\operatorname{tr}(AB) = \operatorname{tr}(BA)$ is the property that matters most.
It gives $\operatorname{tr}(P^{-1} A P) = \operatorname{tr} A$, so the trace is the same in every basis.
Here is a check with $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.
Its characteristic polynomial is
$$\det(xI - A) = (x - 1)(x - 4) - 6 = x^2 - 5x - 2,$$
with roots $\tfrac{5 \pm \sqrt{33}}{2}$, and these add up to $5 = \operatorname{tr} A$.
Any matrix similar to $A$ has the same characteristic polynomial, so the same trace.

### L3 human

Over a field $F$, the trace is up to a scalar the only linear form $\varphi$ on $M_n(F)$ with $\varphi(AB) = \varphi(BA)$ for all $A$ and $B$.
Such a $\varphi$ vanishes on all commutators, and the commutators span the matrices of trace $0$, since $E_{ij} = E_{ii} E_{ij} - E_{ij} E_{ii}$ for $i \neq j$ and $E_{ii} - E_{jj} = E_{ij} E_{ji} - E_{ji} E_{ij}$.
The bilinear form $(A, B) \mapsto \operatorname{tr}(AB)$ is nondegenerate on $M_n(F)$, because $\operatorname{tr}(E_{ij} E_{kl})$ is $1$ when $j = k$ and $i = l$ and $0$ otherwise, so it identifies $M_n(F)$ with its dual space.
The matrices of trace $0$ form the Lie algebra $\mathfrak{sl}_n(F)$.
