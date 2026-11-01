---
tag: HZM2ASCDY4
kind: concept
name: Ornstein–Uhlenbeck process
msc: [60J70, 60G15]
specializes: [22WEM6RTW0, 9HDQ094ADQ]
sources:
  - url: https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process
same_as:
  wikidata: Q1757587
  wikipedia: Ornstein–Uhlenbeck process
---

## Summary

The Ornstein–Uhlenbeck process is a Brownian motion with a pull back towards a long-run mean.
It solves the [[Langevin equation|ZW2RBS9VTR]] $dX_t = \theta(\mu - X_t) \, dt + \sigma \, dW_t$ with $\theta > 0$.
It is Gaussian, Markov and, from a suitable start, stationary, and it models velocities of particles, interest rates and mean-reverting quantities.

## Explanations

### L1 human

Think of a particle tied to the point $\mu$ by a spring, and kicked around at random.
The farther it strays, the harder the spring pulls it back, so it never wanders off for good.
In the long run its position is normally distributed around $\mu$, with spread set by the balance of kicks $\sigma$ and spring strength $\theta$.
Unlike Brownian motion, whose spread grows with time, this process settles into a steady random state.
