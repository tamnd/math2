---
tag: BP331JP8SF
kind: definition
name: Følner condition
msc: [43A07, 20F65]
defines: 82R5XGCART
uses: [G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Følner_sequence
---

## Definition

Let $G$ be a [[group|G5S1M9]], and for a subset $F \subseteq G$ and $g \in G$ let $gF = \set{gx : x \in F}$.
The group $G$ satisfies the *Følner condition* if the following holds.
For every finite set $S \subseteq G$ and every $\varepsilon > 0$, there is a finite nonempty set $F \subseteq G$ with
$$\abs{sF \,\triangle\, F} < \varepsilon \abs{F} \quad \text{for all } s \in S,$$
where $\triangle$ is the symmetric difference.
For a countable group, a *Følner sequence* is a sequence $(F_n)$ of finite nonempty subsets with $\abs{gF_n \triangle F_n} / \abs{F_n} \to 0$ for every $g \in G$.

## Remarks

Example: $G = \Z$ with $F_n = \set{0, 1, \ldots, n-1}$.
For $k \in \Z$ with $\abs{k} \le n$, the sets $k + F_n$ and $F_n$ differ in $2\abs{k}$ points, so $\abs{(k + F_n) \triangle F_n} / n = 2\abs{k}/n \to 0$.
So $(F_n)$ is a Følner sequence.

Non-example: the free group $F_2$ on two generators fails the condition.
Every finite nonempty $F \subseteq F_2$ has some generator $s$ with $\abs{sF \triangle F}$ at least a fixed positive fraction of $\abs{F}$.
This reflects that $F_2$ is not [[amenable|CEAT9BESKK]].

Følner's theorem says that a discrete group satisfies the Følner condition exactly when it is amenable.
For a [[locally compact group|AHV05ZBCYW]], one uses compact sets $F$ of positive [[Haar measure|VY0HXD3GC4]] and compact sets $S$ instead.
