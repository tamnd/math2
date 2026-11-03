---
tag: 5WG6YTAA6J
kind: concept
name: Momentum operator
msc: ["81Q10", "47B25"]
sources:
  - url: https://en.wikipedia.org/wiki/Momentum_operator
same_as:
  wikidata: Q692457
  wikipedia: Momentum operator
---

## Summary

The momentum operator is the [[observable|DF5RN297GE]] that corresponds to the [[momentum|37Q4BTJMXW]] of a particle.
On [[$L^2(\R)$|SASP14MA1Z]] it acts on smooth wave functions by $P\psi = -i\hbar\, \psi'$.
The [[Fourier transform|DPVM34ADZV]] turns it into multiplication by $\hbar k$, so it is self-adjoint with spectrum $\R$, like the [[position operator|7XAKGQQWTP]].
Position and momentum satisfy the canonical commutation relation, which leads to the uncertainty principle.

## Explanations

### L1 human

A wave $e^{ikx}$ wiggles faster when $k$ is larger, and in quantum mechanics faster wiggles mean more momentum, namely $\hbar k$.
The momentum operator reads off this rate by differentiation: $-i\hbar \frac{d}{dx} e^{ikx} = \hbar k\, e^{ikx}$.
A general wave function is a mixture of such waves, and its Fourier transform says how much of each momentum it contains.
A wave function that is narrow in space needs many different wiggle rates, so its momentum is spread out.
