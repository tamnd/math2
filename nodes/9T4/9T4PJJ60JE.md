---
tag: 9T4PJJ60JE
kind: concept
name: Normalized Haar measure on a compact group
msc: [28C10, 43A05, 22C05]
specializes: [VY0HXD3GC4]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
---

## Summary

On a [[compact group|EVHCE5VR6Y]], every [[Haar measure|VY0HXD3GC4]] has finite total mass.
The normalized Haar measure is the unique Haar measure of total mass $1$, so it is a probability measure.
It is both left- and right-invariant, and it gives the natural notion of the average of a function over the group.
It is the measure used in the Peter–Weyl theorem and in the orthogonality relations for characters.

## Explanations

### L1 human

On a finite group, the fair way to choose an element at random is to give each element probability $1/n$, where $n$ is the order of the group.
The normalized Haar measure does the same for compact groups such as the circle or the rotation group.
On the circle it is arc length divided by $2\pi$, so a random point lands in an arc with probability equal to the arc's share of the full turn.
The average of a function over the group is its integral against this measure.
