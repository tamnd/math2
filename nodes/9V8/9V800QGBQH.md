---
tag: 9V800QGBQH
kind: definition
name: Category of elements
msc: [18A25]
defines: S9EJKKRHW1
uses: [A2DE66937D, 28NQ0KRHD3, PC6HG1JEGM, 0WCY42EV9V, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Category_of_elements
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $F \colon \mathcal{C} \to \mathbf{Set}$ be a [[functor|28NQ0KRHD3]] to the category of sets.
The *category of elements* $\int F$, also written $\mathrm{el}(F)$, is defined as follows:

1. its objects are the pairs $(A, x)$ with $A$ an object of $\mathcal{C}$ and $x \in F(A)$;
2. a morphism $(A, x) \to (B, y)$ is a morphism $f \colon A \to B$ of $\mathcal{C}$ with $F(f)(x) = y$;
3. composition and identities are those of $\mathcal{C}$.

## Remarks

Composition is well defined because $F(g \circ f)(x) = F(g)(F(f)(x))$.
It is the [[comma category|PC6HG1JEGM]] $(\ast \downarrow F)$, where $\ast$ is a one-point set, and the map $(A, x) \mapsto A$ is a projection functor $\int F \to \mathcal{C}$.
Example: let $G$ be a [[group|G5S1M9]] seen as a category with one object, and let $F$ be a set $X$ with a [[group action|0WCY42EV9V]] of $G$.
Then $\int F$ has the elements of $X$ as objects and a morphism $g \colon x \to y$ for each $g \in G$ with $g \cdot x = y$; it is the action groupoid.
Non-example: if $g \cdot x \ne y$, then $g$ is not a morphism from $x$ to $y$ in $\int F$, although it is a morphism of $G$.
For a contravariant functor $P \colon \mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$, the same construction is usually written with morphisms $f \colon A \to B$ such that $P(f)(y) = x$.
