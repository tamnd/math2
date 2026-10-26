---
tag: 0MXN7AFBPE
kind: statement
role: theorem
name: Open connected subsets of R^n are path-connected
msc: [54D05]
uses: [0R37DFJKFW, 0K0GE6BCYW, 0DC3MPR7C9]
sources:
  - url: https://en.wikipedia.org/wiki/Connected_space
    locator: Path connectedness
---

## Statement

Let $n \ge 1$ and let $U \subseteq \mathbb{R}^n$ be open and [[connected|0R37DFJKFW]], for the Euclidean topology.
Then $U$ is [[path-connected|0K0GE6BCYW]] or empty.

## Remarks

Proof: fix $x \in U$, and let $P$ be the set of points of $U$ that a path in $U$ joins to $x$. Each [[open ball|0DC3MPR7C9]] in $U$ is convex, so $P$ and $U \setminus P$ are both open. As $U$ is connected and $x \in P$, we get $P = U$.
The proof works in each locally path-connected space, for example in each open subset of a normed space.
In fact, any two points of $U$ can be joined by a path made of finitely many line segments.

## Explanations

### L1 human

For open sets in $\mathbb{R}^n$, being in one piece and being walkable are the same.
The bad behaviour of the topologist's sine curve cannot happen in an open set, because each point has a small ball around it.
