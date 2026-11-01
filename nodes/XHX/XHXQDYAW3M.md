---
tag: XHXQDYAW3M
kind: definition
name: Interacting particle system
msc: [60K35, 82C22]
defines: GR49AM3PSZ
uses: [4HS3C12472, VPA41PWRR1]
sources:
  - url: https://en.wikipedia.org/wiki/Interacting_particle_system
---

## Definition

Let $S$ be a countable set of sites, such as $\Z^d$, and let $W$ be a finite set of local states.
A configuration is an element $\eta \in X = W^S$, and $X$ carries the product topology, in which it is compact.
An *interacting particle system* on $X$ is a [[Feller process|4HS3C12472]] $(\eta_t)_{t \ge 0}$ on $X$ whose transitions change finitely many coordinates at a time.
The rates of these transitions depend on the configuration.
The two main classes, with $W = \set{0, 1}$, are given by their [[generators|VPA41PWRR1]] on functions $f$ that depend on finitely many coordinates:

1. a *spin system* with flip rates $c(x, \eta) \ge 0$ has
$$Lf(\eta) = \sum_{x \in S} c(x, \eta) \big( f(\eta^x) - f(\eta) \big),$$
where $\eta^x$ is $\eta$ with the coordinate at $x$ changed;
2. an *exclusion process* with jump rates $p(x, y) \ge 0$ has
$$Lf(\eta) = \sum_{x, y \in S} p(x, y)\, \eta(x) \big(1 - \eta(y)\big) \big( f(\eta^{x,y}) - f(\eta) \big),$$
where $\eta^{x,y}$ is $\eta$ with the coordinates at $x$ and $y$ exchanged.

## Remarks

The rates must be such that this formula defines the generator of a Feller process.
For a spin system it suffices that $\sup_x c(x, \cdot)$ is bounded, each $c(x, \cdot)$ is continuous, and $\sup_x \sum_{u \in S} \sup_\eta \abs{c(x, \eta^u) - c(x, \eta)} < \infty$.
Example: on $S = \Z^d$, the rates $c(x, \eta) = 1$ if $\eta(x) = 1$ and $c(x, \eta) = \lambda \#\set{y : \abs{y - x} = 1, \eta(y) = 1}$ if $\eta(x) = 0$ define the [[contact process|9RVKQJQ5JJ]]; they are bounded by $\max(1, 2d\lambda)$ and depend only on the $2d + 1$ nearest sites.
Non-example: a probabilistic cellular automaton, in which all sites update together at each discrete time step, is not of this form, since each of its transitions changes infinitely many coordinates.
