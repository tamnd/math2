---
tag: FQXWHS5QT2
kind: definition
name: Orthocomplemented lattice
msc: [06C15, 81P10]
defines: J7KN14DYV3
uses: [72V1Z82M5F, ZT47BK9Y6K]
sources:
  - url: https://en.wikipedia.org/wiki/Complemented_lattice
---

## Definition

Let $L$ be a [[bounded lattice|72V1Z82M5F]] with least element $0$ and greatest element $1$.
An *orthocomplementation* on $L$ is a map $a \mapsto a^\perp$ from $L$ to $L$ such that for all $a, b \in L$:

1. $a \wedge a^\perp = 0$ and $a \vee a^\perp = 1$, so $a^\perp$ is a [[complement|ZT47BK9Y6K]] of $a$;
2. $(a^\perp)^\perp = a$;
3. if $a \le b$, then $b^\perp \le a^\perp$.

An *orthocomplemented lattice*, or *ortholattice*, is a bounded lattice together with an orthocomplementation.

## Remarks

From clauses 2 and 3 follow the De Morgan laws $(a \vee b)^\perp = a^\perp \wedge b^\perp$ and $(a \wedge b)^\perp = a^\perp \vee b^\perp$.

Example: the lattice of closed linear subspaces of a [[Hilbert space|HM2HHE3J51]] $H$, with $M^\perp$ the [[orthogonal complement|0XJXTBCB2T]] of $M$.
Here $M \cap M^\perp = \set{0}$, the closed span of $M$ and $M^\perp$ is $H$, $M^{\perp\perp} = M$ for closed $M$, and $M \subseteq N$ implies $N^\perp \subseteq M^\perp$.

Non-example: the [[diamond lattice M3|JQ6FJH2TP8]] with middle elements $a, b, c$ and the map $a \mapsto b$, $b \mapsto c$, $c \mapsto a$, $0 \mapsto 1$, $1 \mapsto 0$.
Each image is a complement, but $(a^\perp)^\perp = c \ne a$, so clause 2 fails.
