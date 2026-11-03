---
tag: J39ZSFW0YF
kind: concept
name: Gain and phase margin
msc: [93C80, 93D09, 93B35]
sources:
  - url: https://en.wikipedia.org/wiki/Phase_margin
---

## Summary

The gain margin and the phase margin of a feedback loop measure how far its loop [[frequency response|BMY8QZSD9H]] stays from the critical point $-1$.
The gain margin is the factor by which the loop gain can grow before the loop reaches the edge of instability.
The phase margin is the extra phase lag that the loop can take at the frequency where its gain is $1$.
Both are read from a [[Bode plot|EMVW7N54FE]] or a [[Nyquist plot|Z7SPHAWMDX]], and they are the classical measures of robustness in control design.

## Explanations

### L1 human

A feedback loop becomes unstable when a signal goes around the loop and comes back with the same size and turned upside down.
The margins say how far the loop is from that situation.
The gain margin answers: how much louder could the loop be?
The phase margin answers: how much more delay could it take?
Engineers often aim for a phase margin of a few tens of degrees.
