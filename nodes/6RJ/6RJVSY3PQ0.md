---
tag: 6RJVSY3PQ0
kind: definition
name: Atom
msc: [06A06, 06B05]
defines: TTVCTW6TNC
uses: [0QV2JS9RJ3, 0AANKKNHS4, 4HHDPZ4BDY]
sources:
  - url: https://en.wikipedia.org/wiki/Atom_(order_theory)
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]] with a [[least element|0AANKKNHS4]] $0$.
An *atom* of $P$ is an element $a \in P$ such that:

1. $0 < a$;
2. there is no $x \in P$ with $0 < x < a$.

## Remarks

Equivalently, $a$ is an atom when $a$ [[covers|4HHDPZ4BDY]] $0$, or when $a$ is a minimal element of $P \setminus \set{0}$.
Example: in $\N_{>0}$ ordered by divisibility, with least element $1$, every prime $p$ is an atom.
Indeed $1 \ne p$, and the only divisors of $p$ are $1$ and $p$, so nothing lies strictly between them.
Non-example: $4$ is not an atom of this poset, since $1 < 2 < 4$ in the divisibility order, so clause 2 fails.
The interval $[0, 1]$ with its usual order has no atoms, because $0 < a / 2 < a$ for each $a > 0$.
The dual notion, an element just below a greatest element, is a *coatom*.
