---
tag: GRMT65QJAY
kind: definition
name: Atomic lattice
msc: [06B05]
defines: 5SE8EMSDNY
uses: [WH4SFAACAS, 0AANKKNHS4, TTVCTW6TNC]
sources:
  - url: https://en.wikipedia.org/wiki/Atom_(order_theory)
---

## Definition

Let $L$ be a [[lattice|WH4SFAACAS]] with a [[least element|0AANKKNHS4]] $0$.
$L$ is *atomic* if for every $b \in L$ with $b \ne 0$ there is an [[atom|TTVCTW6TNC]] $a$ of $L$ with $a \le b$.

## Remarks

The same definition applies to any partially ordered set with a least element.
Example: every finite lattice $L$ is atomic.
For $b \ne 0$, the set $\set{x \in L : 0 < x \le b}$ is finite and nonempty, so it has a minimal element, and a minimal element of this set is an atom.
Example: $\N_{>0}$ ordered by divisibility is atomic, since every $n > 1$ has a prime divisor.
Non-example: the chain $[0, 1]$ with its usual order is a lattice with least element $0$ and no atoms, so the condition fails for $b = 1$.
