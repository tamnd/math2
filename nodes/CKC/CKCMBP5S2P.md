---
tag: CKCMBP5S2P
kind: concept
name: Mixed state
msc: ["81P16", "46N50"]
specializes: [4NQN47A92F]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_state
---

## Summary

A mixed state is a [[quantum state|4NQN47A92F]] that is not pure.
It is a [[density operator|V1JTB52E8C]] that is a nontrivial convex combination of pure states.
Mixed states describe a system whose preparation is only known statistically, and also the state of one part of an entangled larger system.
Unlike a classical mixture, a mixed state can be written as a mixture of pure states in many different ways.

## Explanations

### L1 human

Suppose a machine prepares a spin "up" or "down" at random, each with probability $1/2$, and does not tell which.
The best description of the spin is then a mixed state: the average $\frac12 \mathrm{diag}(1, 0) + \frac12 \mathrm{diag}(0, 1) = \frac12 I$.
This is different from the pure state $(1, 1)/\sqrt{2}$, an equal superposition, even though a vertical measurement gives "up" half of the time in both cases.
A measurement along a horizontal axis tells them apart: the superposition gives one result with certainty, the mixture gives each result half of the time.
