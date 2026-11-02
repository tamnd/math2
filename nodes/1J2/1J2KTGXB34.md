---
tag: 1J2KTGXB34
kind: concept
name: Feedback linearization
msc: [93B18, 93C10]
sources:
  - url: https://en.wikipedia.org/wiki/Feedback_linearization
same_as:
  wikidata: Q672139
  wikipedia: Feedback linearization
---

## Summary

Feedback linearization transforms a nonlinear [[control system|ZPDTVZQN5K]] into a linear one by a change of state coordinates and a feedback law that cancels the nonlinearities.
After the transformation, the tools of linear control, such as eigenvalue placement, can be used to design a controller.
Exact conditions for it are given in terms of [[Lie brackets|68FGQEBD6J]] of the vector fields of the system.

## Explanations

### L1 human

Many machines obey nonlinear equations, which are hard to control directly.
If the input enters the equations in the right place, one can choose the input to cancel the nonlinear terms exactly.
What is left is a linear system, which is well understood.
For a pendulum $x_1' = x_2$, $x_2' = -\sin x_1 + u$, the choice $u = \sin x_1 + v$ gives $x_1' = x_2$, $x_2' = v$, a linear system in the new input $v$.
