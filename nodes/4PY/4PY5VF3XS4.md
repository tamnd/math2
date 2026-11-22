---
tag: 4PY5VF3XS4
kind: proof
name: Proof of the equivalence of induction and well-ordering by a cycle of implications
msc: ["03F30"]
topics: [EEH2F76CYQ]
audience: ug1
proves: J2P9FWBP3Q
uses: [0ASJVEFA9J, 0KMVFSHFGZ, 01BX15HSRR, 0832XVR512]
methods: [0ASJVEFA9J, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Relationship to the well-ordering principle
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Equivalence with ordinary induction
---

## Proof

We prove that (I) implies (SI), that (SI) implies (WO), and that (WO) implies (I), so that each principle implies the other two.
We use the notation of the [[statement|J2P9FWBP3Q]]: a set $N$ with $0$, a [[successor|0832XVR512]] map $S$ and a relation $<$ that satisfy (B1) to (B4).

1. (I) implies (SI).
   Assume (I), and let $A \subseteq N$ satisfy the hypothesis of (SI): for each $n$, if every $k < n$ lies in $A$, then $n \in A$.
2. Let $Q$ be the set of all $n \in N$ such that every $k < n$ lies in $A$.
   Then $0 \in Q$, because by (B2) no $k$ satisfies $k < 0$.
3. Let $n \in Q$.
   Then $n \in A$ by the hypothesis on $A$.
4. Let $k < S(n)$.
   By (B1), $k < n$ or $k = n$ or $n < k$, and the last case would give $n < k < S(n)$, which (B3) excludes.
5. If $k < n$, then $k \in A$ because $n \in Q$, and if $k = n$, then $k \in A$ by step 3.
   So $S(n) \in Q$.
6. By (I) applied to $Q$, $Q = N$.
   So for each $n$ every $k < n$ lies in $A$, the hypothesis on $A$ gives $n \in A$, and $A = N$.
7. (SI) implies (WO).
   Assume (SI), let $A \subseteq N$ be nonempty, and suppose, for a contradiction, that $A$ has no least element.
8. Let $C = N \setminus A$.
   To apply (SI) to $C$, let $n \in N$ and assume that every $k < n$ lies in $C$.
9. Suppose $n \in A$, and let $x \in A$.
   Then $x < n$ is false, because $x \notin C$, so by (B1) $x = n$ or $n < x$, that is, $n \le x$.
10. So $n$ is a least element of $A$, against the assumption.
    Hence $n \notin A$, that is, $n \in C$.
11. By (SI) applied to $C$, $C = N$, so $A = \emptyset$.
    This contradicts the choice of $A$, so $A$ has a least element.
12. (WO) implies (I).
    Assume (WO), let $A \subseteq N$ contain $0$ and satisfy $S(n) \in A$ for each $n \in A$, and suppose, for a contradiction, that $A \ne N$.
13. Then $N \setminus A$ is nonempty, and (WO) gives a least element $m$ of $N \setminus A$.
14. We have $m \ne 0$, because $0 \in A$.
    By (B4), $m = S(k)$ for some $k$, and $k < m$ by (B3).
15. Suppose $k \notin A$.
    Then $m \le k$, because $m$ is least in $N \setminus A$.
16. If $m = k$, then $k < m$ reads $k < k$, and if $m < k$, then $k < m$ and transitivity give $k < k$.
    Both are excluded by (B1), so $k \in A$.
17. By the closure of $A$ under $S$, $m = S(k) \in A$, which contradicts $m \in N \setminus A$.
    So $A = N$, and (I) holds.
18. The three implications form a cycle, so (I), (SI) and (WO) are equivalent.

## Idea

Each principle becomes the next one by a change of set.
From (I) to (SI), apply induction to the set $Q$ of all $n$ below which everything lies in $A$; this is the stronger-property trick of strong induction.
From (SI) to (WO), apply strong induction to the complement of a set with no least element, which shows that the complement is everything.
From (WO) to (I), take the least element outside $A$: it is a successor of an element inside $A$, and closure under $S$ pulls it inside.
Steps 2 and 4 use (B2) and (B3), step 9 uses (B1), and step 14 uses (B3) and (B4).

## Variants

For the natural numbers built from the [[Peano axioms|0QFT7Z76N5]], the arrow from (I) to (SI) is the [[proof of strong induction|C54QYDXFP3]], which also proves the needed facts about $<$ by induction.
The arrow from (SI) to (WO) for $\mathbb{N}$ is the [[proof of the well-ordering principle|QPX5Z5YFH8]].

The arrow from (WO) to (I) is a [[minimal counterexample|JGRCNPKNGG]] argument.
It can also be written without a contradiction, as a proof that a least element of $N \setminus A$ cannot exist.
The direct arrow from (SI) to (I), which uses only (B3) and (B4), is in the remarks of the [[statement|J2P9FWBP3Q]].
