---
tag: ZQ6G3XW1WR
kind: proof
name: Proof that an intersection of subspaces is a subspace
msc: [15A03]
proves: 0V33SPH7RR
uses: [0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_subspace
    locator: Operations and relations on subspaces
---

## Proof

We first prove the general claim, and then deduce the claims about $U \cap W$.

1. Let $(U_i)_{i \in I}$ be a nonempty family of [[linear subspaces|0EPTJA5QV4]] of $V$. Let $X = \bigcap_{i \in I} U_i$ be the set of vectors that lie in every $U_i$.
2. Each $U_i$ is a subset of $V$, and $I$ is nonempty. So $X$ is a subset of $V$.
3. Each $U_i$ contains $0$, because it is a subspace. So $0 \in X$.
4. Let $u, v \in X$. For each $i \in I$, we have $u, v \in U_i$, so $u + v \in U_i$. Hence $u + v \in X$.
5. Let $a \in F$ and $v \in X$. For each $i \in I$, we have $v \in U_i$, so $av \in U_i$. Hence $av \in X$.
6. By steps 2 to 5, $X$ is a linear subspace of $V$. This proves the general claim.
7. Apply step 6 to the family $(U, W)$, indexed by a set with two elements. So $U \cap W$ is a linear subspace of $V$.
8. By definition, $U \cap W \subseteq U$ and $U \cap W \subseteq W$.
9. Let $Y$ be a subspace of $V$ with $Y \subseteq U$ and $Y \subseteq W$. Each $y \in Y$ lies in $U$ and in $W$, so $y \in U \cap W$. Thus $Y \subseteq U \cap W$.
10. By steps 7 to 9, $U \cap W$ is a subspace contained in $U$ and $W$, and it contains every such subspace. So it is the largest such subspace.

## Idea

The three conditions for a subspace hold in each $U_i$. A vector that lies in all of them therefore satisfies the conditions in all of them at once. The intersection is the largest common subspace because any common subspace already sits inside it.
