---
tag: GJD05AZWQN
kind: statement
role: theorem
name: Behnke–Stein theorem
msc: [32Q28, "32E10", 30F99]
uses: [5K0N8QMV6Q, HMCD0JBFST]
about: [5K0N8QMV6Q, HMCD0JBFST]
sources:
  - url: https://en.wikipedia.org/wiki/Stein_manifold
---

## Statement

Let $X$ be a connected [[Riemann surface|5K0N8QMV6Q]] that is not compact.
Then $X$ is a [[Stein manifold|HMCD0JBFST]].

## Remarks

Heinrich Behnke and Karl Stein proved the theorem in 1949.
The core of the proof is a Runge-type approximation theorem on $X$.
Let $K \subseteq X$ be compact, and assume that $X \setminus K$ has no relatively compact connected component.
Then every function holomorphic near $K$ is a uniform limit on $K$ of holomorphic functions on $X$.
With it one constructs global holomorphic functions that separate points and that are unbounded on any given discrete sequence.
This gives the two conditions in the definition of a Stein manifold.
Example: every connected open subset of a compact Riemann surface, other than the whole surface, carries a nonconstant holomorphic function.
This applies for instance to a torus minus a point.
Noncompactness is necessary: on a compact Riemann surface every holomorphic function is constant.
In several variables the analogue fails: $\C^2 \setminus \set{0}$ is a noncompact complex manifold that is not Stein.
The name Behnke–Stein theorem is also used for an earlier result of the same authors.
It says that the union of an increasing sequence of domains of holomorphy in $\C^n$ is a domain of holomorphy.

## Explanations

### L1 human

On a compact Riemann surface, such as a sphere or a torus, there are no nonconstant holomorphic functions.
The theorem says that as soon as the surface is not compact, there are plenty of them, as many as on a domain in the plane.
So every open Riemann surface behaves, for function theory, like an open subset of $\C$.

### L2 human

The theorem makes the whole theory of Stein manifolds available for open Riemann surfaces.
By Cartan's theorem B, every additive and multiplicative Cousin problem is solvable on an open Riemann surface, because $H^2(X, \Z) = 0$ for a noncompact surface.
So on an open Riemann surface, the theorems of Mittag-Leffler and Weierstrass hold: there are meromorphic functions with prescribed principal parts and holomorphic functions with prescribed zeros.
By the embedding theorem, every open Riemann surface is a closed complex submanifold of $\C^3$.
