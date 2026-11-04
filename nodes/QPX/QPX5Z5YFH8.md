---
tag: QPX5Z5YFH8
kind: proof
name: Proof of the well-ordering principle from strong induction
msc: [03F30]
proves: 01BX15HSRR
uses: [0KMVFSHFGZ, 0Y9H52BT03, 0W5DSDFQ4G, 0832XVR512, 0DFZNHJ0S2, 0ASJVEFA9J]
methods: [0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Relationship to the well-ordering principle
---

## Proof

We first show that the order is total, and then argue by contradiction with strong induction.
Let $S$ be the [[successor function|0832XVR512]], and write $1 = S(0)$.
The [[addition|0W5DSDFQ4G]] satisfies $a + 0 = a$ and $a + S(b) = S(a + b)$. So $n + 1 = S(n)$.
The relations $\le$ and $<$ are the [[order on the natural numbers|0Y9H52BT03]].

1. Lemma A: each natural number $c \neq 0$ equals $S(d)$ for some $d$. We prove "$c = 0$ or $c = S(d)$ for some $d$" by [[induction|0ASJVEFA9J]] on $c$. The case $c = 0$ is clear, and $c + 1 = S(c)$.
2. Lemma B: $S(b) + d = S(b + d)$ for all $b$ and $d$. By the [[commutativity of addition|0DFZNHJ0S2]], $S(b) + d = d + S(b) = S(d + b) = S(b + d)$.
3. Lemma T: for all natural numbers $a$ and $b$, $a \le b$ or $b \le a$. Fix $a$ and use induction on $b$.
4. For $b = 0$: by commutativity, $0 + a = a + 0 = a$. So $0 \le a$.
5. Suppose that $a \le b$ or $b \le a$. If $a \le b$, let $a + c = b$. Then $a + S(c) = S(a + c) = S(b)$, so $a \le S(b)$.
6. If $b \le a$, let $b + c = a$. If $c = 0$, then $a = b$ and $a + 1 = S(b)$, so $a \le S(b)$.
7. If $c \neq 0$, Lemma A gives $c = S(d)$. Then $a = S(b + d) = S(b) + d$ by Lemma B, so $S(b) \le a$.
8. By induction, Lemma T holds for all $b$, and $a$ was arbitrary.
9. Now let $A \subseteq \mathbb{N}$ be nonempty. Suppose, for a contradiction, that $A$ has no least element.
10. For each natural number $n$, let $P(n)$ be the property "$n \notin A$". We check the hypothesis of [[strong induction|0KMVFSHFGZ]].
11. Let $n$ be a natural number, and suppose that $k \notin A$ for every $k < n$. Suppose also that $n \in A$.
12. Let $x \in A$. By Lemma T, $n \le x$ or $x \le n$.
13. If $x \le n$ and $x \neq n$, then $x < n$, so $x \notin A$ by step 11. This is false, so $x \le n$ implies $x = n$.
14. If $x = n$, then $n \le x$ because $n + 0 = x$. So in all cases $n \le x$.
15. Thus $n$ is a least element of $A$, which contradicts step 9. So $n \notin A$, and $P(n)$ holds.
16. By strong induction, $P(n)$ holds for every natural number $n$. So $A$ is empty.
17. This contradicts the hypothesis $A \neq \emptyset$. Therefore $A$ has a least element $a$, with $a \le x$ for each $x \in A$.

## Idea

If a set has no smallest element, then no number can be the first one to enter it.
Strong induction turns this into "no number is in the set at all".
Totality of the order is what makes "nothing smaller is in the set" mean "this is the smallest".
