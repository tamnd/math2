---
tag: 2WFSYYVW5H
kind: proof
name: Proof of the approximation property of the supremum
msc: [26A03]
proves: 0M8TGGP9JP
uses: [0BTMQ04556, 0B5H2V4JW8, 0QSPNASE50]
methods: [0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Infimum_and_supremum
    locator: Identifying infima and suprema
---

## Proof

We argue by contradiction.

1. Let $S$ be a nonempty set of reals that is bounded above, let $b = \sup S$ be its [[supremum|0BTMQ04556]], and let $c < b$.
2. Suppose that no $s \in S$ satisfies $c < s \le b$.
3. Let $s \in S$. Since $b$ is an [[upper bound|0B5H2V4JW8]] of $S$, $s \le b$. By step 2, $c < s$ fails.
4. The order of $\R$ is total, by the [[ordered field property|0QSPNASE50]]. So $s \le c$.
5. Thus $c$ is an upper bound of $S$. Since $b$ is the least upper bound, $b \le c$.
6. This contradicts $c < b$. So some $s \in S$ satisfies $c < s \le b$.

## Idea

A number below the supremum cannot be an upper bound, because the supremum is the least one. So some element of the set lies above it.
