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

Fix $m \ge 2$ and let $V_m = \set{0, \tfrac{1}{m-1}, \tfrac{2}{m-1}, \dots, 1}$.
The *algebra of Post's connectives* of order $m$ is $\mathbf{P}_m = \langle V_m, \neg, \lor, \land \rangle$ with
$$\neg u = \begin{cases} 1 & \text{if } u = 0, \\ u - \tfrac{1}{m-1} & \text{if } u \ne 0, \end{cases} \qquad u \lor v = \max(u, v), \qquad u \land v = \min(u, v).$$
For $1 \le \lambda \le m - 1$, the *Post logic* $\mathrm{P}_m^\lambda$ is the logic of the [[logical matrix|AJEJS6TFWP]] $\langle \mathbf{P}_m, D_\lambda \rangle$, where $D_\lambda$ is the set of the $\lambda$ greatest values.

A set $C$ of [[operations|EJ8YJVM9BW]] on $V_m$ is *functionally complete* when every function $f \colon V_m^n \to V_m$ with $n \ge 1$ is a composition of operations in $C$ and projections.

## Notation

With the labels $0, 1, \dots, m - 1$ in place of $\tfrac{k}{m-1}$, negation is $\neg x = x - 1 \bmod m$.
The *shift* $S x = x + 1 \bmod m$ is $\neg$ applied $m - 1$ times.
SEP records only the number $\lambda$ of designated values; the choice of the $\lambda$ greatest values is the convention used here.

## Remarks

1. Example: in $\mathbf{P}_4$ with labels $0, 1, 2, 3$, negation is the cycle $3 \mapsto 2 \mapsto 1 \mapsto 0 \mapsto 3$.
2. Non-example: the map $u \mapsto 1 - u$ on $V_m$ is not Post's negation for $m \ge 3$: it fixes $\tfrac12$ when $m = 3$, while Post's $\neg$ fixes no value.
3. For $m = 2$, $\mathbf{P}_2$ is the two-element Boolean algebra and $\mathrm{P}_2^1$ is classical logic.
4. The operation $\land$ is redundant: it is a term in $\neg$ and $\lor$, by [[Post's completeness theorem|8P3Y6T0RZS]].

## Explanations

### L1 human

Put $m$ values on a line from $0$ to $1$ in equal steps.
"Or" takes the larger value and "and" the smaller.
"Not" moves one step down, and from $0$ it jumps to $1$.
Some of the top values count as true.

### L2 human

Negation is a rotation of the $m$ values, not a reflection.
Applying it $m$ times returns every value to its start.
A trap: $\neg$ does not reverse the order, so De Morgan's laws fail.
For $m = 3$ at $(\tfrac12, 1)$: $\neg \max(\tfrac12, 1) = \neg 1 = \tfrac12$, but $\min(\neg \tfrac12, \neg 1) = \min(0, \tfrac12) = 0$.
