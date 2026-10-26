---
tag: 0RPDTWY2JS
kind: definition
name: Trace of a linear map
msc: [15A04, 15A15]
defines: 0KZDNGA561
uses: [07PTPSZPME, 0PTF1PTJK0]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a linear operator
---

## Definition

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]].
The *trace* of $T$ is
$$\tr T = \tr [T]_B,$$
the [[trace|0XC1RDBY7A]] of the matrix of $T$ in a basis $B$ of $V$.

## Remarks

The value does not depend on $B$: by the [[change of basis formula|0MQXVZEBMT]], another basis gives $P^{-1} [T]_B P$, and $\tr(P^{-1} A P) = \tr A$.
The trace is a linear map $\End_F(V) \to F$, and $\tr(ST) = \tr(TS)$.
The trace of the identity map of $V$ is $\dim V \cdot 1$.
A [[projection|033DA1WE8Y]] on a real or complex space has trace equal to its rank.

## Explanations

### L1 human

We define the trace of a linear map by its matrix in some basis.
Another basis gives a different matrix, but the trace stays the same.
So the trace belongs to the map, not to the basis.
