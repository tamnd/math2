---
tag: VZHVJ3V0EH
kind: definition
name: Boolean product
msc: [08B25, 08B26, "06E15"]
defines: CED4Q4TFCD
uses: [QJGPT2W0FT, 88WN3AD2VQ, WJ73XYBNE4, ZV38HA5PAQ, DQ4E55T3BW]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_algebras_canonically_defined
---

## Definition

Let $X$ be a [[Stone space|ZV38HA5PAQ]], that is, a compact Hausdorff totally disconnected space.
Let $(\mathbf{A}_x)_{x \in X}$ be a family of [[algebras|QJGPT2W0FT]] of the same signature.
A *Boolean product* of this family is a [[subdirect product|88WN3AD2VQ]] $\mathbf{A}$ of the [[direct product|WJ73XYBNE4]] $\prod_{x \in X} \mathbf{A}_x$ with these two properties:

1. for all $a, b \in A$, the set $\set{x \in X : a(x) = b(x)}$ is [[clopen|DQ4E55T3BW]] in $X$;
2. for all $a, b \in A$ and every clopen set $N \subseteq X$, the function $c$ with $c(x) = a(x)$ for $x \in N$ and $c(x) = b(x)$ for $x \notin N$ lies in $A$.

## Remarks

Clause 2 is called the patchwork property.
An algebra is said to be representable as a Boolean product when it is isomorphic to a Boolean product of some family.

Example: let $\mathbf{B}$ be a Boolean algebra with Stone space $X$, and let $\mathbf{2}$ be the two-element Boolean algebra.
The continuous maps $X \to \mathbf{2}$, with $\mathbf{2}$ discrete, form a Boolean product of copies of $\mathbf{2}$ isomorphic to $\mathbf{B}$.
Two continuous maps to a discrete space agree on a clopen set, and pasting two continuous maps along a clopen set gives a continuous map.

Non-example: let $X = \set{p, q}$ be discrete, and let $A = \set{(0, 0), (1, 1)}$ inside $\mathbf{2} \times \mathbf{2}$.
This is a subdirect product and satisfies clause 1, but pasting $(0, 0)$ on $\set{p}$ with $(1, 1)$ on $\set{q}$ gives $(0, 1) \notin A$, so clause 2 fails.
