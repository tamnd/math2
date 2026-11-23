---
tag: V1A4G16JRZ
kind: proof
name: Proof that prelinearity holds for every left-continuous t-norm
msc: ["03B52"]
topics: [WZP584JQ06]
audience: grad
proves: D0ZADJFPQE
uses: [BHGCVPAJW0, D1R4D2HEPP]
methods: [0WCP0PVET6, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/T-norm
    locator: Residuum; Basic properties of residua
---

## Proof

We prove three small facts about the residuum, and then split into the cases $x \le y$ and $y \le x$.

Let $*$ be a left-continuous [[t-norm|BHGCVPAJW0]], and let $\Rightarrow$ be its residuum, so that $z * x \le y$ holds iff $z \le x \Rightarrow y$.
It exists by [[the left-continuity statement|D1R4D2HEPP]].
The three facts hold for all $a, c, x, y \in [0, 1]$.

1. (R1) $x \Rightarrow y = 1$ iff $x \le y$.
   Put $z = 1$ in residuation and use $1 * x = x$.
2. (R2) $1 \Rightarrow c = c$.
   Since $z * 1 = z$, the condition $z * 1 \le c$ holds iff $z \le c$, and the largest such $z$ is $c$.
3. (R3) $c \le (a \Rightarrow c) \Rightarrow c$.
   By residuation this is $c * (a \Rightarrow c) \le c$, and $c * b \le c * 1 = c$ for every $b$.

Item 1 of the statement follows next.

4. Since $[0, 1]$ is totally ordered, $x \le y$ or $y \le x$.
5. By R1, $x \Rightarrow y = 1$ or $y \Rightarrow x = 1$, so $\max(x \Rightarrow y, y \Rightarrow x) = 1$.

For item 2, let $P = (x \Rightarrow y) \Rightarrow c$ and $Q = ((y \Rightarrow x) \Rightarrow c) \Rightarrow c$.
By R1 it is enough to show $P \le Q$.

6. In the case $x \le y$, R1 gives $x \Rightarrow y = 1$, so $P = 1 \Rightarrow c = c$ by R2.
7. In this case R3 with $a = y \Rightarrow x$ gives $c \le Q$, so $P \le Q$.
8. In the case $y \le x$, R1 gives $y \Rightarrow x = 1$, so $Q = (1 \Rightarrow c) \Rightarrow c = c \Rightarrow c$ by R2.
9. In this case $Q = c \Rightarrow c = 1$ by R1, so $P \le Q$.
10. By step 4 the two cases cover all $x, y$, so $P \Rightarrow Q = 1$ by R1. $\blacksquare$

## Idea

In a chain, one of the two implications $x \Rightarrow y$ and $y \Rightarrow x$ is $1$.
Then the formula reduces either to $c \Rightarrow ((a \Rightarrow c) \Rightarrow c)$ or to $P \Rightarrow 1$, and both are $1$.

## Variants

The proof uses only residuation, the unit law, commutativity, the bound $c * b \le c$ and the total order.
So it proves prelinearity in every linearly ordered commutative integral residuated lattice, that is, in every MTL-chain.
In a Heyting algebra that is not a chain, step 4 fails, and [[the fork|6S7TSV01WB]] refutes $(p \to q) \lor (q \to p)$.
