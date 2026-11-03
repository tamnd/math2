---
tag: ZX29QH2GMT
kind: definition
name: Pareto efficiency
msc: [91B15, 91B50, 90C29]
defines: JREVYHFY4T
uses: [JGP0Q56FRY]
sources:
  - url: https://en.wikipedia.org/wiki/Pareto_efficiency
---

## Definition

Let $A$ be a set of feasible outcomes and let $1, \dots, n$ be agents.
Agent $i$ has a [[preference relation|JGP0Q56FRY]] $\succsim_i$ on $A$, with strict part $\succ_i$.
An outcome $b \in A$ *Pareto dominates* $a \in A$ if $b \succsim_i a$ for every $i$ and $b \succ_j a$ for at least one $j$.
An outcome $a \in A$ is *Pareto efficient* (Pareto optimal) if no outcome in $A$ Pareto dominates it.

## Remarks

Example: in an exchange economy with total endowment $(1, 1)$ and two consumers with utility $\sqrt{x y}$, the allocation giving $(1/2, 1/2)$ to each is Pareto efficient.
Indeed, if consumer $1$ gets $(s, t)$ and consumer $2$ gets $(1 - s, 1 - t)$, then $\sqrt{st} + \sqrt{(1-s)(1-t)} \le \frac{s + t}{2} + \frac{(1-s) + (1-t)}{2} = 1$ by the AM–GM inequality.
So the two utilities cannot both be at least $1/2$ with one above $1/2$.

Non-example: the allocation giving $(1, 0)$ to consumer $1$ and $(0, 1)$ to consumer $2$ gives both utility $0$.
It is Pareto dominated by the allocation above, which gives both utility $1/2$.

With utility functions $u_i$, the outcome $a$ is Pareto efficient when there is no $b \in A$ with $u_i(b) \ge u_i(a)$ for all $i$ and $u_j(b) > u_j(a)$ for some $j$.
A weaker notion, weak Pareto efficiency, only rules out outcomes that are strictly better for every agent.
