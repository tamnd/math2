---
tag: RJSM2ZNV61
kind: concept
name: Underactuated system
msc: [70Q05, "93C10", "70E60"]
specializes: [ZPDTVZQN5K]
sources:
  - url: https://en.wikipedia.org/wiki/Underactuation
same_as:
  wikidata: Q7883433
  wikipedia: Underactuation
---

## Summary

An underactuated system is a controlled mechanical system with fewer independent control inputs than degrees of freedom.
The inputs cannot set all accelerations at will, so some motions can only be influenced through the dynamics.
Examples are the inverted pendulum on a cart, the Furuta pendulum, walking robots, aircraft and underwater vehicles.
Such systems are a main subject of nonlinear [[control|ZPDTVZQN5K]], because the methods for fully actuated robots do not apply to them directly.

## Explanations

### L1 human

A robot arm with a motor at every joint can push each joint as it likes, so it is fully actuated.
If some joints have no motor, they move only because the other parts pull on them, and the system is underactuated.
A child on a swing is an example.
The child cannot push the swing directly, but by moving the legs at the right times the child makes the swing go higher.
For a pendulum on a cart, one force on the cart must control two motions, the cart and the rod.
