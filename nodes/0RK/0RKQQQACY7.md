---
tag: 0RKQQQACY7
kind: definition
name: Slope field
aliases: [direction-field]
msc: [34A26]
defines: 0DQEHHVRBX
uses: [0P97V20RW7, 04SW7WECS8]
sources:
  - url: https://en.wikipedia.org/wiki/Slope_field
    locator: Definition
inventory: [5JB8AD3VH1]
---

## Definition

Let $\Omega$ be an open subset of $\mathbb{R}^2$ and let $f : \Omega \to \mathbb{R}$ be a function.
The slope field of the first-order equation $y' = f(x, y)$ is the map that assigns to each point $(x, y) \in \Omega$ the line through $(x, y)$ with slope $f(x, y)$.
In a picture, one draws a short segment of this line at each point of a grid in $\Omega$.

## Remarks

Let $u$ be a differentiable function on an interval. It is a [[solution|04SW7WECS8]] of $y' = f(x, y)$ if and only if its graph is tangent to the slope field at each of its points.
For $y' = y$, the segments are horizontal on the $x$-axis and get steeper as $|y|$ grows.
For a system $x' = F(x)$ in the plane, the same picture with arrows is a picture of the vector field $F$.

## Explanations

### L1 human

A slope field shows the direction that a solution must take at each point.
You can sketch a solution without a formula: start at a point and follow the small segments.
This gives a quick picture of how all the solutions behave.
