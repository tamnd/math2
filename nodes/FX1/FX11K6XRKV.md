---
tag: FX11K6XRKV
kind: definition
name: Quasifield
msc: ["12K99", "51A40", "51A35"]
defines: JQ22QH86DE
uses: [G5S1M9, 0EA5BTA0CX]
sources:
  - url: https://en.wikipedia.org/wiki/Quasifield
---

## Definition

Let $Q$ be a set with two binary operations $+$ and $\cdot$, and let $Q^* = Q \setminus \set{0}$.
The triple $(Q, +, \cdot)$ is a *(left) quasifield* if the following hold.

1. $(Q, +)$ is a [[group|G5S1M9]] with identity element $0$.
2. $a \cdot 0 = 0 \cdot a = 0$ for all $a \in Q$.
3. $(Q^*, \cdot)$ is a loop: there is $1 \in Q^*$ with $1 \cdot a = a \cdot 1 = a$ for all $a \in Q^*$, and for $a, b \in Q^*$ the equations $a \cdot x = b$ and $y \cdot a = b$ have unique solutions in $Q^*$.
4. $a \cdot (b + c) = a \cdot b + a \cdot c$ for all $a, b, c \in Q$.
5. For all $a, b, c \in Q$ with $a \ne b$, the equation $a \cdot x = b \cdot x + c$ has exactly one solution $x \in Q$.

A *right quasifield* is defined in the same way with $(b + c) \cdot a = b \cdot a + c \cdot a$ in clause 4 and $x \cdot a = x \cdot b + c$ in clause 5.

## Remarks

Example: every [[division ring|0EA5BTA0CX]] $D$ is a quasifield.
Clauses 1 to 4 are axioms of a division ring.
For clause 5, by distributivity $a x = b x + c$ is equivalent to $(a - b) x = c$, which has the unique solution $x = (a - b)^{-1} c$ since $a \ne b$.

Non-example: the integers $\Z$ with the usual operations.
Clause 3 fails, since $2 \cdot x = 1$ has no solution in $\Z \setminus \set{0}$.

One can prove that the additive group $(Q, +)$ of a quasifield is always abelian.
A quasifield in which both distributive laws hold is a [[semifield|AHH97EJ6VH]], and a quasifield whose multiplication is associative is a [[near-field|DSE72WQ5A2]] (on the matching side).
