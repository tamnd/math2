---
tag: JR0N0BDR3B
kind: definition
name: NIP theory
msc: [03C45]
defines: 74VCDYQDGP
uses: [655K8Y7VS8, HYJ10AF6RT, MVCH6N9SNW]
sources:
  - url: https://en.wikipedia.org/wiki/NIP_(model_theory)
---

## Definition

Let $T$ be a [[complete theory|655K8Y7VS8]] in a first-order language $L$.
Let $\varphi(\bar x; \bar y)$ be an $L$-[[formula|HYJ10AF6RT]] whose free variables are split into two tuples $\bar x$ and $\bar y$.
The formula $\varphi$ has the *independence property* in $T$ if the following holds for every $n \in \N$.
There are a [[model|MVCH6N9SNW]] $M$ of $T$, tuples $\bar a_1, \ldots, \bar a_n$ in $M$, and tuples $\bar b_J$ in $M$ for each $J \subseteq \set{1, \ldots, n}$.
For all $i$ and $J$, $M \models \varphi(\bar a_i; \bar b_J)$ holds if and only if $i \in J$.
The theory $T$ is *NIP* if no $L$-formula has the independence property in $T$.

## Remarks

Example: the theory of dense linear orders without endpoints is NIP.
By quantifier elimination, a formula $\varphi(x; \bar y)$ defines, for each parameter $\bar b$, a union of at most $k$ points and intervals.
The endpoints are entries of $\bar b$, and $k$ depends only on $\varphi$.
Such a family cannot cut out all $2^n$ subsets of a set of $n$ points once $n$ is large.
It is a standard fact that it suffices to check formulas with $\bar x$ a single variable.

Non-example: the theory of the [[Rado graph|RMXR0FEF54]] is not NIP.
For the formula $x E y$, take distinct vertices $a_1, \ldots, a_n$; by the extension property, for each $J$ there is a vertex $b_J$ adjacent to $a_i$ exactly when $i \in J$.

Equivalently, $T$ is NIP if for every formula $\varphi(\bar x; \bar y)$ and every model $M$ of $T$, the family $\set{\varphi(M; \bar b) : \bar b \in M}$ has finite [[VC dimension|KCFXR9K3GD]].
Every stable theory and every o-minimal theory is NIP.
