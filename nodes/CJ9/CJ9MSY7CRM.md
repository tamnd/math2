---
tag: CJ9MSY7CRM
kind: concept
name: Coulomb wave function
msc: [33C15, 81Q05]
specializes: [6AZ4ZBN1M8]
sources:
  - url: https://en.wikipedia.org/wiki/Coulomb_wave_function
same_as:
  wikidata: Q17007968
  wikipedia: Coulomb wave function
---

## Summary

Coulomb wave functions are solutions of the Coulomb wave equation $u'' + \left( 1 - \frac{2\eta}{\rho} - \frac{L(L + 1)}{\rho^2} \right) u = 0$.
This equation is the radial part of the [[Schrödinger equation|EPZR6H2WJN]] for a charged particle in the field of a point charge.
The regular solution $F_L(\eta, \rho)$ vanishes at $\rho = 0$, and the irregular solution $G_L(\eta, \rho)$ does not.
Both are [[confluent hypergeometric functions|6AZ4ZBN1M8]] in disguise.

## Explanations

### L1 human

Without the charge, that is for $\eta = 0$, the equation describes a free wave, and for $L = 0$ its solutions are $\sin \rho$ and $\cos \rho$.
The term $2\eta / \rho$ adds the electric attraction or repulsion, and $L(L + 1)/\rho^2$ adds the effect of angular momentum.
Far from the origin the solutions still look like sine waves, but with a phase that drifts slowly like $\eta \log 2\rho$.
The regular function $F_L$ generalises $\sin \rho$, and the irregular function $G_L$ generalises $\cos \rho$.
