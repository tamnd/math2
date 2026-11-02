---
tag: 6D4EW91AJY
kind: statement
role: theorem
name: Capacitability of Borel sets
msc: [28A12, 31C15, 28A05]
uses: [25FRWWHFZV, 584GXXY73M, 0WQXY32Q8D, 3RWWZYPAFV, 0R6EWFKRCF]
about: [25FRWWHFZV]
sources:
  - url: https://en.wikipedia.org/wiki/Choquet_theory
---

## Statement

Let $X$ be a [[Polish space|584GXXY73M]] and let $I$ be a [[Choquet capacity|25FRWWHFZV]] on $X$.
Let $A \subseteq X$ be a Borel set, that is, a member of the [[Borel sigma-algebra|0WQXY32Q8D]] of $X$.
Then $A$ is capacitable for $I$:
$$I(A) = \sup \set{ I(K) : K \subseteq A, \ K \text{ compact} }.$$

## Remarks

The statement is a special case of Choquet's capacitability theorem, which gives the same conclusion for every [[analytic set|3RWWZYPAFV]] of $X$; every Borel subset of a Polish space is analytic.
Proof idea: an analytic set is the image of the space $\N^\N$ under a continuous map.
One uses the continuity of $I$ along increasing sequences to choose, coordinate by coordinate, a closed piece of $\N^\N$ whose image still has capacity close to $I(A)$.
The image of this piece is contained in a decreasing intersection of compact sets, and continuity along decreasing sequences of [[compact sets|0R6EWFKRCF]] finishes the proof.

Example: in $\R^n$ with $n \ge 3$, the outer Newtonian capacity is a Choquet capacity.
So for each Borel set $A$, inner and outer capacity agree: the capacity of $A$ can be computed from compact subsets or from open supersets with the same result.

The hypothesis on the set is needed in general.
Under the axiom of choice, some subsets of $\R$ have positive Lebesgue outer measure but contain no compact set of positive measure.
Lebesgue outer measure restricted to $[0, 1]$ is a Choquet capacity, so such sets are not capacitable.

## Explanations

### L1 human

A capacity measures size, but unlike a measure it is not additive, so it is not clear that the size of a set can be found from its compact pieces.
Choquet's theorem says that this works for every reasonable set: the size of a Borel set is the supremum of the sizes of the compact sets inside it.
This makes capacities usable in the same way as measures.

### L2 human

In potential theory the theorem shows that every Borel set has a well-defined capacity, given equally by compact subsets and by open supersets.
So statements such as "a Borel set of capacity zero is polar" do not depend on which of the two definitions is used.
In probability the same theorem, applied to the capacity given by the probability that a process hits a set, gives the measurability of hitting times of Borel sets.
