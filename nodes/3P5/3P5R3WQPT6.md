---
tag: 3P5R3WQPT6
kind: definition
name: Perspective projection
msc: [51N05, 51N15, 68U05]
defines: YHKSDF59HK
uses: [0XPR1E85W0, 0V3XAMF3C1, 0MP9BCF6DP, FS9FRJ17D2]
sources:
  - url: https://en.wikipedia.org/wiki/Perspective_(graphical)
---

## Definition

Let $E$ be Euclidean 3-space, let $O \in E$ be a point, the centre, and let $\pi$ be a [[plane|0V3XAMF3C1]] not containing $O$, the picture plane.
Let $P \ne O$ be a point such that the [[line|0MP9BCF6DP]] $OP$ is not parallel to $\pi$.
The *perspective projection* from $O$ onto $\pi$ sends $P$ to the point where $OP$ meets $\pi$.
In coordinates with $O = (0, 0, 0)$ and $\pi = \set{z = f}$ for some $f > 0$, it is
$$(x, y, z) \mapsto \left( \frac{f x}{z}, \frac{f y}{z} \right), \qquad z \ne 0.$$

## Remarks

Example: the two rails $(1, -1, t)$ and $(-1, -1, t)$, $t > 0$, are parallel lines in the direction $(0, 0, 1)$.
Their images $(f/t, -f/t)$ and $(-f/t, -f/t)$ lie on the lines $y = -x$ and $y = x$, which meet at $(0, 0)$, and both images tend to $(0, 0)$ as $t \to \infty$.
So $(0, 0)$ is the vanishing point of the direction $(0, 0, 1)$; in general the vanishing point of a direction $v$ with $v_3 \ne 0$ is the image of $v$ itself, $(f v_1 / v_3, f v_2 / v_3)$.
Non-example: the orthographic projection $(x, y, z) \mapsto (x, y)$ is not a perspective projection, since its projecting lines are parallel and do not pass through one centre.
It maps parallel lines to parallel lines.
The points of a line not through $O$ that lie in the domain map to points of one line, and lines parallel to $\pi$ keep their direction.
In [[homogeneous coordinates|FS9FRJ17D2]] the map is linear: $[x : y : z : 1] \mapsto [f x : f y : z]$, which is how graphics systems implement it.
