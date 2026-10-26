---
tag: 0JF9KW2TXB
kind: definition
name: Regular space
msc: [54D15]
defines: 03HMJASQBQ
uses: [0CNQXVBHCX, 01ZQQDCERP, 0G5AV9Q4RR]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_space
    locator: Definitions
---

## Definition

A [[topological space|0CNQXVBHCX]] $X$ is regular when the property that follows holds.
For each [[closed set|0G5AV9Q4RR]] $F \subseteq X$ and each point $x \in X \setminus F$, there are [[open sets|01ZQQDCERP]] $U$ and $V$ with $x \in U$, $F \subseteq V$ and $U \cap V = \varnothing$.

## Remarks

Names vary. Some authors call a space T3 when it is regular and T0, and then it is also [[Hausdorff|0MXB4CKHFW]]. Other authors include this condition in the word regular.
Equivalently, $X$ is regular if and only if each neighbourhood of a point $x$ contains a closed neighbourhood of $x$.
Each metric space is regular. Each [[normal|0AJ646N339]] T1 space is regular.

## Explanations

### L1 human

In a regular space, you can separate a point from a closed set that does not contain it, by two disjoint open sets.
Hausdorff spaces only separate points from points.
