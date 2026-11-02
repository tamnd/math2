---
tag: MCEE53VGBQ
kind: definition
name: Category
msc: [18A05, 18A15]
defines: A2DE66937D
uses: [0BSJ7RQ9BW, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Category_(mathematics)
---

## Definition

A *category* $\mathcal{C}$ consists of the following data:

1. a class $\mathrm{Ob}(\mathcal{C})$, whose members are called the objects of $\mathcal{C}$;
2. for each pair of objects $A, B$, a class $\Hom_{\mathcal{C}}(A, B)$ of morphisms from $A$ to $B$, written $f \colon A \to B$, with these classes pairwise disjoint;
3. for each triple of objects $A, B, C$, a composition map $\Hom_{\mathcal{C}}(B, C) \times \Hom_{\mathcal{C}}(A, B) \to \Hom_{\mathcal{C}}(A, C)$, written $(g, f) \mapsto g \circ f$;
4. for each object $A$, an identity morphism $1_A \in \Hom_{\mathcal{C}}(A, A)$.

These data must satisfy two axioms:

1. associativity: $h \circ (g \circ f) = (h \circ g) \circ f$ for all $f \colon A \to B$, $g \colon B \to C$ and $h \colon C \to D$;
2. identity: $f \circ 1_A = f = 1_B \circ f$ for all $f \colon A \to B$.

## Remarks

The category is *locally small* when every $\Hom_{\mathcal{C}}(A, B)$ is a [[set|0BSJ7RQ9BW]], and *small* when moreover $\mathrm{Ob}(\mathcal{C})$ is a set.
Example: $\mathbf{Set}$ has sets as objects and [[functions|0EPAT51DXQ]] $A \to B$ as morphisms, with the usual composition and the identity functions.
Composition of functions is associative and the identity functions are neutral, so both axioms hold.
Non-example: take sets as objects and, as morphisms $A \to B$, the functions $A \to B$ whose image has at most one point.
A composite of two such functions again has at most one point in its image, so composition is defined.
The identity function of a set with two elements is not such a morphism, so clause 4 fails.
Many authors write $\mathcal{C}(A, B)$ or $\hom(A, B)$ for $\Hom_{\mathcal{C}}(A, B)$, and $gf$ for $g \circ f$.
