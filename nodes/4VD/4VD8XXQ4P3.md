---
tag: 4VD8XXQ4P3
kind: concept
name: Dirichlet eigenvalue
msc: [35P15, 35P05, 35J05]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_eigenvalue
same_as:
  wikidata: Q5280763
  wikipedia: Dirichlet eigenvalue
---

## Summary

A Dirichlet eigenvalue of a bounded domain $\Omega$ is a number $\lambda$ such that $-\Delta u = \lambda u$ has a nonzero solution vanishing on the boundary.
These numbers form an increasing sequence of positive numbers that tends to infinity.
They are the squared frequencies of a vibrating membrane fixed along its edge.
They also control the decay of heat in $\Omega$ with zero boundary temperature.
How they depend on the shape of $\Omega$ is the subject of spectral geometry, with results such as the [[Faber–Krahn inequality|E7TY2TPXX7]].

## Explanations

### L1 human

Fix the edge of a drum and strike it.
The drum can vibrate only in certain patterns, and each pattern has its own pitch.
The Dirichlet eigenvalues are the squares of these pitches, up to a physical constant.
For the interval $(0, \pi)$, the patterns are $\sin(kx)$ and the eigenvalues are $1, 4, 9, 16, \dots$.
