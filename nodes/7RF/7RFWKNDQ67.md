---
tag: 7RFWKNDQ67
kind: concept
name: Switched system
msc: [93C30, 34A38]
specializes: [1EW58ZYR8Y]
sources:
  - url: https://en.wikipedia.org/wiki/Hybrid_system
---

## Summary

A switched system is a dynamical system made of several continuous-time subsystems.
A rule, the switching signal, selects which subsystem is active at each moment.
It is a [[hybrid system|1EW58ZYR8Y]] in which the state flows continuously and only the active vector field changes at the switching times.
Switched systems model power converters, gear changes, controllers that switch between several modes, and networks with changing links.
A main question is stability: switching between stable subsystems can produce an unstable motion, and conversely.

## Explanations

### L1 human

Think of a car with a gearbox: the engine and the car follow different equations in each gear, and the driver switches gears from time to time.
The position and speed of the car do not jump when the gear changes; only the rule of motion changes.
A switched system is any model of this kind, with a finite list of modes and a signal that picks the active mode.
For the two scalar modes $x' = -x$ and $x' = -2x$, every switching signal drives $x$ to $0$, since $x$ shrinks in both modes.
