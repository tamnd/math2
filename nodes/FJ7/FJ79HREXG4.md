---
tag: FJ79HREXG4
kind: definition
name: Prime model
msc: ["03C50", "03C15"]
topics: [6XEXRME4C1]
audience: grad
defines: S8W40PYNHX
uses: [655K8Y7VS8, MVCH6N9SNW, CGH8C8EA9N, MT8TDVPBXB, 484M0TZ1S7, ~309e2d86]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_model
  - book: isbn:9780387987606
---

## Definition

Let $T$ be a [[complete theory|655K8Y7VS8]] in a signature $L$, with infinite models.
A [[model|MVCH6N9SNW]] $M$ of $T$ is a *prime model* of $T$ if $M$ has an [[elementary embedding|CGH8C8EA9N]] into every model $N$ of $T$.

## Notation

There is no standard symbol; some books write $M_0$ for the prime model.
The phrase *prime over $A$* refers to the relative notion with a set $A$ of parameters.

## Remarks

Example: the field $\overline{\Q}$ of algebraic numbers is a prime model of $\mathrm{ACF}_0$, the theory of [[algebraically closed fields|MT8TDVPBXB]] of characteristic $0$.
Every algebraically closed field $K$ of characteristic $0$ contains $\Q$, and hence a copy of the algebraic closure of $\Q$.
This field embedding is elementary, because $\mathrm{ACF}_0$ has quantifier elimination.

Non-example: $\C$ is a model of $\mathrm{ACF}_0$, but it is not prime, since it is uncountable and so cannot embed into the countable model $\overline{\Q}$.

If $L$ is countable, a prime model of $T$ is countable by the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]].
Then a model is prime if and only if it is countable and [[atomic|~fbef995e]], that is, every tuple of it realizes an isolated type.
Two prime models of $T$ are isomorphic; see [[this theorem|~ddda0a28]].
Another example is $(\Q, <)$, the [[prime model|~309e2d86]] of the theory of dense linear orders without endpoints.
This is the definition of the concept [[prime model|S8W40PYNHX]].

## Explanations

### L1 human

A prime model is a model that fits inside every other model of the same complete theory, in a way that keeps all first-order statements true.

### L2 human

To show that a model $M$ is prime, one builds an elementary embedding of $M$ into an arbitrary model $N$.
For $\overline{\Q}$ in $\mathrm{ACF}_0$, the embedding sends $\overline{\Q}$ onto the algebraic closure of $\Q$ inside $N$.
A trap is to forget the word elementary: every field of characteristic $0$ contains $\Q$, but $\Q$ is not a model of $\mathrm{ACF}_0$.
