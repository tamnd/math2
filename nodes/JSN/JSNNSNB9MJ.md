---
tag: JSNNSNB9MJ
kind: concept
name: Analytic semigroup
msc: [47D06, 47D03]
specializes: [EVF180QJXY]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_semigroup
same_as:
  wikidata: Q485292
  wikipedia: Analytic semigroup
---

## Summary

An analytic semigroup is a [[strongly continuous semigroup|EVF180QJXY]] $(T(t))_{t \ge 0}$ that extends holomorphically to complex times $z$.
The allowed $z$ fill a sector of the complex plane around the positive real axis.
Such semigroups have a strong smoothing effect: $T(t)x$ lies in the domain of every power of the generator for $t > 0$.
They are the abstract model of parabolic equations such as the heat equation.
Their generators are characterised by resolvent estimates on a sector, which makes them the sectorial operators.

## Explanations

### L1 human

The heat equation smooths: even a rough initial temperature becomes smooth instantly.
An analytic semigroup is a semigroup with this smoothing property, expressed by the fact that time $t$ may be replaced by a complex number $z$ with small argument.
For a bounded operator $B$, the formula $e^{zB}$ makes sense for every complex $z$, so $e^{tB}$ is analytic.
The heat semigroup $e^{t\Delta}$ on $L^2(\R^n)$ is analytic, with $z$ allowed in the whole right half-plane.
The shift $f(s) \mapsto f(s + t)$ is not analytic: it moves a rough function without smoothing it.
