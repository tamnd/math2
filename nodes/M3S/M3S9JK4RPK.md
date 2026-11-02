---
tag: M3S9JK4RPK
kind: definition
name: Convex join
msc: [52A05]
defines: 1A83RGDDNE
uses: [000AYPA9AJ, VQ4Q2V45RP, 02AS45T3H9, 0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_hull
---

## Definition

Let $V$ be a real [[vector space|000AYPA9AJ]] and let $A, B \subseteq V$.
The *convex join* of $A$ and $B$ is the set
$$\operatorname{join}(A, B) = \bigcup_{a \in A,\ b \in B} [a, b],$$
where $[a, b]$ is the [[line segment|VQ4Q2V45RP]] from $a$ to $b$.

## Remarks

Example: in $\R^2$, let $A = \set{(0, 0)}$ and $B = [(1, 0), (1, 1)]$.
The join is the union of the segments from the origin to the points $(1, s)$ with $0 \le s \le 1$, which is the closed triangle with vertices $(0,0)$, $(1,0)$ and $(1,1)$.

If $A$ and $B$ are nonempty [[convex sets|02AS45T3H9]], then $\operatorname{join}(A, B)$ equals the [[convex hull|0FQSDC2EQ2]] of $A \cup B$.
Indeed, a convex combination of points of $A \cup B$ can be regrouped as $(1 - t) a + t b$ with $a \in A$ and $b \in B$.

Non-example of that identity: if $A = \emptyset$ and $B = \set{b}$, then $\operatorname{join}(A, B) = \emptyset$, while the convex hull of $A \cup B$ is $\set{b}$.
So the nonemptiness hypothesis cannot be dropped.
