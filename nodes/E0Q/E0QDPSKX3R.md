---
tag: E0QDPSKX3R
kind: definition
name: Ternary operation
msc: [08A02, 08A62]
defines: WC47MFR6GW
uses: [EJ8YJVM9BW, 0EPAT51DXQ, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Ternary_operation
---

## Definition

Let $A$ be a set and let $A^3$ be the [[Cartesian product|09CEDJYBKP]] $A \times A \times A$.
A *ternary operation* on $A$ is a [[finitary operation|EJ8YJVM9BW]] of arity $3$, that is, a [[function|0EPAT51DXQ]] $f \colon A^3 \to A$.

## Remarks

Example: on $\R$, the map $m(x, y, z)$ that returns the middle value of $x, y, z$ is a ternary operation.
It is defined for every triple and its value is one of $x, y, z$, so it lies in $\R$.
It satisfies $m(x, x, y) = m(x, y, x) = m(y, x, x) = x$.

Non-example: the map $(x, y, z) \mapsto x / (y - z)$ is not a ternary operation on $\R$, because it is not defined when $y = z$.

A ternary operation is usually written in prefix form $f(x, y, z)$, since there is no standard infix notation for three arguments.
