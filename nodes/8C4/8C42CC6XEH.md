---
tag: 8C42CC6XEH
kind: concept
name: Laplace transform methods in heat conduction
msc: [44A10, 35K05, "80A19"]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Summary

Laplace transform methods solve linear time-dependent heat conduction problems by applying the [[Laplace transform|0V49JEZW06]] in the time variable.
The transform turns the time derivative into multiplication by the transform variable $s$ and builds in the initial temperature.
What remains is a boundary value problem in space only, often an ordinary differential equation that can be solved in closed form.
The temperature is then recovered by the inverse transform, from tables or by contour integration.
The method suits semi-infinite bodies and time-dependent boundary data, where separation of variables does not apply directly.
A worked case is the [[Laplace transform method for the heat equation|WCSZYPBZY4]].
See the [[definition|B4460YC2MQ]].

## Explanations

### L1 human

Time is the awkward variable in a cooling problem, because the answer at each moment depends on the whole past.
The Laplace transform packs the whole time history of the temperature into a single function of a new variable $s$.
In this packed form the heat equation loses its time derivative and becomes an equation in space only.
One solves this simpler equation and then unpacks the answer.
Large $s$ corresponds to short times, so the method also gives good approximations shortly after heating begins.
