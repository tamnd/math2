---
tag: MWMFQR8SMA
kind: problem
name: Congruent number problem
msc: [11D25, 11G05]
uses: [0M7ARED5Q7, 086BE0J3FZ, 427N6S6QQW, ZWEFBG40H9, 08X0VCR2NW]
about: [MWMFQR8SMA]
sources:
  - url: https://en.wikipedia.org/wiki/Congruent_number
same_as:
  wikidata: Q325978
  wikipedia: Congruent number
history:
  posed_by: "Arab mathematicians of the 10th century"
---

## Problem

A positive integer $n$ is a *congruent number* if there is a right triangle with rational side lengths and area $n$.
The problem is to decide, for a given positive integer $n$, whether $n$ is a congruent number.

## Remarks

The problem reduces to [[square-free|08X0VCR2NW]] $n$, since $n$ is congruent if and only if $nk^2$ is congruent for every positive integer $k$.
The number $6$ is congruent, by the triangle with sides $3, 4, 5$, which is a [[Pythagorean triple|0M7ARED5Q7]].
The number $5$ is congruent: the sides $3/2$, $20/3$, $41/6$ satisfy $(3/2)^2 + (20/3)^2 = 1681/36 = (41/6)^2$, and the area is $\frac12 \cdot \frac32 \cdot \frac{20}{3} = 5$.
The number $1$ is not congruent; this is [[Fermat's right triangle theorem|086BE0J3FZ]].
A positive integer $n$ is congruent if and only if the [[elliptic curve|427N6S6QQW]] $y^2 = x^3 - n^2 x$ has a rational point with $y \ne 0$.
Equivalently, this curve has positive rank.
Jerrold Tunnell gave in 1983 an explicit criterion by counting integer solutions of certain ternary quadratic equations.
The criterion is necessary for $n$ to be congruent, and its sufficiency follows from the [[Birch and Swinnerton-Dyer conjecture|ZWEFBG40H9]].
So the problem is open in general.

## Explanations

### L1 human

The question is simple: which whole numbers can be the area of a right triangle whose three sides are fractions?
For $6$ the familiar $3$-$4$-$5$ triangle works, and for $5$ a triangle with sides $3/2$, $20/3$, $41/6$ works.
For $1$, $2$ and $3$ no such triangle exists.
The surprising part is that the question is really about rational points on an elliptic curve.
A complete answer is tied to one of the major open conjectures of number theory.
