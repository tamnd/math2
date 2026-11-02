---
tag: BZK7HQDMT0
kind: concept
name: Particle filter
msc: [62M20, 65C35, 60G35]
sources:
  - url: https://en.wikipedia.org/wiki/Particle_filter
same_as:
  wikidata: Q1151499
  wikipedia: Particle filter
---

## Summary

A particle filter is a Monte Carlo method that tracks the hidden state of a dynamical system from noisy observations.
It represents the conditional distribution of the current state given the observations so far by a cloud of weighted samples, called particles.
At each time step the particles are moved by the system dynamics, reweighted by how well they explain the new observation, and resampled.
It works for nonlinear and non-Gaussian state-space models, such as [[hidden Markov models|HJVM390354]] with continuous states, where exact filtering formulas are not available.

## Explanations

### L1 human

Think of tracking a robot that you cannot see directly, using only a noisy sensor.
You scatter many guesses of where the robot might be.
When the robot moves, you move every guess in the same way, with some random jitter.
When a sensor reading arrives, guesses that agree with it get more weight, and guesses that disagree get less.
Then you copy the heavy guesses and drop the light ones, and the cloud of guesses follows the robot.
