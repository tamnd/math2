---
tag: 47CVS9RJ9D
kind: problem
name: Levi problem
msc: ["32E40", 32T05]
uses: [AHYZMSBBNH, 4487CSC0MB]
about: [AHYZMSBBNH, 4487CSC0MB]
sources:
  - url: https://en.wikipedia.org/wiki/Stein_manifold
history:
  posed_by: "Eugenio Elia Levi"
  first_stated: "1910"
---

## Problem

Let $n \ge 2$ and let $\Omega \subseteq \C^n$ be a domain.
Every [[domain of holomorphy|4487CSC0MB]] is [[pseudoconvex|AHYZMSBBNH]].
Is every pseudoconvex domain $\Omega \subseteq \C^n$ a domain of holomorphy?

## Remarks

The answer is yes.
Kiyoshi Oka proved it for $n = 2$ in 1942.
For all $n$ it was proved in the early 1950s, independently by Oka, by Hans-Joachim Bremermann and by François Norguet.
Hans Grauert solved the analogue for complex manifolds in 1958: a complex manifold with a smooth strictly plurisubharmonic exhaustion function is a Stein manifold.
A modern proof solves the equation $\bar\partial u = f$ with Hörmander's $L^2$ estimates for weights built from a plurisubharmonic exhaustion function.
The problem has no content for $n = 1$, where every domain is both pseudoconvex and a domain of holomorphy.

## Explanations

### L1 human

In several complex variables, not every domain is the natural home of some holomorphic function: on some domains, every holomorphic function extends to a larger domain.
The domains that are natural homes are the domains of holomorphy.
Levi found a geometric condition that they must satisfy, a complex form of convexity of the boundary called pseudoconvexity.
The Levi problem asks whether this geometric condition is enough.
It is, and the proof was one of the main achievements of complex analysis in the twentieth century.
