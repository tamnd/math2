---
tag: SSYN7X11MB
kind: concept
name: Initial value problem for a recurrence
msc: [39A05]
sources:
  - url: https://en.wikipedia.org/wiki/Recurrence_relation
---

## Summary

An initial value problem for a recurrence asks for a sequence that satisfies a given recurrence and has prescribed first terms.
For a recurrence of order $k$ in explicit form, prescribing $k$ initial values gives exactly one solution.
It is the discrete counterpart of the [[initial value problem|0FXDW992DS]] for ordinary differential equations.

## Explanations

### L1 human

A recurrence is a rule that builds each term of a sequence from the terms before it.
The rule alone does not tell you where to start.
An initial value problem fixes the starting terms, and then the rule produces everything else.
For example, $u_{n+1} = 2u_n$ with $u_0 = 3$ gives $3, 6, 12, 24, \dots$, that is $u_n = 3 \cdot 2^n$.
