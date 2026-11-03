---
tag: FQ8TVSR74H
kind: concept
name: Zakai equation
msc: [60G35, 60H15, "93E11"]
sources:
  - url: https://en.wikipedia.org/wiki/Zakai_equation
same_as:
  wikidata: Q8064995
  wikipedia: Zakai equation
---

## Summary

The Zakai equation is a linear [[stochastic partial differential equation|PRCQG82QTK]] for the unnormalized conditional distribution of a hidden diffusion process given noisy observations.
It is a central equation of nonlinear filtering: normalizing its solution gives the solution of the [[filtering problem|T97B6NBPA8]].
Moshe Zakai derived it in 1969.
Because it is linear, it is easier to analyse and to solve numerically than the nonlinear [[Kushner equation|FQD9YT0DRK]] for the normalized conditional distribution.

## Explanations

### L1 human

A hidden particle wanders randomly, and one sees only a noisy signal that depends on its position.
The question is how the probability cloud describing where the particle might be changes as the signal comes in.
The Zakai equation answers this for a version of the cloud that is not scaled to total mass one.
Between observations the cloud spreads and drifts with the particle's motion, and each new piece of signal reweights it toward the places that explain the signal best.
