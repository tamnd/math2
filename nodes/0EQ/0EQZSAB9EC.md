---
tag: 0EQZSAB9EC
kind: definition
name: Homogeneous linear equation
msc: [34A30]
defines: 0KP0QNXPRT
uses: [0PB7K8M7FG]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_differential_equation
    locator: Basic terminology
---

## Definition

Let $I$ be an open interval and let $a_0, \dots, a_{n-1} : I \to \mathbb{R}$ be continuous functions.
A homogeneous linear equation of order $n$ is a [[linear differential equation|0PB7K8M7FG]] with right side $0$:
$$y^{(n)} + a_{n-1}(x)\, y^{(n-1)} + \dots + a_1(x)\, y' + a_0(x)\, y = 0.$$
For a linear equation $L y = b$, the equation $L y = 0$ is the associated homogeneous equation.

## Remarks

The zero function is always a solution.
By the [[superposition principle|0F2VBPXNP9]], the solutions on $I$ form a vector space. It has [[dimension n|0GK68PZ6KH]].
Example: $y'' - y = 0$ is homogeneous, and its solutions are $C_1 e^{x} + C_2 e^{-x}$.

## Explanations

### L1 human

Homogeneous means that the equation has no term without $y$.
So if $y$ is a solution, then $2y$ and $-y$ are solutions, and so is the sum of two solutions.
