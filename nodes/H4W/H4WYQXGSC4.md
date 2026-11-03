---
tag: H4WYQXGSC4
kind: definition
name: Bass stable range
msc: [19B10, 19A13]
defines: DZBM27VRAF
uses: [0B1261B5ED, 07C6ECNJET]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_range_condition
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity and let $m \ge 1$.
A row $(a_1, \ldots, a_m)$ of elements of $R$ is *unimodular* if $R a_1 + \cdots + R a_m = R$.
Let $n \ge 1$.
The ring $R$ satisfies the *stable range condition* $\mathrm{sr}(R) \le n$ if for every unimodular row $(a_1, \ldots, a_{n+1})$ there are $b_1, \ldots, b_n \in R$ such that $(a_1 + b_1 a_{n+1}, \ldots, a_n + b_n a_{n+1})$ is unimodular.
The *stable rank* $\mathrm{sr}(R)$ is the least such $n$, or $\infty$ if there is none.

## Remarks

If $\mathrm{sr}(R) \le n$, then $\mathrm{sr}(R) \le n'$ for every $n' \ge n$.
Bass's original notation $SR_{n+1}$ is the condition $\mathrm{sr}(R) \le n$ here, so the index is shifted by one.
The condition $\mathrm{sr}(R) \le 1$ says: if $Ra + Rb = R$, then $a + tb$ is a [[unit|07C6ECNJET]] for some $t \in R$.
Bass proved that a commutative Noetherian ring of Krull dimension $d$ has $\mathrm{sr}(R) \le d + 1$.

Example: a field $F$ has $\mathrm{sr}(F) = 1$.
If $Fa + Fb = F$ and $a \ne 0$, take $t = 0$; if $a = 0$, then $b \ne 0$ and $a + 1 \cdot b = b$ is a unit.
Every commutative local ring also has stable rank $1$.

Non-example of $\mathrm{sr} \le 1$: the ring $\Z$.
The row $(2, 5)$ is unimodular since $3 \cdot 2 - 5 = 1$, but $2 + 5t$ is never $\pm 1$ for an integer $t$.
So $\mathrm{sr}(\Z) \ge 2$, and Bass's bound with $d = 1$ gives $\mathrm{sr}(\Z) = 2$.
