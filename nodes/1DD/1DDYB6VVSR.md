---
tag: 1DDYB6VVSR
kind: object
name: Real projective space
msc: [57N99, 51N15]
instance_of: [QQQ9B1DK4P]
sources:
  - url: https://en.wikipedia.org/wiki/Real_projective_space
same_as:
  wikidata: Q2597317
  wikipedia: Real projective space
---

## Description

Let $n \ge 1$ be an integer.
The *real projective space* $\mathbb{RP}^n$ is the set of lines through the origin in $\R^{n+1}$.
As a topological space it is the [[quotient|0NQ1H2X495]] of the [[$n$-sphere|T62369RFH6]] $S^n$ by the relation that identifies each point $x$ with its antipode $-x$.
It is a compact [[topological manifold|QQQ9B1DK4P]] of dimension $n$.
For $i = 1, \ldots, n+1$, let $U_i$ be the image of $\set{x \in S^n : x_i \ne 0}$.
The map $U_i \to \R^n$ sending the class of $x$ to the $n$ ratios $x_j / x_i$ with $j \ne i$ is a [[homeomorphism|0QT00PB5G2]], and the $n + 1$ sets $U_i$ cover $\mathbb{RP}^n$.

## Remarks

$\mathbb{RP}^1$ is homeomorphic to the circle $S^1$.
$\mathbb{RP}^2$ is the real projective plane, a closed surface that cannot be embedded in $\R^3$.
$\mathbb{RP}^n$ is [[orientable|702SNFQG0W]] if and only if $n$ is odd.
For $n \ge 2$ the quotient map $S^n \to \mathbb{RP}^n$ is the universal covering, so the fundamental group of $\mathbb{RP}^n$ has order $2$.
$\mathbb{RP}^n$ is a CW complex with one cell in each dimension $0, 1, \ldots, n$.

## Explanations

### L1 human

Take a sphere and declare each point to be the same as the opposite point.
The space of these pairs of opposite points is the real projective space.
Equivalently, each point of it is a line through the centre of the sphere.
In dimension one this gives a circle again: half of the circle, with its two end points glued.
