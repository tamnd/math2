---
tag: ~d376caaa
kind: proof
name: Proof that prelinearity holds for every left-continuous t-norm
msc: ["03B52"]
topics: [WZP584JQ06]
audience: grad
proves: ~2988a2f8
uses: [~a4e21349, ~42fe79f8]
methods: [0WCP0PVET6, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/T-norm
    locator: Residuum; Basic properties of residua
---

## Proof

Let $*$ be a left-continuous [[t-norm|~a4e21349]], and let $\Rightarrow$ be its residuum: $z * x \le y \iff z \le x \Rightarrow y$.
It exists by [[the left-continuity statement|~42fe79f8]].
We first prove three facts, for all $a, c, x, y \in [0, 1]$.

1. (R1) $x \Rightarrow y = 1$ iff $x \le y$: put $z = 1$ in residuation, and use $1 * x = x$.
2. (R2) $1 \Rightarrow c = c$: $z * 1 = z$, so $z * 1 \le c \iff z \le c$, and the largest such $z$ is $c$.
3. (R3) $c \le (a \Rightarrow c) \Rightarrow c$: by residuation this is $c * (a \Rightarrow c) \le c$, and $c * b \le \min(c, b) \le c$ for every $b$.

Item 1 of the statement.

4. Since $[0, 1]$ is totally ordered, $x \le y$ or $y \le x$.
5. By R1, $x \Rightarrow y = 1$ or $y \Rightarrow x = 1$, so $\max(x \Rightarrow y, y \Rightarrow x) = 1$.

Item 2 of the statement.
Let $P = (x \Rightarrow y) \Rightarrow c$ and $Q = ((y \Rightarrow x) \Rightarrow c) \Rightarrow c$; we show $P \Rightarrow Q = 1$, that is $P \le Q$ by R1.

6. Case $x \le y$: by R1, $x \Rightarrow y = 1$, so $P = 1 \Rightarrow c = c$ by R2.
7. In this case, R3 with $a = y \Rightarrow x$ gives $c \le Q$, so $P \le Q$.
8. Case $y \le x$: by R1, $y \Rightarrow x = 1$, so $Q = (1 \Rightarrow c) \Rightarrow c = c \Rightarrow c$ by R2.
9. In this case, $Q = c \Rightarrow c = 1$ by R1, so $P \le Q$.
10. By step 4 the two cases cover all $x, y$, so $P \Rightarrow Q = 1$ by R1. $\blacksquare$

## Idea

In a chain, one of the two implications $x \Rightarrow y$ and $y \Rightarrow x$ is $1$.
Then the formula reduces to $c \Rightarrow ((a \Rightarrow c) \Rightarrow c)$ or to $P \Rightarrow 1$, and both are $1$.

## Variants

The proof uses only residuation, the unit law, commutativity, the bound $c * b \le c$ and the total order.
So it proves prelinearity in every linearly ordered commutative integral residuated lattice, that is, in every MTL-chain.
In a Heyting algebra that is not a chain, step 4 fails, and [[the fork|6S7TSV01WB]] refutes the form $(p \to q) \lor (q \to p)$.
