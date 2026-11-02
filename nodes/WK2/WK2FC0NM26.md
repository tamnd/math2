---
tag: WK2FC0NM26
kind: definition
name: Commuting elements
msc: [08A02, 20A05]
defines: YJRBCWQV6B
uses: [0M418FE7BB]
sources:
  - url: https://en.wikipedia.org/wiki/Commutative_property
---

## Definition

Let $\ast$ be a [[binary operation|0M418FE7BB]] on a set $S$ and let $a, b \in S$.
The elements $a$ and $b$ *commute* if $a \ast b = b \ast a$.

## Remarks

Example: in the set of $2 \times 2$ real matrices with matrix multiplication, every matrix $A$ commutes with $2A$, because $A(2A) = 2A^2 = (2A)A$.

Non-example: the matrices
$$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$$
do not commute, because $AB = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ while $BA = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.

The relation "commutes with" is reflexive and symmetric but not transitive in general.
In the example, $A$ commutes with the identity matrix $I$ and $I$ commutes with $B$, but $A$ and $B$ do not commute.
The operation $\ast$ is commutative if and only if every two elements of $S$ commute.
