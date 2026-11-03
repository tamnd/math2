---
tag: FP202DPQ3D
kind: example
name: Bingham plastic
msc: [76A05]
instance_of: [8DT9MB9V6R]
sources:
  - url: https://en.wikipedia.org/wiki/Bingham_plastic
same_as:
  wikidata: Q863789
  wikipedia: Bingham plastic
---

## Example

A *Bingham plastic* is a fluid with a yield stress $\tau_0 > 0$ and a plastic viscosity $\mu_p > 0$.
In a simple shear flow with shear rate $\dot\gamma$ and shear stress $\tau$, its law is
$$\dot\gamma = 0 \text{ if } \abs{\tau} \le \tau_0, \qquad \tau = \tau_0 \sgn(\dot\gamma) + \mu_p \dot\gamma \text{ if } \dot\gamma \ne 0.$$
So the material does not flow at all until the stress exceeds $\tau_0$, and then the excess stress grows linearly with the shear rate.
For $\dot\gamma > 0$ the apparent viscosity is $\tau / \dot\gamma = \mu_p + \tau_0 / \dot\gamma$.
This depends on $\dot\gamma$ and tends to infinity as $\dot\gamma \to 0$, so a Bingham plastic is a [[non-Newtonian fluid|8DT9MB9V6R]].
It is the case $n = 1$ of the [[Herschel–Bulkley fluid|W14BWSPKNP]].

## Explanations

### L1 human

Toothpaste sits on a brush like a solid, yet flows out of the tube when you squeeze hard enough.
A Bingham plastic is the simplest model of this: below a threshold stress it does not move, and above the threshold it flows like an ordinary viscous fluid.
Mud, drilling fluids and some paints are modelled this way.
