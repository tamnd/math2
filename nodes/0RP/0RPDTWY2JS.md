---
tag: 0RPDTWY2JS
kind: definition
name: Trace of a linear map
msc: ["15A04", "15A15"]
topics: [S6559D61BP]
audience: ug1
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

## Notation

Here $[T]_B$ uses the basis $B$ for both the domain and the codomain.
Other notations are $\operatorname{Tr} T$ and $\operatorname{trace} T$.

## Remarks

The value does not depend on $B$, by the [[theorem on the independence of the basis|0WCPH5Z7FA]].
Another basis gives $P^{-1} [T]_B P$ by the [[change of basis formula|0MQXVZEBMT]], and $\tr(P^{-1} A P) = \tr A$.
The trace is a linear map $\End_F(V) \to F$, and $\tr(ST) = \tr(TS)$.
The trace of the identity map of $V$ is $\dim V \cdot 1$.
A [[projection|033DA1WE8Y]] $P$ has $\tr P = (\rank P) \cdot 1_F$, by the [[theorem on the trace of a projection|~f21ebbcb]].
So $\tr P = \rank P$ in characteristic $0$, but not in general in characteristic $p$.

## Explanations

### L1 human

We define the trace of a linear map by its matrix in some basis.
Another basis gives a different matrix, but the trace stays the same.
So the trace belongs to the map, not to the basis.

### L2 human

The definition needs the same basis on both sides of $[T]_B$.
With two different bases, the diagonal sum of the matrix can change.
