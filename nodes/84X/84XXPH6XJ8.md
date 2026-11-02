---
tag: 84XXPH6XJ8
kind: definition
name: Reduced product
msc: [08B25, 03C20]
defines: F4WRD396PB
uses: [QJGPT2W0FT, WJ73XYBNE4, 15PF73BKY6, DCSXXT4SER, N5KE7FH6CX]
sources:
  - url: https://en.wikipedia.org/wiki/Reduced_product
---

## Definition

Let $I$ be a nonempty set and let $F$ be a [[filter|15PF73BKY6]] on $I$.
Let $(\mathbf{A}_i)_{i \in I}$ be a family of [[algebras|QJGPT2W0FT]] of the same signature, and let $\mathbf{P} = \prod_{i \in I} \mathbf{A}_i$ be their [[direct product|WJ73XYBNE4]].
Define $\theta_F$ on the universe of $\mathbf{P}$ by $(a, b) \in \theta_F$ if and only if $\set{i \in I : a(i) = b(i)} \in F$.
The *reduced product* $\prod_{i \in I} \mathbf{A}_i / F$ is the [[quotient algebra|N5KE7FH6CX]] $\mathbf{P}/\theta_F$.

## Remarks

The relation $\theta_F$ is a [[congruence|DCSXXT4SER]] on $\mathbf{P}$.
Reflexivity uses $I \in F$, and transitivity uses that $F$ is closed under finite intersections and supersets.
Compatibility holds because $\set{i : f(a_1, \dots, a_n)(i) = f(b_1, \dots, b_n)(i)}$ contains the intersection of the sets $\set{i : a_k(i) = b_k(i)}$.

Example: if $F = \set{I}$, then $\theta_F$ is equality and the reduced product is the direct product itself.
If $F = \set{X \subseteq I : J \subseteq X}$ for some nonempty $J \subseteq I$, the reduced product is isomorphic to $\prod_{j \in J} \mathbf{A}_j$.

Non-example: on $I = \set{1, 2, 3}$, the family $G = \set{\set{1, 2}, \set{2, 3}, I}$ is not a filter, since $\set{1, 2} \cap \set{2, 3} = \set{2} \notin G$.
With it, the analogous relation on $\Z^3$ is not transitive: $(0, 0, 0)$ is related to $(0, 0, 1)$, which is related to $(1, 0, 1)$, but $(0, 0, 0)$ and $(1, 0, 1)$ agree only on $\set{2}$.

When $F$ is an ultrafilter, the reduced product is the [[ultraproduct|AX9Q86GB8M]] $\prod_{i \in I} \mathbf{A}_i / F$.
