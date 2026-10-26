---
tag: 00PPY3RPNB
kind: definition
name: Power of a point
msc: [51M04]
defines: 02E9VT1RVQ
uses: [060W5CBZP6, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Power_of_a_point
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Power_of_a_point
    locator: Intersecting secants theorem, intersecting chords theorem
---

## Definition

Let $C$ be a [[circle|060W5CBZP6]] in the Euclidean plane $\mathbb{R}^2$ with the centre $O$ and the radius $r$, and let $d$ be the [[Euclidean distance|0NPPGHQNXQ]].
The power of a point $P \in \mathbb{R}^2$ with respect to $C$ is the real number
$$\Pi(P) = d(P, O)^2 - r^2.$$

## Remarks

$\Pi(P) > 0$ if $P$ is outside $C$, $\Pi(P) = 0$ if $P$ is on $C$, and $\Pi(P) < 0$ if $P$ is inside $C$.
For $P$ outside $C$ and a tangent from $P$ that touches $C$ at $T$, the Pythagorean theorem gives $\Pi(P) = d(P, T)^2$.
Let a line through $P$ meet $C$ at $S_1$ and $S_2$. Then $d(P, S_1)\, d(P, S_2) = |\Pi(P)|$. This contains the [[intersecting chords theorem|0YQQYET8YQ]] and the [[intersecting secants theorem|0J5XR7BW2S]].
Jakob Steiner introduced the power of a point in 1826.

## Explanations

### L1 human

The power of a point measures how far the point is from a circle, in a squared form. For the unit circle and $P = (3, 0)$, the power is $9 - 1 = 8$. A tangent from $P$ to the circle has the length $\sqrt{8}$.
