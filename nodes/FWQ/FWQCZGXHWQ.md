---
tag: FWQCZGXHWQ
kind: definition
name: Net
msc: [54A20]
defines: 4DVJQJV0DG
uses: [0CQHFPGJ45, 0ZCY0Z80B6, 0W4CN9E2W5, 0QEAJB91GZ, 0S1FJ8VEX9]
sources:
  - url: https://en.wikipedia.org/wiki/Net_(mathematics)
---

## Definition

Let $(D, \le)$ be a [[directed set|D9RY4667K6]] and let $X$ be a set.
A *net* in $X$ indexed by $D$ is a map $D \to X$, written $(x_d)_{d \in D}$.
Let $X$ be a [[topological space|0CQHFPGJ45]] and let $x \in X$.
The net $(x_d)_{d \in D}$ *converges* to $x$ if for every [[neighbourhood|0ZCY0Z80B6]] $U$ of $x$ there is $d_0 \in D$ such that $x_d \in U$ for all $d \in D$ with $d \ge d_0$.

## Remarks

Example: a sequence $(x_n)_{n \ge 1}$ is a net indexed by $\N$ with its usual order, and the net converges to $x$ exactly when the sequence [[converges|0W4CN9E2W5]] to $x$.

Example: let $A \subseteq X$ and let $x$ be in the [[closure|0QEAJB91GZ]] of $A$.
Let $D$ be the set of neighbourhoods of $x$, ordered by $U \le V$ when $V \subseteq U$; this is directed because $U \cap V$ is a neighbourhood.
For each $U$ choose $x_U \in U \cap A$.
Then $(x_U)$ converges to $x$: for a neighbourhood $U$ take $d_0 = U$, and every $V \ge U$ gives $x_V \in V \subseteq U$.

Non-example: in $\R$, the sequence $x_n = n$ is a net that converges to no point $x$, since the neighbourhood $(x - 1, x + 1)$ contains $x_n$ for at most two values of $n$.

A point lies in the closure of $A$ if and only if some net in $A$ converges to it.
A space is [[Hausdorff|0S1FJ8VEX9]] if and only if every net in it has at most one limit.
