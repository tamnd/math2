---
tag: J5QPP8REV6
kind: definition
name: Coequalizer
msc: [18A30]
defines: DVSTWGVCSZ
uses: [A2DE66937D, 859F0TFVA3, BJS1CGTKQ5, CTJ5AD8ST5, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Coequalizer
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $f, g \colon X \to Y$ be two [[morphisms|859F0TFVA3]] of $\mathcal{C}$.
A *coequalizer* of $f$ and $g$ is an object $Q$ with a morphism $q \colon Y \to Q$ such that:

1. $q \circ f = q \circ g$;
2. for every object $Z$ and every morphism $k \colon Y \to Z$ with $k \circ f = k \circ g$, there is exactly one morphism $u \colon Q \to Z$ with $u \circ q = k$.

## Remarks

A coequalizer is the [[colimit|BJS1CGTKQ5]] of the diagram formed by $f$ and $g$, and it is an [[equalizer|CTJ5AD8ST5]] in the opposite category.
It is an epimorphism, by the dual of the argument for equalizers.

Example: in the category of sets, let $\sim$ be the smallest [[equivalence relation|0G8VEZ3WTK]] on $Y$ with $f(x) \sim g(x)$ for all $x \in X$, let $Q = Y/{\sim}$ and let $q$ be the quotient map.
Clause 1 holds by construction.
If $k \circ f = k \circ g$, the relation "$k(y) = k(y')$" is an equivalence relation containing all pairs $(f(x), g(x))$, so it contains $\sim$, and $u([y]) = k(y)$ is well defined; it is unique because $q$ is surjective.
In the category of abelian groups the coequalizer of $f$ and $g$ is $Y / \im(f - g)$ with the quotient map.

Non-example: for $X = \{*\}$, $Y = \{0, 1, 2\}$, $f(*) = 0$ and $g(*) = 1$, the constant map $q \colon Y \to \{*\}$ satisfies clause 1 but not clause 2.
The map $k \colon Y \to \{0, 2\}$ with $k(0) = k(1) = 0$ and $k(2) = 2$ has $k \circ f = k \circ g$ but does not factor through a one-point set.
