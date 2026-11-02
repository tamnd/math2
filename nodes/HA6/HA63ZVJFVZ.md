---
tag: HA63ZVJFVZ
kind: definition
name: Monge point
msc: [51M04, 51M20]
defines: NW57FTPF3E
uses: [YX1DJK2QAG, MRC4WMVTAH, 0Y5RHNRKJZ]
sources:
  - url: https://en.wikipedia.org/wiki/Tetrahedron
---

## Definition

Let $n \ge 2$ and let $\Delta$ be an $n$-[[simplex|YX1DJK2QAG]] in $\R^N$ with vertices $v_0, \ldots, v_n$.
Let $o$ be its circumcentre, the centre of its [[circumsphere|MRC4WMVTAH]].
Let $g = \frac{1}{n+1}(v_0 + \cdots + v_n)$ be its [[centroid|0Y5RHNRKJZ]].
The *Monge point* of $\Delta$ is
$$m = o + \frac{n + 1}{n - 1} \, (g - o).$$

## Remarks

For a tetrahedron, $n = 3$ and $m = 2g - o$, the reflection of $o$ in $g$.
In that case $m$ is the common point of the six planes through the midpoint of an edge perpendicular to the opposite edge.

For a triangle, $n = 2$ and $m = 3g - 2o$, which is the [[orthocentre|0WB619CA0V]].
Example: the triangle with vertices $(0, 0)$, $(2, 0)$ and $(0, 2)$ has $o = (1, 1)$ and $g = (\frac{2}{3}, \frac{2}{3})$.
Then $m = (1, 1) + 3 \cdot (-\frac{1}{3}, -\frac{1}{3}) = (0, 0)$, the vertex of the right angle, which is indeed the orthocentre.

Non-example: for a segment, $n = 1$, the factor $\frac{n+1}{n-1}$ is undefined, so a $1$-simplex has no Monge point.

For a regular tetrahedron, $g = o$, so the Monge point is the centre.
