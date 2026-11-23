---
tag: PHGRJ2D97H
kind: definition
name: Post's m-valued logic
msc: ["03B50"]
topics: [WZP584JQ06]
audience: research
defines: YHYSGRE7JV
uses: [66NMTCQNQV, AJEJS6TFWP, EJ8YJVM9BW]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
    locator: Post logics Pm
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 3.3 The expressive power of many-valued logics
---

## Definition

Post's $m$-valued logic puts $m$ values in equal steps from $0$ to $1$ and uses a negation that turns them in a circle.
Fix $m \ge 2$ and let $V_m = \{0, \tfrac{1}{m-1}, \tfrac{2}{m-1}, \dots, 1\}$.
The *algebra of Post's connectives* of order $m$ is $\mathbf{P}_m = \langle V_m, \neg, \lor, \land \rangle$, with the operations below.
$$\neg u = \begin{cases} 1 & \text{if } u = 0, \\ u - \tfrac{1}{m-1} & \text{if } u \ne 0, \end{cases} \qquad u \lor v = \max(u, v), \qquad u \land v = \min(u, v).$$
For $1 \le \lambda \le m - 1$, the *Post logic* $\mathrm{P}_m^\lambda$ is the logic of the [[logical matrix|AJEJS6TFWP]] $\langle \mathbf{P}_m, D_\lambda \rangle$, where $D_\lambda$ is the set of the $\lambda$ greatest values.

A set $C$ of [[operations|EJ8YJVM9BW]] on $V_m$ is *functionally complete* when every function $f \colon V_m^n \to V_m$ with $n \ge 1$ is a composition of operations in $C$ and projections.

## Notation

With the labels $0, 1, \dots, m - 1$ in place of $\tfrac{k}{m-1}$, negation becomes $\neg x = x - 1 \bmod m$.
The *shift* $S x = x + 1 \bmod m$ is $\neg$ applied $m - 1$ times.
The Stanford Encyclopedia records only the number $\lambda$ of designated values; taking the $\lambda$ greatest values is the convention we use.

## Remarks

Each part of the definition has a job.
The values are linearly ordered so that $\max$ and $\min$ make sense as disjunction and conjunction.
The negation is cyclic, not order-reversing, and this is what gives [[functional completeness|8P3Y6T0RZS]].
The designated set $D_\lambda$ turns the algebra into a matrix, so that $\mathrm{P}_m^\lambda$ is a [[many-valued logic|66NMTCQNQV]] with a consequence relation.

For an example, take $\mathbf{P}_4$ with labels $0, 1, 2, 3$.
Negation is the cycle $3 \mapsto 2 \mapsto 1 \mapsto 0 \mapsto 3$, and four steps return every value to its start.
For $m = 2$, $\mathbf{P}_2$ is the two-element Boolean algebra and $\mathrm{P}_2^1$ is classical logic.

A case that fails is the map $u \mapsto 1 - u$ on $V_3$.
It fixes $\tfrac12$, while Post's negation sends $\tfrac12$ to $0$ and fixes no value.
The algebra with $1 - u$ in place of $\neg$ is the algebra of Kleene's logic, and it is not functionally complete.

The operation $\land$ is in the definition for convenience only.
It is a term in $\neg$ and $\lor$, by [[Post's completeness theorem|8P3Y6T0RZS]].
The concept page, [[Post's many-valued logics|YHYSGRE7JV]], works the first examples.

## Explanations

### L1 human

Put $m$ values on a line from $0$ to $1$ in equal steps.
"Or" takes the larger value and "and" the smaller one.
"Not" moves one step down, and from $0$ it jumps to $1$.
Some of the top values count as true.

### L2 human

Negation is a rotation of the $m$ values, not a reflection.
Applying it $m$ times returns every value to its start.
Watch out: because $\neg$ does not reverse the order, De Morgan's laws fail.
Take $m = 3$ at the pair $(\tfrac12, 1)$ and compute both sides:
$$\neg \max(\tfrac12, 1) = \neg 1 = \tfrac12, \qquad \min(\neg \tfrac12, \neg 1) = \min(0, \tfrac12) = 0.$$
The two values differ, so $\neg(p \lor q)$ and $\neg p \land \neg q$ are not equivalent in $\mathrm{P}_3$.
