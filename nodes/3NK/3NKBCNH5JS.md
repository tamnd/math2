---
tag: 3NKBCNH5JS
kind: statement
role: theorem
name: Brouwer's characterization of the Cantor space
msc: [54F65]
uses: [0CQHFPGJ45, 0TVJZYB6SH, 091GJ3FYD7, 0RJSBR9GW1, 628242KN0T, 0QT00PB5G2, W9VYJRBF9N]
about: [W9VYJRBF9N]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor_space
---

## Statement

Let $X$ be a [[topological space|0CQHFPGJ45]].
Then $X$ is [[homeomorphic|0QT00PB5G2]] to the [[Cantor space|W9VYJRBF9N]] $\set{0, 1}^{\N}$ if and only if $X$ is nonempty, [[compact|0TVJZYB6SH]], [[metrizable|091GJ3FYD7]], [[totally disconnected|0RJSBR9GW1]] and has no isolated points.

## Remarks

A compact metrizable totally disconnected space has a base of clopen sets.
With this and the absence of isolated points, one splits $X$ into two nonempty clopen pieces, each piece again into two, and so on, with diameters tending to $0$.
Sending a point to the sequence of left or right choices that leads to it gives a homeomorphism onto $\set{0, 1}^{\N}$.
For example, the product $\set{0,1}^{\N} \times \set{0,1}^{\N}$ satisfies the conditions, so it is homeomorphic to the Cantor space.
No condition can be dropped.
The rationals $\Q$ are metrizable, totally disconnected and without isolated points, but not compact.
The space $\set{0, 1}$ is compact, metrizable and totally disconnected, but its points are isolated.
The interval $[0, 1]$ satisfies all conditions except total disconnectedness.
A product of uncountably many copies of $\set{0, 1}$ satisfies all conditions except metrizability.

## Explanations

### L1 human

The theorem says that the Cantor space is the only compact metric space that is pure dust and has no lonely points.
So many sets built in quite different ways, such as the middle-thirds Cantor set or products of Cantor sets, are all the same space in disguise.

### L2 human

The theorem is used to recognise Cantor spaces in analysis, dynamics and descriptive set theory, for instance the perfect compact subsets of the line that contain no interval.
It combines with the fact that every nonempty compact metric space is a continuous image of the Cantor space.
A similar characterization holds for the [[Baire space of sequences|P2WS16HKD7]], by the Alexandrov–Urysohn theorem.
