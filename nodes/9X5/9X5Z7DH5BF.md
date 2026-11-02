---
tag: 9X5Z7DH5BF
kind: definition
name: Elementary embedding
msc: [03C07]
defines: CGH8C8EA9N
uses: [983GZBQYT4, HYJ10AF6RT, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
---

## Definition

Let $L$ be a signature and let $\mathcal{M}$ and $\mathcal{N}$ be $L$-[[structures|983GZBQYT4]] with domains $M$ and $N$.
A [[map|0EPAT51DXQ]] $j \colon M \to N$ is an elementary embedding of $\mathcal{M}$ into $\mathcal{N}$ when, for every $L$-[[formula|HYJ10AF6RT]] $\varphi(x_1, \dots, x_n)$ and all $a_1, \dots, a_n \in M$,
$$\mathcal{M} \models \varphi(a_1, \dots, a_n) \iff \mathcal{N} \models \varphi(j(a_1), \dots, j(a_n)).$$

## Remarks

An elementary embedding is injective: apply the condition to the formula $x_1 = x_2$.
It is an embedding of structures: apply the condition to the atomic formulas.
Its image is the domain of an [[elementary substructure|8WZF9SBP39]] of $\mathcal{N}$.

Example: the inclusion $\Q \to \R$ is an elementary embedding of $(\Q, <)$ into $(\R, <)$, because $(\Q, <)$ is an elementary substructure of $(\R, <)$.

Non-example: the map $j(n) = n + 1$ from $(\N, <)$ to $(\N, <)$ preserves $<$ and is injective.
It is not elementary: for $\varphi(x) = \exists y \, (y < x)$, $(\N, <) \models \neg\varphi(0)$ but $(\N, <) \models \varphi(j(0))$.

## Explanations

### L1 human

An elementary embedding places a copy of one structure inside another so that no first-order statement changes its truth value.
Each elementary embedding is an isomorphism onto an elementary substructure.
