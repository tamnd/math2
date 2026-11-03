---
tag: J85Q7QGGHS
kind: concept
name: Matrix coefficient
msc: ["22D10", "43A65", "22C05"]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_coefficient
same_as:
  wikidata: Q4356506
  wikipedia: Matrix coefficient
---

## Summary

A matrix coefficient of a [[group representation|WYGRXCG2RN]] is a function on the group.
It is obtained by letting the group act on one vector and pairing the result with a linear functional.
For a finite-dimensional representation written in a basis, these are the entries of the matrices $\pi(g)$ and their linear combinations.
Matrix coefficients turn representations into functions, which is how representation theory enters harmonic analysis.
The [[Peter–Weyl theorem|6VC9QE39XH]] says that the matrix coefficients of a compact group are dense among its continuous functions.

## Explanations

### L1 human

A representation lets each group element act as a matrix.
Pick one entry, say the top left one, and watch how it changes as the group element varies: this gives a function on the group, a matrix coefficient.
For the circle group acting on $\C$ by $\theta \mapsto e^{i n \theta}$, the only entry is $e^{i n \theta}$ itself.
For rotations of the plane, the entries are $\cos \theta$ and $\pm \sin \theta$.
So matrix coefficients generalize the sines, cosines and exponentials of Fourier analysis.
