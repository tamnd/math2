---
tag: HBBE0C1NFD
kind: definition
name: Measurable cardinal
msc: ["03E55"]
defines: AKBWT323RQ
uses: [0EBACQFAZW, 0W7FBYS1F1, J64Y3JC0RE]
sources:
  - url: https://en.wikipedia.org/wiki/Measurable_cardinal
---

## Definition

Let $\kappa$ be a [[cardinal|0EBACQFAZW]].
An [[ultrafilter|J64Y3JC0RE]] $U$ on $\kappa$ is *$\kappa$-complete* if $\bigcap \mathcal{F} \in U$ for every family $\mathcal{F} \subseteq U$ with $0 < \abs{\mathcal{F}} < \kappa$.
It is *nonprincipal* if it contains no set $\set{\alpha}$ with $\alpha < \kappa$.
The cardinal $\kappa$ is *measurable* if:

1. $\kappa$ is [[uncountable|0W7FBYS1F1]].
2. There is a $\kappa$-complete nonprincipal ultrafilter on $\kappa$.

## Remarks

The cardinal $\aleph_0$ satisfies clause 2: every ultrafilter is closed under finite intersections, and nonprincipal ultrafilters on $\omega$ exist by the axiom of choice; it fails only clause 1.
The cardinal $\aleph_1$ fails clause 2, because every measurable cardinal is inaccessible, and $\aleph_1$ is not.
Equivalent form: $\kappa$ is measurable if and only if there is an elementary embedding $j \colon V \to M$, with $M$ a transitive class, whose critical point is $\kappa$.
The critical point condition means that $j(\alpha) = \alpha$ for $\alpha < \kappa$ and $j(\kappa) > \kappa$.
The embedding comes from the ultrapower of $V$ by $U$, and conversely $U = \set{X \subseteq \kappa : \kappa \in j(X)}$.
Scott proved that if a measurable cardinal exists, then $V \neq L$.
