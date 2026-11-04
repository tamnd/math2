---
tag: C54QYDXFP3
kind: proof
name: Proof of strong induction from ordinary induction
msc: [03F30]
proves: 0KMVFSHFGZ
uses: [0ASJVEFA9J, 0Y9H52BT03, 0W5DSDFQ4G, 0832XVR512, 0TBYMWPWWB, 0D752BG155]
methods: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Complete (strong) induction
---

## Proof

We apply ordinary [[induction|0ASJVEFA9J]] to a stronger property.
Let $S$ be the [[successor function|0832XVR512]], and write $1 = S(0)$.
The [[addition|0W5DSDFQ4G]] satisfies $a + 0 = a$ and $a + S(b) = S(a + b)$. So $n + 1 = S(n + 0) = S(n)$.
The relations $\le$ and $<$ are the [[order on the natural numbers|0Y9H52BT03]].
For each natural number $n$, let $Q(n)$ be the property "$P(k)$ holds for every natural number $k < n$".

1. Lemma A: each natural number $c \neq 0$ equals $S(d)$ for some natural number $d$. We prove "$c = 0$ or $c = S(d)$ for some $d$" by induction on $c$.
2. For $c = 0$, the first alternative holds. For $c + 1 = S(c)$, take $d = c$. This proves Lemma A.
3. Lemma B: no natural number $k$ satisfies $k < 0$. Suppose that $k + c = 0$ for a natural number $c$.
4. If $c \neq 0$, Lemma A gives $c = S(d)$. Then $k + c = S(k + d)$, and this is not $0$ because [[zero is not a successor|0D752BG155]].
5. So $c = 0$ and $k = k + 0 = 0$. Thus $k \le 0$ forces $k = 0$, and $k < 0$ is impossible.
6. Lemma C: if $k < n + 1$, then $k < n$ or $k = n$. Indeed, let $k + c = S(n)$ with $k \neq S(n)$.
7. Then $c \neq 0$, because $c = 0$ would give $k = S(n)$. By Lemma A, $c = S(d)$ for some $d$.
8. So $S(k + d) = k + S(d) = S(n)$. Since [[the successor function is injective|0TBYMWPWWB]], $k + d = n$.
9. Thus $k \le n$, so $k < n$ or $k = n$. This proves Lemma C.
10. Base case: by Lemma B, there is no $k < 0$. So $Q(0)$ holds.
11. Induction step: suppose that $Q(n)$ holds. The hypothesis of the statement then gives $P(n)$.
12. Let $k < n + 1$. By Lemma C, $k < n$ or $k = n$. In the first case $P(k)$ holds by $Q(n)$, and in the second by step 11.
13. So $Q(n + 1)$ holds. By induction, $Q(n)$ holds for every natural number $n$.
14. Let $n$ be a natural number. By step 13, $Q(n)$ holds, and the hypothesis of the statement gives $P(n)$.

## Idea

Ordinary induction carries only one case to the next.
The trick is to carry all earlier cases at once, in the property $Q(n)$.
Then the step from $Q(n)$ to $Q(n + 1)$ only needs one new case, $P(n)$, which the hypothesis gives.
