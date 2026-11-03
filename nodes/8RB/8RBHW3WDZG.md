---
tag: 8RBHW3WDZG
kind: definition
name: Simple roots
msc: ["17B22", "20F55"]
defines: CSBM217V1N
uses: [AVVV93CASN, 0KCQ9Y3QKA]
sources:
  - url: https://en.wikipedia.org/wiki/Root_system
---

## Definition

Let $\Phi$ be a [[root system|AVVV93CASN]] in a Euclidean space $E$.
A *base* of $\Phi$ is a subset $\Delta \subseteq \Phi$ such that:

1. $\Delta$ is a [[basis|0KCQ9Y3QKA]] of $E$;
2. each $\beta \in \Phi$ can be written as $\beta = \sum_{\alpha \in \Delta} k_\alpha \alpha$ with integers $k_\alpha$ that are either all $\ge 0$ or all $\le 0$.

The elements of a base are the *simple roots*.
The roots with all $k_\alpha \ge 0$ are the *positive roots*, and the others are the *negative roots*.

## Remarks

Example: in $A_2$, take $\alpha = \varepsilon_1 - \varepsilon_2$ and $\beta = \varepsilon_2 - \varepsilon_3$.
The roots are $\pm \alpha$, $\pm \beta$ and $\pm (\alpha + \beta)$, since $\varepsilon_1 - \varepsilon_3 = \alpha + \beta$, so $\set{\alpha, \beta}$ is a base.
Non-example: $\set{\alpha, \alpha + \beta}$ is a basis of $E$ made of roots, but it fails clause 2, since $\beta = (\alpha + \beta) - \alpha$ has coefficients of both signs.
Every root system has a base.
For a vector $\gamma \in E$ orthogonal to no root, the positive roots $\beta$ with $(\gamma, \beta) > 0$ that are not a sum of two such roots form a base.
For a semisimple Lie algebra, a base is also called a system of simple roots of the Lie algebra.

## Explanations

### L1 human

Simple roots are a smallest set of roots from which all roots are obtained by adding with signs all plus or all minus.
They play the role of a basis that is adapted to the shape of the root system.
