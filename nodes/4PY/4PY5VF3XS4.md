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

We use the notation of the [[statement|J2P9FWBP3Q]]: a set $N$ with $0$, a [[successor|0832XVR512]] map $S$, and a relation $<$ that satisfy (B1) to (B4).
We prove that (I) implies (SI), (SI) implies (WO), and (WO) implies (I).
Then any one of the three principles implies the other two.

1. (I) implies (SI). Assume (I). Let $A \subseteq N$ satisfy the hypothesis of (SI): for each $n$, if every $k < n$ lies in $A$, then $n \in A$.
2. Let $Q$ be the set of all $n \in N$ such that every $k < n$ lies in $A$.
3. We have $0 \in Q$, because no $k$ satisfies $k < 0$, by (B2).
4. Let $n \in Q$. Then $n \in A$, by the hypothesis on $A$. Let $k < S(n)$.
5. By (B1), we have $k < n$, or $k = n$, or $n < k$. The case $n < k < S(n)$ is impossible by (B3).
6. If $k < n$, then $k \in A$, because $n \in Q$. If $k = n$, then $k \in A$ by step 4. So $S(n) \in Q$.
7. By (I) applied to $Q$, we get $Q = N$. So for each $n$, every $k < n$ lies in $A$, and the hypothesis on $A$ gives $n \in A$. Thus $A = N$.
8. (SI) implies (WO). Assume (SI). Let $A \subseteq N$ be nonempty, and suppose, for a contradiction, that $A$ has no least element.
9. Let $C = N \setminus A$. We show that $C$ satisfies the hypothesis of (SI). Let $n \in N$, and assume that every $k < n$ lies in $C$.
10. Suppose $n \in A$. Let $x \in A$. Then $x < n$ is false, because $x \notin C$. By (B1), $x = n$ or $n < x$, so $n \le x$.
11. So $n$ is a least element of $A$, against the assumption. Hence $n \notin A$, that is, $n \in C$.
12. By (SI) applied to $C$, we get $C = N$. So $A = \emptyset$, which contradicts the choice of $A$. Thus $A$ has a least element.
13. (WO) implies (I). Assume (WO). Let $A \subseteq N$ with $0 \in A$, and with $S(n) \in A$ for each $n \in A$. Suppose, for a contradiction, that $A \neq N$.
14. Then $N \setminus A$ is nonempty. By (WO), it has a least element $m$.
15. We have $m \neq 0$, because $0 \in A$. By (B4), $m = S(k)$ for some $k$, and $k < m$ by (B3).
16. Suppose $k \notin A$. Then $m \le k$, because $m$ is least in $N \setminus A$. With $k < m$ and (B1), this gives $m < m$ or $k < k$, which (B1) excludes.
17. So $k \in A$. By the closure of $A$ under $S$, also $m = S(k) \in A$. This contradicts $m \in N \setminus A$.
18. So $A = N$, and (I) holds. The cycle of implications is complete.

## Idea

Each principle is turned into the next by a change of set.
From (I) to (SI), apply induction to the set $Q$ of all $n$ such that everything below $n$ is in $A$; this is the "stronger property" trick.
From (SI) to (WO), apply strong induction to the complement of a set with no least element.
From (WO) to (I), take the least element outside $A$; it is a successor of an element inside $A$.
Steps 3 and 5 use (B2) and (B3), step 10 uses (B1), and step 15 uses (B3) and (B4).

## Variants

1. For the natural numbers built from the [[Peano axioms|0QFT7Z76N5]], the step from (I) to (SI) is the [[proof of strong induction|C54QYDXFP3]]. It also proves the needed facts about $<$ by induction.
2. The step from (SI) to (WO) for $\mathbb{N}$ is the [[proof of the well-ordering principle|QPX5Z5YFH8]].
3. The step from (WO) to (I) is a [[minimal counterexample|JGRCNPKNGG]] argument. It can also be written as a contrapositive, with no contradiction: a least element of $N \setminus A$ cannot exist.
4. The direction from (SI) to (I) has a direct proof that uses only (B3) and (B4). It is given in the Converse section of the [[statement|J2P9FWBP3Q]].
