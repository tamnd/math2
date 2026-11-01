---
tag: 2D619WTPYC
kind: concept
name: Bergman space
msc: [30H20, 32A36]
sources:
  - url: https://en.wikipedia.org/wiki/Bergman_space
same_as:
  wikidata: Q3058183
  wikipedia: Bergman space
---

## Summary

Let $\Omega$ be a domain in $\C$ and let $0 < p < \infty$.
The Bergman space $A^p(\Omega)$ is the space of [[holomorphic functions|0NAHXR1FRH]] $f$ on $\Omega$ such that $\abs{f}^p$ is integrable with respect to area.
Point evaluations are continuous on it, so for $p \ge 1$ it is a closed subspace of $L^p(\Omega)$ and a [[Banach space|06GZ956657]].
The space $A^2(\Omega)$ is a Hilbert space with a reproducing kernel, the [[Bergman kernel|8RWDHW0CXC]].
Bergman spaces differ from [[Hardy spaces|PNNNFJVF6W]] by measuring size over the whole domain instead of on circles near the boundary.

## Explanations

### L1 human

A function is in a Bergman space if the total area under $\abs{f}^p$ over the domain is finite.
This allows more growth near the boundary than a Hardy space does, because area integrals forgive spikes on thin regions.
On the unit disc, $1/(1 - z)$ lies in $A^1$ but not in $A^2$.
The square-integrable case $A^2$ has a rich geometry, because it carries an inner product.
