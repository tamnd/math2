---
tag: 6TF2JBTPPJ
kind: object
name: Constructible universe
msc: ["03E45"]
instance_of: [G78W36EGMB]
uses: [0HE5WDQ9FJ, 0YSCSX5YZC, Y48FA69563]
sources:
  - url: https://en.wikipedia.org/wiki/Constructible_universe
same_as:
  wikidata: Q2777107
  wikipedia: Constructible universe
---

## Description

For a set $X$, let $\operatorname{Def}(X)$ be the set of all subsets of $X$ that are definable in the structure $(X, \in)$.
Here a definition is a first-order formula with parameters from $X$.
Define sets $L_\alpha$ by recursion on the [[ordinals|0YSCSX5YZC]] $\alpha$:
$$L_0 = \emptyset, \qquad L_{\alpha + 1} = \operatorname{Def}(L_\alpha), \qquad L_\lambda = \bigcup_{\alpha < \lambda} L_\alpha \text{ for a limit ordinal } \lambda.$$
The *constructible universe* is the [[class|Y48FA69563]] $L = \bigcup_{\alpha} L_\alpha$, where $\alpha$ runs over all ordinals.
A set is *constructible* when it lies in $L$.

The class $L$ is an [[inner model|G78W36EGMB]] of [[ZF|0HE5WDQ9FJ]].
Each $L_\alpha$ is transitive, so $L$ is transitive.
The ordinal $\alpha$ lies in $L_{\alpha + 1}$, because it is the set of ordinals of $L_\alpha$, and this set is definable over $L_\alpha$.
So $L$ contains every ordinal.
The axioms of ZF hold in $L$; the hardest case is the separation schema, which uses a reflection argument.

## Remarks

For finite $n$ one has $L_n = V_n$, so $L_\omega = V_\omega$ is the set of hereditarily finite sets.
At the next level they differ: $L_{\omega + 1}$ is countable, because there are only countably many formulas with finitely many parameters from the countable set $L_\omega$, while $V_{\omega + 1}$ is uncountable.
The class $L$ satisfies the [[axiom of constructibility|4QKRPRCSXH]] $V = L$, and it is contained in every inner model of ZF.
[[Gödel's theorem|Q9176JRJ5M]] says that the axiom of choice and the generalized continuum hypothesis hold in $L$.

## Explanations

### L1 human

The constructible universe is the smallest world of sets that one can build in stages using only what can be described.
At each stage one keeps exactly the subsets of the sets built so far that a formula can define.
Nothing is added by arbitrary choice, so the world is very thin and very orderly.
For example, at the finite stages every subset can be described, so all finite sets of finite sets appear.
At stage $\omega + 1$ only countably many sets of natural numbers appear, although there are uncountably many in all.
