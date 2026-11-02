---
tag: BKXYBS57T9
kind: concept
name: Dynamic equation on time scales
msc: [34N05, "26E70"]
sources:
  - url: https://en.wikipedia.org/wiki/Time-scale_calculus
---

## Summary

A dynamic equation on a time scale is an equation that involves the delta derivative of an unknown function.
The function lives on a time scale $\mathbb{T}$, a nonempty closed subset of $\R$.
It is the basic object of [[time-scale calculus|30G1M35TK1]].
On $\mathbb{T} = \R$ it is an [[ordinary differential equation|0NT64JV96A]], and on $\mathbb{T} = \Z$ it is a [[recurrence relation|0FYX44GP92]], so one theory covers both cases at once.

## Explanations

### L1 human

Some quantities change continuously, others change in steps, and some do both.
A time scale is the set of times at which the quantity lives, for example all reals, all integers, or a union of intervals.
A dynamic equation tells how the quantity changes from each time to the next one, using a derivative where time flows and a difference quotient across each gap.
For example, the equation $x^\Delta = x$ with $x(0) = 1$ has the solution $e^t$ on $\R$ but $2^t$ on $\Z$, since on $\Z$ it says $x(t + 1) - x(t) = x(t)$.
