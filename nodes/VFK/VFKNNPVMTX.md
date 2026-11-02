---
tag: VFKNNPVMTX
kind: definition
name: Complete Boolean algebra
msc: ["06E10"]
defines: 75BPV95AAS
uses: [0XADJKM699, D7A0ZGZT5S]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_Boolean_algebra
---

## Definition

Let $B$ be a [[Boolean algebra|0XADJKM699]] with order $\le$.
The algebra $B$ is *complete* if every subset $S \subseteq B$ has a supremum $\bigvee S$ in $B$, that is, a least upper bound for $\le$.

## Remarks

Then every subset also has an infimum, $\bigwedge S = \neg \bigvee \set{\neg s : s \in S}$, so $B$ is a [[complete lattice|D7A0ZGZT5S]].
The infinite distributive laws $a \wedge \bigvee S = \bigvee \set{a \wedge s : s \in S}$ hold in every complete Boolean algebra.

Example: the power set of a set $X$, ordered by inclusion.
The supremum of a family of subsets is its union, which is again a subset of $X$.

Non-example: the algebra $B$ of finite and cofinite subsets of $\N$ is not complete.
Let $S = \set{\set{2n} : n \in \N}$.
An upper bound of $S$ in $B$ contains all even numbers, so it is infinite and hence cofinite, and it contains infinitely many odd numbers.
Removing one odd number gives a smaller upper bound in $B$, so there is no least one.

In Mathlib the notion is `CompleteBooleanAlgebra`.
