---
tag: P1FJ5TEFBX
kind: proof
name: Proof that Webb's function is a Sheffer function
msc: ["03B50", "08A40"]
topics: [WZP584JQ06]
audience: research
proves: EPSBDVPKJP
uses: [8P3Y6T0RZS, 6KFS240R42]
methods: [01XM7JEKHY, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_NOR
    locator: Alternative notations and names
---

## Proof

Let $S x = x + 1 \bmod m$, so $w(x, y) = S(\max(x, y))$.

1. $w(x, x) = S(\max(x, x)) = S x$. So $S$ is a term in $w$.
2. By step 1, $S^k$ is a term in $w$ for every $k \ge 1$.
3. $S^m$ is the identity, since $x + m \equiv x \pmod m$.
4. $S^{m-1}(w(x, y)) = S^m(\max(x, y)) = \max(x, y)$, by step 3. So $\max$ is a term in $w$.
5. Post's negation is $\neg x = x - 1 \bmod m = S^{m-1} x$, a term by step 2.
6. By [[Post's theorem|8P3Y6T0RZS]], every operation $V^n \to V$ with $n \ge 1$ is a term in $\neg$ and $\max$.
7. Substituting the terms of steps 4 and 5 gives a term in $w$ alone. So $\set{w}$ is functionally complete.

## Idea

Feeding $w$ the same input twice gives the shift, and enough shifts undo the shift built into $w$.
Then $w$ yields both of Post's connectives.

## Variants

1. For $m = 2$, step 1 gives $\neg x = x \downarrow x$, and step 4 gives $x \lor y = \neg(x \downarrow y)$; this is the classical proof for NOR.
2. A direct proof that builds the tests $J_a$ from $w$ is possible, but it repeats the proof of Post's theorem.
