---
tag: 0430ETCMKD
kind: statement
role: theorem
name: Continuous bijection from a compact space to a Hausdorff space is a homeomorphism
msc: [54D30]
uses: [0MYFJVMN7M, 066HW6D9A7, 0K9AAJ8G51, 05GZ11PWRY, 0B8GPXFSP7]
sources:
  - url: https://en.wikipedia.org/wiki/Homeomorphism
    locator: Properties
---

## Statement

Let $X$ be a [[compact space|0QPHW703PV]], let $Y$ be a [[Hausdorff space|0MXB4CKHFW]] and let $f \colon X \to Y$ be a [[continuous map|0SY9ECQ19Q]] that is [[bijective|0SNQEF7Z53]].
Then $f$ is a [[homeomorphism|05GZ11PWRY]].

## Remarks

Proof: it is enough to show that $f$ maps closed sets to closed sets. A closed $F \subseteq X$ is compact because [[closed subsets of compact sets are compact|066HW6D9A7]]. Then $f(F)$ is compact, and thus closed in $Y$ by [[compact subsets of a Hausdorff space are closed|0MYFJVMN7M]].
The compactness is needed: the map $t \mapsto (\cos t, \sin t)$ from $[0, 2\pi)$ to the unit circle is a continuous bijection, but its inverse is not continuous.

## Explanations

### L1 human

For compact spaces, you do not need to check that the inverse map is continuous: it comes for free.
This is a quick way to show that two compact spaces have the same shape.
