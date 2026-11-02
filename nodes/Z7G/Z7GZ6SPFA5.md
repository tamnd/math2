---
tag: Z7GZ6SPFA5
kind: concept
name: Spectral theory of dynamical systems
msc: [37A30, 37A35, 37A05]
sources:
  - url: https://en.wikipedia.org/wiki/Koopman%E2%80%93von_Neumann_classical_mechanics
---

## Summary

The spectral theory of dynamical systems studies a [[measure-preserving transformation|556WBDAHNP]] through the spectrum of its [[Koopman operator|37TRG5DBQC]] on $L^2$.
Two systems with unitarily equivalent Koopman operators are called spectrally isomorphic, and properties preserved by this relation are spectral invariants.
Ergodicity, weak mixing, mixing and discrete spectrum are spectral invariants.
The theory is complete for ergodic systems with discrete spectrum, by the [[Halmos–von Neumann theorem|AS18AWFXSB]].
In general, spectral data do not determine a system up to isomorphism.

## Explanations

### L1 human

The idea goes back to Koopman and von Neumann, who described classical mechanics by a linear operator on a Hilbert space, as in quantum mechanics.
One then asks which frequencies the system has: an eigenfunction with eigenvalue $e^{2\pi i \theta}$ is a measurement that turns like a clock at frequency $\theta$.
A rotation of the circle has many such clocks; a strongly chaotic system has none besides the constants.
Spectral data are easy to compute but coarse: the [[Kolmogorov–Sinai entropy|X1D1C7VH6P]] separates systems that the spectrum cannot.
