---
tag: MX3CVYMNDV
kind: concept
name: Dedekind eta function
msc: [11F20]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind_eta_function
same_as:
  wikidata: Q1182161
  wikipedia: Dedekind eta function
---

## Summary

The Dedekind eta function is $\eta(\tau) = e^{\pi i \tau / 12} \prod_{n \ge 1} (1 - e^{2 \pi i n \tau})$ on the [[upper half-plane|X6XGGH5FPW]].
It is holomorphic and never zero there, and it transforms like a modular form of weight $1/2$, up to $24$-th roots of unity.
Its $24$-th power is the cusp form $\Delta$ of weight $12$.
Its reciprocal is, up to a factor, the generating function of the [[partition function|0CV69WDRXW]].

## Explanations

### L1 human

The eta function is an infinite product $q^{1/24}(1 - q)(1 - q^2)(1 - q^3) \cdots$ with $q = e^{2 \pi i \tau}$.
Expanding $1/\prod (1 - q^n)$ counts integer partitions, so eta is tied to counting partitions.
Under $\tau \mapsto -1/\tau$ it changes only by the simple factor $\sqrt{-i\tau}$.
This hidden symmetry is the source of the Hardy–Ramanujan formula for the number of partitions.
