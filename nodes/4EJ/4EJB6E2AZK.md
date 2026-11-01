---
tag: 4EJB6E2AZK
kind: concept
name: Semimartingale
msc: [60G48, 60H05]
specializes: [0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Semimartingale
same_as:
  wikidata: Q506346
  wikipedia: Semimartingale
---

## Summary

A semimartingale is a process that is the sum of a [[local martingale|XC2YPC2BSW]] and a process of finite variation.
Semimartingales are the largest natural class of integrators for stochastic integrals.
Brownian motion, Lévy processes and solutions of stochastic differential equations are semimartingales.

## Explanations

### L1 human

A semimartingale is "noise plus drift".
The noise part is a fair game, like Brownian motion, and the drift part changes in a tame way, like an ordinary function of bounded variation.
For example, a share price modelled as $X_t = W_t + 0.05\, t$ is a fair-game noise $W_t$ plus a steady drift.
Itô's formula and stochastic integration work for exactly this kind of process.
