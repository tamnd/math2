---
tag: HHKKPD81J2
kind: concept
name: Fermi–Dirac integral
msc: ["33E20", "33B30"]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_Fermi%E2%80%93Dirac_integral
same_as:
  wikidata: Q167476
  wikipedia: Complete Fermi–Dirac integral
---

## Summary

The complete Fermi–Dirac integral $F_j(x)$ is the integral $\frac{1}{\Gamma(j+1)} \int_0^\infty \frac{t^j}{e^{t-x} + 1} \, dt$.
It arises in the statistical physics of fermions, such as electrons in metals and semiconductors, where $x$ plays the role of a reduced chemical potential.
It is a [[polylogarithm|96CHDZKGQ0]] in disguise: $F_j(x) = -\operatorname{Li}_{j+1}(-e^x)$.

## Explanations

### L1 human

In a gas of electrons, the chance that a state of energy $t$ is filled is $1/(e^{t - x} + 1)$, a smooth step that falls from $1$ to $0$ near $t = x$.
Weighting this step by a power $t^j$ and integrating over all energies gives the Fermi–Dirac integral.
For $j = 0$ the integral can be done by hand and gives $\log(1 + e^x)$.
For very negative $x$ the step is almost an exponential, and $F_j(x)$ is close to $e^x$.
