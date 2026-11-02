---
tag: ZTTPPXGB30
kind: definition
name: Definable set
msc: [03C07, 03C40]
defines: CY1TXHF6KQ
uses: [983GZBQYT4, HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/Definable_set
---

## Definition

Let $L$ be a signature, let $\mathcal{M}$ be an $L$-[[structure|983GZBQYT4]] with domain $M$, and let $A \subseteq M$.
A set $X \subseteq M^n$ is definable with parameters from $A$ when there are an $L$-[[formula|HYJ10AF6RT]] $\varphi(x_1, \dots, x_n, y_1, \dots, y_m)$ and $b_1, \dots, b_m \in A$ such that
$$X = \set{(a_1, \dots, a_n) \in M^n : \mathcal{M} \models \varphi(a_1, \dots, a_n, b_1, \dots, b_m)}.$$
The set $X$ is definable when it is definable with parameters from $M$.
It is definable without parameters, or $\emptyset$-definable, when it is definable with parameters from $\emptyset$.

## Remarks

Example: in the field $(\R, +, \cdot, 0, 1)$, the set $[0, \infty)$ is definable without parameters by $\varphi(x) = \exists y \, (y \cdot y = x)$.
Indeed a real number is a square of a real number exactly when it is nonnegative.

Non-example: in $(\R, <)$, the set $\set{0}$ is not definable without parameters.
The map $\sigma(x) = x + 1$ is an automorphism of $(\R, <)$, and an automorphism maps each $\emptyset$-definable set onto itself; but $\sigma(\set{0}) = \set{1}$.
With the parameter $0$, the formula $x = y_1$ defines $\set{0}$.

The definable subsets of $M^n$ are closed under finite unions, finite intersections and complements, and projections of definable sets are definable.

## Explanations

### L1 human

The definable sets are the sets that the language of the structure can describe.
Allowing parameters means that the description may name finitely many fixed elements.
