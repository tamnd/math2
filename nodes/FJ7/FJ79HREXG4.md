---
tag: FJ79HREXG4
kind: definition
name: Prime model
msc: [03C50, 03C15]
defines: S8W40PYNHX
uses: [655K8Y7VS8, MVCH6N9SNW, CGH8C8EA9N, MT8TDVPBXB]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_model
---

## Definition

Let $T$ be a [[complete theory|655K8Y7VS8]] in a signature $L$, with infinite models.
A [[model|MVCH6N9SNW]] $M$ of $T$ is a *prime model* of $T$ if $M$ has an [[elementary embedding|CGH8C8EA9N]] into every model $N$ of $T$.

## Remarks

Example: the field $\overline{\Q}$ of algebraic numbers is a prime model of $\mathrm{ACF}_0$, the theory of [[algebraically closed fields|MT8TDVPBXB]] of characteristic $0$.
Every algebraically closed field $K$ of characteristic $0$ contains $\Q$, and hence a copy of the algebraic closure of $\Q$.
This field embedding is elementary, because $\mathrm{ACF}_0$ has quantifier elimination.

Non-example: $\C$ is a model of $\mathrm{ACF}_0$, but it is not prime, since it is uncountable and so cannot embed into the countable model $\overline{\Q}$.

If $L$ is countable, a prime model of $T$ is countable by the downward Löwenheim–Skolem theorem.
Then a model is prime if and only if it is countable and atomic, that is, every tuple of it realizes an isolated type.
Two prime models of $T$ are isomorphic.
Another example is $(\Q, <)$, the prime model of the theory of dense linear orders without endpoints.
