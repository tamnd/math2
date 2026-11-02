---
tag: K2KQFX4GVF
kind: definition
name: Directed-complete partial order
msc: [06B35, 06A06, 68Q55]
defines: 7TSXP95QN6
uses: [0QV2JS9RJ3, D9RY4667K6, 0R3H5PANRQ]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_partial_order
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
It is a *directed-complete partial order*, or *dcpo*, if every [[directed subset|D9RY4667K6]] $D \subseteq P$ has a [[supremum|0R3H5PANRQ]] $\bigvee D$ in $P$.
Here $D$ is directed if it is nonempty and every two elements of $D$ have an upper bound in $D$.

## Remarks

A dcpo with a least element $\bot$ is called pointed, and is often simply called a cpo.
Example: the set of partial functions from $\N$ to $\N$, ordered by inclusion of graphs.
If $D$ is a directed family, any two members agree where both are defined, so $\bigcup D$ is again a partial function and is the supremum.
Non-example: $\N$ with its usual order is not a dcpo, because $\N$ itself is directed and has no upper bound.
Every finite poset is a dcpo, since a finite directed set has a greatest element.
Equivalently, by a theorem that uses the axiom of choice, a poset is a dcpo if and only if every nonempty chain has a supremum.
