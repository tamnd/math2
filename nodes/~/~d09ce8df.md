---
tag: ~d09ce8df
kind: statement
role: theorem
name: Hartman–Grobman theorem
aliases: [linearization-theorem]
msc: [37C15, 34C20]
uses: [~3f3b53df, ~cccff9bc, ~0d74ce10, ~df4f9cf2]
sources:
  - url: https://en.wikipedia.org/wiki/Hartman%E2%80%93Grobman_theorem
    locator: Main theorem
same_as:
  wikidata: Q211981
  wikipedia: Hartman–Grobman theorem
---

## Statement

Let $U$ be an open subset of $\mathbb{R}^n$, let $f : U \to \mathbb{R}^n$ be continuously differentiable. Let $\varphi$ be the [[flow|~0d74ce10]] of $x' = f(x)$, and let $x^* \in U$ be a [[hyperbolic equilibrium point|~3f3b53df]].
Let $A = Df(x^*)$.
Then there are open neighbourhoods $V \subseteq U$ of $x^*$ and $W \subseteq \mathbb{R}^n$ of $0$, and a homeomorphism $h : V \to W$ with $h(x^*) = 0$, as follows.
For each $x \in V$ and each $t \in \mathbb{R}$ such that $\varphi_s(x) \in V$ for all $s$ between $0$ and $t$, we have $h(\varphi_t(x)) = e^{tA} h(x)$.

## Remarks

So near $x^*$ the flow is topologically conjugate to the flow of the [[linearisation|~cccff9bc]] $y' = A y$, given by the [[matrix exponential|~df4f9cf2]]. The map $h$ sends trajectories to trajectories and keeps the direction of time.
The map $h$ is in general only continuous, not differentiable.
The hypothesis of hyperbolicity is necessary. For $x' = -x^3$ and $x' = x^3$ on $\mathbb{R}$, the linearisation at $0$ is the same, but the two phase portraits are not conjugate.

## History

The theorem is named after Philip Hartman and David M. Grobman. It is also called the linearization theorem.

## Explanations

### L1 human

Near a hyperbolic equilibrium, a nonlinear system looks like its linear approximation, after a continuous change of coordinates.
So the pattern of trajectories of the linear system, such as a saddle or a spiral, also appears in the nonlinear system.
