---
tag: 3MWNBBG9EH
kind: concept
name: Jordan–Kinderlehrer–Otto scheme
msc: [49Q22, 35Q84, 35K05]
sources:
  - url: https://en.wikipedia.org/wiki/Wasserstein_metric
---

## Summary

The Jordan–Kinderlehrer–Otto scheme, or JKO scheme, is a time discretization of a gradient flow in the space of probability measures with the [[Wasserstein distance|VEY29CS26X]].
At each step it minimizes the energy plus a penalty for moving far, in Wasserstein distance, from the previous measure.
Richard Jordan, David Kinderlehrer and Felix Otto introduced it in 1998 and proved that it converges to solutions of the [[Fokker–Planck equation|FVQWR7NS00]].
It showed that the [[heat equation|VP2HN86VAG]] is the gradient flow of the entropy for the Wasserstein distance, and started the theory of Wasserstein gradient flows.

## Explanations

### L1 human

Imagine a drop of ink spreading in water.
The JKO scheme describes this spreading in small time steps.
At each step, the ink chooses a new distribution that lowers its energy, an entropy term that favours spreading out.
It also pays a cost for how far its mass has to travel.
When the steps become very short, the result is the heat equation, so diffusion is a way of decreasing entropy as fast as possible for the cost of moving mass.
