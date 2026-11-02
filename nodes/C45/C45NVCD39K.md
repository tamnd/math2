---
tag: C45NVCD39K
kind: concept
name: Matched Z-transform method
msc: [93C62, 44A55, 94A12]
sources:
  - url: https://en.wikipedia.org/wiki/Matched_Z-transform_method
same_as:
  wikidata: Q4678053
  wikipedia: Matched Z-transform method
---

## Summary

The matched Z-transform method turns a continuous-time filter with a rational transfer function into a discrete-time filter.
It sends each [[pole|066E7PJCYE]] and each zero $a$ in the $s$-plane to the point $e^{aT}$ in the $z$-plane, where $T$ is the sampling period.
Then it fixes the overall gain.
It is also called the pole–zero mapping method.
It keeps the poles exactly where sampling puts them, and it is simple to apply, but it can distort the frequency response.

## Explanations

### L1 human

A filter for continuous signals is described by its poles and zeros, points of the complex plane.
To build a digital version, one moves each of these points with the map $a \mapsto e^{aT}$, which is how sampling moves exponentials.
Then one scales the result so that, for example, constant signals pass with the same gain as before.
For $H(s) = 1/(s + 1)$ and $T = 0.1$, one gets $H(z) = k/(1 - e^{-0.1} z^{-1})$ with $k = 1 - e^{-0.1}$ for equal gain at $s = 0$, $z = 1$.
