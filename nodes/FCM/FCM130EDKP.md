---
tag: FCM130EDKP
kind: definition
name: Normalization property
msc: [68Q42, 03B40]
defines: GYMQHR3PXF
uses: [Y83TQF6V6A, 05J9NWX07X]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_form_(abstract_rewriting)
---

## Definition

Let $(A, \to)$ be an abstract [[rewriting system|Y83TQF6V6A]]: a set $A$ with a binary relation $\to$ on $A$.
Let $\twoheadrightarrow$ be the reflexive [[transitive closure|05J9NWX07X]] of $\to$.
An element $a \in A$ is a *normal form* if there is no $b \in A$ with $a \to b$.
An element $a$ *has a normal form* if $a \twoheadrightarrow b$ for some normal form $b$.

1. The system is *weakly normalizing* if every element of $A$ has a normal form.
2. The system is *strongly normalizing*, or *terminating*, if there is no infinite sequence $a_0 \to a_1 \to a_2 \to \cdots$ in $A$.

## Remarks

A strongly normalizing system is weakly normalizing.
Indeed, from any $a$, follow reduction steps as long as possible; the path is finite, so it ends in a normal form.

Example: let $A = \N$ and $n \to n - 1$ for $n \ge 1$.
Every path from $n$ has exactly $n$ steps, so the system is strongly normalizing, and $0$ is the only normal form.

Non-example: let $A = \set{a, b}$ with $a \to a$ and $a \to b$.
The element $a$ has the normal form $b$, so the system is weakly normalizing.
It is not strongly normalizing, because $a \to a \to a \to \cdots$ is infinite.

In the untyped lambda calculus with $\beta$-reduction, $(\lambda x.\, x\, x)(\lambda x.\, x\, x)$ has no normal form, so the system is not weakly normalizing.
