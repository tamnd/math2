---
tag: WKK2DC7JE9
kind: definition
name: Chattering control
msc: [49J15, 49K15, 93C15]
defines: 6K8Q2YERTF
uses: [8M31QKB0GW, GK1Z3Q1WRZ]
sources:
  - url: https://en.wikipedia.org/wiki/Bang–bang_control
---

## Definition

Let $U \subseteq \R^m$ be a nonempty set, let $a < b$, and let $u \colon [a, b] \to U$ be a measurable control.
A *switching time* of $u$ is a point $s \in [a, b]$ with this property.
On no neighbourhood of $s$ in $[a, b]$ is $u$ almost everywhere equal to a constant.
The control $u$ is *chattering* if its set of switching times is infinite but has only finitely many accumulation points.

## Remarks

The set of switching times is closed, and on each interval between consecutive switching times the control is almost everywhere constant.
Since $[a, b]$ is compact, the switching times of a chattering control have an accumulation point.
The condition on accumulation points excludes, for example, continuous nonconstant controls such as $u(t) = t$, for which every point is a switching time.
Example: on $[0, 1]$ let $u(t) = (-1)^k$ for $1 - 2^{-k} \le t < 1 - 2^{-k-1}$, $k = 0, 1, 2, \ldots$, and $u(1) = 1$.
Each point $1 - 2^{-k}$ with $k \ge 1$ is a switching time, since $u$ takes the value $1$ on one side and $-1$ on the other.
So $u$ is a chattering [[bang–bang control|GK1Z3Q1WRZ]], and its switching times accumulate at $1$.
Non-example: $u(t) = -1$ for $t < 1/2$ and $u(t) = 1$ for $t \ge 1/2$ has only one switching time, $1/2$.
Some authors also use the word for a sequence of fast-switching ordinary controls that approximates a relaxed control.
