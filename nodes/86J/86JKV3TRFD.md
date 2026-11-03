---
tag: 86JKV3TRFD
kind: concept
name: Transfer function
msc: [93C05, 93C80]
sources:
  - url: https://en.wikipedia.org/wiki/Transfer_function
same_as:
  wikidata: Q334269
  wikipedia: Transfer function
---

## Summary

The transfer function of a [[linear time-invariant system|6J9MPVHSMF]] is the [[Laplace transform|0V49JEZW06]] of its [[impulse response|3X3SYVM7R5]].
It turns the convolution that relates input and output into a product: $Y(s) = G(s) U(s)$.
For systems given by linear differential equations with constant coefficients it is a [[rational function|0XDK9CGYKJ]] of $s$.
Its poles and zeros describe stability and the response to oscillating inputs.
It is the central tool of classical control and of the frequency-domain methods of [[control theory|JXZ0GZXET1]].

## Explanations

### L1 human

A transfer function is a formula that says how a system changes each input "frequency".
In the Laplace domain the messy convolution becomes a simple multiplication, so connecting systems in series multiplies their transfer functions.
For example, the system $y' = -y + u$ has transfer function $G(s) = 1/(s + 1)$.
At $s = 0$ this gives $G(0) = 1$, which says that a constant input $u = 1$ leads in the long run to the output $y = 1$.
