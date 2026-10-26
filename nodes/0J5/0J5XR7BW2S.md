---
tag: 0J5XR7BW2S
kind: statement
role: theorem
name: Intersecting secants theorem
aliases: [secant-theorem]
msc: [51M04]
uses: [049DCJZ448, 0NPPGHQNXQ, 02E9VT1RVQ]
sources:
  - url: https://en.wikipedia.org/wiki/Intersecting_secants_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Power_of_a_point
    locator: Intersecting secants theorem, intersecting chords theorem
same_as:
  wikidata: Q1727461
  wikipedia: Intersecting secants theorem
---

## Statement

Let $A$, $B$, $C$ and $D$ be [[concyclic points|049DCJZ448]] of the Euclidean plane $\mathbb{R}^2$, with $A \neq D$ and $B \neq C$. Let $d$ be the [[Euclidean distance|0NPPGHQNXQ]].
Suppose that the lines $AD$ and $BC$ meet at a point $P$ outside the circle.
Then
$$d(P, A)\, d(P, D) = d(P, B)\, d(P, C).$$

## Remarks

Both products are equal to the [[power|02E9VT1RVQ]] $d(P, O)^2 - r^2$ of $P$, where $O$ is the centre and $r$ the radius.
A proof: the triangles $PAC$ and $PBD$ are similar, because they have the same angle at $P$ and equal inscribed angles at $C$ and $D$.
If the second line becomes tangent, then $B = C$, and the statement becomes the [[tangent–secant theorem|0QX7E9KAAX]].

## Explanations

### L1 human

From a point outside a circle, draw two lines that cut the circle. On each line, multiply the distances from the point to the two crossing points. The two products are equal.
