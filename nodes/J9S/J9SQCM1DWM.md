---
tag: J9SQCM1DWM
kind: definition
name: Starred transform
msc: [44A55, 93C57, 44A10]
defines: 4YQ8JYXBKK
uses: [0V49JEZW06, 0KPHENZ5S7, EPG6JPVJE7, 7KHGQFM8A9]
sources:
  - url: https://en.wikipedia.org/wiki/Starred_transform
---

## Definition

Let $x \colon [0, \infty) \to \C$ be a function and let $T > 0$ be a sampling period.
The impulse-sampled signal is
$$x^*(t) = \sum_{n = 0}^{\infty} x(nT) \, \delta(t - nT),$$
where $\delta$ is the [[Dirac delta|0KPHENZ5S7]].
The *starred transform* of $x$ is the [[Laplace transform|0V49JEZW06]] of $x^*$:
$$X^*(s) = \sum_{n = 0}^{\infty} x(nT) \, e^{-nTs},$$
for the complex $s$ where this series converges absolutely.

## Remarks

The impulse-sampled signal is $x$ times a [[Dirac comb|7KHGQFM8A9]] of period $T$, restricted to $t \ge 0$.
If $X(z)$ is the [[unilateral Z-transform|EPG6JPVJE7]] of the samples $x_n = x(nT)$, then $X^*(s) = X(e^{sT})$.
Example: for $x(t) = e^{-at}$ with $a \in \C$, $X^*(s) = \sum_{n \ge 0} e^{-n T (s + a)} = 1/(1 - e^{-T(s + a)})$ for $\operatorname{Re}(s + a) > 0$.
Non-example: for $x(t) = e^{t^2}$ the terms $e^{n^2 T^2 - nTs}$ do not tend to $0$ for any $s$, so the series converges nowhere and $x$ has no starred transform.
$X^*$ is periodic in the imaginary direction: $X^*(s + 2\pi i/T) = X^*(s)$, since $e^{-nT \cdot 2\pi i/T} = 1$.
