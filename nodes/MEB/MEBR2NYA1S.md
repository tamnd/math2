---
tag: MEBR2NYA1S
kind: definition
name: Congruence-modular variety
msc: [08B10]
defines: QAQAS3JWXW
uses: [AJNZJD8442, REE07CSXHR, QX7WZ92QAK]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_lattice
---

## Definition

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of algebras.
The variety $\mathcal{V}$ is *congruence modular* if, for every algebra $A$ in $\mathcal{V}$, the [[congruence lattice|REE07CSXHR]] $\operatorname{Con} A$ is a [[modular lattice|QX7WZ92QAK]].
That is, for all congruences $\alpha, \beta, \gamma$ of $A$ with $\alpha \le \gamma$,
$$\alpha \vee (\beta \wedge \gamma) = (\alpha \vee \beta) \wedge \gamma.$$

## Remarks

Example: the variety of groups is congruence modular, since the normal subgroups of a group form a modular lattice.
More generally, every congruence-permutable variety and every congruence-distributive variety is congruence modular.
Non-example: the variety of sets, with no operations, is not congruence modular.
The congruences of a set are all its equivalence relations.
On $\set{1, 2, 3, 4}$, let $\alpha$ have the classes $\set{1, 2}, \set{3}, \set{4}$, let $\gamma$ have the classes $\set{1, 2}, \set{3, 4}$, and let $\beta$ have the classes $\set{1, 3}, \set{2, 4}$.
Then $\alpha \le \gamma$, $\beta \wedge \gamma$ is the identity relation and $\alpha \vee \beta$ is the full relation.
So $\alpha \vee (\beta \wedge \gamma) = \alpha$, while $(\alpha \vee \beta) \wedge \gamma = \gamma \ne \alpha$.

## Explanations

### L1 human

A variety is congruence modular when all its algebras have congruence lattices that satisfy the modular law.
