---
tag: 4MR28ZN5ZK
kind: concept
name: Routhian mechanics
msc: [70H03, 70H33]
sources:
  - url: https://en.wikipedia.org/wiki/Routhian_mechanics
same_as:
  wikidata: Q7371608
  wikipedia: Routhian mechanics
---

## Summary

Routhian mechanics is a mixed formulation of mechanics that treats some coordinates in the Lagrangian way and the others in the Hamiltonian way.
It is used mainly when some coordinates are [[cyclic|TGC5C62HYE]], so that their momenta are conserved.
The Routhian replaces the Lagrangian, the conserved momenta become constants, and the problem reduces to fewer degrees of freedom.
It combines ideas of [[Lagrangian mechanics|47JMCBM3VJ]] and [[Hamiltonian mechanics|MPM0RHWCN6]].
See the [[definition|44N4JB99W1]].

## Explanations

### L1 human

Some coordinates of a system do not appear in the Lagrangian at all, for example the angle of a planet around the Sun.
The momentum that goes with such a coordinate never changes.
The Routhian is a new function in which this momentum is a fixed number, so the coordinate can be dropped from the problem.
For a planet, this leaves an equation for the distance $r$ alone, with an extra term $p_\varphi^2/(2 m r^2)$ that acts like a centrifugal barrier.
After solving for $r$, one recovers the angle by a single integration.
