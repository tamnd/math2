---
tag: P1XA7PBR99
kind: proof
name: Proof that the sum of two subspaces is the smallest subspace containing both
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: EDF9C7G048
methods: [0NTF6DMVAP]
uses: [0RMKABS2S5, Z5XKYXTC0K, 05EGHEQZAW]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_subspace
    locator: Operations and relations on subspaces
  - book: isbn:9783031410253
    locator: Section 1C
---

## Proof

We show that $U + W$ passes the [[subspace test|Z5XKYXTC0K]], that it contains $U$ and $W$, and that every subspace containing $U$ and $W$ contains it.

1. Since $0 \in U$ and $0 \in W$, the vector $0 = 0 + 0$ lies in $U + W$. So $U + W$ is nonempty.
2. Let $x, y \in U + W$ and $a \in F$. By the [[definition of the sum|0RMKABS2S5]], we can write $x = u + w$ and $y = u' + w'$ with $u, u' \in U$ and $w, w' \in W$.
3. By the associativity and commutativity of addition (axioms 1 and 2) and the distributive law $a(u' + w') = au' + aw'$ (axiom 7) of the [[vector space definition|05EGHEQZAW]],
$$x + ay = (u + w) + (au' + aw') = (u + au') + (w + aw').$$
4. The vector $u + au'$ lies in $U$, and $w + aw'$ lies in $W$, because $U$ and $W$ are subspaces. So $x + ay \in U + W$.
5. By steps 1 to 4 and the subspace test, $U + W$ is a subspace of $V$.
6. For $u \in U$ we have $u = u + 0$ with $0 \in W$, so $u \in U + W$. Hence $U \subseteq U + W$, and in the same way $W \subseteq U + W$.
7. Let $X$ be a subspace of $V$ with $U \subseteq X$ and $W \subseteq X$, and let $u + w$ be an element of $U + W$.
8. Then $u \in X$ and $w \in X$, so $u + w \in X$, because $X$ is closed under addition. Hence $U + W \subseteq X$.
9. Steps 5, 6 and 8 are the claims of the statement.

## Idea

The sum is closed because we can add and scale the $U$ parts and the $W$ parts separately, after regrouping the four terms.
It is the smallest such subspace because closure under addition forces every subspace that holds $U$ and $W$ to hold each $u + w$.
So the sum is exactly what closure demands, and closure demands nothing more.

## Variants

One can first prove that the [[span|0DTY8B9HMS]] of any set is the smallest subspace that contains it.
Then it remains to show that $\operatorname{span}(U \cup W) = U + W$.
A linear combination of vectors of $U \cup W$ splits into the terms from $U$ and the terms from $W$, and each group adds up to one vector of $U$ or of $W$, because $U$ and $W$ are subspaces.
