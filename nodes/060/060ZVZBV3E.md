---
tag: 060ZVZBV3E
kind: statement
role: theorem
name: Law of cosines
aliases: [cosine-rule]
msc: [51M04]
uses: [0CTNFGYMM2, 0GJAJC6TNZ, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_cosines
    locator: lead section
same_as:
  wikidata: Q164321
  wikipedia: Law of cosines
---

## Statement

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in the Euclidean space $\mathbb{R}^n$. Let $a = d(B, C)$, $b = d(C, A)$ and $c = d(A, B)$ be its side lengths, where $d$ is the [[Euclidean distance|0NPPGHQNXQ]]. Let $\gamma = \angle ACB$ be its [[angle|0GJAJC6TNZ]] at $C$.
Then
$$c^2 = a^2 + b^2 - 2ab \cos \gamma.$$

## Remarks

The proof in vector form is short. With $u = A - C$ and $v = B - C$: $c^2 = \|u - v\|^2 = \|u\|^2 + \|v\|^2 - 2 u \cdot v$, and $u \cdot v = ab \cos \gamma$.
For $\gamma = \pi / 2$ the formula is the [[Pythagorean theorem|0VP3A1290K]].
The formula lets you find the third side from two sides and the angle between them. It also gives each angle from the three sides.
Mathlib states the formula for all points, with its convention for the angle at a repeated point.

## History

Book II of Euclid's Elements contains the statement in the language of areas of rectangles. Propositions 12 and 13 of Book II treat the obtuse and the acute case.

## Explanations

### L1 human

The law of cosines corrects the Pythagorean theorem for triangles without a right angle. If the angle $\gamma$ is larger than a right angle, $\cos \gamma < 0$, and the opposite side is longer than in the right triangle. If $\gamma$ is smaller, the opposite side is shorter.
