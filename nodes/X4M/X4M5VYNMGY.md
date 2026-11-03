---
tag: X4M5VYNMGY
kind: definition
name: Ray tracing
msc: [78A05, 65D18]
defines: 7RRDRHHXC2
uses: [9VGK0SP6EQ, AQ5ZKPZ88R, QDV9SBK6W0, JSTZ7M5VEB, T56WHM058J, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Ray_tracing_(physics)
---

## Definition

Let a region of $\R^3$ be split by smooth surfaces into parts, and let $n > 0$ be a [[refractive index|9VGK0SP6EQ]] that is smooth in each part.
A *ray* is a curve $x(s)$, parametrized by arc length $s$, with these properties:

1. inside each part it satisfies the ray equation of geometrical optics
$$\frac{d}{ds}\left( n(x) \frac{dx}{ds} \right) = \nabla n(x);$$
2. where it meets a surface it continues as a refracted ray by [[Snell's law|QDV9SBK6W0]], or as a reflected ray by the [[law of reflection|JSTZ7M5VEB]].

*Ray tracing* is the computation of rays from given starting points and directions.
It solves the ray equation as an [[ordinary differential equation|0NT64JV96A]], numerically or by straight lines where $n$ is constant.
It applies the rules of clause 2 at each surface.
Along each ray it may also accumulate the [[optical path length|AQ5ZKPZ88R]] $\int n \, ds$.

## Remarks

Example: in a homogeneous medium, $n$ is constant and $\nabla n = 0$.
The ray equation becomes $n \, x'' = 0$, so rays are straight lines, and ray tracing reduces to intersecting lines with surfaces.

Non-example: in the medium $n(x, y, z) = 1 + a y$ with $a > 0$, the straight line $x(s) = (s, 0, 0)$ is not a ray.
Along it $\frac{d}{ds}(n x') = 0$ while $\nabla n = (0, a, 0) \ne 0$, so clause 1 fails; the true ray starting in this direction bends towards larger $y$, where the index is larger.

In [[Hamiltonian form|T56WHM058J]], with $p = n \, dx/ds$ and the parameter $\sigma$ such that $d\sigma = ds / n$, the ray equation becomes the first-order system $dx/d\sigma = p$, $dp/d\sigma = n \nabla n$, with $\abs{p} = n$.
This form is convenient for numerical integration.

## Explanations

### L1 human

A ray bends towards the region where the refractive index is larger, by an amount given by the gradient of the index.
At a sharp surface it bends at once by Snell's law, or bounces back.
Ray tracing follows such rays step by step with a computer.
