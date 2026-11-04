---
tag: 229GVWHHGG
kind: proof
name: Proof of the recurrence for Stirling numbers of the second kind
msc: [11B73]
proves: 0C019SDTER
uses: [0ZN07RQ3JS, 09CCE86A6D, 0EE2V3CHFK, 0GV2573FP4]
sources:
  - url: https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind
    locator: Recurrence relation
---

## Proof

We sort the partitions by the block of the last element.

1. Let $n$ and $k$ be natural numbers. Let $X = \set{1, \dots, n + 1}$, let $z = n + 1$, and let $Y = \set{1, \dots, n}$.
2. By the definition of the [[Stirling numbers of the second kind|0ZN07RQ3JS]], $S(n + 1, k + 1)$ is the number of [[partitions|09CCE86A6D]] of $X$ into $k + 1$ blocks.
3. Let $P$ be such a partition, and let $B$ be its block that contains $z$. Either $B = \set{z}$, or $B$ has another element.
4. Case $B = \set{z}$. Then $P \setminus \set{B}$ is a partition of $Y$ into $k$ blocks.
5. Conversely, if $Q$ is a partition of $Y$ into $k$ blocks, then $Q \cup \set{\set{z}}$ is a partition of $X$ into $k + 1$ blocks. One of its blocks is $\set{z}$.
6. These maps are inverse to each other. So by the [[bijection principle|0GV2573FP4]], this case has $S(n, k)$ partitions.
7. Case $B \ne \set{z}$. Then $B \setminus \set{z}$ is nonempty. Replacing $B$ by $B \setminus \set{z}$ gives a partition $P'$ of $Y$ into $k + 1$ blocks.
8. Map $P$ to the pair $(P', B \setminus \set{z})$. The second entry is a block of $P'$.
9. Conversely, let $Q$ be a partition of $Y$ into $k + 1$ blocks, and let $C \in Q$. Replace $C$ by $C \cup \set{z}$. This gives a partition of $X$ into $k + 1$ blocks. In it, the block of $z$ is not $\set{z}$.
10. These maps are inverse to each other. So this case is in bijection with the pairs $(Q, C)$, where $Q$ is a partition of $Y$ into $k + 1$ blocks and $C \in Q$.
11. Each such $Q$ has exactly $k + 1$ choices of $C$. By the [[rule of sum|0EE2V3CHFK]] over $Q$, there are $(k + 1)\, S(n, k + 1)$ such pairs.
12. The two cases are disjoint and cover all partitions of $X$ into $k + 1$ blocks. By the rule of sum,
$$S(n + 1, k + 1) = (k + 1)\, S(n, k + 1) + S(n, k).$$

## Idea

Remove the last element $z$ from its block. If $z$ was alone, one block disappears and $k$ blocks remain. If not, $k + 1$ blocks remain, and $z$ could have been in any one of them, which gives the factor $k + 1$.
