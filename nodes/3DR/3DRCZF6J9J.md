---
tag: 3DRCZF6J9J
kind: concept
name: Oscillatory solution of a difference equation
msc: [39A21]
sources:
  - url: https://en.wikipedia.org/wiki/Oscillation_theory
---

## Summary

A solution of a difference equation is oscillatory if it keeps changing sign, however far one goes along the sequence.
A solution that is eventually of one sign is called nonoscillatory.
Oscillation theory looks for conditions on the coefficients that force all solutions, or some solutions, to oscillate.
It is the discrete counterpart of the [[oscillation theory|ZH2S50NSZ6]] of differential equations, such as Sturm theory.

## Explanations

### L1 human

Watch the signs of the terms of a sequence.
If they settle down to always plus or always minus, the sequence does not oscillate.
If a sign change keeps happening again and again, it oscillates.
The solution $x_n = (-1)^n$ of $x_{n+1} = -x_n$ oscillates, while the solution $x_n = 2^n$ of $x_{n+1} = 2 x_n$ does not.
