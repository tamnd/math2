---
tag: XA7YE70A6P
kind: counterexample
name: Ol'shanskii's counterexample to the von Neumann conjecture
msc: ["43A07", "20F50", "20F65"]
uses: [TE19BGFFF1, CEAT9BESKK, 0KTW26C80J, 7K2N7P38TZ]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Neumann_conjecture
---

## Counterexample

Let $p$ be a large prime and let $G$ be a [[Tarski monster group|TE19BGFFF1]] for $p$ of the kind constructed by Ol'shanskii.
So $G$ is infinite, and every subgroup of $G$ other than $\set{1}$ and $G$ is cyclic of order $p$.
Ol'shanskii proved in 1980 that such groups can be chosen not [[amenable|CEAT9BESKK]].
On the other hand, $G$ has no subgroup isomorphic to the [[free group|0KTW26C80J]] $F_2$.
So $G$ is a non-amenable group without free subgroups of rank $2$, and the [[von Neumann conjecture|7K2N7P38TZ]] fails.

## Remarks

Why $G$ has no free subgroup: every element $g \ne 1$ of $G$ lies in a proper nontrivial subgroup, which is cyclic of order $p$, so $g^p = 1$.
A free group of rank $2$ has elements of infinite order, so it cannot embed in $G$.
The non-amenability is the hard part; the proof uses Grigorchuk's cogrowth criterion, a form of [[Kesten's criterion|FYJE0R4PGT]].

## Explanations

### L1 human

The von Neumann conjecture said that a group that cannot be averaged fairly must contain a free group.
Ol'shanskii's Tarski monsters are infinite groups in which every element has the same prime order, so they contain no free group.
Yet they still cannot be averaged fairly.
This shows that non-amenability can come from something other than a free subgroup.
