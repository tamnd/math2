---
tag: MWGG1P8WDC
kind: definition
name: Sum-free set
msc: [11B75, 11P70, 05D10]
defines: 7SHV2SPYP6
uses: [082GHNPJ53, XNBN31HQWB]
sources:
  - url: https://en.wikipedia.org/wiki/Sum-free_set
---

## Definition

Let $G$ be an [[abelian group|082GHNPJ53]] written additively, and let $A$ be a subset of $G$.
The set $A$ is *sum-free* if there are no $x, y, z \in A$, not necessarily distinct, with $x + y = z$.

## Remarks

Equivalently, $(A + A) \cap A = \emptyset$, where $A + A$ is the [[sumset|XNBN31HQWB]].
The set of odd integers is sum-free in $\Z$: if $x$ and $y$ are odd, then $x + y$ is even, so it is not in the set.
The set $\set{1, 2, 4}$ is not sum-free: with $x = y = 2$ one gets $x + y = 4$, and repeated elements are allowed.
For a positive integer $N$, the upper half $\set{n : N/2 < n \le N}$ of $\set{1, \dots, N}$ is sum-free, since any sum of two of its elements exceeds $N$.
The set $\set{0}$ is never sum-free, since $0 + 0 = 0$; so a sum-free subset of a group does not contain $0$.
