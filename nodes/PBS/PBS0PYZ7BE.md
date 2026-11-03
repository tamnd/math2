---
tag: PBS0PYZ7BE
kind: statement
role: theorem
name: Painlevé conjecture on noncollision singularities
msc: [70F16, 70F10]
uses: [62SNWC5E45, JE1Z920QKT]
about: [62SNWC5E45]
sources:
  - url: https://en.wikipedia.org/wiki/Painlev%C3%A9_conjecture
same_as:
  wikidata: Q18386040
  wikipedia: Painlevé conjecture
---

## Statement

Consider the [[n-body problem|62SNWC5E45]] with positive masses in $\R^3$.
Let a solution $q(t) = (q_1(t), \ldots, q_n(t))$ be defined on a maximal interval $[0, t^*)$ with $t^* < \infty$, so that $t^*$ is a singularity.
The singularity is a *collision singularity* if $q(t)$ has a limit as $t \to t^*$, and a *noncollision singularity* otherwise.

1. (Painlevé) For $n = 3$, every singularity is a collision singularity.
2. (Xia) For $n = 5$, there are positive masses and initial conditions whose solution has a noncollision singularity.
3. (Xue) For $n = 4$, there are positive masses and initial conditions in the plane whose solution has a noncollision singularity.

## Remarks

Painlevé showed that $t^*$ is a singularity exactly when the minimum of the mutual distances tends to $0$ as $t \to t^*$.
In his 1895 Stockholm lectures he conjectured that noncollision singularities exist for $n \ge 4$.
By a theorem of von Zeipel, at a noncollision singularity the configuration is unbounded: some body escapes to infinity in finite time.
Xia's example uses two binary pairs and a fifth body that bounces between them and gains energy at each close passage, so the system expands without bound in finite time.
Xia published his example in 1992, and Xue's planar four-body result was published in 2020.
Gerver gave earlier constructions in the plane with many bodies.
By item 1, three bodies are not enough for this behaviour, which is why the conjecture is about $n \ge 4$.

## Explanations

### L1 human

Newton's equations for several bodies can break down in finite time.
The obvious way is a collision.
Painlevé asked whether bodies could also reach infinity in finite time without ever colliding.
For three bodies this cannot happen, but for four and five bodies it can.

### L2 human

The result shows that the $n$-body flow can be incomplete in a way that no regularisation of collisions repairs.
It contrasts with Sundman's analysis of three bodies, where all singularities are collisions and binary ones can be regularised.
The constructions use repeated near-collisions to transfer unbounded energy to one body, a mechanism that needs at least four bodies.
