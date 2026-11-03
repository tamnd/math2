---
tag: T4ZFKBZRYK
kind: concept
name: Computational fluid dynamics
msc: [76M20, 76M12, 76M10]
specializes: [B6E54YTR64]
sources:
  - url: https://en.wikipedia.org/wiki/Computational_fluid_dynamics
same_as:
  wikidata: Q815820
  wikipedia: Computational fluid dynamics
---

## Summary

Computational fluid dynamics, or CFD, is the branch of [[numerical analysis|B6E54YTR64]] that computes approximate solutions of the equations of fluid flow.
It replaces the [[Navier–Stokes|18KXZHVF4M]] or [[Euler equations|RW0JK9VDZE]] by a finite system of algebraic equations, using [[finite difference|X7HYEBA5SA]], [[finite volume|HGKN8E09RS]], [[finite element|98GZ9DVHTA]], spectral or particle methods.
Its mathematical questions are stability, consistency, convergence and the correct capture of shocks, boundary layers and turbulence.
It is used to design aircraft, cars, turbines and blood pumps, and to forecast the weather.

## Explanations

### L1 human

The equations of fluid flow are too hard to solve with pen and paper except in simple cases.
CFD cuts the space around an object into millions of small cells and tracks the flow in each cell, step by step in time.
Each step uses only simple arithmetic, which a computer can do very fast.
The art is to choose the cells and the rules so that the computed flow stays close to the real one and does not blow up.
