---
tag: RSZS9SFFZ7
kind: example
name: Fuller's phenomenon
msc: [49K15, 49J15, 93C15]
instance_of: [6K8Q2YERTF]
uses: [6K8Q2YERTF, GK1Z3Q1WRZ, 7RPV2T29CF]
sources:
  - url: https://en.wikipedia.org/wiki/Bang–bang_control
---

## Example

*Fuller's problem* is the optimal control problem
$$\text{minimize } \int_0^\infty x_1(t)^2 \, dt \quad \text{subject to } x_1' = x_2, \; x_2' = u, \; \abs{u(t)} \le 1, \; x(0) = \xi,$$
where $\xi \in \R^2$ is a given nonzero initial state and $u$ is a measurable control.
For every $\xi \ne 0$ the optimal control is [[bang–bang|GK1Z3Q1WRZ]] with $u = \pm 1$.
It switches infinitely many times, and the switching times accumulate at a finite time $t^*$, at which the state reaches the origin.
After $t^*$ the optimal control is $u = 0$ and the state stays at the origin.
So the optimal control is a [[chattering control|6K8Q2YERTF]].
This behaviour is called *Fuller's phenomenon*.

## Remarks

A scaling argument explains the pattern.
If $(x_1(t), x_2(t), u(t))$ is admissible, then so is $(\lambda^2 x_1(t/\lambda), \lambda x_2(t/\lambda), u(t/\lambda))$ for every $\lambda > 0$, and its cost is multiplied by $\lambda^5$.
So the optimal feedback is invariant under this scaling, and the time between two switches shrinks by a fixed factor at each switch.
The intervals then form a geometric series with finite sum, which gives the finite time $t^*$.
The optimal feedback has the form $u = -\sgn(x_1 + C x_2 \abs{x_2})$ for a certain constant $C > 0$.
Necessary conditions of [[Pontryagin's maximum principle|7RPV2T29CF]] together with this scaling are the main tools of the analysis.

## Explanations

### L1 human

A cart on a rail is pushed by a force that can be at most one in either direction.
The goal is to keep the cart's position close to zero in total, measured by the integral of the squared position.
The best strategy pushes at full force, alternating direction, with shorter and shorter pushes.
Infinitely many switches happen before the cart comes to rest at zero, after a finite time.
This shows that optimal controls can be surprisingly wild even for very simple systems.
