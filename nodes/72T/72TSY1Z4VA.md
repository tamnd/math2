---
tag: 72TSY1Z4VA
kind: concept
name: Jacobi transform
msc: [44A20, 33C45]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_polynomials
---

## Summary

The Jacobi transform is a finite [[integral transform|YCK709QB06]] on $[-1, 1]$.
It sends a function to the sequence of its integrals against the [[Jacobi polynomials|TRD7DSF2KR]] $P_n^{(\alpha, \beta)}$ with their weight.
It is the coefficient map of the expansion of a function in Jacobi polynomials.
It turns the Jacobi differential operator into multiplication by $-n(n + \alpha + \beta + 1)$, so it is used to solve boundary value problems on an interval.
The Gegenbauer and Legendre transforms are special cases.

## Explanations

### L1 human

Jacobi polynomials are a family of polynomials that are orthogonal on $[-1, 1]$ for a weight that may favour one end of the interval.
Any reasonable function on $[-1, 1]$ can be written as a sum of these polynomials.
The Jacobi transform records the numbers that tell how much of each polynomial is needed.
For example, the transform of $P_2^{(\alpha, \beta)}$ itself is zero at every $n$ except $n = 2$.
A differential equation for the function becomes a simple algebraic equation for these numbers.
The same name is also used for a transform on the half-line with Jacobi functions as kernel; this node is about the finite transform.
