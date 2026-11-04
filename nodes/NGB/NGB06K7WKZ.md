---
tag: NGB06K7WKZ
kind: proof
name: Proof of Hall's marriage theorem by induction on the number of sets
msc: [05D15]
proves: 08WCB90WND
uses: [0KMVFSHFGZ]
methods: [0ASJVEFA9J, 0WCP0PVET6]
sources:
  - url: https://www.mscs.dal.ca/~janssen/4370/slides/hallstheorem.pdf
---

## Proof

We prove a slightly more general form, for families indexed by any finite set, by strong induction on the number of sets.

*Setup.*

1. Let $I$ be a finite set and $(S_i)_{i \in I}$ a family of finite sets. For $J \subseteq I$, write $S(J) = \bigcup_{i \in J} S_i$. A transversal is an injective function $f$ on $I$ with $f(i) \in S_i$ for all $i \in I$.
2. Say that the family satisfies Hall's condition if $\abs{S(J)} \ge \abs{J}$ for all $J \subseteq I$. For $I = \set{1, \dots, n}$ this is the condition of the statement.

*The condition is necessary.*

3. Let $f$ be a transversal and $J \subseteq I$. Then $f(J) \subseteq S(J)$, since $f(i) \in S_i$ for each $i \in J$.
4. As $f$ is injective, $\abs{f(J)} = \abs{J}$. So $\abs{S(J)} \ge \abs{J}$.

*The condition is sufficient.*

5. We prove by [[strong induction|0KMVFSHFGZ]] on $\abs{I}$ that a family with Hall's condition has a transversal. If $I = \varnothing$, the empty function is a transversal.
6. Let $\abs{I} = n \ge 1$, and suppose the claim holds for all index sets with fewer than $n$ elements. Call $J \subseteq I$ *critical* if $J \ne \varnothing$, $J \ne I$ and $\abs{S(J)} = \abs{J}$.

*Case 1: no subset of $I$ is critical.*

7. Then $\abs{S(J)} \ge \abs{J} + 1$ for every $J$ with $\varnothing \ne J \subsetneq I$.
8. Fix $i_0 \in I$. By Hall's condition for $J = \set{i_0}$, the set $S_{i_0}$ is not empty. Choose $x \in S_{i_0}$.
9. Let $I' = I \setminus \set{i_0}$ and $T_i = S_i \setminus \set{x}$ for $i \in I'$. Write $T(J) = \bigcup_{i \in J} T_i$.
10. The family $(T_i)_{i \in I'}$ satisfies Hall's condition. For $J = \varnothing$ this is clear. For $\varnothing \ne J \subseteq I'$, the set $J$ is a proper subset of $I$, so $\abs{T(J)} \ge \abs{S(J)} - 1 \ge \abs{J}$ by Step 7.
11. Since $\abs{I'} = n - 1$, the induction hypothesis gives a transversal $g$ of $(T_i)_{i \in I'}$. Its values differ from $x$, since $x \notin T_i$.
12. Define $f = g$ on $I'$ and $f(i_0) = x$. Then $f(i) \in S_i$ for all $i$, and $f$ is injective. So $f$ is a transversal.

*Case 2: some $J_0 \subseteq I$ is critical.*

13. Let $A = S(J_0)$, so $\abs{A} = \abs{J_0}$. The subfamily $(S_i)_{i \in J_0}$ satisfies Hall's condition, because subsets of $J_0$ are subsets of $I$.
14. Since $\abs{J_0} < n$, the induction hypothesis gives a transversal $g$ of $(S_i)_{i \in J_0}$. All its values lie in $A$.
15. Let $K_0 = I \setminus J_0$ and $U_i = S_i \setminus A$ for $i \in K_0$. Write $U(K) = \bigcup_{i \in K} U_i$.
16. Let $K \subseteq K_0$. Then $S(K \cup J_0) = S(K) \cup A = U(K) \cup A$, and $U(K)$ is disjoint from $A$. So $\abs{S(K \cup J_0)} = \abs{U(K)} + \abs{A}$.
17. Since $K$ and $J_0$ are disjoint, Hall's condition gives $\abs{U(K)} + \abs{A} \ge \abs{K} + \abs{J_0}$. As $\abs{A} = \abs{J_0}$, we get $\abs{U(K)} \ge \abs{K}$.
18. So $(U_i)_{i \in K_0}$ satisfies Hall's condition. Since $J_0 \ne \varnothing$, we have $\abs{K_0} < n$, and the induction hypothesis gives a transversal $h$ of it. All its values lie outside $A$.
19. Define $f = g$ on $J_0$ and $f = h$ on $K_0$. Then $f(i) \in S_i$ for all $i \in I$.
20. The map $f$ is injective: $g$ and $h$ are injective, values of $g$ lie in $A$, and values of $h$ lie outside $A$. So $f$ is a transversal.

*Conclusion.*

21. By induction, every finite family with Hall's condition has a transversal. With Steps 3 and 4, a family $(S_1, \dots, S_n)$ has a transversal if and only if $\abs{\bigcup_{i \in I} S_i} \ge \abs{I}$ for every $I \subseteq \set{1, \dots, n}$.

## Idea

If every proper subfamily has room to spare, choose any representative for one set and delete it from the others; the condition survives. If some subfamily $J_0$ is tight, its union $A$ must be used up exactly by $J_0$. Solve $J_0$ inside $A$ and the rest outside $A$, and both smaller problems still satisfy the condition.
