---
tag: B8Y0ZRQP17
kind: statement
role: theorem
name: Kesten's theorem on planar bond percolation
msc: [60K35, 82B43]
uses: [BH7YPXCYDK, MP8VSZK19A]
about: [MP8VSZK19A]
sources:
  - url: https://en.wikipedia.org/wiki/Percolation_threshold
---

## Statement

Let $\Z^2$ be the square lattice.
Its vertices are the points of $\R^2$ with integer coordinates, and its edges join points at distance $1$.
Then the [[bond percolation threshold|MP8VSZK19A]] of $\Z^2$ is
$$p_c(\Z^2) = \frac12.$$

## Remarks

The key tool is self-duality.
The dual lattice, with a vertex at the centre of each square face, is a translate of $\Z^2$.
A dual edge is declared open when the primal edge it crosses is closed.
At $p = 1/2$ the primal and dual configurations have the same law.
A box crossing argument then shows that a suitable rectangle is crossed by an open path with probability exactly $1/2$.
Harris proved in 1960 that $\theta(1/2) = 0$, which gives $p_c \ge 1/2$; Kesten proved in 1980 that $p_c \le 1/2$.
So there is no infinite open cluster at $p = 1/2$ itself, while for every $p > 1/2$ there is one almost surely.

## Explanations

### L1 human

Keep each edge of the infinite square grid with probability $p$, independently.
The theorem says that an infinite connected piece appears exactly when $p$ is larger than $1/2$.
The number $1/2$ comes from a symmetry: the open edges and the closed edges of the grid play the same role in the plane.

### L2 human

It is the model case of an exact percolation threshold computed by planar duality.
The same duality idea gives $p_c = 1/2$ for site percolation on the triangular lattice.
Estimates on the probability that open paths cross long rectangles are the main tool of the proof.
In dimensions $d \ge 3$ no exact value of $p_c(\Z^d)$ is known.
