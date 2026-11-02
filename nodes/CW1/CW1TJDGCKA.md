---
tag: CW1TJDGCKA
kind: definition
name: Circumsphere
msc: [51M04, 51M20]
defines: MRC4WMVTAH
uses: [YX1DJK2QAG, P9CM4GQ2T0, 0FFAE5P6R4]
sources:
  - url: https://en.wikipedia.org/wiki/Circumscribed_sphere
---

## Definition

Let $n \ge 1$ and let $\Delta$ be an $n$-[[simplex|YX1DJK2QAG]] in $\R^N$ with vertices $v_0, \ldots, v_n$.
Let $S$ be the [[affine span|0FFAE5P6R4]] of the vertices.
There is exactly one point $o \in S$ with $\norm{o - v_0} = \norm{o - v_1} = \cdots = \norm{o - v_n}$.
This point is the *circumcentre* of $\Delta$, and this common distance $r$ is its *circumradius*.
The *circumsphere* of $\Delta$ is the [[sphere|P9CM4GQ2T0]] $\set{x \in S : \norm{x - o} = r}$ in $S$.

## Remarks

The point $o$ exists and is unique because the conditions $\norm{o - v_i}^2 = \norm{o - v_0}^2$ for $i = 1, \ldots, n$ are $n$ affine equations in $S$.
Their linear parts $v_i - v_0$ are linearly independent, by affine independence of the vertices.

Example: the triangle with vertices $(0, 0)$, $(2, 0)$ and $(0, 2)$ has circumcentre $(1, 1)$ and circumradius $\sqrt{2}$.
Each vertex is at distance $\sqrt{1 + 1} = \sqrt{2}$ from $(1, 1)$.
For $n = 2$ this is the [[circumcircle|03VZJE6C8C]].

Non-example: for four points $(0, 0)$, $(2, 0)$, $(0, 2)$ and $(3, 3)$ in the plane, there is no circle through all of them.
The only circle through the first three has centre $(1, 1)$, and $(3, 3)$ is at distance $2\sqrt{2}$ from it.
The definition needs the vertices of a simplex, which are affinely independent.

Without the condition $o \in S$, the centre would not be unique when $n < N$: every point of the affine subspace through $o$ orthogonal to $S$ is equidistant from the vertices.
