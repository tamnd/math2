---
tag: MGCAASHMC9
kind: proof
name: Proof that connected subsets of the real line are intervals
msc: [54D05]
proves: 0B9ZQFMQNV
uses: [0R37DFJKFW, 0D939CMME7, 0D5YHQGDJY, 0TK8Y3J5RW, 0A26X79RTB, 0AXWET80YW, 0BTMQ04556, 0M8TGGP9JP]
sources:
  - url: https://en.wikipedia.org/wiki/Connected_space
    locator: Examples
---

## Proof

We prove the two directions separately. The second uses the supremum.

1. Recall that $S$ is [[connected|0R37DFJKFW]] when $S$ with the [[subspace topology|0D5YHQGDJY]] is a [[connected space|0D939CMME7]]. A set is open in $S$ exactly when it is $S \cap U$ for some open $U \subseteq \mathbb{R}$.
2. First, let $S$ be connected. Suppose that $S$ is not an [[interval|0TK8Y3J5RW]]. Then there are $a, b \in S$ and $c \notin S$ with $a < c < b$.
3. The sets $(-\infty, c)$ and $(c, \infty)$ are open in $\mathbb{R}$. Each point $x$ of either set has the ball of radius $|x - c|$ around it inside the set, so [[the ball criterion|0A26X79RTB]] applies.
4. Let $U' = S \cap (-\infty, c)$ and $V' = S \cap (c, \infty)$. They are open in $S$, disjoint, and nonempty, since $a \in U'$ and $b \in V'$.
5. Since $c \notin S$, we get $U' \cup V' = S$. So $S$ is not connected, a contradiction. Thus $S$ is an interval.
6. Now let $S$ be an interval. Suppose that $S$ is not connected. Then there are open $U, V \subseteq \mathbb{R}$ with $U' = S \cap U$ and $V' = S \cap V$ nonempty, disjoint, and with union $S$.
7. Choose $a \in U'$ and $b \in V'$. They differ, as $U' \cap V' = \varnothing$. By swapping the names of $U$ and $V$ if needed, we may assume $a < b$.
8. As $S$ is an interval, $[a, b] \subseteq S$. So each point of $[a, b]$ lies in exactly one of $U$ and $V$.
9. Let $T = U \cap [a, b]$. It contains $a$ and is bounded above by $b$. By the [[completeness axiom|0AXWET80YW]], it has a [[supremum|0BTMQ04556]] $c$, with $a \le c \le b$. So $c \in S$.
10. Case $c \in U$. Then $c \neq b$, since $b \in V$. As $U$ is open, there is $\varepsilon > 0$ with $(c - \varepsilon, c + \varepsilon) \subseteq U$, and we may take $\varepsilon \le b - c$.
11. Then $c + \varepsilon / 2$ lies in $[a, b]$ and in $U$, so it lies in $T$. It is larger than $c = \sup T$, a contradiction.
12. Case $c \in V$. Then $c \neq a$, since $a \in U$. As $V$ is open, there is $\varepsilon > 0$ with $(c - \varepsilon, c + \varepsilon) \subseteq V$, and we may take $\varepsilon \le c - a$.
13. By the [[approximation property of the supremum|0M8TGGP9JP]], there is $t \in T$ with $c - \varepsilon < t \le c$. Then $t \in U$ and $t \in V$, and $t \in [a, b] \subseteq S$.
14. So $t \in U' \cap V'$, which contradicts $U' \cap V' = \varnothing$.
15. Since $c \in S = U' \cup V'$, one of the two cases holds, and both are impossible. So $S$ is connected.

## Idea

A gap point $c$ outside $S$ cuts $S$ into a left part and a right part, so a connected set has no gaps. Conversely, if an interval were split into two open pieces, the supremum of the points of the first piece below a point of the second would sit on the border. Openness then shows that this border point can belong to neither piece.
