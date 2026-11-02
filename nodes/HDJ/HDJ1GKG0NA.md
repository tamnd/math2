---
tag: HDJ1GKG0NA
kind: concept
name: Banach lattice
msc: [46B42, 46A40]
specializes: [06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_lattice
same_as:
  wikidata: Q30676598
  wikipedia: Banach lattice
---

## Summary

A Banach lattice is a [[Banach space|06GZ956657]] with an order that is compatible with the vector operations and with the norm.
Every two elements have a largest lower bound and a least upper bound, and a smaller absolute value gives a smaller norm.
The spaces $L^p$, $C(K)$ and $\ell^p$ with the pointwise order are the main examples.
Banach lattices are the setting for positive operators, which appear in probability, in partial differential equations and in economics.

## Explanations

### L1 human

In many function spaces you can compare two functions point by point and take their pointwise maximum.
A Banach lattice keeps exactly this structure, in an abstract form, together with a complete norm.
The rule linking order and norm says that if $\abs{f} \le \abs{g}$ everywhere, then $f$ is not longer than $g$.
For example, in $C([0,1])$ the function $\max(\sin, \cos)$ is again continuous, and its norm is at most $1$ because both $\abs{\sin}$ and $\abs{\cos}$ are at most $1$.
