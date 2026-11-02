---
tag: H3W6ZPAJJV
kind: definition
name: Congruence relation
msc: [08A30]
defines: DCSXXT4SER
uses: [QJGPT2W0FT, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence_relation
---

## Definition

Let $\mathbf{A}$ be an [[algebra|QJGPT2W0FT]] with universe $A$.
A *congruence* on $\mathbf{A}$ is a relation $\theta \subseteq A \times A$ such that:

1. $\theta$ is an [[equivalence relation|0G8VEZ3WTK]] on $A$;
2. for each fundamental operation $f$ of $\mathbf{A}$, of arity $n$, and all $a_1, b_1, \dots, a_n, b_n \in A$ with $(a_i, b_i) \in \theta$ for each $i$, also $(f(a_1, \dots, a_n), f(b_1, \dots, b_n)) \in \theta$.

## Remarks

Clause 2 is called the compatibility property.
One often writes $a \mathrel{\theta} b$ or $a \equiv b \pmod{\theta}$ for $(a, b) \in \theta$.
Every algebra has the trivial congruences $\Delta_A = \set{(a, a) : a \in A}$ and $\nabla_A = A \times A$.

Example: on the ring $(\Z, +, \cdot, -, 0, 1)$, fix $n \ge 1$ and let $a \mathrel{\theta} b$ when $n$ divides $a - b$.
If $n$ divides $a - a'$ and $b - b'$, it divides $(a + b) - (a' + b')$, $-a - (-a')$ and $ab - a'b' = a(b - b') + (a - a')b'$.

Non-example: on the group $(\Z, +, -, 0)$, let $a \mathrel{\theta} b$ when $a$ and $b$ are both positive, both negative, or both $0$.
This is an equivalence relation, but $1 \mathrel{\theta} 2$ while $1 + (-1) = 0$ and $2 + (-1) = 1$ are not related.

In a group, the congruences correspond to the normal subgroups via $\theta \mapsto \set{a : a \mathrel{\theta} e}$.
In a ring, they correspond to the two-sided ideals via $\theta \mapsto \set{a : a \mathrel{\theta} 0}$.
