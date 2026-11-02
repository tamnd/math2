---
tag: A15BF6QHDR
kind: concept
name: Riemann domain over C^n
msc: [32D26]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Summary

A Riemann domain over $\C^n$ is a connected space that lies over $\C^n$ through a [[local homeomorphism|MDH71ZZ8XX]], possibly with several sheets over the same point.
It is the several-variable analogue of a Riemann surface spread over the plane.
Riemann domains are needed because analytic continuation of a holomorphic function can lead to several values over one point.
The envelope of holomorphy of a domain in $\C^n$ is in general a Riemann domain and not a subset of $\C^n$.

## Explanations

### L1 human

Imagine several transparent copies of a region of $\C^n$, stacked on top of each other and glued along some cuts, like a spiral staircase.
Over each point of $\C^n$ there may be several points of the staircase, but near each of its points the staircase looks exactly like an open set of $\C^n$.
For example, the map $(w, z_2) \mapsto (e^w, z_2)$ from $\C^2$ to $\C^2$ makes $\C^2$ into a Riemann domain over $\C^2$ with infinitely many sheets over each point with $z_1 \ne 0$.
On this domain the logarithm of $z_1$ becomes a single-valued function, namely $w$.
