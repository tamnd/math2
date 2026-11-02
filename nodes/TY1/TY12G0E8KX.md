---
tag: TY12G0E8KX
kind: problem
name: Measure problem of Lebesgue
msc: [28A12, "28E15", "03E55"]
uses: [2Z2QVWZ262, D7KB9HFCGZ, 087VJM5Q77]
about: [2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Measurable_cardinal
  - url: https://en.wikipedia.org/wiki/Non-measurable_set
history:
  posed_by: "Henri Lebesgue"
  first_stated: "1902"
---

## Problem

Is there a function $m$, defined on all bounded subsets of $\R$, with values in $[0, \infty)$, such that:

1. $m$ is [[countably additive|D7KB9HFCGZ]]: $m\big(\bigcup_k A_k\big) = \sum_k m(A_k)$ for pairwise disjoint bounded $A_k$ whose union is bounded.
2. $m$ is invariant under congruence: $m(A) = m(B)$ when $B$ is a [[translation|087VJM5Q77]] or reflection of $A$.
3. $m([0, 1]) = 1$.

## Remarks

[[Lebesgue measure|2Z2QVWZ262]] has all three properties on the Lebesgue measurable sets.
The answer is negative: Vitali showed in 1905, with the Vitali set and the axiom of choice, that no such $m$ exists.
Banach and Ulam studied the question without congruence invariance.
Is there a countably additive measure on all subsets of $\R$ that is $0$ on points and $1$ on $[0, 1]$?
Ulam showed that a positive answer implies that some cardinal at most the continuum is real-valued measurable, a notion close to that of a [[measurable cardinal|AKBWT323RQ]].
Such a cardinal is weakly inaccessible, so ZFC cannot prove a positive answer, if ZFC is consistent.
Dropping countable additivity and keeping finite additivity leads to the [[Banach measure problem|JXK6NRDH4V]].

## Explanations

### L1 human

Lebesgue asked whether every bounded set of real numbers can be given a length.
The length should add up over countably many disjoint pieces and should not change when a set is shifted.
The answer is no, and the obstruction is the existence of very wild sets built with the axiom of choice.
Weaker versions of the question lead deep into set theory, to large cardinals.
