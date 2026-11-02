---
tag: HDD0EB48AB
kind: definition
name: Hilbert metric
msc: [51F99, 52A20, 53C60]
defines: P923DHV74J
uses: [02AS45T3H9, 0NPPGHQNXQ, 063W5JMY85]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_metric
---

## Definition

Let $n \ge 1$ and let $\Omega \subseteq \R^n$ be a bounded open [[convex set|02AS45T3H9]].
Write $\abs{pq}$ for the [[Euclidean distance|0NPPGHQNXQ]] of points $p$ and $q$.
Let $x, y \in \Omega$ be distinct.
The line through $x$ and $y$ meets the boundary of $\Omega$ in exactly two points $a$ and $b$.
Name them so that $a, x, y, b$ lie on the line in this order.
The *Hilbert metric* on $\Omega$ is
$$d_\Omega(x, y) = \frac{1}{2} \log \frac{\abs{ay} \, \abs{xb}}{\abs{ax} \, \abs{yb}},$$
with $d_\Omega(x, x) = 0$.

## Remarks

The map $d_\Omega$ is a [[metric|063W5JMY85]] on $\Omega$; the triangle inequality uses the convexity of $\Omega$.

Example: let $\Omega = (-1, 1) \subset \R$ and $0 < y < 1$.
For $x = 0$ the boundary points are $a = -1$ and $b = 1$, so $d_\Omega(0, y) = \frac{1}{2} \log \frac{1 + y}{1 - y}$, which tends to $\infty$ as $y \to 1$.

Non-example: the open half-plane $\set{(u, v) \in \R^2 : v > 0}$ is convex but not bounded.
A horizontal line in it does not meet the boundary at all, so the formula has no meaning.

Some authors omit the factor $\frac{1}{2}$.
When $\Omega$ is the open unit ball, $d_\Omega$ is the hyperbolic distance of the [[Beltrami–Klein model|1WN9B18H86]].
