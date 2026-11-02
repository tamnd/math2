---
tag: JCMTFY6HMA
kind: concept
name: Resolutivity of boundary functions
msc: [31B20, 31A25, 31B05]
sources:
  - url: https://en.wikipedia.org/wiki/Perron_method
---

## Summary

A function on the boundary of a bounded open set is resolutive when the Perron method gives a well-defined harmonic function from it.
This function is then the generalised solution of the [[Dirichlet problem|8D56GQ4AG8]] with that boundary function as data.
The Perron method squeezes the solution between an upper envelope built from [[superharmonic functions|X4V2S56YQQ]] and a lower envelope built from [[subharmonic functions|Z1MHMGFNFW]].
Resolutivity says that the two envelopes meet and give a [[harmonic function|0DEB0JMN0W]].
It is the right notion of "solvable data" for the generalised Dirichlet problem of the [[Perron method|AEZ7PPCNQS]], and it holds for every continuous boundary function.

## Explanations

### L1 human

Imagine trying to fit a soap film to a wire frame whose height is given by a function on the frame.
From above, press down with every "superharmonic lid" that stays above the frame; from below, push up with every "subharmonic floor" that stays below it.
If the lowest lid and the highest floor coincide, the data is resolutive, and the common surface is the answer.
On the unit disc, every continuous boundary function is resolutive, and the answer is its Poisson integral.
A boundary function that is $+\infty$ everywhere is not resolutive, because both envelopes are then $+\infty$.
