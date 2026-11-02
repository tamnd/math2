---
tag: 2E1R3BDDMK
kind: definition
name: Relational structure
msc: [08A02, 03C07]
defines: MJF9M19E3E
uses: [983GZBQYT4, WDVVEYD6AT, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_(mathematical_logic)
---

## Definition

Let $\sigma$ be a [[signature|WDVVEYD6AT]] with no function symbols and no constant symbols.
So each symbol $R \in \sigma$ is a relation symbol with an arity $n_R \ge 1$.
A *relational structure* of signature $\sigma$ is a [[structure|983GZBQYT4]] for $\sigma$.
Explicitly, it is a pair $(A, (R^A)_{R \in \sigma})$ where $A$ is a nonempty set and $R^A \subseteq A^{n_R}$ for each $R \in \sigma$.
Here $A^{n_R}$ is the [[Cartesian product|09CEDJYBKP]] of $n_R$ copies of $A$.

## Remarks

Example: a simple graph $(V, E)$, with $E \subseteq V^2$ the set of pairs $(u, v)$ such that $u$ and $v$ are adjacent, is a relational structure with one binary relation.

Non-example: a group $(G, \cdot)$ is not a relational structure, because its signature has a function symbol.
It can be turned into one by replacing $\cdot$ with its graph, the ternary relation $\set{(a, b, c) : a \cdot b = c}$.

Every structure can be encoded in this way as a relational structure.
Some authors allow an empty domain for relational structures.
