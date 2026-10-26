---
tag: 0PASQ34GHG
kind: statement
role: theorem
name: Law of sines
aliases: [sine-rule]
msc: [51M04]
uses: [0CTNFGYMM2, 0GJAJC6TNZ, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_sines
    locator: lead section
same_as:
  wikidata: Q170181
  wikipedia: Law of sines
---

## Statement

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in the Euclidean space $\mathbb{R}^n$. Let $a = d(B, C)$, $b = d(C, A)$ and $c = d(A, B)$ be its side lengths, where $d$ is the [[Euclidean distance|0NPPGHQNXQ]]. Let $\alpha = \angle BAC$, $\beta = \angle CBA$ and $\gamma = \angle ACB$ be its [[angles|0GJAJC6TNZ]].
Then
$$\frac{a}{\sin \alpha} = \frac{b}{\sin \beta} = \frac{c}{\sin \gamma}.$$

## Remarks

The common value of the three quotients is $2R$, where $R$ is the radius of the [[circumcircle|03VZJE6C8C]] of the triangle.
The angles of a triangle are in $(0, \pi)$, so their sines are positive and the quotients exist.
From two angles and one side, the law of sines gives the other sides. From two sides and an angle that is not between them, it can give two different triangles. This is the ambiguous case.

## History

Ptolemy knew an equivalent form, with chords in place of sines, in the 2nd century.

## Explanations

### L1 human

In a triangle, a larger angle sits opposite a longer side. The law of sines makes this exact: each side divided by the sine of the opposite angle gives the same number. For an equilateral triangle with side $1$, each quotient is $1 / \sin(\pi/3) = 2/\sqrt{3}$.
