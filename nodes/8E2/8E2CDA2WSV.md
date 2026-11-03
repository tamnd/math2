---
tag: 8E2CDA2WSV
kind: concept
name: Measure algebra M(G)
msc: [43A10, 22D15]
sources:
  - url: https://en.wikipedia.org/wiki/Group_algebra_of_a_locally_compact_group
---

## Summary

The measure algebra $M(G)$ of a [[locally compact group|AHV05ZBCYW]] $G$ is the Banach space of finite complex Radon measures on $G$.
Its product is the convolution of measures.
It is a unital Banach $*$-algebra, whose unit is the point mass at the identity.
It contains the [[group algebra|6GD25S53ND]] $L^1(G)$ as a closed ideal and the point masses as a copy of $G$.
It is the natural home of the Fourier–Stieltjes transform and of the multipliers of $L^1(G)$.

## Explanations

### L1 human

The group algebra $L^1(G)$ contains spread-out functions but not single points, so it usually has no unit.
The measure algebra adds measures such as a point mass, which sits entirely at one element.
Convolving with the point mass at $g$ shifts a function by $g$, so the group itself lives inside $M(G)$.
On the integers both algebras are the same: a finite measure on $\Z$ is just an absolutely summable sequence.
In probability, convolving two probability measures on $\R$ gives the distribution of the sum of two independent random variables.
