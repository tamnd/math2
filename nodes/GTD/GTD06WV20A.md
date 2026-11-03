---
tag: GTD06WV20A
kind: concept
name: Multi-compartment model in pharmacokinetics
msc: [92C45, 34A30]
sources:
  - url: https://en.wikipedia.org/wiki/Multi-compartment_model
---

## Summary

A multi-compartment model divides the body into a few well-mixed compartments, such as blood and tissue, and follows the amount of a drug in each.
Drug moves between compartments and leaves the body at rates proportional to the amounts present.
This gives a linear system of [[ordinary differential equations|0NT64JV96A]], whose solutions are sums of exponentials.
Such models are the standard way to fit drug concentration curves and to plan doses.

## Explanations

### L1 human

Imagine a few connected tanks of water with dye.
Dye is poured into one tank, flows between tanks through pipes, and drains out through a hole.
Each flow is proportional to how much dye is in the tank it leaves.
Take a two-compartment model of a drug injected into the blood.
The concentration first falls fast while the drug spreads into the tissues, then falls slowly as it is eliminated.
On a log scale this gives two nearly straight pieces.
