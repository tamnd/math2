---
tag: H4NXEY6QTZ
kind: concept
name: Wiener–Hopf method
msc: ["45E10", 47A68, "30E25"]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener%E2%80%93Hopf_method
same_as:
  wikidata: Q2079672
  wikipedia: Wiener–Hopf method
---

## Summary

The Wiener–Hopf method solves [[Wiener–Hopf equations|QYY4NMDY5H]] and boundary value problems whose conditions change type across a half-line.
It takes [[Fourier transforms|DPVM34ADZV]], so that functions supported on a half-line become functions holomorphic in a half-plane.
The key step factors the symbol of the problem into two factors.
One is holomorphic and nonzero in the upper half-plane, the other in the lower half-plane.
An argument with [[Liouville's theorem|0EHKVRF4J6]] then pins down the solution.
It was introduced by Norbert Wiener and Eberhard Hopf for integral equations on a half-line.
It is a standard tool in diffraction theory, radiative transfer and fracture mechanics.

## Explanations

### L1 human

A function that vanishes on the negative half-line has a Fourier transform that extends nicely to the upper half of the complex plane.
A function that vanishes on the positive half-line extends to the lower half.
The method rewrites the equation so that one side extends to the upper half-plane and the other side to the lower half-plane.
Since both sides are equal on the real line, together they form one function on the whole plane, which is then a polynomial by Liouville's theorem.
Reading off this polynomial gives the solution.
