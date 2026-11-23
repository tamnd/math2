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

We define Post's negation and $\max$ from $w$, and then apply Post's theorem.
Let $S x = x + 1 \bmod m$, so that $w(x, y) = S(\max(x, y))$.

1. Put the same variable in both places.
   Then $w(x, x) = S(\max(x, x)) = S x$, so $S$ is a term in $w$.
2. Composing the term of step 1 with itself shows that $S^k$ is a term in $w$ for every $k \ge 1$.
3. The power $S^m$ is the identity on $V$, because $x + m \equiv x \pmod m$.
4. Apply $S^{m-1}$ to $w(x, y)$.
   Step 3 gives $S^{m-1}(w(x, y)) = S^m(\max(x, y)) = \max(x, y)$, so $\max$ is a term in $w$.
5. Post's negation is $\neg x = x - 1 \bmod m$, and $x - 1 \equiv x + (m - 1)$, so $\neg x = S^{m-1} x$.
   By step 2 it is a term in $w$.
6. By [[Post's theorem|8P3Y6T0RZS]], every operation $V^n \to V$ with $n \ge 1$ is a term in $\neg$ and $\max$.
7. Replace each $\neg$ and each $\max$ in such a term by the terms of steps 5 and 4.
   The result is a term in $w$ alone with the same values.

So every operation on $V$ is a term in $w$, and $w$ is a [[Sheffer function|6KFS240R42]].

## Idea

Feeding $w$ the same input twice gives the shift, and enough shifts undo the shift that is built into $w$.
Then $w$ yields both of Post's connectives, and Post's theorem does the rest.
The whole proof is a reduction to a set that is already known to be complete.

## Variants

For $m = 2$, step 1 gives $\neg x = x \downarrow x$, and step 4 gives $x \lor y = \neg(x \downarrow y)$.
This is the classical proof that NOR alone is complete.
One can also build the value tests of [[Post's proof|FR9JC8MNBJ]] directly from $w$, without passing through $\neg$ and $\max$.
That route gives the same terms after substitution, so it repeats Post's proof in a longer notation.
