---
tag: Y1XE9SQB5A
kind: concept
name: Szegő kernel
msc: [32A25, 32A35]
sources:
  - url: https://en.wikipedia.org/wiki/Szeg%C5%91_kernel
same_as:
  wikidata: Q7664533
  wikipedia: Szegő kernel
---

## Summary

Let $\Omega \subset \C^n$ be a bounded domain with smooth boundary.
Its Szegő kernel is the reproducing kernel of the [[Hardy space|PNNNFJVF6W]] of holomorphic functions with square-integrable boundary values on $\partial\Omega$.
It plays for boundary integrals the role that the [[Bergman kernel|8RWDHW0CXC]] plays for volume integrals.
It gives a canonical integral formula that recovers a holomorphic function inside $\Omega$ from its values on the boundary.
On the unit disc it is the Cauchy kernel, and on the unit ball it has an explicit closed form.

## Explanations

### L1 human

A holomorphic function on a nice domain is fixed by its values on the boundary.
The Szegő kernel is the weight that tells how much each boundary point contributes to the value at an inside point $z$.
To get $f(z)$, average the boundary values of $f$ against this weight.
On the unit disc the weight is $\frac{1}{2\pi(1 - z\bar\zeta)}$, and this average is exactly Cauchy's integral formula.
