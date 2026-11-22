---
tag: QPX5Z5YFH8
kind: proof
name: Proof of the well-ordering principle from strong induction
msc: [03F30]
topics: [EEH2F76CYQ]
audience: ug1
proves: 01BX15HSRR
uses: [0KMVFSHFGZ, 0Y9H52BT03, 0W5DSDFQ4G, 0832XVR512, 0DFZNHJ0S2, 0ASJVEFA9J]
methods: [0J0XBKG64S, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Relationship to the well-ordering principle
---

## Proof

We first show that any two natural numbers can be compared, and then prove by strong induction that a set with no least element contains no number at all.

Let $S$ be the [[successor function|0832XVR512]], and write $1 = S(0)$.
[[Addition|0W5DSDFQ4G]] satisfies $a + 0 = a$ and $a + S(b) = S(a + b)$, so $n + 1 = S(n)$.
The relation $k \le n$ means that $k + c = n$ for some natural number $c$, and $k < n$ means $k \le n$ and $k \ne n$; this is the [[order on the natural numbers|0Y9H52BT03]].

1. Lemma A: each natural number $c \ne 0$ equals $S(d)$ for some $d$.
   We prove "$c = 0$ or $c = S(d)$ for some $d$" by [[induction|0ASJVEFA9J]] on $c$.
   For $c = 0$ the first alternative holds, and for $c + 1 = S(c)$ we take $d = c$.
2. Lemma B: $S(b) + d = S(b + d)$ for all $b$ and $d$.
   By the [[commutativity of addition|0DFZNHJ0S2]], $S(b) + d = d + S(b) = S(d + b) = S(b + d)$.
3. Lemma T: for all natural numbers $a$ and $b$, $a \le b$ or $b \le a$.
   We fix $a$ and use induction on $b$.
4. For $b = 0$, commutativity gives $0 + a = a + 0 = a$, so $0 \le a$.
5. Suppose $a \le b$ or $b \le a$, and first let $a \le b$, say $a + c = b$.
   Then $a + S(c) = S(a + c) = S(b)$, so $a \le S(b)$.
6. Now let $b \le a$, say $b + c = a$.
   If $c = 0$, then $a = b$, and $a + 1 = S(b)$ gives $a \le S(b)$.
7. If $c \ne 0$, Lemma A gives $c = S(d)$.
   Then $a = b + S(d) = S(b + d) = S(b) + d$ by Lemma B, so $S(b) \le a$.
8. So the claim holds for $S(b)$, and induction proves Lemma T for all $b$; since $a$ was arbitrary, it holds for all $a$ and $b$.
9. Now let $A \subseteq \mathbb{N}$ be nonempty, and suppose, for a contradiction, that $A$ has no least element.
10. For each natural number $n$, let $P(n)$ be the property "$n \notin A$".
    We check the hypothesis of [[strong induction|0KMVFSHFGZ]] for $P$.
11. Let $n$ be a natural number, assume that $k \notin A$ for every $k < n$, and suppose that $n \in A$.
12. Let $x \in A$.
    By Lemma T, $n \le x$ or $x \le n$.
13. If $x \le n$ and $x \ne n$, then $x < n$, so $x \notin A$ by step 11, which is false.
    So $x \le n$ implies $x = n$, and then $n \le x$ because $n + 0 = x$.
14. So $n \le x$ for every $x \in A$, and $n$ is a least element of $A$.
    This contradicts step 9, so $n \notin A$, and $P(n)$ holds.
15. Strong induction now gives $P(n)$ for every natural number $n$, so $A$ is empty.
16. This contradicts the hypothesis $A \ne \emptyset$.
    Therefore $A$ has a least element, which is the [[well-ordering principle|01BX15HSRR]].

## Idea

If a set has no smallest element, then no number can be the first to enter it.
Zero cannot be in it, since it would be smallest, and once no number below $n$ is in it, $n$ cannot be in it either.
Strong induction turns this into "no number is in the set", which contradicts the set being nonempty.
Lemma T is needed so that "nothing smaller is in the set" really means "this is the smallest", because a least element must be compared with every element.

## Variants

Ordinary [[induction|0ASJVEFA9J]] also works, applied to the claim "every subset of $\mathbb{N}$ that contains a number $k \le n$ has a least element".
For $n = 0$ the set contains $0$, and $0$ is least.
For the step, let $A$ contain some $k \le n + 1$.
If $A$ contains a number $\le n$, the induction hypothesis applies.
Otherwise $k = n + 1$, and every element of $A$ is at least $n + 1$, so $n + 1$ is least.

The converse, that the well-ordering principle implies induction when each nonzero natural number is a successor, is part of the [[equivalence of induction and well-ordering|J2P9FWBP3Q]].
