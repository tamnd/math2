---
tag: ~ede3f62f
kind: statement
role: theorem
name: Universal property of the abelianisation
msc: [20F12]
uses: [~430a7a50, ~a3f4ba4c, ~83091c4f]
sources:
  - url: https://en.wikipedia.org/wiki/Commutator_subgroup
    locator: Abelianization
---

## Statement

Let $G$ be a [[group|G5S1M9]], let $\pi \colon G \to G^{\mathrm{ab}}$ be the projection to its [[abelianisation|~f4e7603e]], and let $A$ be an [[abelian group|~b6df27fe]].
For each [[group homomorphism|~c666c876]] $\varphi \colon G \to A$, there is exactly one group homomorphism $\bar{\varphi} \colon G^{\mathrm{ab}} \to A$ with $\bar{\varphi} \circ \pi = \varphi$.

## Remarks

Each commutator goes to $e$ under $\varphi$, because $A$ is abelian, so $[G, G] \subseteq \ker \varphi$.
Then the [[universal property of the quotient group|~a3f4ba4c]] gives $\bar{\varphi}$.
Thus the homomorphisms from $G$ to $A$ correspond exactly to the homomorphisms from $G^{\mathrm{ab}}$ to $A$.

## Explanations

### L1 human

A homomorphism into an abelian group cannot see the commutators of $G$.
So it factors through the abelianisation, where the commutators are gone.
This makes the abelianisation the best abelian approximation of $G$.
