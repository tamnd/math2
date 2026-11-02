---
tag: QQ98C2AXZP
kind: concept
name: Heaviside operational calculus
msc: [44A45]
specializes: [8050R3Z6HA]
sources:
  - url: https://en.wikipedia.org/wiki/Operational_calculus
---

## Summary

The Heaviside operational calculus is the formal method of Oliver Heaviside for linear differential equations, developed for electrical circuits.
The derivative $d/dt$ is written as a symbol $p$.
The response of a system to a unit step input is written as a function of $p$ applied to the step.
This expression is then expanded and interpreted by fixed rules.
The method gave correct answers long before it was justified; the [[Laplace transform|0V49JEZW06]] and the [[Bromwich integral|5KNAXNHRY6]] later explained why.

## Explanations

### L1 human

Heaviside treated "differentiate" as a letter $p$ that can be multiplied, divided and expanded like a number.
Dividing by $p$ means integrating from time $0$.
A circuit switched on at time $0$ is then described by a fraction in $p$, and expanding that fraction gives the current or voltage as a function of time.
For example, the expression $1/(1 - a/p)$ applied to the unit step expands to $1 + a t + a^2 t^2/2 + \cdots = e^{at}$.
