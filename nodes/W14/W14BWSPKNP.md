---
tag: W14BWSPKNP
kind: example
name: Herschel–Bulkley fluid
msc: [76A05]
instance_of: [8DT9MB9V6R]
sources:
  - url: https://en.wikipedia.org/wiki/Herschel–Bulkley_fluid
same_as:
  wikidata: Q10862968
  wikipedia: Herschel–Bulkley fluid
---

## Example

A *Herschel–Bulkley fluid* has a yield stress $\tau_0 \ge 0$, a consistency $k > 0$ and a flow index $n > 0$.
In a simple shear flow with shear rate $\dot\gamma \ge 0$ and shear stress $\tau \ge 0$, its law is
$$\dot\gamma = 0 \text{ if } \tau \le \tau_0, \qquad \tau = \tau_0 + k \dot\gamma^{\,n} \text{ if } \dot\gamma > 0.$$
For $\dot\gamma > 0$ the apparent viscosity is $\tau / \dot\gamma = \tau_0 / \dot\gamma + k \dot\gamma^{\,n - 1}$.
Unless $\tau_0 = 0$ and $n = 1$, this depends on $\dot\gamma$, so the fluid is a [[non-Newtonian fluid|8DT9MB9V6R]].

## Remarks

The model contains the two simpler ones.
For $n = 1$ it is the [[Bingham plastic|FP202DPQ3D]].
For $\tau_0 = 0$ it is the [[power-law fluid|C6RVY7R8S6]].
For $\tau_0 = 0$ and $n = 1$ it is a Newtonian fluid with viscosity $k$.

## Explanations

### L1 human

Some materials, like mayonnaise or wet concrete, need a push before they flow, and once flowing they get thinner or thicker with speed.
The Herschel–Bulkley law combines a yield threshold with a power law for the flowing part.
It fits many pastes, slurries and foods better than either piece alone.
