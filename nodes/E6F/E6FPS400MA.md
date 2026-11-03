---
tag: E6FPS400MA
kind: concept
name: Chemostat model
msc: [92C70, 92D25, 34C60]
sources:
  - url: https://en.wikipedia.org/wiki/Chemostat
---

## Summary

A chemostat is a bioreactor in which fresh medium flows in at a constant rate.
Culture flows out at the same rate, so the volume stays constant.
The chemostat model is a system of [[ordinary differential equations|0NT64JV96A]] for the nutrient and the biomass in the vessel.
It shows a threshold: if the dilution rate is too high the microbes wash out, and otherwise they settle at a positive steady state.
It is a basic model of microbial ecology and competition for a single resource.

## Explanations

### L1 human

Think of a tank of bacteria with a tap that adds food at a steady rate and a drain that removes liquid at the same rate.
The bacteria eat the food and multiply, but the drain keeps carrying some of them away.
If they cannot grow faster than the drain removes them, they disappear.
If they can, the population and the food level settle at fixed values, where growth exactly balances the loss through the drain.
