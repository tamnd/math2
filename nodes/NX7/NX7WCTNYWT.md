---
tag: NX7WCTNYWT
kind: definition
name: Groupoid
msc: [20L05, 18B40]
defines: FH3C0T643F
uses: [A2DE66937D, G5S1M9, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Groupoid
---

## Definition

A *groupoid* is a [[category|A2DE66937D]] $\mathcal{G}$ in which every morphism is an isomorphism.
That is, for every morphism $f \colon x \to y$ of $\mathcal{G}$ there is a morphism $g \colon y \to x$ with $g \circ f = \id_x$ and $f \circ g = \id_y$.

## Remarks

A groupoid is *small* if its objects form a set.
For each object $x$, the morphisms $x \to x$ form a [[group|G5S1M9]], the vertex group at $x$.

Example: let $\sim$ be an [[equivalence relation|0G8VEZ3WTK]] on a set $X$.
Take $X$ as the set of objects, with exactly one morphism $x \to y$ when $x \sim y$ and none otherwise.
Composition exists by transitivity, identities by reflexivity, and the inverse of $x \to y$ is the morphism $y \to x$, which exists by symmetry.

Non-example: the category with objects $0, 1$ and one non-identity arrow $0 \to 1$, the poset $0 \le 1$.
There is no morphism $1 \to 0$, so the arrow $0 \to 1$ has no inverse.

A group $G$ gives a groupoid with one object whose morphisms are the elements of $G$, and every one-object groupoid arises in this way.
