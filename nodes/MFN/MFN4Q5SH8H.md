---
tag: MFN4Q5SH8H
kind: concept
name: Rarefaction wave
msc: [35L65, 35L67, 76L05]
sources:
  - url: https://en.wikipedia.org/wiki/Rarefaction
---

## Summary

A rarefaction wave is a continuous solution of a [[conservation law|8RA7AMWSAF]] that spreads out from a point like a fan.
In the fan, the unknown takes every value between two states.
It is self-similar: it depends only on $x/t$.
It is the admissible solution when the characteristics on the two sides of a jump move apart.
In that case a [[shock wave|JSDMGGTG7G]] would violate the entropy condition.
Together with shocks and contact discontinuities, rarefaction waves are the building blocks of solutions of the [[Riemann problem|GJWKX22VVE]].
See the [[definition|MM6TXKN90V]].

## Explanations

### L1 human

When a traffic light turns green, the dense queue of cars does not leave as one block.
The front cars drive off fast, the cars behind start later, and the queue thins out gradually.
The density goes smoothly from jammed to free over a stretch of road that grows with time.
This spreading fan is a rarefaction wave.
For Burgers' equation with value $0$ on the left and $1$ on the right, it is $u(x, t) = x/t$ for $0 \le x \le t$.
