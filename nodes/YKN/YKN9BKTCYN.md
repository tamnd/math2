---
tag: YKN9BKTCYN
kind: definition
name: Kauffman bracket
msc: [57K14]
defines: JYKVYS4N32
uses: [1A5WRCNTM3]
sources:
  - url: https://en.wikipedia.org/wiki/Bracket_polynomial
---

## Definition

Let $D$ be an unoriented diagram of a tame [[link|1A5WRCNTM3]] in $\R^3$, with crossing set $X$.
At a crossing, the *A-regions* are the two regions swept out when the over-strand is turned counterclockwise.
The *A-smoothing* joins the two A-regions, and the *B-smoothing* joins the other two regions.
A *state* $s$ of $D$ chooses a smoothing at each crossing; let $a(s)$ and $b(s)$ count its A- and B-smoothings.
Let $\abs{s}$ be the number of circles in the resulting diagram without crossings.
The *Kauffman bracket* of $D$ is
$$\langle D \rangle = \sum_{s} A^{a(s) - b(s)} \, (-A^2 - A^{-2})^{\abs{s} - 1} \in \Z[A, A^{-1}],$$
where the sum runs over all $2^{\abs{X}}$ states.

## Remarks

Equivalently, $\langle O \rangle = 1$ for a single circle, adding a disjoint circle multiplies by $-A^2 - A^{-2}$, and each crossing expands as $A$ times its A-smoothing plus $A^{-1}$ times its B-smoothing.
Example: a one-crossing diagram of the [[unknot|1TQ06R4Q66]] has one state with one circle and one with two circles.
Depending on the sign of the kink, the bracket is $A + A^{-1}(-A^2 - A^{-2}) = -A^{-3}$ or its mirror value $-A^{3}$.
Non-example of invariance: this kinked diagram and the round circle depict the same knot but have brackets $-A^{\mp 3}$ and $1$, so $\langle \cdot \rangle$ is not a link invariant.
It is invariant under the second and third [[Reidemeister moves|T3HAGWYKK7]], and the first move multiplies it by $-A^{\pm 3}$.
For an oriented diagram with writhe $w(D)$, the product $(-A^3)^{-w(D)} \langle D \rangle$ is an invariant, and $A = t^{-1/4}$ turns it into the [[Jones polynomial|4SPC17FPXE]].
