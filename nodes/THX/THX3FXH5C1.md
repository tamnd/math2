---
tag: THX3FXH5C1
kind: definition
name: Central force
msc: [70F05, 70A05]
defines: APR7XN00N3
uses: [05R9NF2J49, 5T5GAKQD3S, F5W4PMJF8V]
sources:
  - url: https://en.wikipedia.org/wiki/Central_force
---

## Definition

Let $c \in \R^3$ and let $f \colon (0, \infty) \to \R$ be a function.
The *central force* with centre $c$ and magnitude $f$ is the force field $F \colon \R^3 \setminus \set{c} \to \R^3$ given by
$$F(x) = f(\abs{x - c})\, \frac{x - c}{\abs{x - c}}.$$
The force is attractive at $x$ if $f(\abs{x - c}) < 0$ and repulsive if $f(\abs{x - c}) > 0$.

## Remarks

Example: Newtonian gravity of a mass $M$ at the origin on a mass $m$ is central with $c = 0$ and $f(r) = -G M m / r^2$, where $G$ is the gravitational constant.
Non-example: $F(x) = (-x_2, x_1, 0)$ is not central about $0$, since $F(x)$ is orthogonal to $x$ and not parallel to it.
If $f$ is continuous, $F$ is a [[conservative vector field|05R9NF2J49]] with [[potential energy|5T5GAKQD3S]] $V(x) = -\int_{r_0}^{\abs{x - c}} f(s)\, ds$ for any fixed $r_0 > 0$.
Since $(x - c) \times F(x) = 0$, the [[angular momentum|F5W4PMJF8V]] about $c$ of a particle moving under $F$ alone is constant, and the motion stays in a plane through $c$.
Some texts call a force central whenever $F(x)$ is parallel to $x - c$, without asking that its size depend only on $\abs{x - c}$.

## Explanations

### L1 human

A central force pulls or pushes along the line to a fixed centre, and its strength depends only on the distance.
Turning the picture around the centre does not change the force.
