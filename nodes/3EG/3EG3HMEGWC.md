---
tag: 3EG3HMEGWC
kind: definition
name: Formal concept analysis
msc: [06B99, 68T30, 06A15]
defines: G83JY7CY7Q
uses: [05AVARPXA2, 00E0YZCERH, Q5JHEPRYQ6, D7A0ZGZT5S]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_concept_analysis
---

## Definition

A *formal context* is a triple $(G, M, I)$ of a set $G$ of objects, a set $M$ of attributes and a [[binary relation|05AVARPXA2]] $I \subseteq G \times M$.
One reads $g \mathrel{I} m$ as "object $g$ has attribute $m$".
For $A \subseteq G$ and $B \subseteq M$, put
$$A' = \set{m \in M : g \mathrel{I} m \text{ for all } g \in A}, \qquad B' = \set{g \in G : g \mathrel{I} m \text{ for all } m \in B}.$$
A *formal concept* of $(G, M, I)$ is a pair $(A, B)$ with $A \subseteq G$, $B \subseteq M$, $A' = B$ and $B' = A$.
The set $A$ is its extent and $B$ is its intent.
Formal concepts are ordered by $(A_1, B_1) \le (A_2, B_2)$ if and only if $A_1 \subseteq A_2$, which holds if and only if $B_2 \subseteq B_1$.
The ordered set of all formal concepts is the *concept lattice* $\mathfrak{B}(G, M, I)$.
*Formal concept analysis* is the study of formal contexts through their concept lattices.

## Remarks

The two maps $A \mapsto A'$ and $B \mapsto B'$ between the [[power sets|00E0YZCERH]] of $G$ and $M$ form an antitone [[Galois connection|Q5JHEPRYQ6]].
The extents are the closed sets of the closure operator $A \mapsto A''$.
The concept lattice is a [[complete lattice|D7A0ZGZT5S]]: the meet of concepts $(A_i, B_i)$ is $\left(\bigcap_i A_i, \left(\bigcup_i B_i\right)''\right)$.
Conversely, every complete lattice $L$ is isomorphic to the concept lattice of the context $(L, L, \le)$.
Example: for $G = \set{1, 2}$, $M = \set{a, b}$ and $I = \set{(1, a), (2, a), (2, b)}$, the concepts are $(\set{1, 2}, \set{a})$ and $(\set{2}, \set{a, b})$; for instance $\set{1, 2}' = \set{a}$ and $\set{a}' = \set{1, 2}$.
Non-example: in the same context, $(\set{1}, \set{a})$ is not a concept, because $\set{a}' = \set{1, 2} \ne \set{1}$.
