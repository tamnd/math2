---
tag: BMY8QZSD9H
kind: concept
name: Frequency response
msc: [93C80, 93C05]
sources:
  - url: https://en.wikipedia.org/wiki/Frequency_response
same_as:
  wikidata: Q1054694
  wikipedia: Frequency response
---

## Summary

The frequency response of a [[linear time-invariant system|6J9MPVHSMF]] is its [[transfer function|86JKV3TRFD]] evaluated on the imaginary axis, $\omega \mapsto G(i\omega)$.
For a stable system it tells how a sinusoidal input of angular frequency $\omega$ is scaled and shifted in phase at steady state.
It is the starting point of the classical frequency-domain methods of control: [[Bode plots|EMVW7N54FE]], [[Nyquist plots|Z7SPHAWMDX]] and [[Nichols plots|V4178DP7FD]].

## Explanations

### L1 human

Shake a system gently back and forth at a fixed rate and wait until the start-up effects die out.
A linear system then shakes back at the same rate, only bigger or smaller and a little late.
The frequency response records, for each rate, how much bigger and how late.
For example, the system $y' = -y + u$ has $G(s) = 1/(s + 1)$; at $\omega = 1$ the gain is $\abs{G(i)} = 1/\sqrt{2}$ and the output lags by $45$ degrees.
