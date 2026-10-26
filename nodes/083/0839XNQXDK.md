---
tag: 0839XNQXDK
kind: definition
name: Intersection of a family of sets
aliases: [indexed-intersection, arbitrary-intersection]
msc: ["03E20"]
defines: 0ZNMMA9TF5
uses: [05Q6G4EH2G, 0B88PQTJ66, 0HBRW4E6G1]
sources:
  - url: https://en.wikipedia.org/wiki/Intersection_(set_theory)
    locator: Arbitrary intersections
---

## Definition

Let $(A_i)_{i \in I}$ be a [[family of sets|05Q6G4EH2G]] with a nonempty index set $I$.
The intersection of the family is the set
$$\bigcap_{i \in I} A_i = \{x \mid \forall i \in I, \, x \in A_i\}.$$
So $x$ is an element of the intersection when $x \in A_i$ for each $i \in I$.

## Remarks

For $I = \{1, 2\}$, this is the [[intersection|0HBRW4E6G1]] $A_1 \cap A_2$.
For an empty index set, the condition is [[vacuously true|0V4QXPGJQK]] for each $x$.
So the intersection is defined only relative to a [[universal set|0BPYRMHJ48]] $U$, and it is $U$.
Example: $\bigcap_{n \ge 1} (-1/n, 1/n) = \{0\}$ in $\mathbb{R}$.

## Explanations

### L1 human

The intersection of a family keeps only the elements that are in every member of the family.
It generalizes $A \cap B$ from two sets to any number of sets.
