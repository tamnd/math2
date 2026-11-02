---
tag: BBF9SCQRM9
kind: definition
name: Semitopological group
msc: [22A05, 54H11]
defines: 5WGMRS4JSE
uses: [G5S1M9, 0CQHFPGJ45, 0VGFHTM75Y, 92700QAB5Y]
sources:
  - url: https://en.wikipedia.org/wiki/Semitopological_group
---

## Definition

A *semitopological group* is a [[group|G5S1M9]] $G$ together with a [[topology|0CQHFPGJ45]] on $G$ such that the multiplication $G \times G \to G$ is separately continuous.
That is, for each $a \in G$ the left translation $x \mapsto ax$ and the right translation $x \mapsto xa$ are [[continuous|0VGFHTM75Y]] maps $G \to G$.

## Remarks

Example: $(\Z, +)$ with the cofinite topology.
Each translation $x \mapsto x + a$ is a bijection, so it maps cofinite sets to cofinite sets and is continuous.
This group is not a [[topological group|92700QAB5Y]]: every nonempty basic open set $U \times V$ of $\Z \times \Z$ contains a pair $(x, -x)$, so the preimage of $\Z \setminus \set{0}$ under addition is not open.
Non-example: the multiplicative group $\R \setminus \set{0}$ with the topology whose open sets are $\emptyset$, the whole set, and the sets $(a, \infty) \setminus \set{0}$ for $a \in \R$.
The left translation $x \mapsto (-1) x$ is not continuous: the preimage of the open set $(1, \infty)$ is $(-\infty, -1)$, which is not open.
Every topological group is a semitopological group, since joint continuity of multiplication implies separate continuity.
In a semitopological group each translation is a homeomorphism, with inverse the translation by $a^{-1}$.
