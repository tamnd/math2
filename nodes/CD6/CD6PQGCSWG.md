---
tag: CD6PQGCSWG
kind: proof
name: Proof of the basic properties of the orthogonal complement
msc: [15A63, 46C05]
topics: [8GQVME4SZZ]
audience: ug1
proves: T5Q51M5BAK
uses: [079D68S3AW, 0VGSYBWHV2, 0DTY8B9HMS, 0RMKABS2S5, 0EPTJA5QV4]
methods: [0NTF6DMVAP, MKHVRNW68H]
sources:
  - book: isbn:9783031410253
    locator: Section 6C
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Properties
---

## Proof

We check each part from the axioms of an [[inner product|0VGSYBWHV2]], and we prove each equality of sets by two inclusions.
Let $V$ be an inner product space over $\mathbb{K} = \R$ or $\C$.
We use linearity in the first argument, conjugate symmetry $\ip{y}{x} = \overline{\ip{x}{y}}$, and positivity $\ip{x}{x} > 0$ for $x \ne 0$.

1. Orthogonality is symmetric: $\ip{x}{y} = 0$ if and only if $\ip{y}{x} = 0$. The reason is that $\ip{y}{x} = \overline{\ip{x}{y}}$, and a complex number is $0$ exactly when its conjugate is $0$.
2. The inner product is additive and conjugate-linear in the second argument. By conjugate symmetry and linearity in the first argument, $\ip{v}{a x + b y} = \overline{\ip{a x + b y}{v}} = \overline{a}\, \ip{v}{x} + \overline{b}\, \ip{v}{y}$.
3. Part 1, the zero vector. For every $s \in S$, linearity gives $\ip{0}{s} = \ip{0 \cdot 0}{s} = 0 \cdot \ip{0}{s} = 0$. So $0 \in S^\perp$.
4. Part 1, closure. Let $x, y \in S^\perp$ and $a, b \in \mathbb{K}$. For each $s \in S$, linearity gives $\ip{a x + b y}{s} = a \cdot 0 + b \cdot 0 = 0$, so $a x + b y \in S^\perp$.
5. By steps 3 and 4 and the [[subspace criterion|0EPTJA5QV4]], $S^\perp$ is a subspace of $V$. This proves part 1.
6. Part 2. Let $S \subseteq T$ and $v \in T^\perp$. Each $s \in S$ lies in $T$, so $\ip{v}{s} = 0$. Hence $v \in S^\perp$, and $T^\perp \subseteq S^\perp$.
7. Part 3, first inclusion. Since $S \subseteq \operatorname{span} S$, step 6 gives $(\operatorname{span} S)^\perp \subseteq S^\perp$.
8. Part 3, second inclusion. Let $v \in S^\perp$ and $u \in \operatorname{span} S$. By the definition of the [[span|0DTY8B9HMS]], $u = a_1 s_1 + \dots + a_k s_k$ with $s_i \in S$ and $a_i \in \mathbb{K}$.
9. Step 2 gives $\ip{v}{u} = \overline{a_1}\, \ip{v}{s_1} + \dots + \overline{a_k}\, \ip{v}{s_k} = 0$, because each $\ip{v}{s_i}$ is $0$. So $v \in (\operatorname{span} S)^\perp$, and with step 7 this proves part 3.
10. Part 4. The vector $0$ lies in $U$, because $U$ is a subspace, and in $U^\perp$, by step 3. So $\{0\} \subseteq U \cap U^\perp$.
11. Let $x \in U \cap U^\perp$. Since $x \in U^\perp$ and $x \in U$, the definition gives $\ip{x}{x} = 0$. Positivity forces $x = 0$, and this proves part 4.
12. Part 5, first inclusion. We have $U \subseteq U + W$ and $W \subseteq U + W$, since $u = u + 0$ and $w = 0 + w$. Step 6 gives $(U + W)^\perp \subseteq U^\perp$ and $(U + W)^\perp \subseteq W^\perp$, so $(U + W)^\perp \subseteq U^\perp \cap W^\perp$.
13. Part 5, second inclusion. Let $v \in U^\perp \cap W^\perp$ and $x \in U + W$. By the definition of the [[sum|0RMKABS2S5]], $x = u + w$ with $u \in U$ and $w \in W$.
14. Step 2 gives $\ip{v}{x} = \ip{v}{u} + \ip{v}{w} = 0 + 0 = 0$. So $v \in (U + W)^\perp$, and with step 12 this proves part 5.
15. Part 6, first claim. For every $v \in V$, the computation of step 3 gives $\ip{0}{v} = 0$, and step 1 gives $\ip{v}{0} = 0$. So $\{0\}^\perp = V$.
16. Part 6, second claim. Since $V^\perp \subseteq V$, we have $V \cap V^\perp = V^\perp$. Part 4 for the subspace $V$ gives $V^\perp = \{0\}$.

This proves all six parts.

## Idea

Each condition $\ip{v}{s} = 0$ is linear in $v$, so the set of solutions is a subspace.
Being orthogonal to a set is the same as being orthogonal to its span, because the inner product turns a linear combination in the second slot into a combination of zeros.
The sum rule is the same remark for two subspaces at once.
Positivity enters only in parts 4 and 6, through the fact that a vector orthogonal to itself is zero.

## Variants

In $\R^n$ with the dot product there is a matrix proof of part 1 for a finite set $S$.
Put the vectors of $S$ into the rows of a matrix $A$; then $S^\perp$ is the null space of $A$, and null spaces are subspaces.
Part 5 also follows from the rules for [[annihilators|0ASHNYF7AG]], through the map $v \mapsto \ip{\cdot}{v}$ from $V$ to the dual space.
