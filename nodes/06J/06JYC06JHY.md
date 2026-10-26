---
tag: 06JYC06JHY
kind: definition
name: Branch cut
aliases: [slit-plane]
msc: [30A99]
defines: 0W8QHVSN95
uses: [03CPD1HGF3, 0SQ1F2BEDS]
sources:
  - url: https://en.wikipedia.org/wiki/Branch_point
    locator: Branch cuts
  - url: https://en.wikipedia.org/wiki/Complex_logarithm
    locator: Branch cuts
---

## Definition

Let $U \subseteq \mathbb{C}$ be an open set and let $F$ be a [[multivalued function|03CPD1HGF3]] on $U$.
A branch cut for $F$ is a closed subset $K$ of $U$, usually a curve or a union of curves, such that $F$ has a continuous single-valued branch on the open set $U \setminus K$.
A branch on $U \setminus K$ is a continuous function $f$ on $U \setminus K$ with $f(z) \in F(z)$ for each $z \in U \setminus K$.
The standard branch cut for the logarithm on $\mathbb{C} \setminus \{0\}$ is the ray $(-\infty, 0)$. The open set $\mathbb{C} \setminus (-\infty, 0]$ is the slit plane.

## Remarks

A branch cut usually joins branch points. A branch point of $F$ is a point $z_0$ such that the values of $F$ do not come back to their start when $z$ goes once around a small circle with center $z_0$.
For $\log z$ and $\sqrt z$, the branch points are $0$ and $\infty$, so a cut is a curve from $0$ to $\infty$.
The [[principal branches|0YKY4M3KRQ]] of the logarithm and of the square root use the slit plane. Each other ray from $0$ is also a valid branch cut and gives other [[branches|0SQ1F2BEDS]].
The slit plane is $\{z \in \mathbb{C} : \operatorname{Re} z > 0 \text{ or } \operatorname{Im} z \neq 0\}$.

## Explanations

### L1 human

You cannot choose the logarithm continuously on a full circle around $0$.
A branch cut is a line that you remove from the plane so that no path can go around $0$. On what is left, a continuous choice is possible.
Crossing the cut makes the chosen value jump, for the logarithm by $2\pi i$.
