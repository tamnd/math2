---
tag: NX4V39GJCV
kind: definition
name: Thin set
msc: [31C40, 31B15]
defines: 7DGF6MMEGX
uses: [X4V2S56YQQ, 033RZ32T4Q, 07EGCNHAVW]
sources:
  - url: https://en.wikipedia.org/wiki/Fine_topology_(potential_theory)
---

## Definition

Let $n \ge 2$, let $E \subseteq \R^n$ and let $x \in \R^n$.
The set $E$ is *thin at* $x$ if one of the following holds.

1. The point $x$ is not a [[limit point|07EGCNHAVW]] of $E$.
2. The point $x$ is a limit point of $E$, and there is a [[superharmonic function|X4V2S56YQQ]] $u$ on an open neighbourhood of $x$ such that
$$\liminf_{y \to x,\ y \in E \setminus \set{x}} u(y) > u(x).$$

## Remarks

The left side of clause 2 is a [[limit inferior|033RZ32T4Q]] along points of $E$ other than $x$.
Example: in $\R^3$ let $x_k = 2^{-k} e_1$ for $k \ge 1$ and $E = \set{x_k : k \ge 1}$, with $x = 0$.
Put $u(y) = \sum_{k \ge 1} 4^{-k} \abs{y - x_k}^{-1}$.
This is a series of positive Newtonian potentials with $u(0) = \sum_k 4^{-k} 2^{k} = 1$, so $u$ is superharmonic on $\R^3$.
Since $u(x_k) = +\infty$ for every $k$, clause 2 holds, and $E$ is thin at $0$.
Non-example: a closed ball $B$ is not thin at a point $x \in \partial B$.
If $u$ were as in clause 2, then $u(x)$ is finite and $u \ge u(x) + \varepsilon$ on $B$ near $x$ for some $\varepsilon > 0$, while $u \ge u(x) - \delta$ near $x$ for any $\delta > 0$ by lower semicontinuity.
A small sphere about $x$ has nearly half of its area in $B$, so its mean value of $u$ exceeds $u(x)$, against the super-mean value inequality.
For $n \ge 3$, Wiener's criterion says that $E$ is thin at a limit point $x$ if and only if $\sum_{k} 2^{k(n-2)} c(E_k) < \infty$, where $E_k = \set{y \in E : 2^{-k-1} \le \abs{y - x} \le 2^{-k}}$ and $c$ is Newtonian capacity.
