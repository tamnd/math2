---
tag: WFQV4R1EMN
kind: concept
name: Mehler–Fock transform
msc: [44A15, 44A20, 33C45]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Mehler%E2%80%93Fock_transform
same_as:
  wikidata: Q13577951
  wikipedia: Mehler–Fock transform
---

## Summary

The Mehler–Fock transform is an [[integral transform|YCK709QB06]] on the half-line $[1, \infty)$ whose kernel is a conical [[Legendre function|69XMERM6KJ]] $P_{-1/2 + i\tau}(x)$.
It is an index transform: the transform variable $\tau$ sits in the degree of the Legendre function, not in its argument.
It plays for the Legendre operator the role that the Fourier transform plays for $d^2/dx^2$.
It is used to solve boundary value problems for cones and in harmonic analysis on the hyperbolic plane.

## Explanations

### L1 human

The functions $P_{-1/2 + i\tau}$, one for each $\tau \ge 0$, are the basic waves of the Legendre differential operator on $[1, \infty)$.
The transform measures how much of each wave a function contains, as a Fourier transform measures frequencies.
The inverse transform adds the waves back with the right weights.
For example, the transform of the function equal to $1$ on $[1, 2]$ and $0$ elsewhere is $\int_1^2 P_{-1/2 + i\tau}(x)\, dx$, a smooth function of $\tau$.
