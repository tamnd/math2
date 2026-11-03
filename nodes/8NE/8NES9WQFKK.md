---
tag: 8NES9WQFKK
kind: definition
name: Minimum phase system
msc: [93C80, 93C05]
defines: 7PWB4YS8PA
uses: [NSGTEGWZY0, 86JKV3TRFD, 6J9MPVHSMF, BMY8QZSD9H]
sources:
  - url: https://en.wikipedia.org/wiki/Minimum_phase
---

## Definition

Let $G$ be a proper real rational [[transfer function|86JKV3TRFD]] of a continuous-time single-input single-output [[linear time-invariant system|6J9MPVHSMF]], not identically zero.
The system is *minimum phase* if all its [[poles and zeros|NSGTEGWZY0]] have negative real part.
A discrete-time system with proper rational transfer function $G(z)$ is *minimum phase* if all its poles and zeros satisfy $\abs{z} < 1$.

## Remarks

Some authors require only the condition on the zeros, or allow zeros on the imaginary axis; the condition on the poles then says separately that the system is stable.
If $G$ is minimum phase and $G(s)$ has a nonzero limit as $\abs{s} \to \infty$, then $1/G$ is again proper, stable and minimum phase.
For a minimum phase $G$, the phase of the [[frequency response|BMY8QZSD9H]] $G(i\omega)$ is determined by the gain $\abs{G(i\omega)}$ through Bode's gain-phase relation.

Example: $G(s) = (s + 1)/(s + 2)$ has the pole $-2$ and the zero $-1$, both with negative real part, so it is minimum phase.

Non-example: $G(s) = (1 - s)/(1 + s)$ is stable but has the zero $1$, so it is not minimum phase.
For real $\omega$, $\abs{G(i\omega)} = 1$, the same gain as the constant $1$, but its phase is $-2 \arctan \omega$, which lags further and further behind.
