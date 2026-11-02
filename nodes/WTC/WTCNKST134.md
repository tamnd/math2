---
tag: WTCNKST134
kind: example
name: Diffeomorphism group
msc: [58D05, "22E65", 57S05]
instance_of: [G5S1M9]
uses: [0KZZ70ZHXP, F45VQ47GPV, 0299VCW1TH, EBMCFQT0JN, 7JBRGCVJRB, H3QX1ZFC8K]
sources:
  - url: https://en.wikipedia.org/wiki/Diffeomorphism
---

## Example

Let $M$ be a [[smooth manifold|F45VQ47GPV]].
The *diffeomorphism group* $\operatorname{Diff}(M)$ is the set of all [[diffeomorphisms|0KZZ70ZHXP]] $f \colon M \to M$, with composition as the operation.
It is a [[group|G5S1M9]].
The composition of two diffeomorphisms is a diffeomorphism, and composition is associative.
The identity map $\id_M$ is the identity element, and the inverse of $f$ is the inverse map $f^{-1}$, a diffeomorphism too.

When $M$ is compact, $\operatorname{Diff}(M)$ is an infinite-dimensional Lie group.
It is a [[Fréchet manifold|EBMCFQT0JN]] modelled on the space of smooth [[vector fields|0299VCW1TH]] on $M$, with smooth composition and inversion.
Its Lie algebra is the space of vector fields; with the usual conventions, the bracket is the negative of the Lie bracket of vector fields.

## Remarks

Unlike a finite-dimensional [[Lie group|7JBRGCVJRB]], $\operatorname{Diff}(M)$ has an [[exponential map|H3QX1ZFC8K]], given by the time-one flow of a vector field, that need not be onto any neighbourhood of the identity.
This happens already for $M = S^1$.
So some results of finite-dimensional Lie theory fail for diffeomorphism groups.

## Explanations

### L1 human

The diffeomorphism group of a space collects all ways to deform the space smoothly and reversibly onto itself.
For the circle, these are the smooth bijections of the circle with smooth inverse, such as rotations and smooth stretchings.
Doing one deformation after another is again a deformation, and each can be undone, so they form a group.
This group is too big to be a Lie group in the usual sense, since it has infinitely many independent directions, one for each vector field.
