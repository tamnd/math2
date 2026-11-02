---
tag: NA44T2NZE2
kind: definition
name: Idempotent semiring
msc: ["16Y60", "06F05"]
defines: JCSAC9Y1CV
uses: [Q07RA7AMDE, 011C29Q1S1, 27ZPTJP9PP]
sources:
  - url: https://en.wikipedia.org/wiki/Semiring
---

## Definition

Let $(S, +, \cdot, 0, 1)$ be a [[semiring|Q07RA7AMDE]].
The semiring $S$ is *idempotent* if $a + a = a$ for all $a \in S$.

## Remarks

In an idempotent semiring, the relation $a \le b \iff a + b = b$ is a [[partial order|011C29Q1S1]].
For this order, $a + b$ is the least upper bound of $a$ and $b$, the element $0$ is the least element, and multiplication is monotone on both sides.
Example: the Boolean semiring $\set{0, 1}$ with $a + b = \max(a, b)$ and $a \cdot b = \min(a, b)$ is idempotent, since $\max(a, a) = a$.
Example: the subsets of the [[free monoid|27ZPTJP9PP]] $\Sigma^*$ on an alphabet $\Sigma$, with union as addition and concatenation as multiplication, form an idempotent semiring, since $L \cup L = L$.
Non-example: $\N$ with the usual operations is a semiring but is not idempotent, since $1 + 1 = 2 \ne 1$.
A ring is idempotent only if it is the zero ring, since $a + a = a$ gives $a = 0$.
Idempotent semirings are also called *dioids*.
