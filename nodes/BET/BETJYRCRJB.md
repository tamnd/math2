---
tag: BETJYRCRJB
kind: definition
name: Vertex of a polytope
msc: [52B05, 52B11]
defines: R7V3S9V891
uses: [300K6CB1KH, KY7SB854VH, 3MSGFJM2NX, 0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Vertex_(geometry)
---

## Definition

Let $P \subset \R^d$ be a [[convex polytope|300K6CB1KH]].
A *vertex* of $P$ is a [[face|KY7SB854VH]] of $P$ of dimension $0$, identified with the single point it contains.
Equivalently, a point $v \in P$ is a vertex if there is a vector $c \in \R^d$ such that $c \cdot v > c \cdot x$ for every $x \in P$ with $x \ne v$.

## Remarks

Example: in the square $P = [0,1]^2$, the point $v = (1,1)$ is a vertex.
Take $c = (1,1)$: then $c \cdot v = 2$, and $c \cdot x = x_1 + x_2 < 2$ for every other point $x$ of $P$.

Non-example: the point $(1, \tfrac12)$ of the same square is not a vertex.
For any $c$, the points $(1, \tfrac12 \pm t)$ for small $t > 0$ lie in $P$, and $c \cdot x$ is at least $c \cdot (1,\tfrac12)$ at one of them, so no $c$ singles it out.

The vertices of $P$ are exactly its [[extreme points|3MSGFJM2NX]].
If $V$ is the set of vertices, then $P$ is the [[convex hull|0FQSDC2EQ2]] of $V$, and every finite set whose convex hull is $P$ contains $V$.
