---
tag: DS3W88FESM
kind: definition
name: Diffeology
msc: [58A40, 58A03]
defines: 7JS0JFR89E
uses: [0V33BNKZ9S, F45VQ47GPV, BFBNQ36QS8, 081WKEDK6C]
sources:
  - url: https://en.wikipedia.org/wiki/Diffeology
---

## Definition

Let $X$ be a set.
A *parametrization* of $X$ is a map $p \colon U \to X$, where $U$ is an open subset of $\R^n$ for some $n \ge 0$.
A *diffeology* on $X$ is a set $\mathcal{D}$ of parametrizations of $X$, called *plots*, with these properties.

1. Covering: every constant parametrization $U \to X$ is a plot.
2. Locality: if a parametrization $p \colon U \to X$ is such that each $u \in U$ has an open neighbourhood $V \subseteq U$ with $p|_V \in \mathcal{D}$, then $p \in \mathcal{D}$.
3. Smooth compatibility: let $p \colon U \to X$ be a plot and let $V$ be an open subset of some $\R^m$. For every [[smooth map|0V33BNKZ9S]] $f \colon V \to U$, the map $p \circ f$ is a plot.

A *diffeological space* is a set with a diffeology.
A map $F \colon X \to Y$ between diffeological spaces is *smooth* if $F \circ p$ is a plot of $Y$ for every plot $p$ of $X$.

## Remarks

Example: let $M$ be a [[smooth manifold|F45VQ47GPV]] and let the plots be all smooth maps $p \colon U \to M$.
Constant maps are smooth, smoothness is a local property, and composites of smooth maps are smooth, so the three clauses hold.
A map between manifolds is smooth in the usual sense exactly when it is smooth for these diffeologies.

Non-example: on $X = \R$, let the parametrizations be the real-[[analytic|081WKEDK6C]] maps $U \to \R$.
Clauses 1 and 2 hold, but clause 3 fails: the identity of $\R$ is analytic, while its composite with the smooth non-analytic map $f(t) = e^{-1/t^2}$ for $t \ne 0$, $f(0) = 0$, is not analytic.

Every subset and every quotient of a diffeological space carries a natural diffeology.
Diffeological spaces with smooth maps form a [[cartesian closed category|BFBNQ36QS8]], so the set of smooth maps between two diffeological spaces is again a diffeological space.
