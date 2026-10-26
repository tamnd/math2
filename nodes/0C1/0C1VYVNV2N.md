---
tag: 0C1VYVNV2N
kind: object
name: pi
aliases: [archimedes-constant]
msc: [11Y60, 33B10]
uses: [0WB57D9488, 00KAFBR32E, 0V2DV29EGT]
sources:
  - url: https://en.wikipedia.org/wiki/Pi
    locator: Definition
same_as:
  wikidata: Q167
  wikipedia: Pi
---

## Description

The cosine function has exactly one zero in the interval $[0, 2]$. The number $\pi$ is twice this zero.
So $\cos(\pi/2) = 0$, and
$$\pi \approx 3.14159265.$$

## Remarks

A zero exists by the [[intermediate value theorem|00KAFBR32E]], since $\cos 0 = 1$ and $\cos 2 < 0$. It is unique because $\cos$ is strictly decreasing on $[0, 2]$, by [[its derivative|0V2DV29EGT]] $-\sin$.
With this definition, $\pi$ is the ratio of the circumference of a circle to its diameter, and the area of the unit disc.
Mathlib defines `Real.pi` in the same way, as twice the zero of $\cos$ in $[1, 2]$.
William Jones first used the letter $\pi$ for this ratio, in 1706. Around 250 BC, Archimedes approximated $\pi$ with regular polygons.

## Explanations

### L1 human

The number $\pi$ is the length of half of the unit circle.
In analysis, we find it through the first positive zero of cosine, which is $\pi/2$.
