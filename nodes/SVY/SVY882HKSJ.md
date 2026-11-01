---
tag: SVY882HKSJ
kind: definition
name: Valuation
msc: [12J20, 13F30]
defines: B85T5VKR3M
uses: [0QA8CHH8MG, 071DDFVG4J]
sources:
  - url: https://en.wikipedia.org/wiki/Valuation_(algebra)
---

## Definition

Let $K$ be a [[field|0QA8CHH8MG]] and let $\Gamma$ be a totally ordered [[abelian group|071DDFVG4J]], written additively.
Add to $\Gamma$ a symbol $\infty$ with $\gamma < \infty$ and $\gamma + \infty = \infty + \gamma = \infty + \infty = \infty$ for all $\gamma \in \Gamma$.
A *valuation* on $K$ with values in $\Gamma$ is a map $v \colon K \to \Gamma \cup \set{\infty}$ such that:

1. $v(x) = \infty$ if and only if $x = 0$.
2. $v(xy) = v(x) + v(y)$ for all $x, y \in K$.
3. $v(x + y) \ge \min(v(x), v(y))$ for all $x, y \in K$.

The subgroup $v(K^\times)$ of $\Gamma$ is the *value group* of $v$.
The pair $(K, v)$ is a *valued field*.

## Remarks

Example: for a prime $p$, the [[p-adic valuation|04VCPS30ZE]] $v_p$ on $\Q$ with values in $\Z$ is a valuation.
If $x = p^m a/b$ and $y = p^n c/d$ with $a, b, c, d$ prime to $p$ and $m \le n$, then $xy = p^{m+n} ac/(bd)$ gives clause 2, and $x + y = p^m (ad + p^{n-m} cb)/(bd)$ gives $v_p(x + y) \ge m$, which is clause 3.
Example: on the field $k(t)$ of rational functions over a field $k$, the map $f/g \mapsto \deg g - \deg f$ is a valuation with values in $\Z$.
Non-example: the map $v \colon \Q \to \Z \cup \set{\infty}$ with $v(0) = \infty$ and $v(x) = 1$ for $x \ne 0$ fails clause 2, since $v(1 \cdot 1) = 1 \ne 2 = v(1) + v(1)$.
Every field has the *trivial valuation*, with $v(x) = 0$ for all $x \ne 0$.
Clauses 1 and 2 give $v(1) = 0$, $v(-x) = v(x)$ and $v(x^{-1}) = -v(x)$ for $x \ne 0$.
The set $\set{x \in K : v(x) \ge 0}$ is a [[valuation ring|QSX12D8RQM]] of $K$.
Some texts write valuations multiplicatively, with the reverse order; for $\Gamma \subseteq \R$ the map $x \mapsto c^{v(x)}$ with $0 < c < 1$ is a [[non-Archimedean absolute value|1H5F1BP6XS]].
