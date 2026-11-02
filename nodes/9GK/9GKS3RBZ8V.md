---
tag: 9GKS3RBZ8V
kind: statement
role: lemma
name: Δ-system lemma
msc: ["03E05", 05D05]
uses: [0SJ3RX9TXA, 0X55M9XET4, 0ZG61TFBES, N6TH42TD7F]
about: [0SJ3RX9TXA]
sources:
  - url: https://en.wikipedia.org/wiki/Sunflower_(mathematics)
---

## Statement

A family $\mathcal{A}$ of [[sets|0SJ3RX9TXA]] is a Δ-system if there is a set $r$, the root, with $a \cap b = r$ for all distinct $a, b \in \mathcal{A}$.
Let $\mathcal{A}$ be an [[uncountable|0X55M9XET4]] family of finite sets.
Then there is an uncountable subfamily $\mathcal{B} \subseteq \mathcal{A}$ that is a Δ-system.

## Remarks

The proof first passes to an uncountable subfamily whose sets all have the same size $n$.
This is possible since $\mathcal{A}$ is the union of [[countably|0ZG61TFBES]] many subfamilies, one for each size.
Then it inducts on $n$.
If some element lies in uncountably many sets, remove it, apply the induction hypothesis to those sets, and add it back to the root.
Otherwise each element lies in countably many sets, and a recursion of length $\omega_1$ picks uncountably many pairwise disjoint sets, a Δ-system with empty root.
Example: the family $\set{\set{0, \alpha} : 0 < \alpha < \omega_1}$ is a Δ-system with root $\set{0}$.
Finiteness matters: the countable ordinals $\alpha < \omega_1$ are countable sets, and they have no uncountable Δ-subsystem.
Indeed $\alpha \cap \beta = \min(\alpha, \beta)$, and this set is not the same for all pairs in an uncountable subfamily.
A general form: let $\kappa$ be an infinite cardinal and $\theta > \kappa$ a regular cardinal with $\abs{\alpha}^{<\kappa} < \theta$ for all $\alpha < \theta$.
Then each family of at least $\theta$ sets, each of size less than $\kappa$, has a Δ-subsystem of size $\theta$.
The finite analogue is the [[sunflower lemma|N6TH42TD7F]] of Erdős and Rado, where a Δ-system is called a sunflower.

## Explanations

### L1 human

A Δ-system is a family of sets that all overlap in exactly the same common part.
The lemma says that from uncountably many finite sets one can always pick uncountably many that form such a pattern.
So, after throwing some sets away, the overlaps become as simple as possible.

### L2 human

The Δ-system lemma is a standard tool in forcing.
It is the usual way to show that a forcing notion satisfies the countable chain condition, for example the forcing that adds Cohen reals.
Given uncountably many finite conditions, one finds uncountably many whose domains form a Δ-system, and then two of them agree on the root and are compatible.
