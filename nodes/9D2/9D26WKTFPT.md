---
tag: 9D26WKTFPT
kind: definition
name: Scott topology
msc: [06B35, 06B30, 54A10]
defines: ZR8A03FV67
uses: [0QV2JS9RJ3, ETCE287E2R, D9RY4667K6, 0R3H5PANRQ, 0CQHFPGJ45, CMYVK9CEKZ]
sources:
  - url: https://en.wikipedia.org/wiki/Scott_continuity
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
A subset $U \subseteq P$ is *Scott-open* if:

1. $U$ is an [[upper set|ETCE287E2R]]: if $x \in U$ and $x \le y$, then $y \in U$;
2. $U$ is inaccessible by directed suprema: for every [[directed subset|D9RY4667K6]] $D \subseteq P$ that has a [[supremum|0R3H5PANRQ]] with $\bigvee D \in U$, the set $D \cap U$ is nonempty.

The Scott-open sets form a topology on $P$, the *Scott topology*.

## Remarks

The Scott topology makes $P$ a [[topological space|0CQHFPGJ45]] that is $T_0$, and its [[specialization preorder|CMYVK9CEKZ]] is the order $\le$; the closure of $\set{x}$ is $\set{y : y \le x}$.
It is $T_1$ only when the order is trivial.
Example: in $\N \cup \set{\infty}$, the set $U = \set{n \in \N : n \ge 3} \cup \set{\infty}$ is Scott-open.
It is an upper set, and a directed $D$ with $\bigvee D \in U$ either contains its supremum, or is infinite and so contains some $n \ge 3$.
Non-example: in the same poset, $\set{\infty}$ is an upper set but is not Scott-open, since $D = \N$ has supremum $\infty$ and $D \cap \set{\infty} = \varnothing$.
Closed sets of the Scott topology are the down-sets closed under suprema of directed subsets.
