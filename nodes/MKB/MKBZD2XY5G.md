---
tag: MKBZD2XY5G
kind: concept
name: Common midpoint stacking
msc: [86A22, 94A12]
sources:
  - url: https://en.wikipedia.org/wiki/Reflection_seismology
---

## Summary

Common midpoint stacking is the summation of reflection traces that share the same midpoint between source and receiver, after [[normal moveout|8E7KGS4ZQH]] correction.
For horizontal layers, these traces sample the same reflection point at different offsets, so their reflections line up after the correction and add up.
Random noise does not line up, so stacking $N$ traces improves the signal-to-noise ratio by about a factor $\sqrt{N}$.
The velocity that makes the stack strongest also gives an estimate of the seismic velocity, so stacking is a core step of reflection seismic processing.

## Explanations

### L1 human

A survey records the same spot underground many times, with source and receiver pairs at different distances but centred on the same point.
Each recording is noisy, and its echo arrives at a slightly different time.
After shifting the echoes to the same time, adding the recordings strengthens the echo and averages out the noise.
With $4$ recordings, the echo keeps its size, while the random noise in the average shrinks to half its size.
