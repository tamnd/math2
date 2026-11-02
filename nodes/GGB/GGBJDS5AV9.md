---
tag: GGBJDS5AV9
kind: definition
name: Congruence-distributive variety
msc: [08B10]
defines: 9GZ7F6ETC6
uses: [AJNZJD8442, REE07CSXHR, 0HM0HQCK6N]
sources:
  - url: https://en.wikipedia.org/wiki/Distributive_lattice
---

## Definition

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of algebras.
The variety $\mathcal{V}$ is *congruence distributive* if, for every algebra $A$ in $\mathcal{V}$, the [[congruence lattice|REE07CSXHR]] $\operatorname{Con} A$ is a [[distributive lattice|0HM0HQCK6N]].
That is, for all congruences $\alpha, \beta, \gamma$ of $A$,
$$\alpha \wedge (\beta \vee \gamma) = (\alpha \wedge \beta) \vee (\alpha \wedge \gamma).$$

## Remarks

Example: the variety of lattices is congruence distributive.
Every lattice $L$ has the majority term $m(x, y, z) = (x \wedge y) \vee (y \wedge z) \vee (x \wedge z)$, which satisfies $m(x, x, y) = m(x, y, x) = m(y, x, x) = x$, and a variety with a majority term is congruence distributive.
Non-example: the variety of groups is not congruence distributive.
In the Klein four-group $V = \Z/2\Z \times \Z/2\Z$, every subgroup is normal, so $\operatorname{Con} V$ is isomorphic to the lattice of subgroups.
For three distinct subgroups $A, B, C$ of order $2$, $A \wedge (B \vee C) = A \wedge V = A$, while $(A \wedge B) \vee (A \wedge C)$ is the trivial subgroup.
Every congruence-distributive variety is congruence modular.

## Explanations

### L1 human

A variety is congruence distributive when all its algebras have congruence lattices that satisfy the distributive law.
