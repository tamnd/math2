---
tag: 1ZE51P7GRQ
kind: concept
name: Milnor number
msc: [32S05, 32S10, 32S25]
sources:
  - url: https://en.wikipedia.org/wiki/Milnor_number
same_as:
  wikidata: Q6860251
  wikipedia: Milnor number
---

## Summary

The Milnor number $\mu$ of a holomorphic germ $f$ at a critical point is the dimension of its local algebra, see the [[definition|HZCH4KNGY2]].
The local algebra is the quotient of the power series ring by the partial derivatives of $f$.
It is finite exactly when $f$ has an [[isolated singularity|VTGYEES3VS]].
It measures how many simple critical points are merged at the point: a small generic perturbation of $f$ has exactly $\mu$ nondegenerate critical points nearby.
Topologically, it is the number of spheres in the [[Milnor fibre|X5HMTTGB62]] of $f$.

## Explanations

### L1 human

A function like $z^2$ has a simple critical point at $0$, while $z^3$ has a worse one.
If you perturb $z^3$ to $z^3 - tz$ with small $t \ne 0$, the critical point splits into two simple ones, at $z = \pm \sqrt{t/3}$.
The Milnor number counts this: it is $1$ for $z^2$ and $2$ for $z^3$.
In general it is computed by pure algebra, as the dimension of a vector space of power series.
