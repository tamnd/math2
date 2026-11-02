---
tag: PVD7VZJZ9B
kind: concept
name: Transport equation
msc: [35F05, 35F10, 35L02]
specializes: [GC5BDZ6QBC]
sources:
  - url: https://en.wikipedia.org/wiki/Advection
---

## Summary

The transport equation $u_t + b \cdot \nabla u = 0$ says that a quantity $u$ is carried along by a flow of velocity $b$ without changing.
It is the simplest first-order [[partial differential equation|GC5BDZ6QBC]], also called the advection equation.
Its solutions are the initial profile moved along the flow.
It is the model problem for the [[method of characteristics|7XAPBCJK3B]] and for numerical schemes of hyperbolic equations.
See the [[definition|R3X5WFHV8P]].

## Explanations

### L1 human

Think of dye in a river that flows at constant speed.
If the dye does not spread out, the picture of the dye at a later time is the first picture shifted downstream.
The transport equation is the formula for this.
In one dimension, with speed $c$, it reads $u_t + c\, u_x = 0$, and its solutions are $u(x, t) = g(x - ct)$.
For example, a bump centred at $x = 0$ at time $0$ is centred at $x = 3c$ at time $3$.
