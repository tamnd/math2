---
tag: J4SZVFBHS5
kind: statement
role: proposition
name: Orthogonal complement of the column space is the null space of the transpose
msc: ["15A03", "15A18"]
topics: [S6559D61BP]
audience: ug1
about: [03AJKXH1AV, 0PQ2GGY1QV]
uses: [03AJKXH1AV, 0PQ2GGY1QV, 0W809K6AW0, 0XJXTBCB2T]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-2.xml#L878
    locator: src/section6-2.xml:878
---

## Statement

Let $A$ be an $m \times n$ real matrix, with [[transpose|0W809K6AW0]] $A^\top$.
Use the standard dot product on $\R^m$.
Then the [[orthogonal complement|0XJXTBCB2T]] of the [[column space|03AJKXH1AV]] of $A$ is the [[null space|0PQ2GGY1QV]] of $A^\top$:
$$\operatorname{Col}(A)^\perp = \operatorname{Nul}(A^\top).$$

## Remarks

### Why each hypothesis is needed

The equality of sets holds over every field, with $\operatorname{Col}(A)^\perp$ read as the set of $y$ with $y^\top b = 0$ for all $b \in \operatorname{Col}(A)$.
The name "orthogonal complement" needs a positive definite product, such as the real dot product.
Over $\C$ with the Hermitian product, the correct statement uses the conjugate transpose: $\operatorname{Col}(A)^\perp = \operatorname{Nul}(A^*)$.

### Consequences

- $Ax = b$ has a solution if and only if $b \perp \operatorname{Nul}(A^\top)$. This is the [[Fredholm alternative|4HH8C9V8JQ]].
- $\R^m = \operatorname{Col}(A) \oplus \operatorname{Nul}(A^\top)$, part of the [[theorem on the four fundamental subspaces|~c3d8720b]].

### Converse

Applied to $A^\top$, the statement gives $\operatorname{Row}(A)^\perp = \operatorname{Nul}(A)$.

### Generalizations

For a linear map $T \colon V \to W$ between finite-dimensional inner product spaces, $(\im T)^\perp = \ker T^*$, where $T^*$ is the adjoint.

## History

The result is part of the theory of the four fundamental subspaces in Strang's textbooks.

## Explanations

### L1 human

A vector $y$ is orthogonal to the column space exactly when it is orthogonal to each column of $A$.
The dot product of $y$ with column $j$ of $A$ is entry $j$ of $A^\top y$.
So $y$ is orthogonal to all columns exactly when $A^\top y = 0$.

### L2 human

The left null space of $A$ is the set of normal vectors to the column space.
For a $3 \times 2$ matrix of rank $2$, the column space is a plane and the left null space is its normal line.

### L3 human

Over any field, the left null space is the annihilator of the column space under the standard pairing $(y, b) \mapsto y^\top b$.
Over $\R$ this pairing is positive definite, so the annihilator is a complement of the column space.
