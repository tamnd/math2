---
tag: QVREFP7BH7
kind: concept
name: H-infinity norm of a system
msc: [93B36, 93C05, 30H10]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy_space
---

## Summary

The H-infinity norm of a stable linear time-invariant system is the largest factor by which the system can amplify the energy of an input signal.
For a system with [[transfer function|86JKV3TRFD]] matrix $G$ it is the supremum over all frequencies of the largest [[singular value|09VMDSRXWJ]] of $G(i\omega)$.
It is the norm of the [[Hardy space|PNNNFJVF6W]] $H^\infty$ of bounded analytic functions on the right half-plane.
It is the quantity minimized in [[H-infinity control|E3WZ90H2XQ]] and bounded in the [[small-gain theorem|1CF728E75M]].

## Explanations

### L1 human

Feed a stable system with sine waves of every frequency and see how much each one is amplified.
The H-infinity norm is the worst amplification, the height of the highest peak of the gain curve in the [[Bode plot|EMVW7N54FE]].
For $G(s) = 1/(s + 1)$, the gain at frequency $\omega$ is $1/\sqrt{1 + \omega^2}$, largest at $\omega = 0$, so the norm is $1$.
A small H-infinity norm means that no input, however it is shaped, can be blown up much.
