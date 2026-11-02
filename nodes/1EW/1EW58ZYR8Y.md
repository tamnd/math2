---
tag: 1EW58ZYR8Y
kind: concept
name: Hybrid system
msc: [34A38, 93C30]
sources:
  - url: https://en.wikipedia.org/wiki/Hybrid_system
same_as:
  wikidata: Q2665508
  wikipedia: Hybrid system
---

## Summary

A hybrid system is a dynamical system whose state has a continuous part and a discrete part, called the mode.
The continuous part flows by [[ordinary differential equations|0NT64JV96A]], and the mode changes by jumps.
In each mode the continuous state follows its own [[vector field|0299VCW1TH]].
When it reaches a switching condition, the mode changes and the continuous state may be reset.
Hybrid systems model mechanical systems with impacts, digital controllers acting on physical plants, and switching circuits.

## Explanations

### L1 human

A thermostat is the classic picture.
The room temperature changes smoothly, but the heater is either on or off, and it switches when the temperature crosses a threshold.
A bouncing ball is another example: it falls smoothly under gravity, and at each impact its velocity jumps from downward to upward.
A hybrid system is any model that mixes such smooth motion with sudden switches.
