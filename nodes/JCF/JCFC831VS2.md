---
tag: JCFC831VS2
kind: concept
name: Convolutional code
msc: [94B10]
sources:
  - url: https://en.wikipedia.org/wiki/Convolutional_code
same_as:
  wikidata: Q1395022
  wikipedia: Convolutional code
---

## Summary

A convolutional code encodes a stream of input symbols into a stream of output symbols by a linear filter with finite memory.
At each time step, $k$ input symbols enter and $n$ output symbols leave.
Each output is a fixed linear combination of the current and the last few inputs.
Algebraically it is the image of a $k \times n$ generator matrix over the ring of polynomials or power series in a delay variable $D$.
Convolutional codes are decoded efficiently by the [[Viterbi algorithm|356PTJ3R46]], and they are the building blocks of [[turbo codes|SGRYABP8D0]].

## Explanations

### L1 human

Think of a shift register holding the last few input bits.
Each new input bit is pushed in, and a few output bits are computed as sums modulo $2$ of chosen cells of the register.
For the classic rate $1/2$ code with generators $1 + D + D^2$ and $1 + D^2$, input bit $u_t$ produces the two output bits $u_t + u_{t-1} + u_{t-2}$ and $u_t + u_{t-2}$.
Unlike a [[block code|EFGYF9P0PN]], the input is not cut into independent blocks: each output depends on a sliding window of inputs.
