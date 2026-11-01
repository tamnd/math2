---
tag: ZYK5F0GBK6
kind: definition
name: Discrete valuation
msc: [12J20, 13F30]
defines: A2KKZAV29W
uses: [B85T5VKR3M, 0QA8CHH8MG]
sources:
  - url: https://en.wikipedia.org/wiki/Valuation_(algebra)
---

## Definition

Let $K$ be a [[field|0QA8CHH8MG]].
A *discrete valuation* on $K$ is a [[valuation|B85T5VKR3M]] $v \colon K \to \Z \cup \set{\infty}$ such that $v(K^\times) = \Z$.
An element $\pi \in K$ with $v(\pi) = 1$ is a *uniformizer* of $v$.

## Remarks

Example: for a prime $p$, the [[p-adic valuation|04VCPS30ZE]] $v_p$ on $\Q$ is a discrete valuation.
It is a valuation, and $v_p(p^n) = n$ for every $n \in \Z$, so it is onto $\Z$; the prime $p$ is a uniformizer.
Example: for a field $k$, the order of vanishing at $0$ on $k(t)$, given by $v(t^n f/g) = n$ for polynomials $f, g$ with $f(0) g(0) \ne 0$, is a discrete valuation with uniformizer $t$.
Non-example: the trivial valuation on a field, with $v(x) = 0$ for all $x \ne 0$, takes values in $\Z$ but has $v(K^\times) = \set{0} \ne \Z$.
Some texts call a valuation discrete when its value group is isomorphic to $\Z$; dividing by a positive generator then gives a valuation onto $\Z$, called normalized.
Every $x \in K^\times$ is $x = u \pi^{v(x)}$ with $v(u) = 0$.
The set $\set{x : v(x) \ge 0}$ is a [[discrete valuation ring|MGM3CNJW9V]] with maximal ideal $\pi \cdot \set{x : v(x) \ge 0}$.
