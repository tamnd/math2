---
tag: CXV1969XGB
kind: definition
name: Topological ring
msc: [16W80, 54H13]
defines: TSF8RZDD5B
uses: [0894J980RK, 0CNQXVBHCX, 0SY9ECQ19Q, 0Z57EC6YX3]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_ring
---

## Definition

Let $R$ be a [[ring|0894J980RK]] and let $\mathcal{T}$ be a [[topology|0CNQXVBHCX]] on the set $R$.
Give $R \times R$ the [[product topology|0Z57EC6YX3]].
The pair $(R, \mathcal{T})$ is a *topological ring* if the following maps are [[continuous|0SY9ECQ19Q]]:

1. addition $R \times R \to R$, $(a, b) \mapsto a + b$;
2. negation $R \to R$, $a \mapsto -a$;
3. multiplication $R \times R \to R$, $(a, b) \mapsto ab$.

## Remarks

Clauses 1 and 2 say that $(R, +)$ is a topological group.
Example: $\R$ with the usual topology; continuity of $(a, b) \mapsto ab$ follows from $ab - a'b' = a(b - b') + (a - a')b'$.
Example: any ring with the discrete topology, since every map from a discrete space is continuous.
Example: for an ideal $I$ of a commutative ring $R$, the $I$-adic topology, with the ideals $I^n$ as a base of neighbourhoods of $0$.
Non-example: $\R$ with the lower limit topology, whose base is the intervals $[a, b)$.
Negation is not continuous: the preimage of the open set $[0, 1)$ is $(-1, 0]$, which is not open there.
