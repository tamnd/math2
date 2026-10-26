---
tag: 0MQQQ5NA2S
kind: statement
role: theorem
name: Compact Hausdorff spaces are normal
msc: [54D30]
uses: [0AJ646N339, 0QPHW703PV, 0MXB4CKHFW, 066HW6D9A7]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_space
    locator: Examples of normal spaces
---

## Statement

Let $X$ be a [[compact space|0QPHW703PV]] that is [[Hausdorff|0MXB4CKHFW]].
Then $X$ is [[normal|0AJ646N339]].

## Remarks

Proof sketch: closed subsets of $X$ are compact, by [[closed subsets of a compact set are compact|066HW6D9A7]]. In a Hausdorff space, a point and a disjoint compact set have disjoint open neighbourhoods. A second use of compactness separates two disjoint compact sets.
With [[Urysohn's lemma|01EY3VR7ZD]], this shows that compact Hausdorff spaces have many continuous real functions.

## Explanations

### L1 human

In a compact Hausdorff space, you first separate points by open sets, and then compactness lets you combine finitely many of these choices.
The result separates any two disjoint closed sets.
