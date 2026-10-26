---
tag: 0GA1V8NN8C
kind: statement
role: theorem
name: Inscribed angle theorem
aliases: [central-angle-theorem]
msc: [51M04]
uses: [060W5CBZP6, 03YN70NK0Z, 0GJAJC6TNZ]
sources:
  - url: https://en.wikipedia.org/wiki/Inscribed_angle
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Inscribed_angle
    locator: Proof
---

## Statement

Let $A$, $B$ and $V$ be distinct points of a [[circle|060W5CBZP6]] with the centre $O$ in the Euclidean plane $\mathbb{R}^2$. Let $\measuredangle$ be the [[oriented angle|03YN70NK0Z]], with values in $\mathbb{R} / 2\pi\mathbb{Z}$.
Then
$$\measuredangle AOB = 2 \, \measuredangle AVB.$$

## Remarks

For the unoriented [[angles|0GJAJC6TNZ]], with values in $[0, \pi]$: if $V$ and $O$ are not on opposite sides of the line $AB$, then $\angle AVB = \frac{1}{2} \angle AOB$. If they are on opposite sides, then $\angle AVB = \pi - \frac{1}{2} \angle AOB$.
Thus the inscribed angle does not change when $V$ moves on one arc from $A$ to $B$.
[[Thales's theorem|0GSDHYMA1T]] is the case where $AB$ is a diameter.
The oldest known version is in Propositions 20 and 21 of Book III of Euclid's Elements.

## Explanations

### L1 human

Fix two points $A$ and $B$ on a circle. The angle at the centre that looks at the arc $AB$ is twice the angle at any point of the circle on the other arc. The proof starts with the case where the line $VO$ passes through $B$. Then the triangle $VOA$ is isosceles, and its angle sum gives the result.
