---
tag: JE1Z920QKT
kind: problem
name: Three-body problem
msc: [70F07, 37N05, 70F15]
uses: [0NT64JV96A, 0EDKGA2FAK, 62SNWC5E45]
about: [62SNWC5E45]
sources:
  - url: https://en.wikipedia.org/wiki/Three-body_problem
same_as:
  wikidata: Q607699
  wikipedia: Three-body problem
history:
  posed_by: "Isaac Newton"
  first_stated: "1687"
---

## Problem

Let $G > 0$ be the gravitational constant and let $m_1, m_2, m_3 > 0$ be masses.
Let the positions $x_1(t), x_2(t), x_3(t) \in \R^3$ satisfy Newton's equations
$$x_i'' = \sum_{j \ne i} \frac{G m_j (x_j - x_i)}{\norm{x_j - x_i}^3}, \qquad i = 1, 2, 3.$$
Given distinct initial positions and initial velocities, describe the solution for all time.

## Remarks

This is the case $n = 3$ of the [[n-body problem|62SNWC5E45]].
Bruns showed in 1887 that the ten classical first integrals are the only independent algebraic ones.
Poincaré found that the problem is not integrable and that its orbits can behave in a very complicated way, near homoclinic orbits; this was the beginning of chaos theory.
Sundman found in 1912 a convergent power series solution for all initial conditions with nonzero angular momentum, but it converges too slowly to be of practical use.

Special periodic solutions exist.
Euler found solutions with the three bodies on a rotating line, and Lagrange found solutions with the three bodies at the vertices of a rotating equilateral triangle.
For three equal masses there is a solution in which the bodies chase each other along a figure-eight curve.
Moore found it numerically in 1993, and Chenciner and Montgomery proved its existence in 2000.

In the planar circular restricted three-body problem one body has negligible mass and moves in the plane of the other two, which move on circles.
In a rotating frame it is a [[Hamiltonian system|0EDKGA2FAK]] with two degrees of freedom.

## Explanations

### L1 human

Three bodies, such as the Sun, the Earth and the Moon, attract each other by gravity.
The problem asks how they move.
Unlike the case of two bodies, there is no general formula: tiny changes of the starting positions can lead to completely different motions.
Yet there are beautiful special motions, like three bodies at the corners of a rotating triangle, and the search for them shaped the study of [[ordinary differential equations|0NT64JV96A]].
