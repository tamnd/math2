---
tag: C54QYDXFP3
kind: proof
name: Proof of strong induction from ordinary induction
msc: [03F30]
topics: [EEH2F76CYQ]
audience: ug1
proves: 0KMVFSHFGZ
uses: [0ASJVEFA9J, 0Y9H52BT03, 0W5DSDFQ4G, 0832XVR512, 0TBYMWPWWB, 0D752BG155]
methods: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Complete (strong) induction
---

## Proof

We apply ordinary [[induction|0ASJVEFA9J]] to the stronger property "every case below $n$ holds", after three small lemmas about the order.

Let $S$ be the [[successor function|0832XVR512]], and write $1 = S(0)$.
[[Addition|0W5DSDFQ4G]] satisfies $a + 0 = a$ and $a + S(b) = S(a + b)$, so $n + 1 = S(n + 0) = S(n)$.
The relation $k \le n$ means that $k + c = n$ for some natural number $c$, and $k < n$ means $k \le n$ and $k \ne n$; this is the [[order on the natural numbers|0Y9H52BT03]].
Assume the hypothesis of [[strong induction|0KMVFSHFGZ]]: for each $n$, if $P(k)$ holds for every $k < n$, then $P(n)$ holds.
For each natural number $n$, let $Q(n)$ be the property "$P(k)$ holds for every natural number $k < n$".

1. Lemma A: each natural number $c \ne 0$ equals $S(d)$ for some natural number $d$.
   We prove "$c = 0$ or $c = S(d)$ for some $d$" by induction on $c$.
   For $c = 0$ the first alternative holds, and for $c + 1 = S(c)$ we take $d = c$.
2. Lemma B: no natural number $k$ satisfies $k < 0$.
   Suppose that $k + c = 0$ for a natural number $c$.
3. If $c \ne 0$, then Lemma A gives $c = S(d)$, so $k + c = S(k + d)$.
   This is not $0$, because [[zero is not a successor|0D752BG155]], so this case is impossible.
4. So $c = 0$ and $k = k + 0 = 0$.
   Thus $k \le 0$ forces $k = 0$, and $k < 0$ is impossible.
5. Lemma C: if $k < n + 1$, then $k < n$ or $k = n$.
   Let $k + c = S(n)$ with $k \ne S(n)$.
6. Then $c \ne 0$, because $c = 0$ would give $k = S(n)$.
   By Lemma A, $c = S(d)$ for some $d$.
7. So $S(k + d) = k + S(d) = S(n)$, and $k + d = n$ because [[the successor function is injective|0TBYMWPWWB]].
8. Thus $k \le n$, which means $k < n$ or $k = n$.
   This proves Lemma C.
9. Base case: by Lemma B there is no $k < 0$, so $Q(0)$ holds with nothing to check.
10. Induction step: suppose that $Q(n)$ holds.
    The hypothesis of strong induction, applied at $n$, then gives $P(n)$.
11. Let $k < n + 1$.
    By Lemma C, $k < n$ or $k = n$; in the first case $P(k)$ holds by $Q(n)$, and in the second case by step 10.
12. So $Q(n + 1)$ holds, and ordinary induction gives $Q(n)$ for every natural number $n$.
13. Let $n$ be any natural number.
    By step 12, $Q(n)$ holds, and the hypothesis of strong induction turns $Q(n)$ into $P(n)$.
14. So $P(n)$ holds for every natural number $n$, which is the conclusion of strong induction.

## Idea

Ordinary induction carries one fact from each number to the next.
The trick is to make that one fact a whole list: $Q(n)$ says that all the cases below $n$ hold.
Then the step from $Q(n)$ to $Q(n + 1)$ needs only one new case, $P(n)$, and the strong hypothesis supplies it.
Lemmas A to C only make sure that "the numbers below $n + 1$" are exactly "the numbers below $n$, and $n$".

## Variants

Many books take the order of $\mathbb{N}$ as known and treat Lemmas B and C as facts, and then the proof is steps 9 to 14 alone.

Some books apply ordinary induction to $Q'(n)$: "$P(k)$ holds for every $k \le n$".
The base case is then $P(0)$, which the strong hypothesis gives at $n = 0$ with an empty assumption.

Strong induction also follows from the [[well-ordering principle|01BX15HSRR]].
If some $P(n)$ fails, take the least such $n$.
Then $P(k)$ holds for every $k < n$, and the strong hypothesis gives $P(n)$, a contradiction.
The [[equivalence of induction and well-ordering|J2P9FWBP3Q]] gives the details and the base theory.
