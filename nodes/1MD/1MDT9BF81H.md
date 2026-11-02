---
tag: 1MDT9BF81H
kind: concept
name: Cylindric algebra
msc: ["03G15"]
specializes: [0XADJKM699]
sources:
  - url: https://en.wikipedia.org/wiki/Cylindric_algebra
same_as:
  wikidata: Q5199278
  wikipedia: Cylindric algebra
---

## Summary

A cylindric algebra is a [[Boolean algebra|0XADJKM699]] with extra operations that model existential quantifiers and constants that model equality of variables.
Alfred Tarski and his collaborators introduced them to do for [[predicate logic|086QKPF0A6]] with equality what Boolean algebras do for propositional logic.
The cylindrification $c_\kappa$ plays the role of "there exists $x_\kappa$", and the diagonal element $d_{\kappa\lambda}$ plays the role of the formula $x_\kappa = x_\lambda$.

## Explanations

### L1 human

Think of the set of points of the plane that satisfy a formula $\varphi(x, y)$.
The formula "there exists $x$ such that $\varphi(x, y)$" describes the set swept out when that region is moved along the $x$-direction: a cylinder over the shadow of the region.
That is why the operation is called cylindrification.
The diagonal line $\set{(x, y) : x = y}$ is the set of the formula $x = y$.
A cylindric algebra keeps only the rules that these operations obey, so it can be studied with algebra.
