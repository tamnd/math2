---
tag: B219G9SHJA
kind: concept
name: Stochastic differential equation
msc: [60H10, 34F05]
specializes: [003R0V5M7V]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_differential_equation
same_as:
  wikidata: Q1545585
  wikipedia: Stochastic differential equation
---

## Summary

A stochastic differential equation describes a quantity whose change in a short time is a drift plus a random kick.
The kick is proportional to the increment of a [[Wiener process|22735FGJV6]].
It is written $dX_t = b(t, X_t) \, dt + \sigma(t, X_t) \, dW_t$ and is made precise as an integral equation with an Itô integral from [[Itô calculus|JA95NH206E]].
Such equations model stock prices, noisy physical systems, and population sizes under random effects, and their solutions are diffusion processes.

## Explanations

### L1 human

An ordinary differential equation tells a particle exactly where to go next.
A stochastic differential equation adds a random push at each moment, built from the jittery path of Brownian motion.
The drift $b$ says where the particle tends to move, and the coefficient $\sigma$ says how strong the noise is.
For example, the solution of $dX_t = X_t \, dW_t$ with $X_0 = 1$ is $X_t = e^{W_t - t/2}$, not $e^{W_t}$, because the rules of calculus change for such rough paths.
