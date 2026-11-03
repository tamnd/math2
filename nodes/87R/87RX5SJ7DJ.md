---
tag: 87RX5SJ7DJ
kind: concept
name: Multibody system
msc: ["70E55", "70E60"]
sources:
  - url: https://en.wikipedia.org/wiki/Multibody_system
same_as:
  wikidata: Q1917564
  wikipedia: Multibody system
---

## Summary

A multibody system is a mechanical system made of several bodies, usually rigid, connected by joints that restrict their relative motion.
Robots, vehicles, linkages, the human skeleton and spacecraft with moving parts are modelled as multibody systems.
Their equations of motion are large systems of ordinary differential equations, or differential-algebraic equations when the joints form closed loops.
Multibody dynamics studies how to set up and solve these equations efficiently.

## Explanations

### L1 human

Think of a robot arm: a chain of rigid links, each one joined to the next by a hinge or a sliding joint.
Each joint lets the two links move relative to each other in only some ways.
The whole arm is a multibody system, and its motion depends on the masses of the links, the joints and the forces of the motors.
A bicycle with its frame, fork and wheels is another example.
