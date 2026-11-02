---
tag: 3JGEQYCF6S
kind: definition
name: Filter limit
msc: [54A20, 40J05]
defines: F6QDHKE6J3
uses: [15PF73BKY6, 0CQHFPGJ45, 0ZCY0Z80B6, 70M1VAPFN0, 0W4CN9E2W5, 0S1FJ8VEX9]
sources:
  - url: https://en.wikipedia.org/wiki/Filter_(mathematics)
---

## Definition

Let $S$ be a set and let $\mathcal{F}$ be a [[filter|15PF73BKY6]] on $S$.
Let $X$ be a [[topological space|0CQHFPGJ45]], let $f \colon S \to X$ be a map, and let $x \in X$.
The map $f$ *tends to $x$ along $\mathcal{F}$*, and $x$ is a *limit of $f$ along $\mathcal{F}$*, if $f^{-1}(U) \in \mathcal{F}$ for every [[neighbourhood|0ZCY0Z80B6]] $U$ of $x$.

## Remarks

Equivalently, the image filter $f(\mathcal{F}) = \set{B \subseteq X : f^{-1}(B) \in \mathcal{F}}$ [[converges|70M1VAPFN0]] to $x$.

Example: on $S = \N$ let $\mathcal{F}$ be the filter of sets that contain $\set{n : n \ge N}$ for some $N$; in Mathlib this is `Filter.atTop`.
A sequence $f(n) = x_n$ tends to $x$ along $\mathcal{F}$ exactly when for every neighbourhood $U$ of $x$ there is $N$ with $x_n \in U$ for all $n \ge N$.
This is the usual [[convergence of a sequence|0W4CN9E2W5]].

Non-example: the sequence $f(n) = (-1)^n$ in $\R$ has no limit along this filter.
For $x \ne 1$, some neighbourhood of $x$ misses $1$, so its preimage misses all even numbers and contains no tail.
For $x = 1$, the preimage of $(0, 2)$ is the set of even numbers, which contains no tail either.

Example: for $a \in \R$, the sets $V \setminus \set{a}$ with $V$ a neighbourhood of $a$ generate a filter on $\R \setminus \set{a}$, and the limit along it is the usual limit $\lim_{t \to a} f(t)$.

If $X$ is [[Hausdorff|0S1FJ8VEX9]] and $\emptyset \notin \mathcal{F}$, then $f$ has at most one limit along $\mathcal{F}$.
