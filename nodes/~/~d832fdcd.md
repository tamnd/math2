---
tag: ~d832fdcd
kind: definition
name: Orthogonal complement
msc: [15A63, 46C05]
defines: ~dc8d80e7
uses: [~28284caf, ~f558a11d]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Inner product spaces
---

## Definition

Let $V$ be an inner product space over $\R$ or $\C$, and let $W$ be a [[subspace|~92144797]] of $V$.
The *orthogonal complement* of $W$ is
$$W^\perp = \{v \in V : \langle v, w \rangle = 0 \text{ for all } w \in W\}.$$

## Remarks

$W^\perp$ is a subspace of $V$, and $W \cap W^\perp = 0$.
In $\R^3$ with the dot product, the orthogonal complement of a plane through $0$ is its normal line.
For a real $m \times n$ matrix $A$, the null space of $A$ is the orthogonal complement of the row space of $A$ in $\R^n$.
In finite dimensions, $V = W \oplus W^\perp$, see [[the orthogonal decomposition|~966aedb4]].

## Explanations

### L1 human

The orthogonal complement collects all vectors that are perpendicular to a subspace.
The complement of a line in $\R^3$ is a plane, and the complement of a plane is a line.
A subspace and its complement together fill the space.
