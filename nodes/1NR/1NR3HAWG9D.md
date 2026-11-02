---
tag: 1NR3HAWG9D
kind: statement
role: theorem
name: Compactness theorem
msc: [03C07, 03B10]
uses: [DKFGQTRYZE, MVCH6N9SNW, QN7M1JCGT9]
about: [QN7M1JCGT9]
sources:
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
same_as:
  wikidata: Q1149458
  wikipedia: Compactness theorem
---

## Statement

Let $\sigma$ be a signature and let $\Gamma$ be a set of first-order [[sentences|DKFGQTRYZE]] over $\sigma$.
Then $\Gamma$ has a [[model|MVCH6N9SNW]] if and only if every finite subset of $\Gamma$ has a model.

## Remarks

One direction is clear, since a model of $\Gamma$ is a model of each subset.
For the other, if $\Gamma$ had no model, then by [[Gödel's completeness theorem|WQ1ZE255SF]] it would derive a contradiction.
That derivation uses only finitely many sentences of $\Gamma$, and this finite subset would have no model.
A second proof builds a model as an [[ultraproduct|AX9Q86GB8M]] of models of the finite subsets.
Application: let $\Gamma$ be the true sentences of arithmetic, plus $c > \underline{n}$ for a new constant $c$ and each numeral $\underline{n}$.
Each finite subset holds in $\N$ with $c$ a large number, so $\Gamma$ has a model, a [[non-standard model of arithmetic|1QWN5CV4CG]].
In Mathlib the theorem is `FirstOrder.Language.Theory.isSatisfiable_iff_isFinitelySatisfiable`.

## Explanations

### L1 human

If every finite part of a list of axioms can be made true, then the whole infinite list can be made true at once.
This sounds simple, but it has strong consequences.
For example, it gives models of arithmetic with numbers larger than every ordinary natural number.

### L2 human

Compactness is the main tool of [[model theory|HFTBG5PMXC]].
A typical use shows that some property cannot be expressed in first-order logic.
If a theory has finite models of every size, then it has an infinite model, so "the domain is finite" is not first-order.
The theorem is named after compactness in topology: it says that a certain space of complete theories, the Stone space, is compact.
By [[Lindström's theorem|FYZ3CJGZYV]], first-order logic is the strongest logic that has both compactness and the downward [[Löwenheim–Skolem theorem|484M0TZ1S7]].
