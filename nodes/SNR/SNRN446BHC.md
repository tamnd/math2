---
tag: SNRN446BHC
kind: concept
name: Order of a difference equation
msc: [39A05]
sources:
  - url: https://en.wikipedia.org/wiki/Recurrence_relation
---

## Summary

The order of a difference equation is the gap between the largest and the smallest index of the unknown sequence that occur in it.
When the equation can be solved for its highest term, the order is the number of initial values needed to fix a solution.
It plays the role that the order of a differential equation plays for derivatives.

## Explanations

### L1 human

A difference equation ties a term of a sequence to some terms before it.
The order counts how far back the equation looks.
The Fibonacci rule $u_{n+2} = u_{n+1} + u_n$ looks two steps back, so it has order $2$.
A rule like $u_{n+1} = 3 u_n$ looks only one step back and has order $1$.
To start a sequence of order $k$ you must choose its first $k$ terms by hand.
