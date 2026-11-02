---
tag: FVQWR7NS00
kind: concept
name: Fokker–Planck equation
msc: [35Q84, 60J60]
sources:
  - url: https://en.wikipedia.org/wiki/Fokker%E2%80%93Planck_equation
same_as:
  wikidata: Q891766
  wikipedia: Fokker–Planck equation
---

## Summary

The Fokker–Planck equation is the parabolic equation for the probability density of a [[diffusion process|9HDQ094ADQ]].
Let $X_t$ solve a [[stochastic differential equation|B219G9SHJA]] with drift $\mu$ and diffusion coefficient $\sigma$.
Then its density $p(x, t)$ obeys a linear second-order equation built from $\mu$ and $\sigma\sigma^T$.
Its spatial operator is the adjoint of the [[infinitesimal generator|VPA41PWRR1]] of the process, which is why it is also called the forward Kolmogorov equation.
It links stochastic processes with partial differential equations.

## Explanations

### L1 human

Release many particles that drift with a velocity field and are also kicked by random noise.
The Fokker–Planck equation describes how the cloud of particles moves and spreads.
The drift term transports the density, and the noise term makes it diffuse.
For pure noise in one dimension, $dX = dW$, the equation is $p_t = \frac{1}{2} p_{xx}$, a [[heat equation|VP2HN86VAG]].
