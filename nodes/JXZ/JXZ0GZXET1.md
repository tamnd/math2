---
tag: JXZ0GZXET1
kind: concept
name: Control theory
msc: [93A10, 93C15, 93B52]
sources:
  - url: https://en.wikipedia.org/wiki/Control_theory
same_as:
  wikidata: Q6501221
  wikipedia: Control theory
---

## Summary

Control theory is the branch of mathematics that studies how to influence a dynamical system through inputs that can be chosen.
Its basic object is the [[control system|ZPDTVZQN5K]], a system whose evolution depends on a control.
It asks whether the state can be steered anywhere ([[controllability|A9WFM77Z4P]]) and whether it can be recovered from measurements ([[observability|C4HN3EAQWM]]).
It also asks how to make the system stable by [[feedback|7NYES2D0Z4]], and how to steer it in the best way ([[optimal control|T3V6ZNAMDN]]).
It uses linear algebra, differential equations, complex analysis and optimization, and it underlies much of engineering.

## Explanations

### L1 human

A thermostat is a small controller: it measures the room temperature and switches the heating on or off to keep the temperature near a target.
Control theory makes this idea precise for any system that changes in time and can be pushed by an input.
One models the system by equations, then designs a rule that chooses the input from what one measures.
For example, for the system $x' = x + u$ the state grows without control, but the rule $u = -2x$ gives $x' = -x$, and the state now decays to $0$.
