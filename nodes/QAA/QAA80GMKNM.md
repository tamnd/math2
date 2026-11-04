---
tag: QAA80GMKNM
kind: proof
name: Proof of the rule of sum
msc: [05A05]
proves: 0EE2V3CHFK
uses: [05099E1NMJ, 0SNQEF7Z53, 0W4RPA8QH3]
methods: [0ASJVEFA9J]
sources:
  - url: https://proofwiki.org/wiki/Sum_Rule_for_Counting
---

## Proof

We first treat two sets, and then argue by induction on $k$.

1. Let $m = |A|$ and $n = |B|$. By the definition of [[cardinality|05099E1NMJ]], there are [[bijections|0SNQEF7Z53]] $f : \set{1, \dots, m} \to A$ and $g : \set{1, \dots, n} \to B$.
2. Define $h : \set{1, \dots, m + n} \to A \cup B$ by $h(i) = f(i)$ for $i \le m$ and $h(i) = g(i - m)$ for $m < i \le m + n$.
3. The map $h$ is surjective. An element of $A$ is $f(i) = h(i)$ for some $i \le m$. An element of $B$ is $g(j) = h(m + j)$ for some $j \le n$.
4. The map $h$ is injective. Let $h(i) = h(i')$. If $i, i' \le m$, then $f(i) = f(i')$, so $i = i'$ because $f$ is injective.
5. If $i, i' > m$, then $g(i - m) = g(i' - m)$, so $i = i'$ because $g$ is injective.
6. If $i \le m < i'$, then $h(i) \in A$ and $h(i') \in B$. This is impossible, because $A$ and $B$ are [[disjoint|0W4RPA8QH3]]. The case $i' \le m < i$ is the same.
7. So $h$ is a bijection, $A \cup B$ is finite, and $|A \cup B| = m + n = |A| + |B|$.
8. Now let $A_1, \dots, A_k$ be pairwise disjoint finite sets. For $k = 0$ the union is empty and both sides are $0$. For $k = 1$ the formula $|A_1| = |A_1|$ holds.
9. Suppose the formula holds for $k$ sets, and let $A_1, \dots, A_{k+1}$ be pairwise disjoint finite sets. Put $U = A_1 \cup \dots \cup A_k$.
10. By the induction hypothesis, $U$ is finite and $|U| = |A_1| + \dots + |A_k|$.
11. The sets $U$ and $A_{k+1}$ are disjoint. Indeed, an element of both would lie in $A_i \cap A_{k+1}$ for some $i \le k$, and this set is empty.
12. By steps 1 to 7, $|U \cup A_{k+1}| = |U| + |A_{k+1}| = |A_1| + \dots + |A_{k+1}|$. This completes the induction.

## Idea

Number the elements of $A$ first and then continue the numbering through the elements of $B$.
Because no element is in both sets, no element gets two numbers. So the numbers $1$ to $|A| + |B|$ count the union exactly once.
