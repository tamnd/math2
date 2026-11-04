---
tag: Z51Z4CTP5J
kind: proof
name: Proof of the first Borel–Cantelli lemma
msc: [60F20]
proves: 0T6WS7TT77
uses: [0EGSEE9J9R, 00SQGJNRTB, 0ZYBZ34RT2]
sources:
  - url: https://en.wikipedia.org/wiki/Borel–Cantelli_lemma
    locator: Proof
---

## Proof

We bound the limit superior by the tails of the convergent series.

1. Let $L = \limsup_{n} A_n = \bigcap_{n \ge 1} B_n$, where $B_n = \bigcup_{m \ge n} A_m$. Each $B_n$ and $L$ are [[events|00SQGJNRTB]], as countable unions and intersections of events.
2. For each $n$, $L \subseteq B_n$. So $P(L) \le P(B_n)$, by the monotonicity of the measure $P$ on the [[probability space|0ZYBZ34RT2]].
3. By [[Boole's inequality|0EGSEE9J9R]], $P(B_n) \le \sum_{m = n}^{\infty} P(A_m)$.
4. Let $s = \sum_{m=1}^{\infty} P(A_m)$, a finite number by hypothesis. The tail $\sum_{m \ge n} P(A_m) = s - \sum_{m=1}^{n-1} P(A_m)$ tends to $s - s = 0$ as $n \to \infty$.
5. By steps 2 to 4, $0 \le P(L) \le \sum_{m \ge n} P(A_m)$ for each $n$. Let $n \to \infty$ to get $P(L) = 0$.
6. Claim: $\omega \in L$ if and only if $\omega \in A_m$ for infinitely many $m$. If $\omega$ lies in infinitely many $A_m$, then for each $n$ some $m \ge n$ has $\omega \in A_m$, so $\omega \in B_n$ for all $n$.
7. Conversely, if $\omega$ lies in only finitely many $A_m$, let $N$ exceed all these indices. Then $\omega \notin B_N$, so $\omega \notin L$.
8. By steps 5 to 7, the set of outcomes that lie in infinitely many $A_n$ has probability $0$. So almost surely only finitely many $A_n$ occur.

## Idea

An outcome that lies in infinitely many $A_n$ lies, for every $n$, in some $A_m$ with $m \ge n$. The probability of that is at most the tail of a convergent series, which tends to $0$.
