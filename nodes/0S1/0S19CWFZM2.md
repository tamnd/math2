---
tag: 0S19CWFZM2
kind: statement
role: corollary
name: Size of an orbit times the size of the stabiliser
msc: [20B05]
uses: [0E2HSCKZ6C, 3C53TD, 04DC0SRN2K]
sources:
  - url: https://en.wikipedia.org/wiki/Group_action
    locator: Orbit–stabilizer theorem
---

## Statement

Let a finite [[group|G5S1M9]] $G$ [[act|0WCY42EV9V]] on a set $X$, and let $x \in X$.
Then $|G \cdot x| \cdot |G_x| = |G|$.
In particular, the size of each [[orbit|0YQPZB5Q1G]] divides $|G|$.

## Remarks

This follows from the [[orbit-stabiliser theorem|0E2HSCKZ6C]] and from $[G : G_x] \cdot |G_x| = |G|$, which is [[Lagrange's theorem|3C53TD]].
For example, the rotation group of a cube acts transitively on the $6$ faces, and the stabiliser of a face has $4$ elements. So the group has order $24$.

## Explanations

### L1 human

Each point of the orbit is reached by exactly $|G_x|$ group elements.
So the group elements are counted by the orbit size times the stabiliser size.
This is a good way to compute the order of a symmetry group.
