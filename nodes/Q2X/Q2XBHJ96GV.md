---
tag: Q2XBHJ96GV
kind: statement
role: theorem
name: Incomparability theorem
msc: [13B21]
uses: [B7X0KFY1S1, 00MHHZ9SNE, 5GCANV7337]
about: [B7X0KFY1S1, 00MHHZ9SNE]
sources:
  - url: https://en.wikipedia.org/wiki/Going_up_and_going_down
---

## Statement

Let $A \subseteq B$ be commutative rings with $B$ [[integral over|B7X0KFY1S1]] $A$.
Let $\mathfrak{q} \subseteq \mathfrak{q}'$ be [[prime ideals|00MHHZ9SNE]] of $B$ with $\mathfrak{q} \cap A = \mathfrak{q}' \cap A$.
Then $\mathfrak{q} = \mathfrak{q}'$.

## Remarks

Let $\mathfrak{p} = \mathfrak{q} \cap A$ and localize at $\mathfrak{p}$.
Then $B_{\mathfrak{p}}/\mathfrak{q} B_{\mathfrak{p}}$ is a domain integral over the field $A_{\mathfrak{p}}/\mathfrak{p} A_{\mathfrak{p}}$, so it is a field by [[integral extensions of fields|5GCANV7337]].
Hence $\mathfrak{q} B_{\mathfrak{p}}$ is maximal, and the larger prime $\mathfrak{q}' B_{\mathfrak{p}}$ must equal it, which gives $\mathfrak{q} = \mathfrak{q}'$.

A consequence: a prime $\mathfrak{q}$ of $B$ is maximal if and only if $\mathfrak{q} \cap A$ is maximal in $A$.

Example: in $\Z \subseteq \Z[i]$, the primes $0 \subsetneq (2 + i)$ contract to $0$ and $5\Z$, which differ, as the theorem demands.

Integrality is needed: for $k[x] \subseteq k[x, y]$, the primes $0 \subsetneq (y)$ both contract to $0$.

## Explanations

### L1 human

Over a fixed prime of the small ring there may be several primes of the big ring, but none of them lies inside another.
In geometry: the fibres of an integral map have dimension zero.

### L2 human

Incomparability says that chains of primes cannot get longer when one passes to an integral extension.
With [[going-up|GHKYR5PBQC]] it gives $\dim B = \dim A$.
It is also the reason that the maximal ideals of $B$ are exactly the primes over maximal ideals of $A$.
