---
tag: 0B9ZQFMQNV
kind: statement
role: theorem
name: Connected subsets of the real line are intervals
msc: [54D05]
uses: [0R37DFJKFW, 0TK8Y3J5RW, 0BTMQ04556, 0AXWET80YW]
sources:
  - url: https://en.wikipedia.org/wiki/Connected_space
    locator: Examples
---

## Statement

Let $S \subseteq \mathbb{R}$, where $\mathbb{R}$ has the usual topology.
Then $S$ is [[connected|0R37DFJKFW]] if and only if $S$ is an [[interval|0TK8Y3J5RW]], that is, for all $a, b \in S$ and all $c \in \mathbb{R}$ with $a < c < b$, $c \in S$.

## Remarks

If $S$ is not an interval, take $a < c < b$ with $a, b \in S$ and $c \notin S$. Then $(-\infty, c)$ and $(c, \infty)$ split $S$.
The proof that an interval $I$ is connected uses the [[completeness axiom|0AXWET80YW]]. If open sets $U$ and $V$ split $I$, with $a \in U$, $b \in V$ and $a < b$, let $c$ be the [[supremum|0BTMQ04556]] of the points of $U \cap [a, b]$. Then $c$ lies in neither $U$ nor $V$.
Under this definition the empty set and single points are intervals, and they are connected.
The statement fails for $\mathbb{Q}$: no interval of $\mathbb{Q}$ with more than one point is connected.

## Explanations

### L1 human

On the real line, the sets in one piece are exactly the intervals.
The proof needs the completeness of $\mathbb{R}$, because $\mathbb{Q}$ has gaps where it can be split.
