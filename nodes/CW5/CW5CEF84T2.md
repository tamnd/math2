---
tag: CW5CEF84T2
kind: definition
name: Sigma-finite measure
msc: [28A12]
defines: WEBBT18D4X
uses: [P15VQS5DJ9, PR11BZQQPG, 63Z1Q4FS23, 01TQB88H4C]
sources:
  - url: https://en.wikipedia.org/wiki/Σ-finite_measure
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]].
The [[measure|PR11BZQQPG]] $\mu$ is *σ-finite* if there are sets $A_1, A_2, \ldots$ in $\Sigma$ such that $X = \bigcup_{n=1}^{\infty} A_n$ and $\mu(A_n) < \infty$ for every $n$.

## Remarks

Lebesgue measure on $\R$ is σ-finite: take $A_n = [-n, n]$, of measure $2n$.
Counting measure on the power set of $\R$ is not σ-finite.
A set of finite counting measure is finite, a [[countable union|01TQB88H4C]] of finite sets is countable, and $\R$ is uncountable.
Every [[finite measure|63Z1Q4FS23]] is σ-finite, with $A_n = X$.
The sets $A_n$ can be chosen increasing, or pairwise disjoint, by the usual rearrangements.
