---
tag: QQAWHC9X60
kind: statement
role: theorem
name: Schreier refinement theorem
msc: ["20E15", 20D30]
uses: [0ZZR8D7Y1Z, 0KYX2N69J0, 21JJ523V95]
about: [0ZZR8D7Y1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Schreier_refinement_theorem
same_as:
  wikidata: Q7432872
  wikipedia: Schreier refinement theorem
---

## Statement

Let $G$ be a [[group|G5S1M9]].
A refinement of a [[subnormal series|0ZZR8D7Y1Z]] of $G$ is a subnormal series of $G$ that contains every term of the given series.
Two subnormal series of $G$ are equivalent when they have the same length and their factors agree up to a permutation and isomorphism.
Then any two subnormal series of $G$ have refinements that are equivalent.

## Remarks

Let the two series be $(G_i)_{0 \le i \le n}$ and $(H_j)_{0 \le j \le m}$.
The proof inserts the groups $G_{i,j} = G_{i-1}(G_i \cap H_j)$ between $G_{i-1}$ and $G_i$, and the groups $H_{j,i} = H_{j-1}(H_j \cap G_i)$ between $H_{j-1}$ and $H_j$.
Both refined series have length $nm$, and the [[Zassenhaus lemma|21JJ523V95]] gives $G_{i,j}/G_{i,j-1} \cong H_{j,i}/H_{j,i-1}$ for each pair $(i, j)$.
For example, in $\Z/12\Z$ the series $0 \le 6\Z/12\Z \le \Z/12\Z$ and $0 \le 4\Z/12\Z \le \Z/12\Z$ refine to $0 \le 6\Z/12\Z \le 2\Z/12\Z \le \Z/12\Z$ and $0 \le 4\Z/12\Z \le 2\Z/12\Z \le \Z/12\Z$.
Both refinements have factors of orders $2, 3, 2$ in some order, namely $\Z/2\Z$, $\Z/3\Z$, $\Z/2\Z$ and $\Z/3\Z$, $\Z/2\Z$, $\Z/2\Z$.

## Explanations

### L1 human

A subnormal series cuts a group into layers.
Two different ways of cutting may look unrelated.
The theorem says that you can always cut each of them further so that both give the same list of layers, up to order.

### L2 human

The theorem is the main step in the proof of the [[Jordan–Hölder theorem|0E088ZP533]].
A [[composition series|0XV2A49X6Q]] has no proper refinement other than itself with repeated terms, so two composition series are already equivalent once the repeated terms are removed.
The same argument works for groups with operators and for modules, where it gives the uniqueness of composition factors of modules of finite length.
