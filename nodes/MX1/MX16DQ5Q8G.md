---
tag: MX16DQ5Q8G
kind: concept
name: Suspension flow
msc: [37C10, 37A10, 37B02]
sources:
  - url: https://en.wikipedia.org/wiki/Mapping_torus
---

## Summary

The suspension flow of an invertible map turns a discrete-time system into a continuous-time flow.
Each point moves up at unit speed along a vertical segment whose height is given by a positive roof function.
At the top it jumps to the base above the image point.
The original map is recovered as the first-return map of the flow to the base.
Suspensions with constant roof $1$ give the natural flow on the mapping torus.
Suspensions with general roofs are a standard way to build examples of flows and to reduce flows to maps.

## Explanations

### L1 human

Picture each point $x$ of a space sitting at the bottom of a vertical stick of height $r(x)$.
A particle starts at the bottom of the stick, climbs at speed one, and when it reaches the top it is moved to the bottom of the stick over $T(x)$.
Watching only the moments when particles are at the bottom shows the map $T$ step by step.
For example, with $T$ a rotation of a circle and $r = 1$, the space of all sticks is a torus, and the flow is a linear flow winding around it.
