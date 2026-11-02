---
tag: BWEGTCW5RJ
kind: statement
role: theorem
name: Centerpoint theorem
msc: [52A35, 52C35]
uses: [02AS45T3H9, 0FQSDC2EQ2, F1W3QRBNGJ]
about: [0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Centerpoint_(geometry)
---

## Statement

Let $d \ge 1$ and let $X$ be a finite set of $n$ points in $\R^d$.
Then there is a point $c \in \R^d$ such that every closed half-space of $\R^d$ that contains $c$ contains at least $\dfrac{n}{d+1}$ points of $X$.
Such a point $c$ is called a *centerpoint* of $X$.

## Remarks

Consider all closed half-spaces that contain more than $\frac{d}{d+1} n$ points of $X$, and the [[convex hulls|0FQSDC2EQ2]] of the points of $X$ in each of them.
Each such half-space misses fewer than $\frac{n}{d+1}$ points of $X$, so $d + 1$ of them together miss fewer than $n$ points, and some point of $X$ lies in all $d + 1$ hulls.
By [[Helly's theorem|F1W3QRBNGJ]] all these hulls have a common point $c$.
Suppose a closed half-space containing $c$ had fewer than $\frac{n}{d+1}$ points.
Its open complement would contain more than $\frac{d}{d+1} n$ points, and a slightly smaller closed half-space inside it would give a hull that misses $c$, a contradiction.
In dimension $1$ a median of $X$ is a centerpoint, with the bound $n/2$.
The bound $n/(d+1)$ cannot be improved in general.
Take $d + 1$ equal small clusters of points near the vertices of a simplex: for any point $c$, some closed half-space through $c$ meets only one cluster.

## Explanations

### L1 human

A centerpoint is a point that sits "deep" inside a cloud of points.
However one cuts space in two halves by a flat wall through it, each half keeps a fair share of the points.
In the plane that fair share is at least one third of the points.
On a line it is the median, which has half the points on each side.

### L2 human

The centerpoint theorem is a standard consequence of [[Helly's theorem|F1W3QRBNGJ]].
It generalizes the median to higher dimensions and gives a notion of depth for data.
It is used in divide-and-conquer algorithms and in the proof of separator theorems for planar graphs and meshes.
The [[ham sandwich theorem|GDXX60SNG5]] is a different statement about dividing point sets by hyperplanes.
