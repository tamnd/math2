---
tag: K6QV4WSTXX
kind: concept
name: Linear recurrence with polynomial coefficients
msc: [39A06, 33F10]
specializes: [0FYX44GP92]
sources:
  - url: https://en.wikipedia.org/wiki/Holonomic_function
---

## Summary

A linear recurrence with polynomial coefficients relates consecutive terms of a sequence linearly, with coefficients that are polynomials in the index $n$.
It generalizes the [[linear recurrences with constant coefficients|0NDVHBVBXB]] and covers many sequences of combinatorics, such as factorials, Catalan numbers and harmonic numbers.
The sequences that satisfy such a recurrence are the [[holonomic sequences|NWKX329T01]], and their generating functions are [[holonomic functions|7H44JD9NQD]].
Computer algebra uses these recurrences as finite descriptions of infinite sequences.

## Explanations

### L1 human

In the Fibonacci rule $u_{n+2} = u_{n+1} + u_n$, the coefficients are fixed numbers.
Here the coefficients may grow with $n$, like the factor $n + 1$ in $u_{n+1} = (n+1) u_n$.
That rule, started at $u_0 = 1$, produces the factorials $1, 1, 2, 6, 24, \dots$.
The rule is still linear: the terms of the sequence are only multiplied by known quantities and added.
