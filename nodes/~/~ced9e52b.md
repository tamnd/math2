---
tag: ~ced9e52b
kind: proof
name: Proof of the basic properties of the orthogonal complement
msc: [15A63, 46C05]
topics: [8GQVME4SZZ]
audience: ug1
proves: ~2c397fab
uses: [079D68S3AW, 0VGSYBWHV2, 0DTY8B9HMS, 0RMKABS2S5, 0EPTJA5QV4]
methods: [0NTF6DMVAP, MKHVRNW68H]
sources:
  - book: isbn:9783031410253
    locator: Section 6C
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Properties
---

## Proof

Let $V$ be an inner product space over $\mathbb{K} = \R$ or $\C$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$.
We use three axioms: linearity in the first argument, $\ip{y}{x} = \overline{\ip{x}{y}}$, and $\ip{x}{x} > 0$ for $x \ne 0$.

1. For $x, y \in V$, $\ip{x}{y} = 0$ if and only if $\ip{y}{x} = 0$. Reason: $\ip{y}{x} = \overline{\ip{x}{y}}$, and $\overline{z} = 0$ exactly when $z = 0$.
2. Part 1, zero vector: for every $s \in S$, $\ip{0}{s} = \ip{0 \cdot 0}{s} = 0 \cdot \ip{0}{s} = 0$ by linearity. So $0 \in S^\perp$.
3. Part 1, closure: let $x, y \in S^\perp$ and $a, b \in \mathbb{K}$. For each $s \in S$, linearity gives $\ip{ax + by}{s} = a \ip{x}{s} + b \ip{y}{s} = a \cdot 0 + b \cdot 0 = 0$.
4. By steps 2 and 3 and the [[subspace criterion|0EPTJA5QV4]], $S^\perp$ is a subspace of $V$. This proves part 1.
5. Part 2: let $S \subseteq T$ and $v \in T^\perp$. Each $s \in S$ lies in $T$, so $\ip{v}{s} = 0$. Hence $v \in S^\perp$, and $T^\perp \subseteq S^\perp$.
6. Part 3, first inclusion: $S \subseteq \operatorname{span} S$, so step 5 gives $(\operatorname{span} S)^\perp \subseteq S^\perp$.
7. Part 3, second inclusion: let $v \in S^\perp$ and $u \in \operatorname{span} S$. By the definition of the [[span|0DTY8B9HMS]], $u = a_1 s_1 + \dots + a_k s_k$ with $s_i \in S$ and $a_i \in \mathbb{K}$.
8. By steps 1 and 3 applied to the subspace $v^\perp$, which contains each $s_i$, the combination $u$ is in $v^\perp$. So $\ip{u}{v} = 0$, and step 1 gives $\ip{v}{u} = 0$.
9. Hence $v \in (\operatorname{span} S)^\perp$. With step 6, $S^\perp = (\operatorname{span} S)^\perp$. This proves part 3.
10. Part 4: $0 \in U$ because $U$ is a subspace, and $0 \in U^\perp$ by step 2. So $\set{0} \subseteq U \cap U^\perp$.
11. Let $x \in U \cap U^\perp$. Since $x \in U^\perp$ and $x \in U$, the definition gives $\ip{x}{x} = 0$. Positivity forces $x = 0$. This proves part 4.
12. Part 5, first inclusion: $U \subseteq U + W$ and $W \subseteq U + W$, since $u = u + 0$ and $w = 0 + w$. By step 5, $(U + W)^\perp \subseteq U^\perp$ and $(U + W)^\perp \subseteq W^\perp$.
13. So $(U + W)^\perp \subseteq U^\perp \cap W^\perp$.
14. Part 5, second inclusion: let $v \in U^\perp \cap W^\perp$, and let $x \in U + W$. By the definition of the [[sum|0RMKABS2S5]], $x = u + w$ with $u \in U$ and $w \in W$.
15. Conjugate symmetry and linearity in the first argument give additivity in the second argument: $\ip{v}{u + w} = \overline{\ip{u + w}{v}} = \overline{\ip{u}{v}} + \overline{\ip{w}{v}} = \ip{v}{u} + \ip{v}{w}$.
16. So $\ip{v}{x} = \ip{v}{u} + \ip{v}{w} = 0 + 0 = 0$. Hence $v \in (U + W)^\perp$.
17. Steps 13 and 16 give $(U + W)^\perp = U^\perp \cap W^\perp$. This proves part 5.
18. Part 6, first claim: every $v \in V$ satisfies $\ip{v}{0} = \overline{\ip{0}{v}} = 0$ by steps 1 and 2. So $\set{0}^\perp = V$.
19. Part 6, second claim: $V$ is a subspace with $V \cap V^\perp = V^\perp$. By part 4, $V^\perp = \set{0}$.

This proves all six parts.

## Idea

Each condition $\ip{v}{s} = 0$ is linear in $v$, so the set of solutions is a subspace.
Being orthogonal to a set is the same as being orthogonal to its span, because orthogonality survives linear combinations.
Positivity enters only once: a vector orthogonal to itself is zero.

## Variants

In $\R^n$ with the dot product, part 1 has a matrix proof: if the rows of a matrix $A$ are the vectors of a finite set $S$, then $S^\perp$ is the null space of $A$, and null spaces are subspaces.
Part 5 also follows from the rules for [[annihilators|0ASHNYF7AG]], through the map $v \mapsto \ip{\cdot}{v}$ from $V$ to the dual space.
