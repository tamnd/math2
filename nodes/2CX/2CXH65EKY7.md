---
tag: 2CXH65EKY7
kind: object
name: E8 lattice
msc: [11H06, 11H31, 52C17]
uses: [WN9V7WSJKF, 0XPR1E85W0]
sources:
  - url: https://en.wikipedia.org/wiki/E8_lattice
same_as:
  wikidata: Q4662154
  wikipedia: E8 lattice
---

## Description

The $E_8$ lattice is the [[lattice|WN9V7WSJKF]] in the [[Euclidean space|0XPR1E85W0]] $\R^8$ given by
$$E_8 = \set{x \in \Z^8 \cup (\Z + \tfrac12)^8 : x_1 + x_2 + \dots + x_8 \in 2\Z}.$$
So its points have all coordinates integers or all coordinates half-integers, with even coordinate sum.

## Remarks

It is closed under addition and negation, so it is a subgroup of $\R^8$, and it contains $8$ independent vectors.
It is even: $x \cdot x \in 2\Z$ for all $x \in E_8$.
It is unimodular: its covolume is $1$.
Up to isometry, it is the unique even unimodular lattice in $\R^8$.
Its shortest nonzero vectors have length $\sqrt 2$, and there are $240$ of them.
They are the $112$ vectors with two coordinates $\pm 1$ and six coordinates $0$.
The other $128$ are the vectors with all coordinates $\pm\tfrac12$ and an even number of minus signs.
These $240$ vectors form the root system of type $E_8$.
Balls of radius $\sqrt 2/2$ centred at the points of $E_8$ form the densest [[sphere packing|HF32CBN5MA]] in $\R^8$, with density $\pi^4/384$, as proved by Viazovska.
Each ball touches $240$ others, which is the [[kissing number|B408FZYXF9]] in dimension $8$.

## Explanations

### L1 human

The $E_8$ lattice is a grid of points in eight dimensions.
Take all points whose coordinates are either all whole numbers or all halves of odd numbers, and keep those whose coordinates add up to an even number.
This grid is extremely symmetric, and placing equal balls at its points gives the tightest possible packing of balls in eight dimensions.
