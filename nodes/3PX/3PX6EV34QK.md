---
tag: 3PX6EV34QK
kind: concept
name: Mixed-integer linear program
msc: [90C11, 90C10]
sources:
  - url: https://en.wikipedia.org/wiki/Integer_programming
---

## Summary

A mixed-integer linear program (MILP) is a [[linear program|VNMXB0J2KA]] in which some of the variables, but not necessarily all, must take integer values.
It contains linear programs (no integer variables) and pure [[integer programs|9GX3WH5EQF]] (all variables integer) as special cases.
Integer variables model discrete choices such as opening a facility, while continuous variables model quantities such as amounts shipped.
Many practical optimization models in logistics, energy and scheduling are MILPs, solved by [[branch and cut|AJ786D5KK7]] solvers.

## Explanations

### L1 human

Some decisions are whole-number choices, such as "build a warehouse or not", and others are amounts, such as "how many tonnes to ship".
A mixed-integer linear program has both kinds of variables, linked by linear conditions, and a linear cost to minimize or profit to maximize.
For example, a link that can carry goods only if it is built is modelled by $0 \le x \le 100 y$ with $y \in \set{0, 1}$.
When $y = 0$ nothing flows, and when $y = 1$ up to $100$ units flow.
