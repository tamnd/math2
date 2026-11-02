---
tag: E8X03PNHM0
kind: definition
name: Injectivity radius
msc: [53C22, 53C20]
defines: Y6ZSKVAE3V
uses: [7CBT4SM83Y, Y7Z0AGY1A7, 0KZZ70ZHXP, 0QF1MZ9FRG]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_Riemannian_and_metric_geometry
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] and $p \in M$.
For $r > 0$, let $B_r(0) = \set{v \in T_pM : g_p(v, v) < r^2}$.
Let $A_p$ be the set of $r > 0$ such that:

1. $B_r(0)$ lies in the domain of the [[exponential map|Y7Z0AGY1A7]] $\exp_p$;
2. $\exp_p$ restricted to $B_r(0)$ is a [[diffeomorphism|0KZZ70ZHXP]] onto an open subset of $M$.

The *injectivity radius* of $M$ at $p$ is $\operatorname{inj}(p) = \sup A_p$.
The injectivity radius of $M$ is the [[infimum|0QF1MZ9FRG]] $\operatorname{inj}(M) = \inf_{p \in M} \operatorname{inj}(p)$.

## Remarks

Example: on the unit sphere $S^n$, for any $p$, $\exp_p$ is a diffeomorphism from $B_\pi(0)$ onto $S^n$ minus the antipode $-p$.
It maps the whole sphere $\set{\abs{v} = \pi}$ to $-p$, so no larger ball works, and $\operatorname{inj}(p) = \pi$.

Non-example: for the same $p$ on $S^n$, the radius $r = 2\pi$ does not belong to $A_p$, because $\exp_p$ is not injective on $B_{2\pi}(0)$.

For $\R^n$ with the Euclidean metric, $\operatorname{inj}(p) = \infty$ for every $p$.
The injectivity radius is always positive at each point; if $M$ is compact, then $\operatorname{inj}(M) > 0$.
If $M$ is complete, $\operatorname{inj}(p)$ is the distance from $p$ to its [[cut locus|X5WKGC5Q6T]].
