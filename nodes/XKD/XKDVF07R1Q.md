---
tag: XKDVF07R1Q
kind: concept
name: Canonical coordinates
msc: [70H15, 53D05, 70G10]
sources:
  - url: https://en.wikipedia.org/wiki/Canonical_coordinates
same_as:
  wikidata: Q1501876
  wikipedia: Canonical coordinates
---

## Summary

Canonical coordinates are coordinates $(q_1, \ldots, q_n, p_1, \ldots, p_n)$ on a phase space in which the [[symplectic form|CAN490EPRT]] takes its standard form $\sum_i dp_i \wedge dq_i$.
In them the [[Poisson brackets|2S0MXDT4YH]] of the coordinates are $\{q_i, p_j\} = \delta_{ij}$ and all others vanish, and the equations of motion take the form of [[Hamilton's equations|CFYQ6R38YP]].
Darboux's theorem says that such coordinates exist near every point of a symplectic manifold.
See the [[definition|48BJAVECEN]].

## Explanations

### L1 human

In mechanics, positions and their momenta come in pairs, such as $x$ and $p_x$, or an angle and its angular momentum.
Canonical coordinates are any set of such pairs in which the laws of motion keep their standard Hamiltonian form.
The usual positions and momenta are canonical, but so are many less obvious choices.
For example, on the plane $(q, p)$ with $p > 0$, the pair $Q = \log p$, $P = -q p$ is again canonical.
Finding good canonical coordinates is often the key step in solving a mechanical problem.
