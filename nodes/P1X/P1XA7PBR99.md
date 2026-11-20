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

We use the [[subspace test|Z5XKYXTC0K]] and the axioms of the [[vector space definition|05EGHEQZAW]].

1. $0 = 0 + 0$ with $0 \in U$ and $0 \in W$, so $0 \in U + W$, and $U + W$ is nonempty.
2. Let $x = u + w$ and $y = u' + w'$ be in $U + W$, with $u, u' \in U$ and $w, w' \in W$, and let $a \in F$.
3. By axioms 1, 2 and 7, $x + ay = (u + au') + (w + aw')$.
4. Here $u + au' \in U$ and $w + aw' \in W$, because $U$ and $W$ are subspaces. So $x + ay \in U + W$.
5. By the subspace test and steps 1 to 4, $U + W$ is a subspace.
6. For $u \in U$, we have $u = u + 0$ with $0 \in W$. So $U \subseteq U + W$; in the same way $W \subseteq U + W$.
7. Let $X$ be a subspace with $U \subseteq X$ and $W \subseteq X$. Let $u + w \in U + W$.
8. Then $u \in X$ and $w \in X$, so $u + w \in X$, by closure of $X$ under addition. So $U + W \subseteq X$.

## Idea

The sum is closed because we can add and scale the $U$ parts and the $W$ parts separately.
It is the smallest such subspace because closure under addition forces every subspace that holds $U$ and $W$ to hold each $u + w$.
