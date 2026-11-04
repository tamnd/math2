---
tag: KQ6VX2WPHC
kind: proof
name: Proof that path-connected spaces are connected
msc: [54D05]
proves: 0ZMT1GP4KM
uses: [0K0GE6BCYW, 0D939CMME7, 0R37DFJKFW, 0D5YHQGDJY, 0TK8Y3J5RW, 0B9ZQFMQNV, 0EPD87YVG8]
sources:
  - url: https://en.wikipedia.org/wiki/Connected_space
    locator: Path connectedness
---

## Proof

We argue by contradiction, and restrict a splitting of $X$ to the image of a path.

1. Suppose that $X$ is not [[connected|0D939CMME7]]. Then there are open $U, V \subseteq X$, both nonempty and disjoint, with $U \cup V = X$.
2. Choose $x \in U$ and $y \in V$. Since $X$ is [[path-connected|0K0GE6BCYW]], there is a continuous $\gamma \colon [0, 1] \to X$ with $\gamma(0) = x$ and $\gamma(1) = y$.
3. The set $[0, 1]$ is an [[interval|0TK8Y3J5RW]], so it is a [[connected subset|0R37DFJKFW]] of $\mathbb{R}$, by [[connected subsets of the real line are intervals|0B9ZQFMQNV]]. So $[0, 1]$ with its [[subspace topology|0D5YHQGDJY]] is a connected space.
4. By [[continuous image of a connected set is connected|0EPD87YVG8]], applied to $\gamma$ on the space $[0, 1]$, the set $K = \gamma([0, 1])$ is connected.
5. The sets $K \cap U$ and $K \cap V$ are open in $K$. They are disjoint, because $U \cap V = \varnothing$, and their union is $K$, because $U \cup V = X$.
6. They are nonempty, because $x = \gamma(0) \in K \cap U$ and $y = \gamma(1) \in K \cap V$.
7. So $K$ is not connected, which contradicts step 4. Thus $X$ is connected.

## Idea

A path is a continuous image of the connected interval $[0, 1]$, so its image is connected. If $X$ split into two open pieces, the path from a point of one piece to a point of the other would split too.
