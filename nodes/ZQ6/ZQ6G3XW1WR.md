---
tag: ZQ6G3XW1WR
kind: proof
name: Proof of the intersection and union properties of subspaces
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: 0V33SPH7RR
methods: [0NTF6DMVAP, 0J0XBKG64S, 0WCP0PVET6]
uses: [0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_subspace
    locator: Operations and relations on subspaces
  - book: isbn:9783031410253
    locator: Section 1C
---

## Proof

We prove the three parts in order.

1. (Part 1) Let $(U_i)_{i \in I}$ be a nonempty family of [[linear subspaces|0EPTJA5QV4]] of $V$. Let $X = \bigcap_{i \in I} U_i$ be the set of vectors that lie in every $U_i$.
2. Each $U_i$ is a subset of $V$, and $I$ is nonempty. So $X$ is a subset of $V$.
3. Each $U_i$ contains $0$, because it is a subspace. So $0 \in X$.
4. Let $u, v \in X$. For each $i \in I$, we have $u, v \in U_i$, so $u + v \in U_i$. Hence $u + v \in X$.
5. Let $a \in F$ and $v \in X$. For each $i \in I$, we have $v \in U_i$, so $av \in U_i$. Hence $av \in X$.
6. By steps 2 to 5, $X$ is a linear subspace of $V$. This proves part 1.
7. (Part 2) Apply step 6 to the family $(U, W)$, indexed by a set with two elements. So $U \cap W$ is a linear subspace of $V$.
8. By definition, $U \cap W \subseteq U$ and $U \cap W \subseteq W$.
9. Let $Y$ be a subspace of $V$ with $Y \subseteq U$ and $Y \subseteq W$. Each $y \in Y$ lies in $U$ and in $W$, so $y \in U \cap W$. Thus $Y \subseteq U \cap W$.
10. By steps 7 to 9, $U \cap W$ is the largest subspace contained in $U$ and $W$. This proves part 2.
11. (Part 3, "if") If $U \subseteq W$, then $U \cup W = W$, which is a subspace. If $W \subseteq U$, then $U \cup W = U$.
12. (Part 3, "only if") Assume that $U \cup W$ is a subspace, and, for a contradiction, that $U \not\subseteq W$ and $W \not\subseteq U$.
13. Choose $u \in U$ with $u \notin W$, and $w \in W$ with $w \notin U$.
14. Both $u$ and $w$ lie in $U \cup W$, so $u + w \in U \cup W$, by condition 2 for this subspace.
15. Case $u + w \in U$: then $w = (u + w) + (-1)u$ lies in $U$, because $U$ is a subspace. This contradicts the choice of $w$.
16. Case $u + w \in W$: then $u = (u + w) + (-1)w$ lies in $W$. This contradicts the choice of $u$.
17. Both cases give a contradiction, so $U \subseteq W$ or $W \subseteq U$. This proves part 3.

## Idea

The three subspace conditions hold in each $U_i$, so they hold for the vectors that lie in all of them.
For the union, one vector from each side gives a sum that cannot lie on either side.
