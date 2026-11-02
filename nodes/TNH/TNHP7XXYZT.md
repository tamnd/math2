---
tag: TNHP7XXYZT
kind: concept
name: Formal group law in topology
msc: [55N22, 14L05]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_group_law
---

## Summary

A formal group law over a commutative ring $R$ is a power series $F(x, y) = x + y + \cdots$ in two variables.
It behaves like the addition of a group.
In topology, every complex-oriented [[generalized cohomology theory|H28PSZR7XG]] $E$ carries such a law.
The law expresses the first Chern class of a tensor product of line bundles through the Chern classes of the factors.
Ordinary cohomology gives the additive law $x + y$ and complex K-theory gives a multiplicative law.
[[Quillen's theorem|4E518M24MA]] says that [[complex cobordism|5CZHFNY9F3]] carries the universal formal group law, which links stable homotopy theory to the algebraic geometry of formal groups.

## Explanations

### L1 human

For complex line bundles, the first Chern class of $L_1 \otimes L_2$ is $c_1(L_1) + c_1(L_2)$ in ordinary cohomology.
In other cohomology theories the rule is no longer plain addition but a power series, such as $x + y + \beta x y$ in K-theory.
Such a power series still acts like addition: it is commutative and associative and has $0$ as a neutral element.
This "twisted addition" is a formal group law.
Its shape records a lot about the cohomology theory, and the study of these laws by height leads to chromatic homotopy theory.
