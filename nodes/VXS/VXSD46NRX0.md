---
tag: VXSD46NRX0
kind: problem
name: Unknotting problem
msc: [57K10, 68Q17]
uses: [QYEAZTYGPT, 1TQ06R4Q66, T3HAGWYKK7]
about: [QYEAZTYGPT]
sources:
  - url: https://en.wikipedia.org/wiki/Unknotting_problem
  - url: https://arxiv.org/abs/math/9807016
    locator: Section 1
same_as:
  wikidata: Q7896950
  wikipedia: Unknotting problem
history:
  posed_by: "Max Dehn"
  first_stated: "1910"
---

## Problem

The input is a finite diagram of a tame [[knot|QYEAZTYGPT]] in $\R^3$, for example a polygon with finitely many vertices given by rational coordinates.
The question is whether the knot is the [[unknot|1TQ06R4Q66]], that is, whether it is ambient isotopic to a round circle.
The problem asks for an algorithm that answers this question for every input, and for the cost of such an algorithm.

## Remarks

Dehn's work of 1910 began the search for such an algorithm, through the fundamental group of the knot complement.
Haken proved with his theory of normal surfaces, published in 1961, that the problem is decidable.
His method searches for a disk bounded by the knot among finitely many normal surfaces in the knot complement.
Hass, Lagarias and Pippenger proved in 1999 that the problem lies in the complexity class NP.
Lackenby proved without extra hypotheses that it also lies in co-NP.
It is not known whether the problem can be solved in polynomial time.
[[Reidemeister moves|T3HAGWYKK7]] give another approach: a diagram of the unknot can be reduced to a circle by such moves, and there are explicit bounds on the number of moves needed.

## Explanations

### L1 human

Take a tangled loop of string whose ends are glued together.
The question is whether you can untangle it into a plain circle without cutting it.
A messy picture of the plain circle can look very knotted, so the answer is not obvious.
Mathematicians know that a computer can always decide this, but they do not know whether it can be done quickly for large diagrams.
