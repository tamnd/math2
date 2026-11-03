---
tag: CJW50K5HZB
kind: concept
name: Material derivative
msc: [76A02]
sources:
  - url: https://en.wikipedia.org/wiki/Material_derivative
same_as:
  wikidata: Q1801562
  wikipedia: Material derivative
---

## Summary

The material derivative of a field is its rate of change seen by a fluid parcel that moves with the flow.
For a field $f$ and a velocity field $\mathbf{u}$ it equals $\partial f / \partial t + \mathbf{u} \cdot \nabla f$.
It links the [[Lagrangian and Eulerian descriptions|5E6K4ATM9W]] of a flow.
It appears in every law of motion of a continuum, such as the acceleration term of the [[Navier–Stokes equations|18KXZHVF4M]].

## Explanations

### L1 human

Suppose you ride a balloon carried by the wind and you read a thermometer.
The temperature you see changes for two reasons: the weather changes in time, and the wind carries you to warmer or colder places.
The material derivative adds these two effects.
For example, let the temperature be $T = x$ (warmer to the east) at all times, and let the wind blow east at speed $2$.
Then your thermometer rises at rate $2$.
