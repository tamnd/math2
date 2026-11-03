---
tag: VSBFY8EN2H
kind: concept
name: Effective medium approximations
msc: [74Q15, "74E30", 78A48]
specializes: [5RSREPYN0F]
sources:
  - url: https://en.wikipedia.org/wiki/Effective_medium_approximations
same_as:
  wikidata: Q2894695
  wikipedia: Effective medium approximations
---

## Summary

Effective medium approximations are explicit formulas for the effective property of a composite, such as its conductivity or stiffness.
They use the properties and volume fractions of its phases.
The exact effective property is defined by [[homogenization|5RSREPYN0F]] and depends on the whole geometry of the microstructure, so it is rarely computable in closed form.
Effective medium approximations replace this geometry by a simple model, for example spherical grains surrounded by an averaged medium.
Classical examples are the Maxwell Garnett formula, the Bruggeman formula and the [[Mori–Tanaka method|F79NNVV0B1]].

## Explanations

### L1 human

Mix copper powder into rubber and ask how well the mixture conducts electricity.
Each grain sees a complicated neighbourhood, but from far away the mixture behaves like one uniform material.
An effective medium approximation guesses the conductivity of that uniform material by a formula.
For example, the Bruggeman formula pictures each grain as a ball sitting in the uniform medium it is trying to describe.
It then asks that the disturbances of all grains cancel on average.
