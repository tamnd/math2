---
tag: NN6QM9JMKB
kind: definition
name: Complete theory
msc: [03C35, 03C07]
defines: 655K8Y7VS8
uses: [92SWXST1ZM, MVCH6N9SNW, DKFGQTRYZE]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_theory
---

## Definition

Let $L$ be a signature and let $T$ be an $L$-[[theory|92SWXST1ZM]].
For an $L$-[[sentence|DKFGQTRYZE]] $\varphi$, write $T \models \varphi$ when every [[model|MVCH6N9SNW]] of $T$ satisfies $\varphi$.
The theory $T$ is complete when the following hold.

1. $T$ has a model.
2. For every $L$-sentence $\varphi$, $T \models \varphi$ or $T \models \neg\varphi$.

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
