---
tag: ~2e5ebdfc
kind: definition
name: Line
aliases: [straight-line]
msc: [51N20]
defines: ~4d2065b5
uses: [~885ad94c, ~c49bcc05]
sources:
  - url: https://en.wikipedia.org/wiki/Line_(geometry)
    locator: Parametric equation
---

## Definition

Let $n \geq 2$ be an integer. A line in the [[Euclidean space|~885ad94c]] $\mathbb{R}^n$ is a set of the form
$$L = \{\, p + t v \;:\; t \in \mathbb{R} \,\},$$
where $p$ is a point of $\mathbb{R}^n$ and $v$ is a nonzero [[vector|~c49bcc05]] of $\mathbb{R}^n$. The vector $v$ is a direction vector of $L$.

## Remarks

For two distinct points $A$ and $B$, exactly one line contains both: the line through $A$ with the direction vector $\overrightarrow{AB}$.
The point $p$ and the vector $v$ are not unique. The same line has each point of $L$ as a base point, and each nonzero multiple of $v$ as a direction vector.
In the plane $\mathbb{R}^2$, the lines are also the sets $\{(x, y) : a x + b y = c\}$ with real numbers $a$, $b$, $c$ and $(a, b) \neq (0, 0)$.
In the language of affine geometry, a line is an [[affine subspace|~b4bd557a]] of dimension 1.

## Explanations

### L1 human

Start at a point $p$ and walk forward or backward in the direction $v$, for any amount of time $t$. The points you can reach form the line. For example, with $p = (0, 1)$ and $v = (1, 2)$ you get the line $y = 2x + 1$ in the plane.
