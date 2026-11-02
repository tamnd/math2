---
tag: BSCYBP6AS6
kind: concept
name: Nonlinear integral equation
msc: [45G10]
specializes: [R3SG1SN7JQ]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Summary

A nonlinear integral equation is an [[integral equation|R3SG1SN7JQ]] that is not a [[linear integral equation|AYZCKG34QK]].
Typical forms are the Urysohn equation $\varphi(x) = f(x) + \int_a^b H(x, s, \varphi(s)) \, ds$ and the Hammerstein equation $\varphi(x) = f(x) + \int_a^b K(x, s) g(s, \varphi(s)) \, ds$.
They arise from nonlinear differential equations, such as initial value problems for $y' = F(x, y)$.
The main tools are fixed point theorems, such as the [[Banach fixed point theorem|0VK6VEH345]].

## Explanations

### L1 human

In a nonlinear equation the unknown function appears in a curved way, for example squared or inside a sine.
Then solutions cannot be added, and there may be no solution, one solution or several.
For example, $\varphi(x) = 1 + \int_0^x \varphi(s)^2 \, ds$ is the integral form of $y' = y^2$, $y(0) = 1$.
Its solution $\varphi(x) = 1/(1 - x)$ exists only for $x < 1$.
