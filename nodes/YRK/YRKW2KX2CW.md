---
tag: YRKW2KX2CW
kind: concept
name: Integro-differential equation
msc: [45J05]
sources:
  - url: https://en.wikipedia.org/wiki/Integro-differential_equation
same_as:
  wikidata: Q2380676
  wikipedia: Integro-differential equation
---

## Summary

An integro-differential equation involves both derivatives and integrals of the unknown function.
A typical form is $x'(t) = f(t, x(t)) + \int_{t_0}^{t} K(t, s, x(s)) \, ds$, in which the integral describes memory of the past.
Such equations appear in viscoelasticity, population dynamics with age structure, circuit theory and epidemiology.
They are studied with the Laplace transform, by turning them into integral equations, or as functional differential equations.

## Explanations

### L1 human

In an ordinary differential equation, the rate of change depends on the present state.
In an integro-differential equation, it can also depend on an accumulated total over the past.
In an electric circuit with a resistor, an inductor and a capacitor, the voltage across the capacitor is the integral of the current.
So the circuit law mixes the current, its derivative and its integral.
The equation $x'(t) = -\int_0^t x(s) \, ds$ with $x(0) = 1$ has the solution $x(t) = \cos t$.
