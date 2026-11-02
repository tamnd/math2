---
tag: J0EVKMWT94
kind: statement
role: theorem
name: Tait conjectures
msc: [57K10, 57K14]
uses: [QYEAZTYGPT, SWJZ4QRF9W, 4SPC17FPXE]
about: [QYEAZTYGPT, SWJZ4QRF9W]
sources:
  - url: https://en.wikipedia.org/wiki/Tait_conjectures
same_as:
  wikidata: Q7676466
  wikipedia: Tait conjectures
---

## Statement

A diagram of a [[knot|QYEAZTYGPT]] is *alternating* if the crossings alternate between over and under along the knot.
It is *reduced* if no crossing can be removed by turning one side of the diagram over, that is, it has no nugatory crossing.
Let $K$ be a knot that has an alternating diagram.

1. Every reduced alternating diagram of $K$ has $c(K)$ crossings, where $c(K)$ is the [[crossing number|SWJZ4QRF9W]] of $K$.
2. Any two reduced alternating diagrams of $K$ have the same writhe.
3. If $K$ is prime, then any two reduced alternating diagrams of $K$ are related by a finite sequence of flypes.

## Remarks

Part 1 was proved in 1987 by Kauffman, Murasugi and Thistlethwaite, independently, with the [[Jones polynomial|4SPC17FPXE]].
Part 2 was proved soon after, also with polynomial invariants.
The key fact is that the span of the Jones polynomial is at most the number of crossings of any connected diagram, with equality for reduced alternating diagrams.
Part 3, the flyping conjecture, was proved by Menasco and Thistlethwaite.
Example: the standard diagram of the [[figure-eight knot|C01XBGAHC6]] is reduced and alternating, so its crossing number is $4$ and its writhe $0$ is the same in every reduced alternating diagram.
The hypothesis that the diagram is reduced is needed: adding a nugatory kink keeps a diagram alternating but adds a crossing.
Part 2 shows that an alternating knot with a reduced alternating diagram of nonzero writhe is not isotopic to its mirror image.

## Explanations

### L1 human

Peter Guthrie Tait made knot tables in the nineteenth century and guessed some rules about alternating drawings.
In such a drawing, travelling along the knot you go over, under, over, under, and so on.
The first rule says that a clean alternating drawing already uses the fewest possible crossings.
The second says that all clean alternating drawings of one knot have the same twist count.
The third says that they are all related by a simple local flip, the flype.

### L2 human

The theorems make the tabulation of alternating knots possible: crossing number is read off any reduced alternating diagram, and diagrams can be compared through flypes.
The proof of part 1 is an early triumph of the Jones polynomial and of the [[Kauffman bracket|JYKVYS4N32]] state sum.
For a reduced alternating diagram, the extreme states of the bracket each contribute a single monomial that cannot cancel.
The writhe result gives a quick test for chirality of alternating knots.
For non-alternating knots, finding the crossing number is much harder.
