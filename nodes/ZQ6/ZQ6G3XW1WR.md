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

We check the three conditions of a subspace for the intersection, and for the union we argue by contradiction with one vector from each side.

1. (Part 1) Let $(U_i)_{i \in I}$ be a nonempty family of [[linear subspaces|0EPTJA5QV4]] of $V$, and let $X = \bigcap_{i \in I} U_i$ be the set of vectors that lie in every $U_i$. Since $I$ is nonempty, $X$ is contained in some $U_i$, so $X \subseteq V$.
2. Each $U_i$ contains $0$, because it is a subspace. So $0 \in X$.
3. Let $u, v \in X$. For each $i \in I$ we have $u, v \in U_i$, so $u + v \in U_i$ because $U_i$ is closed under addition. Hence $u + v \in X$.
4. Let $a \in F$ and $v \in X$. For each $i \in I$ we have $v \in U_i$, so $av \in U_i$ because $U_i$ is closed under scaling. Hence $av \in X$.
5. By steps 2 to 4, $X$ satisfies the three conditions of the definition, so $X$ is a subspace of $V$. This proves part 1.
6. (Part 2) Apply part 1 to the family $(U, W)$, indexed by a set with two elements. So $U \cap W$ is a subspace of $V$, and $U \cap W \subseteq U$ and $U \cap W \subseteq W$ by the definition of an intersection.
7. Let $Y$ be a subspace of $V$ with $Y \subseteq U$ and $Y \subseteq W$. Each $y \in Y$ lies in $U$ and in $W$, so $y \in U \cap W$. Thus $Y \subseteq U \cap W$, and $U \cap W$ is the largest such subspace. This proves part 2.
8. (Part 3, "if") If $U \subseteq W$, then $U \cup W = W$, which is a subspace. If $W \subseteq U$, then $U \cup W = U$, which is a subspace.
9. (Part 3, "only if") Assume that $U \cup W$ is a subspace, and, for a contradiction, that $U \not\subseteq W$ and $W \not\subseteq U$. Choose $u \in U$ with $u \notin W$, and $w \in W$ with $w \notin U$.
10. Both $u$ and $w$ lie in $U \cup W$, which is closed under addition by assumption, so $u + w \in U \cup W$. So $u + w \in U$ or $u + w \in W$.
11. If $u + w \in U$, then $w = (u + w) + (-1)u$ lies in $U$, because $U$ is closed under addition and scaling. This contradicts the choice of $w$.
12. If $u + w \in W$, then $u = (u + w) + (-1)w$ lies in $W$ for the same reason. This contradicts the choice of $u$.
13. Both cases give a contradiction, so $U \subseteq W$ or $W \subseteq U$. This proves part 3.

## Idea

Each subspace condition is a statement "if these vectors are inside, then this new vector is inside".
A vector that lies in every $U_i$ produces new vectors that lie in every $U_i$, so the conditions pass to the intersection.
For the union, take a vector that only $U$ has and a vector that only $W$ has.
Their sum cannot lie in $U$, since subtracting $u$ would put $w$ in $U$, and in the same way it cannot lie in $W$.

## Variants

Part 1 also follows from the [[subspace test|Z5XKYXTC0K]]: $X$ is nonempty because it contains $0$, and if $u, v \in X$ and $a \in F$, then $u + av$ lies in each $U_i$ and so in $X$.
Part 3 can be phrased without contradiction: if $u \in U \setminus W$, then for each $w \in W$ the vector $u + w$ lies in $U \cup W$ but not in $W$, so it lies in $U$, and then $w \in U$; this proves $W \subseteq U$.
