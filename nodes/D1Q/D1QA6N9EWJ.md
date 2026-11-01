---
tag: D1QA6N9EWJ
kind: definition
name: Difference set
msc: [05B10]
defines: MG1KM4S1BV
uses: [G5S1M9, 0BJR9QR08E]
sources:
  - url: https://en.wikipedia.org/wiki/Difference_set
---

## Definition

Let $G$ be a finite [[group|G5S1M9]] of order $v$ with identity $e$, and let $k$ and $\lambda$ be positive integers.
A $(v, k, \lambda)$ difference set in $G$ is a [[subset|0BJR9QR08E]] $D \subseteq G$ with $k$ elements with the following property.
Each element $g \ne e$ of $G$ can be written as $g = d_1 d_2^{-1}$ with $d_1, d_2 \in D$ in exactly $\lambda$ ways.

## Remarks

When $G$ is abelian and written additively, the condition is about differences $d_1 - d_2$.
Counting the $k(k - 1)$ pairs $(d_1, d_2)$ with $d_1 \ne d_2$ gives $k(k-1) = \lambda (v - 1)$.
Example: $D = \set{1, 2, 4}$ in $\Z/7\Z$.
The six differences are $2 - 1 = 1$, $1 - 2 = 6$, $4 - 1 = 3$, $1 - 4 = 4$, $4 - 2 = 2$, $2 - 4 = 5$, so each nonzero residue occurs once, and $D$ is a $(7, 3, 1)$ difference set.
Non-example: $D = \set{0, 1, 2}$ in $\Z/7\Z$ is not a difference set, since $1 = 1 - 0 = 2 - 1$ occurs twice while $3$ does not occur.
If $D$ is a $(v, k, \lambda)$ difference set with $k < v$, the translates $Dg = \set{dg : d \in D}$ for $g \in G$ are the blocks of a symmetric $2$-$(v, k, \lambda)$ [[block design|TGZATGBHTH]].
