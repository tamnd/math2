---
tag: A1MRBS3Z5C
kind: definition
name: Polymorphism of a relation
msc: [08A40, 08A02]
defines: A0K9EZRM7E
uses: [EJ8YJVM9BW, 09CEDJYBKP, 05AVARPXA2]
sources:
  - url: https://en.wikipedia.org/wiki/Clone_(algebra)
---

## Definition

Let $A$ be a set, let $m, n \ge 1$, and let $R \subseteq A^m$ be an $m$-ary relation on $A$.
An $n$-ary [[operation|EJ8YJVM9BW]] $f \colon A^n \to A$ is a *polymorphism* of $R$ if for all tuples
$$(a_{1 1}, \dots, a_{m 1}), \; \dots, \; (a_{1 n}, \dots, a_{m n}) \in R$$
the tuple
$$\bigl(f(a_{1 1}, \dots, a_{1 n}), \dots, f(a_{m 1}, \dots, a_{m n})\bigr)$$
is also in $R$.
For a set $\Gamma$ of finitary relations on $A$, $\operatorname{Pol}(\Gamma)$ denotes the set of operations that are polymorphisms of every $R \in \Gamma$.
For a set $F$ of finitary operations on $A$, $\operatorname{Inv}(F)$ denotes the set of finitary relations on $A$ of which every $f \in F$ is a polymorphism.

## Remarks

Example: on $\set{0, 1}$, the majority operation $m$ is a polymorphism of the [[binary relation|05AVARPXA2]] $R = \set{(0, 1), (1, 0)}$.
Check: given three pairs $(a_j, 1 - a_j)$ in $R$, the second coordinates are the complements of the first, so $m(1 - a_1, 1 - a_2, 1 - a_3) = 1 - m(a_1, a_2, a_3)$ and the result lies in $R$.
Non-example: the operation $\wedge$ on $\set{0, 1}$ is not a polymorphism of the same $R$, since applying it to $(0, 1)$ and $(1, 0)$ gives $(0, 0) \notin R$.
For a unary relation $B \subseteq A$, the polymorphisms are the operations under which $B$ is closed, so $B$ is a subuniverse.
For an equivalence relation, the polymorphisms are the operations compatible with it, as in the definition of a congruence.
If $A$ carries a relational structure, its polymorphisms are the homomorphisms from its $n$-th power to itself.
