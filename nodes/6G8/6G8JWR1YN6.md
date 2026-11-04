---
tag: 6G8JWR1YN6
kind: proof
name: Proof of the intermediate value theorem for connected spaces
msc: [54D05]
proves: 098C0KZZAP
uses: [0D939CMME7, 0R37DFJKFW, 0D5YHQGDJY, 0SY9ECQ19Q, 0EPD87YVG8, 0B9ZQFMQNV]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: General metric and topological spaces
---

## Proof

We combine the two facts that images of connected sets are connected and that connected subsets of $\mathbb{R}$ are intervals.

1. The subspace topology on $X$ as a subset of itself is the topology of $X$. So $X$ is a [[connected subset|0R37DFJKFW]] of $X$, because $X$ is a [[connected space|0D939CMME7]].
2. The map $f$ is [[continuous|0SY9ECQ19Q]]. By [[continuous image of a connected set is connected|0EPD87YVG8]], the set $f(X) \subseteq \mathbb{R}$ is connected.
3. By [[connected subsets of the real line are intervals|0B9ZQFMQNV]], $f(X)$ is an interval. So for $p, q \in f(X)$ and $p < c < q$, we have $c \in f(X)$.
4. Let $c$ be between $f(a)$ and $f(b)$. If $c = f(a)$, take $x = a$. If $c = f(b)$, take $x = b$.
5. Otherwise $c$ lies strictly between the two values. Let $p$ be the smaller and $q$ the larger of $f(a)$ and $f(b)$. Then $p, q \in f(X)$ and $p < c < q$.
6. By step 3, $c \in f(X)$. So there is $x \in X$ with $f(x) = c$.

## Idea

The image of a connected space under a continuous map is connected. In $\mathbb{R}$ the connected sets are the intervals, and an interval that contains $f(a)$ and $f(b)$ contains each value between them.
