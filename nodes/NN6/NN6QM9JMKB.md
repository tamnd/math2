---
tag: NN6QM9JMKB
kind: definition
name: Complete theory
msc: ["03C35", "03C07"]
topics: [AY09KYSW81]
audience: ug2
defines: 655K8Y7VS8
uses: [92SWXST1ZM, MVCH6N9SNW, DKFGQTRYZE]
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.Theory.IsComplete
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Complete_theory
    locator: Complete theories
  - book: isbn:9780387987606
    locator: Chapter 2
---

## Definition

Let $L$ be a signature and let $T$ be an $L$-[[theory|92SWXST1ZM]].
For an $L$-[[sentence|DKFGQTRYZE]] $\varphi$, write $T \models \varphi$ when every [[model|MVCH6N9SNW]] of $T$ satisfies $\varphi$.
The theory $T$ is complete when the following hold.

1. $T$ has a model.
2. For every $L$-sentence $\varphi$, $T \models \varphi$ or $T \models \neg\varphi$.

## Notation

Mathlib's `T.IsComplete` is the conjunction of `T.IsSatisfiable` and the condition that `T ⊨ᵇ φ` or `T ⊨ᵇ φ.not` for each sentence `φ`; so it also requires a model, as clause 1 does.

## Remarks

Example: for any $L$-structure $\mathcal{M}$, the theory $\mathrm{Th}(\mathcal{M})$ of all sentences true in $\mathcal{M}$ is complete.
It has the model $\mathcal{M}$, and for each sentence $\varphi$ either $\varphi$ or $\neg\varphi$ is true in $\mathcal{M}$, hence lies in $\mathrm{Th}(\mathcal{M})$.

Non-example: the theory of groups has a model but is not complete.
For $\varphi = \forall x \, \forall y \, (x \cdot y = y \cdot x)$, the group $\Z$ satisfies $\varphi$ and the symmetric group $S_3$ satisfies $\neg\varphi$.

A satisfiable theory $T$ is complete if and only if all its models are [[elementarily equivalent|P3B1V182N4]].
By the completeness theorem, $T \models \varphi$ can be replaced by $T \vdash \varphi$, provability from $T$.
Some authors do not require clause 1.

## Explanations

### L1 human

A complete theory answers every question that its language can ask.
Each structure has a complete theory, its full list of true sentences.
A natural list of axioms is complete only in special cases, such as the axioms of dense linear orders without endpoints, or of algebraically closed fields of a fixed characteristic.

### L2 human

We check that $T = \set{\forall x \, \forall y \, (x = y)}$ in the empty signature is complete.

1. $T$ has a model, a one-element set.
2. Every model of $T$ has exactly one element, and any two one-element sets are isomorphic.
3. Isomorphic structures satisfy the same sentences. So for each $\varphi$, either every model of $T$ satisfies $\varphi$ or every model satisfies $\neg\varphi$.

A trap is to forget clause 1: the theory $\set{\exists x \, \neg(x = x)}$ has no model and is not complete under this definition.
