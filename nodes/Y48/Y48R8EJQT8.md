---
tag: Y48R8EJQT8
kind: statement
role: theorem
name: Kirchberger's theorem
msc: [52A35]
uses: [0XPR1E85W0, 0S52TNNTH9, F1W3QRBNGJ, 02AS45T3H9]
about: [02AS45T3H9]
sources:
  - url: https://en.wikipedia.org/wiki/Kirchberger%27s_theorem
same_as:
  wikidata: Q31838822
  wikipedia: Kirchberger's theorem
---

## Statement

Let $d \ge 1$ and let $P, Q \subseteq \R^d$ be finite sets.
Call $P' \subseteq P$ and $Q' \subseteq Q$ strictly separated if the following holds.
There are $a \in \R^d$ and $b \in \R$ with $a \cdot p < b$ for all $p \in P'$ and $a \cdot q > b$ for all $q \in Q'$, where $a \cdot x$ is the [[dot product|0S52TNNTH9]].
Suppose that for every set $T \subseteq P \cup Q$ with at most $d + 2$ points, the sets $T \cap P$ and $T \cap Q$ are strictly separated.
Then $P$ and $Q$ are strictly separated.

## Remarks

Proof idea: for each $p \in P$, the set of pairs $(a, b) \in \R^{d+1}$ with $a \cdot p < b$ is an open half-space, hence [[convex|02AS45T3H9]], and likewise for each $q \in Q$ with $a \cdot q > b$.
The hypothesis says that every $d + 2$ of these half-spaces in $\R^{d+1}$ have a common point.
By [[Helly's theorem|F1W3QRBNGJ]] in $\R^{d+1}$, all of them have a common point $(a, b)$, which separates $P$ from $Q$.

Example: take finite sets of red and blue points in the plane.
If every four of the points can be split by a line according to their colours, then so can all of them.

The number $d + 2$ cannot be lowered.
In the plane, take the red points $(0, 0)$, $(1, 1)$ and the blue points $(1, 0)$, $(0, 1)$.
No line separates them, since the two diagonals cross, while every three of the four points can be separated.

## Explanations

### L1 human

You have red and blue points and want a straight wall with all red points on one side and all blue points on the other.
Kirchberger's theorem says you only need to test small groups: in the plane, groups of four points.
If every small group can be split correctly, the whole set can.

### L2 human

The theorem is a Helly-type result for linear separability.
In machine learning it bounds the size of a certificate that two finite classes are not linearly separable: some $d + 2$ points already show it.
The proof shows a general pattern: a separation problem becomes a common-point problem for convex sets in a space of parameters, where Helly's theorem applies.
