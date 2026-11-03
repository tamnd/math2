---
tag: 611BTKNJE5
kind: definition
name: Quasigroup
msc: [20N05]
defines: ZJD31SPPFP
uses: [9689SFPVE9, 0M418FE7BB]
sources:
  - url: https://en.wikipedia.org/wiki/Quasigroup
---

## Definition

Let $Q$ be a set with a [[binary operation|0M418FE7BB]] $Q \times Q \to Q$, written $(a, b) \mapsto ab$, so that $Q$ is a [[magma|9689SFPVE9]].
The magma $Q$ is a *quasigroup* if for all $a, b \in Q$:

1. there is exactly one $x \in Q$ with $ax = b$;
2. there is exactly one $y \in Q$ with $ya = b$.

A *loop* is a quasigroup $Q$ with an element $e$ such that $ea = ae = a$ for all $a \in Q$.

## Remarks

Example: $\Z$ with $a \ast b = a - b$.
The equation $a - x = b$ has the unique solution $x = a - b$, and $y - a = b$ has the unique solution $y = a + b$.
It is not a loop: $0$ is a right identity, but $0 - a \ne a$ for $a \ne 0$.

Non-example: $\N = \set{0, 1, 2, \ldots}$ with addition.
The equation $1 + x = 0$ has no solution in $\N$, so clause 1 fails.

Clauses 1 and 2 say that left and right multiplication by any fixed element are bijections of $Q$.
One often writes the solutions as $x = a \backslash b$ and $y = b / a$, and views a quasigroup as an algebra with the three operations $\cdot$, $\backslash$ and $/$.
A nonempty associative quasigroup is a group.
