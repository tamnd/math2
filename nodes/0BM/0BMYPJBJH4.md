---
tag: 0BMYPJBJH4
kind: definition
name: Line
msc: [51N20]
defines: 0MP9BCF6DP
uses: [0XPR1E85W0, 0QN3D80AWP]
sources:
  - url: https://en.wikipedia.org/wiki/Line_(geometry)
    locator: Parametric equation
---

## Definition

Let $n \geq 2$ be an integer. A line in the [[Euclidean space|0XPR1E85W0]] $\mathbb{R}^n$ is a set of the form
$$L = \{\, p + t v \;:\; t \in \mathbb{R} \,\},$$
where $p$ is a point of $\mathbb{R}^n$. Here $v$ is a nonzero [[vector|0QN3D80AWP]] of $\mathbb{R}^n$. The vector $v$ is a direction vector of $L$.

## Remarks

For two distinct points $A$ and $B$, exactly one line contains both: the line through $A$ with the direction vector $\overrightarrow{AB}$.
The point $p$ and the vector $v$ are not unique. The same line has each point of $L$ as a base point, and each nonzero multiple of $v$ as a direction vector.
In the plane $\mathbb{R}^2$, the lines are also the sets $\{(x, y) : a x + b y = c\}$ with real numbers $a$, $b$, $c$ and $(a, b) \neq (0, 0)$.
In the language of affine geometry, a line is an [[affine subspace|0PYW26VNT6]] of dimension 1.

## Explanations

### L1 human

Start at a point $p$ and walk forward or backward in the direction $v$, for any amount of time $t$. The points you can reach form the line. For example, with $p = (0, 1)$ and $v = (1, 2)$ you get the line $y = 2x + 1$ in the plane.
