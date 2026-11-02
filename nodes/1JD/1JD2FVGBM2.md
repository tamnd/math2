---
tag: 1JD2FVGBM2
kind: definition
name: Arithmetical variety
msc: [08B05, 08B10]
defines: GW78A05TNA
uses: [AJNZJD8442, 1B3N9T68YV, 9GZ7F6ETC6]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence-permutable_algebra
---

## Definition

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of algebras.
The variety $\mathcal{V}$ is *arithmetical* if it is both a [[congruence-permutable variety|1B3N9T68YV]] and a [[congruence-distributive variety|9GZ7F6ETC6]].

## Remarks

Equivalently, $\mathcal{V}$ is arithmetical if and only if it has a Pixley term $p$, with $p(x, y, y) = x$, $p(x, x, y) = y$ and $p(x, y, x) = x$.
Example: the variety of Boolean algebras is arithmetical.
It is congruence distributive because Boolean algebras are lattices, and it is congruence permutable because the term $p(x, y, z) = (x \wedge \neg y) \vee (x \wedge z) \vee (\neg y \wedge z)$ is a Mal'cev term.
Non-example: the variety of groups is congruence permutable but not congruence distributive, so it is not arithmetical.
Non-example: the variety of lattices is congruence distributive but not congruence permutable.

## Explanations

### L1 human

A variety is arithmetical when the congruences of each of its algebras both permute and satisfy the distributive law, as the congruences of the integers do.
