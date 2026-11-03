---
tag: 3DNDHFASZQ
kind: definition
name: Optical parametric amplifier
msc: [78A60]
defines: 8K67PTYTJ7
uses: [7N71T3FKZ6, J7NEMSG2MD]
sources:
  - url: https://en.wikipedia.org/wiki/Optical_parametric_amplifier
---

## Definition

Let a medium have second-order [[nonlinear susceptibility|7N71T3FKZ6]] $\chi^{(2)} \ne 0$.
Let a strong *pump* wave of frequency $\omega_p$ and a weak *signal* wave of frequency $\omega_s < \omega_p$ enter it together.
Let $\omega_i = \omega_p - \omega_s$ be the frequency of a third wave, the *idler*.
An *optical parametric amplifier* is such a medium in which the three-wave process $\omega_p = \omega_s + \omega_i$ is [[phase matched|J7NEMSG2MD]].
In it, energy flows from the pump to the signal and the idler.

## Remarks

Assume perfect phase matching, an undepleted pump, and no idler at the input.
Then the signal amplitude grows as $\cosh(g z)$ along the medium, where the gain $g$ is proportional to $\chi^{(2)}$ and to the pump amplitude.
The idler amplitude grows as $\sinh(g z)$.

Example: a pump at $\omega_p$ and a signal at $\omega_s = 0.6\,\omega_p$ in a phase-matched crystal give an idler at $\omega_i = 0.4\,\omega_p$, and both the signal and the idler grow.

Non-example: second-harmonic generation in the same crystal is not parametric amplification.
There energy flows from the low frequency $\omega$ to $2\omega$, and no weak input wave is amplified.

An optical parametric amplifier placed in a resonant cavity is an optical parametric oscillator.
