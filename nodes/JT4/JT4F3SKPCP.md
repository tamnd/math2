---
tag: JT4F3SKPCP
kind: definition
name: Growth rate of a group
msc: [20F69, 20F65]
defines: 4CMRM3975W
uses: [082DWWXMRJ, 0RP7VWQ0YN, 0KTW26C80J]
sources:
  - url: https://en.wikipedia.org/wiki/Growth_rate_(group_theory)
---

## Definition

Let $G$ be a [[finitely generated group|082DWWXMRJ]] and let $S$ be a finite [[generating set|0RP7VWQ0YN]] of $G$.
The *word length* $\abs{g}_S$ of $g \in G$ is the least $n$ such that $g = s_1 \cdots s_n$ with each $s_i \in S \cup S^{-1}$.
The *growth function* of $G$ with respect to $S$ is
$$\gamma_S(n) = \abs{\set{g \in G : \abs{g}_S \le n}}, \quad n \in \N.$$
For functions $f, h \colon \N \to \N$, write $f \preceq h$ if there is a constant $C \ge 1$ with $f(n) \le h(Cn)$ for all $n$, and $f \sim h$ if $f \preceq h$ and $h \preceq f$.
The *growth rate* of $G$ is the $\sim$-class of $\gamma_S$.

1. $G$ has *polynomial growth* if $\gamma_S(n) \le C n^d$ for some constants $C, d > 0$ and all $n \ge 1$.
2. $G$ has *exponential growth* if $\gamma_S(n) \ge a^n$ for some $a > 1$ and all $n$.
3. $G$ has *intermediate growth* if it has neither polynomial nor exponential growth.

## Remarks

The class of $\gamma_S$ does not depend on $S$.
If $S'$ is another finite generating set, each element of $S'$ is a word of length at most some $C$ in $S$, so $\gamma_{S'}(n) \le \gamma_S(Cn)$.
Hence the three types above do not depend on $S$.

Example: $G = \Z^2$ with $S = \set{(1, 0), (0, 1)}$.
The elements of length at most $n$ are the $(a, b)$ with $\abs{a} + \abs{b} \le n$, so $\gamma_S(n) = 2n^2 + 2n + 1$, and $\Z^2$ has polynomial growth.

Example: the [[free group|0KTW26C80J]] on $\set{a, b}$.
There are $4 \cdot 3^{k-1}$ reduced words of length $k \ge 1$, so $\gamma_S(n) = 2 \cdot 3^n - 1$, and the growth is exponential.

Non-example: the additive group $\Q$ is not finitely generated, so the definition does not apply; with an infinite generating set the balls may be infinite.

Since $\gamma_S(m + n) \le \gamma_S(m) \gamma_S(n)$, the limit $\lim_{n \to \infty} \gamma_S(n)^{1/n}$ exists, and $G$ has exponential growth exactly when this limit is greater than $1$.
