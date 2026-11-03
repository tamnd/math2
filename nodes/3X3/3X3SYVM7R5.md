---
tag: 3X3SYVM7R5
kind: concept
name: Impulse response
msc: [93C05, 94A12]
sources:
  - url: https://en.wikipedia.org/wiki/Impulse_response
same_as:
  wikidata: Q1139726
  wikipedia: Impulse response
---

## Summary

The impulse response of a [[linear time-invariant system|6J9MPVHSMF]] is its output when the input is a unit impulse.
The unit impulse is the [[Dirac delta|0KPHENZ5S7]] in continuous time, and the sequence that is $1$ at time $0$ and $0$ elsewhere in discrete time.
It determines the system completely: the output for any input is the [[convolution|2Z29JN3VES]] of the input with the impulse response.
Its [[Laplace transform|0V49JEZW06]] is the [[transfer function|86JKV3TRFD]].
Properties of the system, such as causality and stability, can be read off from it.

## Explanations

### L1 human

Hit a bell once with a hammer and record the sound: that recording is the impulse response of the bell.
Since the bell responds linearly and the same way at every time, any way of striking it is a sum of single hits at different times and strengths.
So the sound for any striking pattern is a sum of shifted and scaled copies of that one recording.
For the system $y(t) = \int_{-\infty}^{t} e^{-(t - s)} u(s) \, ds$, the impulse response is $e^{-t}$ for $t \ge 0$ and $0$ for $t < 0$.
