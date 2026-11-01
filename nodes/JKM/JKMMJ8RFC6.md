---
tag: JKMMJ8RFC6
kind: object
name: Hilbert cube
msc: ["54E45", 57N20]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_cube
same_as:
  wikidata: Q1618171
  wikipedia: Hilbert cube
---

## Description

Let $\ell^2$ be the space of real sequences $x = (x_n)_{n \ge 1}$ with $\sum_n x_n^2 < \infty$ and the norm $\norm{x}_2 = (\sum_n x_n^2)^{1/2}$.
The *Hilbert cube* is the subset
$$H = \set{x \in \ell^2 : 0 \le x_n \le 1/n \text{ for all } n \ge 1}$$
with the metric induced by $\norm{\cdot}_2$.

## Remarks

The map $(t_n)_{n \ge 1} \mapsto (t_n / n)_{n \ge 1}$ is a [[homeomorphism|0QT00PB5G2]] from $[0, 1]^{\N}$, with the [[product topology|0GBG8B49AA]], onto $H$.
So $H$ is [[compact|0TVJZYB6SH]], for example by [[Tychonoff's theorem|0JTRSJKCFB]].
It is also convex in $\ell^2$.

Every [[separable|0Z2P41SVDP]] metrizable space is homeomorphic to a subspace of $H$.
This is the embedding behind the [[Urysohn metrization theorem|HBFHDH4EJX]].

The Hilbert cube has the [[fixed-point property|JQDHHFXBF3]]: every continuous map $H \to H$ has a fixed point.
This follows from the Schauder fixed-point theorem, since $H$ is a compact convex subset of a Banach space.

## Explanations

### L1 human

The Hilbert cube is an infinite-dimensional cube whose sides get shorter and shorter: $1$, $1/2$, $1/3$, and so on.
Because the sides shrink, the cube stays compact, unlike the unit ball of an infinite-dimensional space.
It is big enough to contain a copy of every separable metric space, up to homeomorphism.
