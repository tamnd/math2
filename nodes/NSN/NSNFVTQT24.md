---
tag: NSNFVTQT24
kind: definition
name: Configuration space
msc: [70G10, 70G45, 70F20]
defines: MGYKGP7PW3
uses: [AXA8HN8Y45, F45VQ47GPV, VKFW27WXEZ, KQB7WTZ1TX]
sources:
  - url: https://en.wikipedia.org/wiki/Configuration_space_(physics)
---

## Definition

Consider a system of $N$ point particles with position vector $x = (x_1, \dots, x_N) \in \R^{3N}$.
Let $U \subseteq \R^{3N}$ be open, and let $f_1, \dots, f_k$ be smooth functions on $U$.
Let the system obey the independent time-independent [[holonomic constraints|AXA8HN8Y45]] $f_1(x) = 0, \dots, f_k(x) = 0$.
The *configuration space* of the system is the set
$$Q = \set{x \in U : f_1(x) = \dots = f_k(x) = 0}.$$
By the [[regular value theorem|KQB7WTZ1TX]], $Q$ is a [[submanifold|VKFW27WXEZ]] of $\R^{3N}$ of dimension $3N - k$ whenever it is not empty.

## Remarks

Example: a particle on a sphere of radius $\ell > 0$ has the single constraint $f(x) = \abs{x}^2 - \ell^2$ on $U = \R^3$.
Its gradient $2x$ is nonzero on $Q$, so $Q$ is the sphere, a surface of dimension $3 - 1 = 2$.
Non-example: the constraints $f_1(x) = z$ and $f_2(x) = z^2$ for one particle in $\R^3$ define the plane $z = 0$.
Their gradients $(0,0,1)$ and $(0,0,2z)$ are dependent on that plane, and the count $3 - 2 = 1$ is wrong; independence excludes such families.
For a system with no constraints, $Q$ is the open set $U$, for example $\R^{3N}$.
More abstractly, a configuration space is any [[smooth manifold|F45VQ47GPV]] whose points label the positions of the system.
For instance, $SO(3)$ is the configuration space of a rigid body with one fixed point.
