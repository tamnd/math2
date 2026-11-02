---
tag: A9WFM77Z4P
kind: concept
name: Controllability
msc: [93B05, 34H05]
sources:
  - url: https://en.wikipedia.org/wiki/Controllability
same_as:
  wikidata: Q1331104
  wikipedia: Controllability
---

## Summary

A [[control system|ZPDTVZQN5K]] is controllable if every state can be steered to every other state by a suitable choice of the control.
It is the first question of control theory: before asking how to steer well, one asks whether steering is possible at all.
For linear systems $x' = A x + B u$ it is decided by the [[Kalman rank condition|9NSCZ2KBEB]], and for systems without drift by the [[Chow–Rashevskii theorem|VQPN24VDH1]].

## Explanations

### L1 human

Imagine a cart on a rail that can be pushed forward or backward.
By pushing at the right times, one can bring it to any position with any velocity, so the cart is controllable.
If instead the push only acts on a second cart that is not attached to the first, the first cart cannot be moved, and the system is not controllable.
Controllability asks whether the inputs reach every direction of the state, directly or through the dynamics.
