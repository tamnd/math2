---
tag: 2BJE1ABGDJ
kind: definition
name: Factor congruence
msc: [08A30, 08B25]
defines: 6N268PHKQA
uses: [QJGPT2W0FT, DCSXXT4SER, REE07CSXHR, WJ73XYBNE4]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence_relation
---

## Definition

Let $\mathbf{A}$ be an [[algebra|QJGPT2W0FT]] with universe $A$.
Let $\Delta_A = \set{(a, a) : a \in A}$ and $\nabla_A = A \times A$.
A [[congruence|DCSXXT4SER]] $\theta$ on $\mathbf{A}$ is a *factor congruence* when there is a congruence $\theta^*$ on $\mathbf{A}$ such that:

1. $\theta \cap \theta^* = \Delta_A$;
2. $\theta \circ \theta^* = \nabla_A$, where $(a, c) \in \theta \circ \theta^*$ means that $(a, b) \in \theta$ and $(b, c) \in \theta^*$ for some $b \in A$.

Then $\theta$ and $\theta^*$ are called a pair of complementary factor congruences.

## Remarks

For such a pair, the map $a \mapsto (a/\theta, a/\theta^*)$ is an isomorphism from $\mathbf{A}$ onto the [[direct product|WJ73XYBNE4]] $\mathbf{A}/\theta \times \mathbf{A}/\theta^*$.
Conversely, if $\mathbf{A} = \mathbf{B} \times \mathbf{C}$, the kernels of the two projections are complementary factor congruences.
The conditions say that $\theta$ and $\theta^*$ are complements in the [[congruence lattice|REE07CSXHR]] and that they permute.

Example: on the group $\Z/6\Z$, take $\theta$ to be congruence modulo $2$ and $\theta^*$ congruence modulo $3$.
An element congruent to $0$ modulo $2$ and modulo $3$ is $0$, so clause 1 holds.
For any $a, c$ there is $b$ with $b \equiv a \pmod 2$ and $b \equiv c \pmod 3$, by the Chinese remainder theorem, so clause 2 holds.

Non-example: on $\Z/4\Z$, congruence modulo $2$ is not a factor congruence.
The congruences of $\Z/4\Z$ are $\Delta$, congruence modulo $2$, and $\nabla$.
Only $\theta^* = \Delta$ satisfies clause 1, and then $\theta \circ \theta^* = \theta \ne \nabla$.

The congruences $\Delta_A$ and $\nabla_A$ are always factor congruences, complementary to each other.
