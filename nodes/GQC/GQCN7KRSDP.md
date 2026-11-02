---
tag: GQCN7KRSDP
kind: problem
name: Goddard problem
msc: [49K15, 49N90, 70Q05]
uses: [7RPV2T29CF, 91RFB97TNV, GK1Z3Q1WRZ, 0NT64JV96A]
about: [T3V6ZNAMDN]
sources:
  - url: https://en.wikipedia.org/wiki/Goddard_problem
same_as:
  wikidata: Q5576265
  wikipedia: Goddard problem
history:
  posed_by: "Robert H. Goddard"
  first_stated: "1919"
---

## Problem

A rocket rises vertically from rest, with height $h(t)$, velocity $v(t)$ and mass $m(t)$.
Its thrust $T(t)$ is the control, with $0 \le T(t) \le T_{\max}$.
The motion follows the [[ordinary differential equations|0NT64JV96A]]
$$h' = v, \qquad v' = \frac{T - D(h, v)}{m} - g(h), \qquad m' = -\frac{T}{c},$$
where $D(h, v) \ge 0$ is the aerodynamic drag, $g(h) > 0$ is the gravitational acceleration and $c > 0$ is the exhaust speed.
The initial mass $m(0) = m_0$ and the mass $m_f < m_0$ of the empty rocket are given.
Choose the thrust program $T$ and the final time $t_f$, with $m(t_f) \ge m_f$, so that the final height $h(t_f)$ is as large as possible.

## Remarks

In this optimal control problem the control enters the dynamics linearly.
So the [[Pontryagin maximum principle|7RPV2T29CF]] does not by itself fix the thrust where the switching function vanishes.
With significant drag, optimal solutions can contain a [[singular arc|91RFB97TNV]] on which the thrust takes intermediate values, between arcs of full thrust and of zero thrust.
So the optimal control is not always [[bang-bang|GK1Z3Q1WRZ]], and the problem is a standard test case for singular controls.
Goddard raised the question in his 1919 work on rockets for reaching high altitudes.

## Explanations

### L1 human

A rocket has a fixed amount of fuel and wants to climb as high as possible.
Burning everything at once wastes fuel against air drag at high speed, while burning too slowly wastes fuel just holding the rocket up against gravity.
The best program balances these two losses, and in the optimum the engine may run at partial power for a while.
