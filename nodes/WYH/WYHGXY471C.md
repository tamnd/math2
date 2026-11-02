---
tag: WYHGXY471C
kind: counterexample
name: Vitali set
msc: [28A05, "03E25"]
uses: [2Z2QVWZ262, 0HTGB13FE2, 0G8VEZ3WTK, 01TQB88H4C]
sources:
  - url: https://en.wikipedia.org/wiki/Vitali_set
same_as:
  wikidata: Q257387
  wikipedia: Vitali set
---

## Counterexample

On $[0, 1]$, let $x \sim y$ mean that $x - y$ is a rational number.
This is an [[equivalence relation|0G8VEZ3WTK]].
By the [[axiom of choice|0HTGB13FE2]], there is a set $V \subseteq [0, 1]$ that contains exactly one element of each equivalence class.
Such a set $V$ is called a Vitali set.
No Vitali set is measurable for [[Lebesgue measure|2Z2QVWZ262]] $\lambda$.

## Remarks

Let $q_1, q_2, \ldots$ list the [[countable set|01TQB88H4C]] $\Q \cap [-1, 1]$, and put $V_k = V + q_k = \set{v + q_k : v \in V}$.
The sets $V_k$ are pairwise disjoint: if $v + q_k = w + q_j$ with $v, w \in V$, then $v \sim w$, so $v = w$ and $q_k = q_j$.
Every $x \in [0, 1]$ is equivalent to some $v \in V$, and then $x - v \in \Q \cap [-1, 1]$; so $[0, 1] \subseteq \bigcup_k V_k \subseteq [-1, 2]$.
If $V$ were measurable, each $V_k$ would be measurable with $\lambda(V_k) = \lambda(V)$, by translation invariance.
Countable additivity would give $1 \le \sum_{k} \lambda(V) \le 3$.
This is impossible: the sum is $0$ if $\lambda(V) = 0$ and $\infty$ otherwise.
The same argument shows that there is no translation-invariant, countably additive measure on all subsets of $\R$ that gives $[0, 1]$ a finite positive value.
Some form of choice is needed.
Solovay showed that, if an inaccessible cardinal is consistent with ZFC, then so is ZF with dependent choice and all sets of reals Lebesgue measurable.

## Explanations

### L1 human

Group the numbers of $[0, 1]$ into classes, putting two numbers in the same class when they differ by a fraction.
Pick one number from each class to form the set $V$.
Countably many shifted copies of $V$ fill $[0, 1]$ without overlap and stay inside $[-1, 2]$.
If $V$ had a length, these equal lengths would have to add up to a number between $1$ and $3$.
But countably many equal numbers add up to $0$ or to $\infty$.
So $V$ cannot be given a length at all.
