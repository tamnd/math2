---
tag: T4PGC6NH56
kind: definition
name: Sphere packing
msc: [52C17, 11H31, 05B40]
defines: HF32CBN5MA
uses: [0XPR1E85W0, 0Q0H13G8ZB, WN9V7WSJKF]
sources:
  - url: https://en.wikipedia.org/wiki/Sphere_packing
---

## Definition

Let $n \ge 1$ and let $r > 0$.
A *sphere packing* in the [[Euclidean space|0XPR1E85W0]] $\R^n$ with radius $r$ is a set $C \subset \R^n$ of centres such that $\abs{x - y} \ge 2r$ for all distinct $x, y \in C$.
The packing is the family of [[closed balls|0Q0H13G8ZB]] $B(x, r)$ with $x \in C$; their interiors are pairwise disjoint.
The packing is a *lattice packing* if $C$ is a [[lattice|WN9V7WSJKF]], or a translate of one.

## Remarks

Example: in $\R^2$ take $C = \Z^2$ and $r = \tfrac12$.
Two distinct integer points are at distance at least $1 = 2r$, so the discs of radius $\tfrac12$ centred at them form a lattice packing, the square packing.
Non-example: $C = \Z^2$ with $r = 0.6$; the points $(0, 0)$ and $(1, 0)$ are at distance $1 < 1.2$, so their discs overlap.
For a lattice $\Lambda$ with shortest nonzero vector of length $m$, the largest radius is $r = m/2$.
Some authors allow balls of different radii; the term "sphere packing" then refers to any family of balls with disjoint interiors.
