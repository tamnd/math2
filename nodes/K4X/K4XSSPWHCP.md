---
tag: K4XSSPWHCP
kind: concept
name: Calderón projector
msc: [35S15, 35J40, 58J40]
sources:
  - url: https://en.wikipedia.org/wiki/Calder%C3%B3n_projector
same_as:
  wikidata: Q25304637
  wikipedia: Calderón projector
---

## Summary

The Calderón projector of an elliptic differential operator $P$ on a domain $\Omega$ is a projection acting on boundary data.
Its range is exactly the set of Cauchy data on $\partial\Omega$ of the solutions of $Pu = 0$ in $\Omega$.
It is a matrix of [[pseudo-differential operators|FF27N0BWTP]] on the boundary.
It reduces boundary value problems in $\Omega$ to equations on $\partial\Omega$, and it is the tool behind the general theory of [[elliptic boundary value problems|C1F7T523G0]].

## Explanations

### L1 human

A solution of an elliptic equation inside a region leaves a trace on the boundary: its values and its normal derivatives there.
Not every list of boundary data comes from a solution, because the interior equation imposes a hidden relation between them.
The Calderón projector is a projection that keeps the boundary data of solutions unchanged and sends every list of boundary data to the data of some solution.
For the Laplacian in the plane, the data are a pair $(f, g)$ of the boundary values and the normal derivative.
The projector fixes the pairs $(u|_{\partial\Omega}, \partial_\nu u|_{\partial\Omega})$ of [[harmonic functions|0DEB0JMN0W]] $u$ and sends every other pair to such a pair.
