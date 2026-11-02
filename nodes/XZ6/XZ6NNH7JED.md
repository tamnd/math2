---
tag: XZ6NNH7JED
kind: definition
name: Morphism
msc: [18A05, 18A20]
defines: 859F0TFVA3
uses: [A2DE66937D, 0JYTG5K9Y4, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Morphism
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $A$, $B$ be objects of $\mathcal{C}$.
A *morphism* from $A$ to $B$ is a member $f$ of $\Hom_{\mathcal{C}}(A, B)$, written $f \colon A \to B$.
The object $A$ is its domain and the object $B$ is its codomain.
Special kinds of morphisms are defined as follows:

1. $f \colon A \to B$ is an *isomorphism* if there is $g \colon B \to A$ with $g \circ f = 1_A$ and $f \circ g = 1_B$;
2. $f$ is an *endomorphism* if $A = B$;
3. $f$ is an *automorphism* if it is both an endomorphism and an isomorphism.

## Remarks

The morphism $g$ in clause 1 is unique: if $g'$ also works, then $g' = g' \circ (f \circ g) = (g' \circ f) \circ g = g$.
It is called the inverse $f^{-1}$, and $A$ and $B$ are then *isomorphic*, written $A \cong B$.
Example: in the category of groups, the morphisms are the [[group homomorphisms|0JYTG5K9Y4]].
The isomorphisms are the bijective homomorphisms, since the inverse map of a bijective homomorphism is again a homomorphism.
Non-example: in the category of topological spaces with [[continuous maps|0VGFHTM75Y]], let $X$ be $[0, 1]$ with the discrete topology and $Y$ be $[0, 1]$ with the usual topology.
The identity map $X \to Y$ is a continuous bijection, but its inverse $Y \to X$ is not continuous, so it is not an isomorphism.
The endomorphisms of $A$ form a monoid $\End(A)$ under composition, and the automorphisms form a group $\Aut(A)$.
