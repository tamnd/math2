---
tag: 3T5Q9WVQX8
kind: concept
name: Wave front set
msc: [35A18, 35A27, 58J47]
sources:
  - url: https://en.wikipedia.org/wiki/Wave_front_set
same_as:
  wikidata: Q7975304
  wikipedia: Wave front set
---

## Summary

The wave front set of a distribution records where the distribution fails to be smooth, and in which frequency directions it fails.
It is a closed subset of $\Omega \times (\R^n \setminus \set{0})$ that is conic in the second variable.
Its projection to $\Omega$ is the singular support, the set of points near which the distribution is not a smooth function.
It is the basic object of [[microlocal analysis|5B6WEQX7XK]] and the language of [[propagation of singularities|P2QJ7NPW3Y]].
See the [[definition|PF3G0J5JD6]].

## Explanations

### L1 human

A function with a jump along a line is rough at the points of the line, but only in one direction: across the line.
Along the line it looks perfectly regular.
The wave front set keeps track of this: at each bad point it lists the directions in which the function oscillates without control.
One finds these directions by cutting the function off near the point and checking in which directions the [[Fourier transform|DPVM34ADZV]] of the piece decays slowly.
For the jump function $H(x_1)$ in the plane, the bad points form the line $x_1 = 0$, and the bad directions there are $(\pm 1, 0)$, the two normal directions.
