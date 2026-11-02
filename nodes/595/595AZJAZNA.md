---
tag: 595AZJAZNA
kind: concept
name: Potential operator of a Markov process
msc: [60J45, 60J35]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_kernel
---

## Summary

The potential operator of a Markov process integrates the transition semigroup over all times.
Applied to the indicator of a set, it gives the expected total time that the process spends in that set.
It is the probabilistic analogue of the Newtonian potential, and formally it inverts minus the generator of the process.
Its finiteness distinguishes transient processes from recurrent ones.

## Explanations

### L1 human

Start a random particle at a point and ask how long, in total over its whole life, it will spend inside a given region.
The potential operator answers this question, on average, for every starting point and every region.
For Brownian motion in three-dimensional space the answer is finite for bounded regions, because the particle drifts away for good.
In the plane the particle keeps coming back, and the expected time in any disc is infinite.
