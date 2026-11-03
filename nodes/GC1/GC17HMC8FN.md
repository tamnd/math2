---
tag: GC17HMC8FN
kind: concept
name: Chaplygin's equation
msc: [76N15, 76H05, 35M10]
sources:
  - url: https://en.wikipedia.org/wiki/Chaplygin%27s_equation
same_as:
  wikidata: Q5073247
  wikipedia: Chaplygin's equation
---

## Summary

Chaplygin's equation is the linear partial differential equation of steady planar potential flow of a gas in hodograph variables.
These variables are the speed and the flow angle.
It comes from the [[hodograph transformation|9AR4ZZRRAM]], which turns the nonlinear equations of compressible flow into linear ones.
The equation is elliptic where the flow is subsonic and hyperbolic where it is supersonic.
So it is a basic model of mixed type, related to the [[Tricomi equation|21DD2334NR]].
It is named after Sergey Chaplygin, who used it to study gas jets.
See the [[definition|PTFTEAFZ7G]].

## Explanations

### L1 human

The flow of air past a wing is described by nonlinear equations, which are hard to solve.
If one uses the speed and the direction of the flow as coordinates instead of the position, the equation becomes linear.
Then solutions can be added and built from simple pieces, as for sound waves or heat flow.
The equation changes character at the speed of sound: below it behaves like Laplace's equation, above it like a wave equation.
For instance, any function of the flow angle alone of the form $A\theta + B$ is a solution, and it describes a swirling vortex flow.
