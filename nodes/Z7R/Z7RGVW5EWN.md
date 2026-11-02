---
tag: Z7RGVW5EWN
kind: definition
name: Successor order
msc: [06A06, 06A05]
defines: NT44831EFE
uses: [0QV2JS9RJ3, 0AK9TGSNXY]
sources:
  - url: https://en.wikipedia.org/wiki/Successor_function
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]], and write $a < b$ when $a \le b$ and $a \ne b$.
A *successor order* on $P$ is a map $\operatorname{succ} \colon P \to P$ such that:

1. $a \le \operatorname{succ}(a)$ for all $a \in P$.
2. If $\operatorname{succ}(a) \le a$, then $a$ is a maximal element of $P$.
3. If $a < b$, then $\operatorname{succ}(a) \le b$.

## Remarks

When $a$ is not maximal, the clauses say that $\operatorname{succ}(a)$ is the least element of $\set{b \in P : a < b}$; when $a$ is maximal, $\operatorname{succ}(a) = a$.
So the map, if it exists, is unique.

Example: $\Z$ with $\operatorname{succ}(n) = n + 1$.
Check: $n \le n + 1$; the inequality $n + 1 \le n$ never holds, so clause 2 is empty; and $n < m$ for integers means $n + 1 \le m$.
On $\N$ this is the [[successor function|0AK9TGSNXY]].

Non-example: $\Q$ with the usual order has no successor order.
No rational is maximal, so clauses 1 and 2 force $a < \operatorname{succ}(a)$; then $b = (a + \operatorname{succ}(a))/2$ satisfies $a < b < \operatorname{succ}(a)$, which breaks clause 3.

The dual notion is a predecessor order.
In Mathlib this is the class `SuccOrder`.
