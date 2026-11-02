---
tag: PF5HS26Q0H
kind: definition
name: Lattice polytope
msc: [52B20, 11P21]
defines: F39N9NBFPZ
uses: [300K6CB1KH, R7V3S9V891, WN9V7WSJKF]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_polytope
---

## Definition

A *lattice polytope* in $\R^n$ is a [[convex polytope|300K6CB1KH]] $P \subseteq \R^n$ all of whose [[vertices|R7V3S9V891]] lie in $\Z^n$.
Equivalently, $P$ is the convex hull of a finite subset of $\Z^n$.

## Remarks

Example: the triangle with vertices $(0,0)$, $(3,0)$, $(0,2)$ is a lattice polygon, since all three vertices have integer coordinates.

Non-example: the triangle with vertices $(0,0)$, $(1,0)$, $(0, 1/2)$ is not a lattice polygon, since the vertex $(0, 1/2)$ is not in $\Z^2$.
It is a rational polytope: its vertices lie in $\Q^2$.

More generally, for a [[lattice|WN9V7WSJKF]] $\Lambda \subseteq \R^n$, a lattice polytope with respect to $\Lambda$ is a convex polytope with all vertices in $\Lambda$.
A linear change of coordinates turns $\Lambda$ into $\Z^n$, so the case $\Lambda = \Z^n$ is the standard one.
Two lattice polytopes are usually regarded as the same when an affine map $x \mapsto Ax + b$ with $A \in GL_n(\Z)$ and $b \in \Z^n$ carries one onto the other.
