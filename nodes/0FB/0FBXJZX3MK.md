---
tag: 0FBXJZX3MK
kind: statement
role: proposition
name: Closed subsets of complete spaces are complete
msc: ["54E50"]
uses: [08EWT7J0SC, 09GQ3ZTQJ9, 0T2WYDTRP2]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_metric_space
    locator: Some theorems
---

## Statement

Let $(X, d)$ be a [[complete metric space|08EWT7J0SC]] and let $F$ be a [[closed subset|0G5AV9Q4RR]] of $X$.
Then $F$ with the [[subspace metric|0T2WYDTRP2]] is complete.

## Remarks

Proof: let $(x_n)$ be a Cauchy sequence in $F$. It is Cauchy in $X$, so it converges to some $x \in X$. Then $x \in F$, because [[closed sets contain their limits|09GQ3ZTQJ9]].
For example, $[0, 1]$, $\mathbb{Z}$ and each closed ball of $\mathbb{R}^n$ are complete.
The converse is [[complete subspaces are closed|0W41XG4W60]].

## Explanations

### L1 human

A Cauchy sequence in $F$ has a limit in the big complete space.
Because $F$ is closed, this limit cannot escape from $F$.
