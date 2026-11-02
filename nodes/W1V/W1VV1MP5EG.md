---
tag: W1VV1MP5EG
kind: definition
name: Coproduct
msc: [18A30]
defines: 4FJ0S71P58
uses: [A2DE66937D, 859F0TFVA3, BJS1CGTKQ5, S5744QZV4N, 0S7W6EG32V, TM7QS7P7X9, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Coproduct
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $(X_i)_{i \in I}$ be a family of objects of $\mathcal{C}$ indexed by a set $I$.
A *coproduct* of the family is an object $C$ with [[morphisms|859F0TFVA3]] $\iota_i \colon X_i \to C$ for $i \in I$, called *injections*, with the following property.
For every object $Y$ and every family of morphisms $f_i \colon X_i \to Y$, there is exactly one morphism $f \colon C \to Y$ with $f \circ \iota_i = f_i$ for all $i$.
The object $C$ is written $\coprod_{i \in I} X_i$, or $X_1 \sqcup X_2$ for two objects, and $f$ is written $[f_1, f_2]$.

## Remarks

A coproduct is the [[colimit|BJS1CGTKQ5]] of the diagram whose shape is the set $I$ with only identity morphisms, and it is a [[product|S5744QZV4N]] in the opposite category.
The coproduct of the empty family is an initial object.

Example: in the category of [[abelian groups|082GHNPJ53]], the [[direct sum|0S7W6EG32V]] $A \oplus B$ with $\iota_A(a) = (a, 0)$ and $\iota_B(b) = (0, b)$ is a coproduct.
Given homomorphisms $f_A \colon A \to Y$ and $f_B \colon B \to Y$, the map $f(a, b) = f_A(a) + f_B(b)$ is a homomorphism because $Y$ is abelian, it satisfies $f \circ \iota_A = f_A$ and $f \circ \iota_B = f_B$, and it is forced since $(a, b) = (a, 0) + (0, b)$.
In the category of sets the coproduct is the disjoint union, and in the category of groups it is the [[free product|TM7QS7P7X9]].

Non-example: in the category of fields, $\mathbb{F}_2$ and $\mathbb{F}_3$ have no coproduct, since no field receives homomorphisms from both: a field homomorphism preserves the characteristic.
