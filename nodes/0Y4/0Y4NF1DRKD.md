---
tag: 0Y4NF1DRKD
kind: statement
role: proposition
name: Trace of a product is symmetric
msc: [15A15]
uses: [07PTPSZPME, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a product
---

## Statement

Let $R$ be a commutative ring.
Let $A$ be an $m \times n$ matrix and $B$ an $n \times m$ matrix over $R$.
Then $\tr(AB) = \tr(BA)$, where $\tr$ is the [[trace|0XC1RDBY7A]].

## Remarks

Both sides equal $\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} b_{ji}$.
The matrices $AB$ and $BA$ can have different sizes, and the identity still holds.
A consequence is $\tr(P^{-1} A P) = \tr A$, so similar matrices have the same trace.
For three matrices, only cyclic permutations are allowed in general: $\tr(ABC) = \tr(BCA)$, but $\tr(ABC)$ can differ from $\tr(BAC)$.

## Explanations

### L1 human

Although $AB$ and $BA$ are usually different matrices, they have the same trace.
Each diagonal sum adds the same products $a_{ij} b_{ji}$, only in another order.
This fact makes the trace a property of a linear map, not of the basis that we choose.
