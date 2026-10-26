---
tag: ~fca8ea5d
kind: statement
role: theorem
name: Continuous bijection from a compact space to a Hausdorff space is a homeomorphism
msc: [54D30]
uses: [~775d2019, ~436de6d7, ~5764c01f, ~0e10d672, ~30e373fc]
sources:
  - url: https://en.wikipedia.org/wiki/Homeomorphism
    locator: Properties
---

## Statement

Let $X$ be a [[compact space|~68153d33]], let $Y$ be a [[Hausdorff space|~a1fe0c25]] and let $f \colon X \to Y$ be a [[continuous map|~18b16c9f]] that is [[bijective|0SNQEF7Z53]].
Then $f$ is a [[homeomorphism|~0e10d672]].

## Remarks

Proof: it is enough to show that $f$ maps closed sets to closed sets. A closed $F \subseteq X$ is compact because [[closed subsets of compact sets are compact|~436de6d7]]. Then $f(F)$ is compact, and thus closed in $Y$ by [[compact subsets of a Hausdorff space are closed|~775d2019]].
The compactness is needed: the map $t \mapsto (\cos t, \sin t)$ from $[0, 2\pi)$ to the unit circle is a continuous bijection, but its inverse is not continuous.

## Explanations

### L1 human

For compact spaces, you do not need to check that the inverse map is continuous: it comes for free.
This is a quick way to show that two compact spaces have the same shape.
