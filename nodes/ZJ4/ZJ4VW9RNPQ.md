---
tag: ZJ4VW9RNPQ
kind: proof
name: Proof that the Cantor set is closed
msc: [54F65]
proves: 01VT24J1SD
uses: [0BXNDZFQME, 0G5AV9Q4RR, 0A26X79RTB, 09NDE9V7X1, 09YMV8H4X5]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor_set
    locator: Topological and analytical properties
---

## Proof

We show that each stage $C_n$ is closed, and then intersect.

1. In the construction of the [[Cantor set|0BXNDZFQME]], $C_0 = [0, 1]$ is one closed interval. Removing the open middle third of a closed interval $[a, b]$ leaves the two closed intervals $[a, a + \tfrac{b-a}{3}]$ and $[b - \tfrac{b-a}{3}, b]$.
2. So, by induction on $n$, each $C_n$ is a union of $2^n$ closed intervals.
3. A closed interval $[a, b]$ is [[closed|0G5AV9Q4RR]] in $\mathbb{R}$. Its complement is $(-\infty, a) \cup (b, \infty)$. Each point $x$ of it has the ball of radius $\min(|x - a|, |x - b|)$ inside the complement, so the complement is open by [[the ball criterion|0A26X79RTB]].
4. A finite union $F_1 \cup \cdots \cup F_k$ of closed sets is closed. Its complement is $(\mathbb{R} \setminus F_1) \cap \cdots \cap (\mathbb{R} \setminus F_k)$, which is open by [[finite intersection of open sets is open|09NDE9V7X1]].
5. By steps 2 to 4, each $C_n$ is closed in $\mathbb{R}$.
6. By [[intersection of closed sets is closed|09YMV8H4X5]], with the nonempty index set $\{0, 1, 2, \ldots\}$, the set $C = \bigcap_{n \ge 0} C_n$ is closed in $\mathbb{R}$.

## Idea

Each stage of the construction is a finite union of closed intervals, so it is closed. Closed sets stay closed under arbitrary intersections, and the Cantor set is the intersection of all stages.
