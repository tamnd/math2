---
tag: PCMW7KN5P4
kind: concept
name: Inverse problem
msc: [35R30, 47A52, 65J22]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_problem
same_as:
  wikidata: Q1567213
  wikipedia: Inverse problem
---

## Summary

An inverse problem asks for the causes of observed effects: to recover the parameters of a model from measured data that the model produces.
The forward problem goes the other way and computes the data from known parameters.
Inverse problems are often ill-posed in the sense of Hadamard: small errors in the data can cause large errors in the answer.
So they need regularization.
Examples are medical imaging, seismic exploration of the Earth, and the [[Calderón problem|R8Y8DDTWBM]].

## Explanations

### L1 human

A doctor sees a CT scan, but the scanner only measures how much X-ray light passes through the body along many lines.
Turning those line measurements back into a picture of the inside is an inverse problem.
The forward direction, from body to measurements, is easy and stable.
The inverse direction can magnify noise: two very different pictures may give almost the same measurements.
A small example: knowing a function $y$, find $x = y'$; a tiny wiggle in $y$ can produce a huge wiggle in its derivative.
