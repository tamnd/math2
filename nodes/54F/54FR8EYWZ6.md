---
tag: 54FR8EYWZ6
kind: definition
name: Climate model
msc: [86A08, 86A10, 35Q86]
defines: M49PQ7BDYN
uses: [18KXZHVF4M, EX9YYRMAJA, GC5BDZ6QBC, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Climate_model
---

## Definition

A *climate model* is a mathematical model of the climate system, given by:

1. state variables, such as temperature, velocity, humidity, salinity and ice cover, for one or more components (atmosphere, ocean, land, ice, biosphere);
2. [[ordinary|0NT64JV96A]] or [[partial differential equations|GC5BDZ6QBC]] for these variables, from conservation of mass, momentum and energy, with radiation to space;
3. prescribed external forcings, such as the incoming solar radiation and the atmospheric concentrations of greenhouse gases, or equations for them.

The climate predicted by the model is the statistics of its solutions over long times, rather than a single trajectory.

## Remarks

Example: a general circulation model of the atmosphere solves the primitive equations on a grid over the globe.
These approximate the [[Navier–Stokes equations|18KXZHVF4M]] for a thin layer on a rotating sphere, and are coupled with the [[radiative transfer equation|EX9YYRMAJA]].
It meets clause 1 with fields on the grid, clause 2 with the primitive equations and the energy equation, and clause 3 with the solar input and the gas concentrations.

Non-example: a statistical fit of observed temperatures against time is not a climate model, since it has no evolution equations derived from conservation laws (clause 2 fails).

Processes too small for the grid, such as clouds and turbulence, enter through parameterisations, which express their average effect in terms of the resolved variables.
