---
tag: ATSXD280T1
kind: definition
name: Sphere bundle
msc: [55R25, 55R10]
defines: 3VQ2V5HH3R
uses: [CX4M8K61AB, T62369RFH6]
sources:
  - url: https://en.wikipedia.org/wiki/Sphere_bundle
---

## Definition

Let $k \ge 0$ be an integer.
A *sphere bundle* with fiber $S^k$ is a [[fiber bundle|CX4M8K61AB]] $\pi \colon E \to B$ whose fiber is the [[$k$-sphere|T62369RFH6]] $S^k$.

## Remarks

Many authors also require the structure group to be the orthogonal group $O(k+1)$ acting on $S^k$, so that the transition functions are rotations and reflections.
The main example: let $V \to B$ be a real vector bundle of rank $k + 1$ with a continuous inner product.
Then the unit sphere bundle $S(V) = \set{v \in V : \abs{v} = 1}$ is a sphere bundle with fiber $S^k$ and structure group $O(k+1)$.
A sphere bundle with fiber $S^1$ is called a circle bundle.

Example: the unit tangent bundle of $S^2$, the set of pairs $(x, v)$ with $x, v \in S^2$ and $v \perp x$, is a circle bundle over $S^2$.
Its total space is homeomorphic to $\R P^3$.

Non-example: the Möbius band over the circle is a fiber bundle, but its fiber is a closed interval, not a sphere, so it is not a sphere bundle.
Its boundary, however, is a sphere bundle with fiber $S^0$: it is the connected double cover of the circle.
