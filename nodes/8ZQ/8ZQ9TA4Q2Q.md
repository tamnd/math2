---
tag: 8ZQ9TA4Q2Q
kind: example
name: Poincaré group
msc: ["22E43", "83A05", "22E70"]
instance_of: [7JBRGCVJRB]
uses: [QWK3BYVJ9W, 0H3WZXCZNF, 087VJM5Q77]
sources:
  - url: https://en.wikipedia.org/wiki/Poincaré_group
same_as:
  wikidata: Q1066449
  wikipedia: Poincaré group
---

## Example

Let $O(1, 3)$ be the [[Lorentz group|QWK3BYVJ9W]], acting on Minkowski space $\R^{1,3} = \R^4$.
The *Poincaré group* is the set of pairs $(\Lambda, a)$ with $\Lambda \in O(1, 3)$ and $a \in \R^4$, acting on $\R^4$ by
$$(\Lambda, a) \cdot x = \Lambda x + a,$$
a Lorentz transformation followed by a [[translation|087VJM5Q77]].
Composing two such maps gives the group law
$$(\Lambda, a)(\Lambda', a') = (\Lambda \Lambda', \ \Lambda a' + a).$$
Check: $(\Lambda, a) \cdot ((\Lambda', a') \cdot x) = \Lambda(\Lambda' x + a') + a = \Lambda\Lambda' x + (\Lambda a' + a)$.
The identity is $(I, 0)$ and the inverse of $(\Lambda, a)$ is $(\Lambda^{-1}, -\Lambda^{-1} a)$.

So the Poincaré group is the [[semidirect product|0H3WZXCZNF]] $\R^4 \rtimes O(1, 3)$, a [[Lie group|7JBRGCVJRB]] of dimension $4 + 6 = 10$.

## Remarks

The Poincaré group is the group of all isometries of Minkowski space, that is, the bijections $f$ of $\R^4$ with $Q(f(x) - f(y)) = Q(x - y)$ for the Minkowski form $Q$.
The translations form an abelian normal subgroup, so the Poincaré group is not semisimple.
Often the name refers to the identity component $\R^4 \rtimes SO^+(1, 3)$.
Its irreducible unitary representations, studied by Wigner, are labelled by mass and spin in physics.

## Explanations

### L1 human

The Poincaré group is the full symmetry group of special relativity.
Besides rotations and boosts, it contains the shifts of space and time.
Its $10$ dimensions count $4$ translations, $3$ rotations and $3$ boosts.
The laws of physics in flat space-time have the same form in every frame related by an element of this group.
