---
tag: 1N7TZCPBF0
kind: concept
name: Abstract Volterra equation
msc: [45N05, 45D05, 47D06]
specializes: [DND8CBEVXT]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
---

## Summary

An abstract Volterra equation is a Volterra integral equation whose unknown takes values in a [[Banach space|06GZ956657]].
Its memory term involves a linear operator, often unbounded.
Its standard form is $u(t) = f(t) + \int_0^t a(t - s) A u(s) \, ds$ with a scalar kernel $a$ and a [[closed operator|VM7B38PA87]] $A$.
It contains abstract first-order and second-order evolution equations as the cases $a = 1$ and $a(t) = t$.
Other kernels model heat conduction and viscoelasticity with memory, where $A$ is a differential operator in space.

## Explanations

### L1 human

Many physical systems change in time according to a rule that involves their whole history.
When the state at each time is a function of space, such as a temperature profile, the state is a point of an infinite-dimensional space.
The abstract Volterra equation writes the rule as an integral over the past.
A weight $a$ says how strongly the past is remembered, and an operator $A$ acts in space.
If $a = 1$, all of the past counts equally, and the equation is the integrated form of $u' = A u$.
