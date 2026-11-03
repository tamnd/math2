---
tag: 1708HMRRSW
kind: concept
name: Large eddy simulation
msc: [76F65]
sources:
  - url: https://en.wikipedia.org/wiki/Large_eddy_simulation
same_as:
  wikidata: Q1755722
  wikipedia: Large eddy simulation
---

## Summary

Large eddy simulation, or LES, is a method for computing [[turbulent|VY307F8Z0S]] flows that resolves the large eddies and models the small ones.
It applies a spatial low-pass filter to the [[Navier–Stokes equations|18KXZHVF4M]] and solves the filtered equations on a grid whose spacing is about the filter width.
The effect of the unresolved scales enters through a subgrid-scale stress that must be modelled, often by an eddy viscosity.
It sits between direct numerical simulation, which resolves all scales, and the Reynolds-averaged equations, which model all fluctuations.

## Explanations

### L1 human

A turbulent flow has eddies from the size of the whole flow down to tiny ones, and computing all of them is usually far too expensive.
The large eddies carry most of the energy and depend on the particular flow, while the small eddies behave in a more universal way.
Large eddy simulation computes the large eddies directly and replaces the small ones by a simple model of their average effect.
It was first developed by meteorologists, with Smagorinsky's model of 1963, to simulate the atmosphere.
