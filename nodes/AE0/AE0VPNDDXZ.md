---
tag: AE0VPNDDXZ
kind: definition
name: Signed measure
msc: [28A10]
defines: VG2P7R91Z7
uses: [N4KDT83V3S, D7KB9HFCGZ, 0GSZ7B0CGR]
sources:
  - url: https://en.wikipedia.org/wiki/Signed_measure
---

## Definition

Let $(X, \Sigma)$ be a [[measurable space|N4KDT83V3S]].
A *signed measure* on $(X, \Sigma)$ is a map $\nu \colon \Sigma \to [-\infty, \infty]$, with values in the [[extended real line|0GSZ7B0CGR]], such that:

1. $\nu(\emptyset) = 0$;
2. $\nu$ takes at most one of the two values $+\infty$ and $-\infty$;
3. $\nu$ is [[countably additive|D7KB9HFCGZ]]: for pairwise disjoint $E_1, E_2, \ldots$ in $\Sigma$,
$$\nu\Big( \bigcup_{n} E_n \Big) = \sum_{n} \nu(E_n),$$
where the series converges absolutely when the left side is finite.

## Remarks

Example: let $\mu$ be a measure on $(X, \Sigma)$ and $f \in L^1(\mu)$ real-valued.
Then $\nu(E) = \int_E f \, d\mu$ is a signed measure with finite values.
Countable additivity follows from the dominated convergence theorem, and absolute convergence from $\sum_n \abs{\nu(E_n)} \le \int \abs{f} \, d\mu$.
More generally, $\mu_1 - \mu_2$ is a signed measure whenever $\mu_1, \mu_2$ are measures and at least one of them is finite.

Non-example: on $X = \set{a, b}$ with all subsets measurable, no signed measure has $\nu(\set{a}) = +\infty$ and $\nu(\set{b}) = -\infty$.
Clause 2 excludes it, and indeed $\nu(\set{a, b}) = \nu(\set{a}) + \nu(\set{b})$ would be $\infty - \infty$.

A *finite* signed measure is one with values in $\R$.
Every measure is a signed measure.
