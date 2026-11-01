---
tag: 55B7ZCDKS9
kind: definition
name: Matroid rank
msc: [05B35]
defines: SYRCTH853H
uses: [PX31ZNYS3Z, QTSQR7130G]
sources:
  - url: https://en.wikipedia.org/wiki/Matroid_rank
---

## Definition

Let $M = (E, \mathcal{I})$ be a [[matroid|PX31ZNYS3Z]].
The *rank function* of $M$ is the map $r \colon \mathcal{P}(E) \to \set{0, 1, 2, \dots}$ given by
$$r(A) = \max \set{\abs{I} : I \in \mathcal{I}, \ I \subseteq A}.$$
The *rank* of $M$ is $r(E)$.

## Remarks

The maximum exists because $\emptyset \subseteq A$ is independent.
All maximal independent subsets of $A$ have $r(A)$ elements, and $r(E)$ is the size of every [[basis|QTSQR7130G]] of $M$.
A set $A$ is independent if and only if $r(A) = \abs{A}$.

The rank function satisfies, for all $A, B \subseteq E$:

1. $0 \le r(A) \le \abs{A}$.
2. If $A \subseteq B$, then $r(A) \le r(B)$.
3. $r(A \cup B) + r(A \cap B) \le r(A) + r(B)$ (submodularity).

Conversely, every function with these three properties is the rank function of exactly one matroid.

Example: for the matroid of the columns of a matrix, $r(A)$ is the [[rank|0ZC9YTXZRY]] of the submatrix formed by the columns in $A$.
For the graphic matroid of a graph with vertex set $V$, $r(A) = \abs{V} - c(A)$, where $c(A)$ is the number of connected components of the graph $(V, A)$.

Non-example: in the uniform matroid $U_{2,3}$, whose independent sets are the subsets of $\set{1, 2, 3}$ with at most $2$ elements, the size function $A \mapsto \abs{A}$ is not the rank function, because $r(\set{1, 2, 3}) = 2 \ne 3$.
