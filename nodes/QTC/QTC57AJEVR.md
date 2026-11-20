---
tag: QTC57AJEVR
kind: definition
name: Categorical theory
msc: ["03C35"]
topics: [6XEXRME4C1]
audience: grad
defines: 1JJCGNX240
uses: [92SWXST1ZM, MVCH6N9SNW, 0EBACQFAZW, 0G0ASKNA6Z, MT8TDVPBXB, CAEHMSX9RT]
sources:
  - url: https://en.wikipedia.org/wiki/Categorical_theory
    locator: lead section
  - book: isbn:9780387987606
---

## Definition

Let $T$ be a [[theory|92SWXST1ZM]] in a first-order signature $L$, and let $\kappa$ be an infinite [[cardinal|0EBACQFAZW]].
The theory $T$ is *$\kappa$-categorical* if two conditions hold.

1. $T$ has a [[model|MVCH6N9SNW]] whose domain has [[cardinality|0G0ASKNA6Z]] $\kappa$.
2. Any two models of $T$ of cardinality $\kappa$ are isomorphic.

## Remarks

A theory is *uncountably categorical* if it is $\kappa$-categorical for every uncountable $\kappa$, and *totally categorical* if it is $\kappa$-categorical for every infinite $\kappa$.
Some authors drop condition 1 from the definition.
For a theory with an infinite model and $\kappa \ge \abs{L}$, condition 1 holds by the Löwenheim-Skolem theorem, so the two versions agree.
The main page of the idea is [[categorical theory|1JJCGNX240]].

Example: the theory $\mathrm{ACF}_0$ of [[algebraically closed fields|MT8TDVPBXB]] of characteristic $0$ is $\kappa$-categorical for every uncountable $\kappa$.
By [[Steinitz's theorem|CAEHMSX9RT]], such a field is determined up to isomorphism by its transcendence degree over $\Q$, and a field of uncountable size $\kappa$ has transcendence degree $\kappa$.

Non-example: $\mathrm{ACF}_0$ is not $\aleph_0$-categorical.
The fields $\overline{\Q}$ and the algebraic closure of $\Q(t)$ are both countable models, of transcendence degree $0$ and $1$, so they are not isomorphic.

The theory of dense linear orders without endpoints is $\aleph_0$-categorical, by Cantor's back-and-forth argument, but not $\kappa$-categorical for any uncountable $\kappa$.
