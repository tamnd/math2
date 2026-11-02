---
tag: B1WPAD1M03
kind: definition
name: Set-valued measure
msc: [28B20]
defines: 13F6B3BGA4
uses: [N4KDT83V3S]
sources:
  - url: https://en.wikipedia.org/wiki/Set-valued_function
---

## Definition

Let $(\Omega, \mathcal{F})$ be a [[measurable space|N4KDT83V3S]] and let $n \ge 1$.
A *set-valued measure* on $(\Omega, \mathcal{F})$ with values in $\R^n$ is a map $M$ from $\mathcal{F}$ to the nonempty subsets of $\R^n$ such that:

1. $M(\emptyset) = \set{0}$.
2. For every sequence of pairwise disjoint sets $A_1, A_2, \dots$ in $\mathcal{F}$ with union $A$,
$$M(A) = \set{\sum_{i=1}^{\infty} x_i : x_i \in M(A_i) \text{ for all } i, \ \sum_{i=1}^{\infty} \abs{x_i} < \infty}.$$

## Remarks

Many authors also require the values to be closed, compact or convex, and some work in a Banach space instead of $\R^n$.
Example: let $\mu$ be a finite measure on $\mathcal{F}$, let $K \subseteq \R^n$ be nonempty, compact and convex, and let $M(A) = \mu(A) K$.
Then $M(\emptyset) = \set{0}$.
Given $x_i \in \mu(A_i) K$, the series converges absolutely since $K$ is bounded, and its sum lies in $\mu(A) K$ because $K$ is convex and closed.
Conversely $\mu(A) k = \sum_i \mu(A_i) k$ for $k \in K$, so clause 2 holds.
Non-example: let $\Omega = \set{a, b}$ with counting measure $\mu$ and $K = \set{0, 1}$, which is not convex.
Then $M(\Omega) = 2K = \set{0, 2}$, while the sums from $M(\set{a})$ and $M(\set{b})$ form $\set{0, 1, 2}$, so clause 2 fails.
A [[vector measure|PS28BSAJKJ]] $\nu$ gives the set-valued measure $A \mapsto \set{\nu(A)}$.
