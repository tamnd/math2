---
tag: MZW52JVTBX
kind: definition
name: Infinitary operation
msc: [08A65]
defines: WFVC137TYB
uses: [MSXX2P86CY, 0EPAT51DXQ, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Arity
---

## Definition

Let $A$ be a set and let $I$ be an infinite set.
Write $A^I$ for the [[Cartesian product|09CEDJYBKP]] of copies of $A$ indexed by $I$, the set of families $(a_i)_{i \in I}$ of elements of $A$.
An *infinitary operation* on $A$ with index set $I$ is a [[function|0EPAT51DXQ]] $f \colon A^I \to A$.
Its [[arity|MSXX2P86CY]] is the cardinal $\abs{I}$.

## Remarks

Example: on $[0, 1]$, the map $s \colon [0,1]^{\N} \to [0, 1]$, $s((x_n)_{n \in \N}) = \sup_n x_n$, is an infinitary operation of arity $\aleph_0$.
Each sequence in $[0, 1]$ is bounded above by $1$, so its supremum exists and lies in $[0, 1]$.

Non-example: the map $(x_n)_{n \in \N} \mapsto \sum_{n} x_n$ is not an infinitary operation on $\R$, because it is not defined on the whole of $\R^{\N}$: the series $\sum_n 1$ diverges.

Some authors index the arguments by an infinite ordinal $\alpha$ instead of an arbitrary set $I$, and call $\alpha$ the arity.
