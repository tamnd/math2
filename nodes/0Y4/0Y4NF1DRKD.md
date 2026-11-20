---
tag: 0Y4NF1DRKD
kind: statement
role: theorem
name: Cyclic property of the trace
msc: ["15A15"]
topics: [Y1ESNQ2V52]
audience: ug1
about: [0XC1RDBY7A]
uses: [07PTPSZPME, 076JGP6R3T]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.trace_mul_comm
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a product
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Cyclic property
---

## Statement

Let $R$ be a commutative ring.
Let $A$ be an $m \times n$ matrix and $B$ an $n \times m$ matrix over $R$.
Then $\operatorname{tr}(AB) = \operatorname{tr}(BA)$, where $\operatorname{tr}$ is the [[trace|07PTPSZPME]].

## Remarks

### Why each hypothesis is needed

- Commutativity of $R$ is necessary. Over the quaternions, the $1 \times 1$ matrices $(i)$ and $(j)$ give $\operatorname{tr}(ij) = k$ and $\operatorname{tr}(ji) = -k$.
- The sizes make $AB$ ($m \times m$) and $BA$ ($n \times n$) square. They need not be equal: for a column $x$ and a row $y^{\mathsf{T}}$, $\operatorname{tr}(x y^{\mathsf{T}}) = y^{\mathsf{T}} x$.

### Consequences

- Cyclic shifts: $\operatorname{tr}(A_1 A_2 \cdots A_k) = \operatorname{tr}(A_2 \cdots A_k A_1)$. Apply the theorem to $A_1$ and $A_2 \cdots A_k$.
- So $\operatorname{tr}(ABC) = \operatorname{tr}(BCA) = \operatorname{tr}(CAB)$. Other orders can give other values, as [[this counterexample|~59a53e89]] shows.
- $\operatorname{tr}(P^{-1} A P) = \operatorname{tr}(A P P^{-1}) = \operatorname{tr} A$ for an [[invertible|0EB9N0S33C]] $P$. So [[similar matrices|0E89HQATM8]] have the same trace.
- $\operatorname{tr}(AB - BA) = 0$ for square $A$ and $B$. Hence [[AB − BA = I has no solution|~94d188c9]] over a field of characteristic $0$.

### Generalizations

- For linear maps $f : V \to W$ and $g : W \to V$ between finite-dimensional spaces, $\operatorname{tr}(g \circ f) = \operatorname{tr}(f \circ g)$; see the [[trace of a linear map|0KZDNGA561]].
- Over a field, $AB$ and $BA$ have the same nonzero eigenvalues with the same multiplicities, a later result that implies the theorem.

## Explanations

### L1 human

Although $AB$ and $BA$ are usually different matrices, they have the same trace.
Each diagonal sum adds the same products $a_{ij} b_{ji}$, only in another order.

### L2 human

The trace of $AB$ is the sum of $a_{ij} b_{ji}$ over all $i$ and $j$.
This expression is symmetric in the roles of $A$ and $B$.
This fact makes the trace a property of a linear map, not of the basis that we choose.
