---
tag: D186VNHFZJ
kind: definition
name: Newton polygon
msc: [12J25, 11S05]
defines: H7QNCE2QZJ
uses: [SVY882HKSJ, 0TCHAS04WK]
sources:
  - url: https://en.wikipedia.org/wiki/Newton_polygon
---

## Definition

Let $K$ be a field with a [[valuation|SVY882HKSJ]] $v \colon K \to \R \cup \set{\infty}$.
Let $f = a_0 + a_1 X + \cdots + a_n X^n \in K[X]$ with $n \ge 1$ and $a_0 a_n \ne 0$.
Let $S = \set{(i, v(a_i)) : 0 \le i \le n,\ a_i \ne 0} \subseteq \R^2$.
The *Newton polygon* of $f$ is the lower boundary of the [[convex hull|0TCHAS04WK]] of $S$.
It is the graph of the largest convex function $\varphi \colon [0, n] \to \R$ with $\varphi(i) \le v(a_i)$ for every $(i, v(a_i)) \in S$.

It is a broken line from $(0, v(a_0))$ to $(n, v(a_n))$ whose vertices lie in $S$ and whose slopes increase from left to right.

## Remarks

Main property: let $L$ be a splitting field of $f$ over $K$ and $w$ an extension of $v$ to $L$.
If the Newton polygon has a segment of slope $s$ and horizontal length $\ell$, then exactly $\ell$ roots of $f$ in $L$ have $w$-value $-s$, counted with multiplicity.
Example: over $\Q_p$, take $f = X^2 + X + p$.
The points are $(0, 1)$, $(1, 0)$, $(2, 0)$, and the lower boundary has a segment of slope $-1$ from $(0, 1)$ to $(1, 0)$ and a segment of slope $0$ from $(1, 0)$ to $(2, 0)$.
So one root has valuation $1$ and one has valuation $0$; this agrees with the product of the roots being $p$ and their sum being $-1$.
Non-example: for $f = 1 + pX + X^2$ the points are $(0, 0)$, $(1, 1)$, $(2, 0)$.
The broken line through all three points is not the Newton polygon, because it is not the graph of a convex function.
The point $(1, 1)$ lies above the segment from $(0, 0)$ to $(2, 0)$, and this segment is the whole Newton polygon.
So both roots have valuation $0$.
