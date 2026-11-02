---
tag: 7EFDMJSVDP
kind: concept
name: Whittaker function
msc: [33C15]
specializes: [6AZ4ZBN1M8]
sources:
  - url: https://en.wikipedia.org/wiki/Whittaker_function
same_as:
  wikidata: Q3754618
  wikipedia: Whittaker function
---

## Summary

The Whittaker functions $M_{\kappa, \mu}(z)$ and $W_{\kappa, \mu}(z)$ are solutions of Whittaker's equation $w'' + \left( -\frac14 + \frac{\kappa}{z} + \frac{\frac14 - \mu^2}{z^2} \right) w = 0$.
They are the [[confluent hypergeometric functions|6AZ4ZBN1M8]] rewritten so that the equation has no first derivative term.
This normal form is convenient in physics and in asymptotic analysis, and it makes the symmetry $\mu \mapsto -\mu$ visible.

## Explanations

### L1 human

Kummer's equation has a first derivative term; multiplying the unknown by $e^{-z/2} z^{b/2}$ removes it.
The result is Whittaker's equation, which looks like a Schrödinger equation with a constant, a Coulomb-type term $\kappa / z$ and a centrifugal-type term $(\frac14 - \mu^2)/z^2$.
The function $M_{\kappa, \mu}$ is the solution that behaves like $z^{\mu + 1/2}$ near $0$, and $W_{\kappa, \mu}$ is the solution that decays like $e^{-z/2} z^{\kappa}$ at $+\infty$.
A simple case is $W_{0, 1/2}(z) = e^{-z/2}$, which indeed satisfies $w'' - \frac14 w = 0$.
