---
tag: 8MEDVAEERQ
kind: example
name: Loop group
msc: ["22E67", "22E65"]
instance_of: [G5S1M9]
uses: [7JBRGCVJRB, EBMCFQT0JN, 04EAFVFTF7]
sources:
  - url: https://en.wikipedia.org/wiki/Loop_group
same_as:
  wikidata: Q6675827
  wikipedia: Loop group
---

## Example

Let $G$ be a [[Lie group|7JBRGCVJRB]] and let $S^1$ be the circle.
The *loop group* of $G$ is the set
$$LG = \set{\gamma \colon S^1 \to G : \gamma \text{ smooth}},$$
with pointwise multiplication $(\gamma\delta)(z) = \gamma(z)\delta(z)$.
It is a [[group|G5S1M9]].
The pointwise product and the pointwise inverse $z \mapsto \gamma(z)^{-1}$ of smooth loops are smooth, because multiplication and inversion of $G$ are smooth.
The identity element is the constant loop at $e$, and associativity holds pointwise.

For compact $G$, $LG$ is an infinite-dimensional Lie group and a [[Fréchet manifold|EBMCFQT0JN]].
Its Lie algebra is the loop algebra $L\mathfrak{g}$ of smooth maps $S^1 \to \mathfrak{g}$ with the pointwise bracket.

## Remarks

The constant loops form a copy of $G$ inside $LG$.
For $G$ the [[circle group|04EAFVFTF7]] $U(1)$, a loop $\gamma \colon S^1 \to U(1)$ has a winding number, and $LU(1)$ has one connected component for each integer.
Central extensions of loop groups of compact Lie groups are closely tied to affine Lie algebras and their representations.

## Explanations

### L1 human

A loop group consists of all smooth closed paths in a Lie group, where two paths are multiplied by multiplying their values at each moment.
In the circle group, take a loop that runs once around and a loop that runs once around the other way.
Their product is a loop of winding number $0$.
Loop groups are among the best understood infinite-dimensional groups, and they appear in conformal field theory and the theory of integrable systems.
