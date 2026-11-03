---
tag: FQD9YT0DRK
kind: concept
name: Kushner equation
msc: [60G35, "93E11", 60H15]
sources:
  - url: https://en.wikipedia.org/wiki/Kushner_equation
same_as:
  wikidata: Q6448080
  wikipedia: Kushner equation
---

## Summary

The Kushner equation, or Kushner–Stratonovich equation, is a stochastic differential equation for the conditional law of a hidden diffusion.
The conditioning is on noisy observations of the diffusion.
It solves the continuous-time nonlinear [[filtering problem|T97B6NBPA8]]: it tells how the best estimate of the hidden state changes as new observations arrive.
It is the normalized counterpart of the [[Zakai equation|FQ8TVSR74H]], and for linear Gaussian systems it reduces to the Kalman–Bucy filter.

## Explanations

### L1 human

Imagine a particle that moves at random, and a sensor that reports its position blurred by noise.
At each moment you hold a probability distribution that describes where the particle may be.
The Kushner equation says how this distribution changes in time.
It drifts and spreads as the particle itself would, and each new observation shifts weight toward the places that explain the observation better.
For example, if the particle stands still at an unknown point and the sensor reports that point plus noise, the distribution sharpens around the true point as data accumulates.
