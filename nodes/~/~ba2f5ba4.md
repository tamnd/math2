---
tag: ~ba2f5ba4
kind: statement
role: proposition
name: Closed subsets of complete spaces are complete
msc: ["54E50"]
uses: [~aae963c7, ~26824759, ~e02a631b]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_metric_space
    locator: Some theorems
---

## Statement

Let $(X, d)$ be a [[complete metric space|~aae963c7]] and let $F$ be a [[closed subset|~dfeacff3]] of $X$.
Then $F$ with the [[subspace metric|~e02a631b]] is complete.

## Remarks

Proof: let $(x_n)$ be a Cauchy sequence in $F$. It is Cauchy in $X$, so it converges to some $x \in X$. Then $x \in F$, because [[closed sets contain their limits|~26824759]].
For example, $[0, 1]$, $\mathbb{Z}$ and each closed ball of $\mathbb{R}^n$ are complete.
The converse is [[complete subspaces are closed|~71d47767]].

## Explanations

### L1 human

A Cauchy sequence in $F$ has a limit in the big complete space.
Because $F$ is closed, this limit cannot escape from $F$.
