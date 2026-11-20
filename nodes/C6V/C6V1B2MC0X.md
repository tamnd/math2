---
tag: C6V1B2MC0X
kind: proof
name: Proof of the dimension theorem for infinite bases by cardinal arithmetic
msc: ["15A03", "03E10"]
topics: [MVH97H8B2J]
audience: grad
proves: 0WK0Y8RH1M
methods: [0NTF6DMVAP, 0J0XBKG64S]
uses: [WXB40PTZNV, H75GS7QVPB, 0VTQTPQGAV, 0QKPNZKNEA, 0A9V6RKQG6]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_theorem_for_vector_spaces
    locator: Proof
  - url: https://en.wikipedia.org/wiki/Cardinal_number
    locator: Cardinal arithmetic
  - book: isbn:9780387728285
    locator: Chapter 1
---

## Proof

Since a basis is an independent family, its members are distinct; so we treat bases as sets.
We cite one fact of cardinal arithmetic, which uses the axiom of choice: for an infinite [[cardinal|0QKPNZKNEA]] $\kappa$, $\kappa \cdot \aleph_0 = \kappa$, and a union of $\kappa$ finite sets has cardinality at most $\kappa \cdot \aleph_0$.

1. Let $B$ and $C$ be bases of $V$. If one of them is finite, then both are finite of the same size, by the [[finite proof|WXB40PTZNV]]. So assume that $B$ and $C$ are both infinite.
2. For $c \in C$, write $c = \sum_{b \in B} a_b b$ with finitely many $a_b \ne 0$, and let $S_c = \set{b \in B : a_b \ne 0}$. Each $S_c$ is a finite subset of $B$.
3. We claim that $B = \bigcup_{c \in C} S_c$. Suppose, for a contradiction, that some $b_0 \in B$ lies in no $S_c$.
4. Then each $c \in C$ is a combination of vectors of $B \setminus \set{b_0}$, so $C \subseteq \operatorname{span}(B \setminus \set{b_0})$.
5. Since $C$ spans $V$, the subspace $\operatorname{span}(B \setminus \set{b_0})$ is all of $V$, and it contains $b_0$.
6. So $b_0$ is a combination of the other vectors of $B$, and $B$ is dependent, by the [[dependence lemma|H75GS7QVPB]]. This contradicts the independence of $B$, and the claim holds.
7. By step 3, $B$ is a union of $\abs{C}$ finite sets. By the cited fact, $\abs{B} \le \abs{C} \cdot \aleph_0 = \abs{C}$, because $C$ is infinite.
8. Steps 2 to 7 with $B$ and $C$ exchanged give $\abs{C} \le \abs{B}$.
9. By the [[Schröder-Bernstein theorem|0A9V6RKQG6]], $\abs{B} = \abs{C}$.

## Idea

Each vector of one basis uses only finitely many vectors of the other basis.
All vectors of the other basis must be used, or one of them would be redundant.
So one basis is covered by $\abs{C}$ finite sets, which have at most $\abs{C}$ elements in total.
