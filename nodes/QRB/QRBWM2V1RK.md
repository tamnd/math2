---
tag: QRBWM2V1RK
kind: proof
name: Proof of the uniqueness of the supremum
msc: [06A06]
proves: 04ETX30HT2
uses: [0BTMQ04556, 0B5H2V4JW8, 011C29Q1S1]
sources:
  - url: https://proofwiki.org/wiki/Supremum_is_Unique
---

## Proof

1. Let $(P, \le)$ be a partially ordered set, let $S \subseteq P$, and let $b$ and $b'$ be [[suprema|0BTMQ04556]] of $S$.
2. By the first condition of the definition, $b$ is an [[upper bound|0B5H2V4JW8]] of $S$.
3. By the second condition for $b'$, applied to the upper bound $b$, we get $b' \le b$.
4. In the same way, $b'$ is an upper bound of $S$ and $b$ is a supremum, so $b \le b'$.
5. The relation $\le$ is a [[partial order|011C29Q1S1]], so it is antisymmetric. From $b' \le b$ and $b \le b'$ we get $b = b'$.

## Idea

Each supremum is an upper bound, and each supremum lies below every upper bound. So two suprema lie below each other, and antisymmetry makes them equal.
